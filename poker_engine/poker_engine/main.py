import os
from poker_engine.message_handler import MessageHandler

def main():
    # Get configuration from environment variables
    rabbitmq_host = os.environ.get('RABBITMQ_HOST', 'localhost')
    rabbitmq_queue = os.environ.get('RABBITMQ_QUEUE', 'poker_engine_queue')

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
