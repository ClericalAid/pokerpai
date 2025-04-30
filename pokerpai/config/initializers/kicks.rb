require "sneakers"

Sneakers.configure(
  amqp: ENV["RABBITMQ_URL"] || "amqp://guest:guest@localhost:5672",
  vhost: "/",
  exchange: "sneakers",
  exchange_type: :direct,
  durable: true,
)

Sneakers.logger = Rails.logger
Sneakers.logger.level = Logger::WARN
