module PokerEngine
  class ResponseConsumer
    include Hutch::Consumer
    consume "poker_engine.responses"

    def process(message)
      payload = JSON.parse(message.body)
      Rails.logger.info "Received from poker engine: #{payload.inspect}"
    end
  end
end
