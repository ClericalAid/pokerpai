module PokerEngine
  class CommunicationService
    class << self
      POKER_ENGINE_QUEUE = "poker_engine.commands"

      def send_message(message:)
        Hutch.publish(POKER_ENGINE_QUEUE, message)
      end

      def create_game
        message = {
          action: "create_game"
        }
        send_message(message:)
      end

      def send_command_to_game(command:, game_id:)
        message = {
          action: "game_command",
          game_id:,
          command:
        }

        send_message(message:)
      end
    end
  end
end
