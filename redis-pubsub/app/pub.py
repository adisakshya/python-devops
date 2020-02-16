import os
import redis
from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

application = app = Flask(__name__)
CORS(app)

api = Api(app)

channels = dict()

# Publishers
class Publishers(Resource):
    
    # Constructor
    def __init__(self):

        redis_host = os.environ.get('REDIS_HOST', '192.168.99.100')
        redis_port = os.environ.get('REDIS_PORT', 6379)

        self.queue = redis.Redis(host=redis_host, port=redis_port, db=0)
        
        # Publisher
        channel = self.queue.pubsub()

    # GET
    # get channels
    def get(self):
        try:
            
            # Get all channels
            res = channels

            # Return response
            return make_response(jsonify({'success':True, 'error':None, 'message':res}, 200))
        
        except Exception as error:
            
            # Report error
            print("[ERROR] ==>", error)
            return make_response(jsonify({'success':False, 'error':str(error), 'message':None}), 500)

    # PUT
    # publish message
    def put(self):
        try:
            
            _channel = request.form.get('channel')
            _message = request.form.get('message')
            
            # Publish Message
            self.queue.publish(_channel, _message)

            # Return response
            return make_response(jsonify({'success':True, 'error':None, 'message':_message}, 200))
        
        except Exception as error:
            
            # Report error
            print("[ERROR] ==>", error)
            return make_response(jsonify({'success':False, 'error':str(error), 'message':None}), 500)

    # POST
    # new channel
    def post(self):
        try:
            
            _channel = request.form.get('channel')
            
            # Create new channel
            channels[_channel] = 0

            # Return response
            return make_response(jsonify({'success':True, 'error':None, 'message':channels[_channel]}, 200))
        
        except Exception as error:
            
            # Report error
            print("[ERROR] ==>", error)
            return make_response(jsonify({'success':False, 'error':str(error), 'message':None}), 500)

# API Resources
api.add_resource(Publishers, '/api/publisher')

if __name__ == "__main__":
    
    port = os.environ.get("PORT", 5000)
    app.run(debug=True, host="localhost", port=port)
