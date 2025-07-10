class MessageService
  def self.broadcast_message(message = nil)
    message ||= "Server message at #{Time.now}"
    ActionCable.server.broadcast("message_channel", message)
    puts "Broadcasted: #{message}"
  end
end