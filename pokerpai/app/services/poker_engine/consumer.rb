module PokerEngine
  class Consumer
    include Hutch::Consumer
    consume "poker_engine.responses"

    def process(message)
      puts "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
      puts "@ Message received from poker engine: @"
      puts "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
      puts "#{message}"
    end
  end
end
