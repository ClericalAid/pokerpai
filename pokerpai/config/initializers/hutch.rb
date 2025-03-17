Hutch::Config.set(:mq_host, ENV["RABBITMQ_HOST"] || "localhost")
Hutch::Config.set(:mq_exchange, "pokerpai")
Hutch.connect
