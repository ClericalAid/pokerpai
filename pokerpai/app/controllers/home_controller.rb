class HomeController < ApplicationController
  def index
  end

  def test_message
    ActionCable.server.broadcast("message_channel", "Message from server: #{Time.now}")
    render json: { status: "Message sent" }
  end
end
