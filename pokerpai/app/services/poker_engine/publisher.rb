module PokerEngine
  class Publisher
    def self.hello_world
      message = {
        action: "hello_world",
        message: "Hello from Rails!"
      }

      Hutch.publish("poker_engine.commands", message)
    end
  end
end
