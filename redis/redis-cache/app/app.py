import os
from flask import Flask, make_response, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from utils.cache import CacheManagement

application = app = Flask(__name__)
CORS(app)

api = Api(app)

# API

# Cache Management
class Cache(Resource):

    # Constructor
    def __init__(self):
        
        # Cache Instance
        self.cacheObj = CacheManagement()

    # GET
    # Returns key -> value
    def get(self):

        try:
            
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('key', type=str, help='key')
            args = parser.parse_args()

            _key = args['key']

            # Get value by key from cache
            value = {
                'value': self.cacheObj.get(_key)
            }

            # Return response
            return make_response(jsonify({'success':True, 'error':None, 'message':value}), 200)
        
        except Exception as error:
            
            # Report error
            print("[ERROR] ==>", error)
            return make_response(jsonify({'success':False, 'error':str(error), 'message':None}), 500)
    
    # POST
    # Create new key -> value
    def post(self):

        try:
            
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('key', type=str, help='key')
            parser.add_argument('value', type=str, help='value')
            args = parser.parse_args()

            _key = args['key']
            _value = args['value']
            
            # Cache
            self.cacheObj.insert(_key, _value)

            # Return response
            return make_response(jsonify({'success':True, 'error':None, 'message':{'key' : _key}}), 200)
        
        except Exception as error:
            
            # Report error
            print("[ERROR] ==>", error)
            return make_response(jsonify({'success':False, 'error':str(error), 'message':None}), 500)
    
    # DELETE
    # Delete key -> value
    def delete(self):

        try:
            
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('key', type=str, help='key')
            args = parser.parse_args()

            _key = args['key']
            
            # Delete cache
            self.cacheObj.delete(_key)

            # Return response
            return make_response(jsonify({'success':True, 'error':None, 'message':{'key' : _key}}), 200)
        
        except Exception as error:
            
            # Report error
            print("[ERROR] ==>", error)
            return make_response(jsonify({'success':False, 'error':str(error), 'message':None}), 500)

# Clear all cached data
class ClearCache(Resource):

    # Constructor
    def __init__(self):
        
        # Cache Instance
        self.cacheObj = CacheManagement()
    
    # DELETE
    # Clear Cache
    def delete(self):

        try:
            
            # Clear complete cache
            self.cacheObj.clear()

            # Return response
            return make_response(jsonify({'success':True, 'error':None, 'message':None}, 200))
        
        except Exception as error:
            
            # Report error
            print("[ERROR] ==>", error)
            return make_response(jsonify({'success':False, 'error':str(error), 'message':None}), 500)


# API Resources
api.add_resource(Cache, '/api/cache')
api.add_resource(ClearCache, '/api/cache/clear')

