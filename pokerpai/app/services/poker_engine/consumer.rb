module PokerEngine
  class Consumer
    include Hutch::Consumer
    consume "poker_engine.responses"

    def process(message)
      puts "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
      puts "@ Message received from poker engine: @"
      puts "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
      puts "#{message}"

      case message.body[:command]
      when "get_game"
        get_game(message:)
      end
    end

    def get_game(message:)
      ActionCable.server.broadcast("message_channel", message.body)
    end
  end
end
