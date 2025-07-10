class TestJob
  # include Sneakers::Worker
  # from_queue "test"

  # def work(msg)
  #   puts "running TestJob"
  #   worker_trace "worker_trace method called BLAHBLAH"
  #   puts method(:ack!)
  #   ack!
  # end
end
