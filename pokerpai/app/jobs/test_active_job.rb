class TestActiveJob < ApplicationJob
  queue_as :default

  def perform(*ags)
    puts "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    puts "@ TestActiveJob has run the perform method WOOHOO @"
    puts "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
  end
end
