import pika
import json
import os
from typing import Optional, Dict, Any
from poker_engine.game_manager import GameManager

class MessageHandler:
    def __init__(self, host: str = 'localhost', queue_name: str = 'poker_queue'):
        self.host = host
        self.queue_name = queue_name
        self.connection: Optional[pika.SelectConnection] = None
        self.channel: Optional[pika.channel.Channel] = None
        self.game_manager = GameManager()

    def connect(self) -> None:
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.host)
            )
            self.channel = self.connection.channel()

            self.channel.queue_declare(queue=self.queue_name)
            print(f"Connected to RabbitMQ and declared queue: {self.queue_name}")

        except pika.exceptions.AMQPConnectionError as e:
            print(f"Failed to connect to RabbitMQ: {e}")
            raise

    def send_message(self, message: Dict[str, Any]) -> None:
        try:
            if not self.channel:
                self.connect()

            self.channel.basic_publish(
                exchange='',
                routing_key=self.queue_name,
                body=json.dumps(message)
            )
            print(f"Sent message: {message}")

        except Exception as e:
            print(f"Failed to send message: {e}")
            raise

    def callback(self, ch, method, properties, body):
        try:
            message = json.loads(body.decode())
            print(f"Received message: {message}")
            
            if 'action' not in message:
                print("Error: Message is missing 'action' field")
                return
                
            action = message['action']
            
            if action == 'create_game':
                starting_stacks = message.get('starting_stacks')
                game_id = self.game_manager.create_game(starting_stacks=starting_stacks)
                response = {'status': 'success', 'game_id': game_id}
                self.send_message(response)
                
            elif action == 'game_command':
                game_id = message.get('game_id')
                command = message.get('command')
                
                if game_id is None or command is None:
                    print("Error: Message is missing required fields")
                    return
                    
                self.game_manager.get_command(game_id, command)
                response = {'status': 'success', 'game_id': game_id, 'command': command}
                self.send_message(response)
                
            else:
                print(f"Unknown action: {action}")
                
        except json.JSONDecodeError:
            print(f"Error: Unable to parse message as JSON: {body.decode()}")
        except Exception as e:
            print(f"Error processing message: {e}")

    def receive_messages(self, timeout: Optional[int] = None) -> None:
        try:
            if not self.channel:
                self.connect()

            print("Waiting for messages...")

            # Set up the consumer
            self.channel.basic_consume(
                queue=self.queue_name,
                auto_ack=True,
                on_message_callback=self.callback
            )

            if timeout:
                # Start consuming with timeout
                print(f"Will stop after {timeout} seconds")
                self.connection.call_later(timeout, self.stop_consuming)
                
            # Start consuming
            self.channel.start_consuming()

        except Exception as e:
            print(f"Error receiving messages: {e}")
            raise

    def stop_consuming(self):
        if self.channel:
            self.channel.stop_consuming()

    def close(self):
        if self.connection:
            self.connection.close()

def main():
    # Get configuration from environment variables
    rabbitmq_host = os.environ.get('RABBITMQ_HOST', 'localhost')
    rabbitmq_queue = os.environ.get('RABBITMQ_QUEUE', 'poker_queue')

    handler = MessageHandler(host=rabbitmq_host, queue_name=rabbitmq_queue)

    try:
        print(f"Connecting to RabbitMQ at {rabbitmq_host} with queue {rabbitmq_queue}")
        handler.connect()
        print("Message handler started. Ready to process game commands.")
        handler.receive_messages()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        handler.close()

if __name__ == "__main__":
    main()

