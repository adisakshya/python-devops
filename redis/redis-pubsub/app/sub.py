import redis
import os
import time

# Subscriber
class Subscriber:

    def __init__(self, channel_name):

        redis_host = os.environ.get('REDIS_HOST', '192.168.99.100')
        redis_port = os.environ.get('REDIS_PORT', 6379)
        self.r = redis.Redis(host=redis_host, port=redis_port, db=0)
        self.p = self.r.pubsub()
        self.p.subscribe(channel_name)
    
    def getMessages(self):

        print('Listing for messages!')
        while True:
            try:
                message = self.p.get_message()
                if message:
                    print("Subscriber: %s" % message['data'])
            except KeyboardInterrupt:
                print('Exciting')
                break

# Driver Code
subscriber_object = Subscriber('mychannel')
subscriber_object.getMessages()