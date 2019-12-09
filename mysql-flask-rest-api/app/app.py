import os
import hashlib, uuid
from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
from flask_cors import CORS

mysql = MySQL()
application = app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'my_database'
app.config['MYSQL_DATABASE_HOST'] = 'flask_database_container'


mysql.init_app(app)
api = Api(app)

class MySQL(Resource):

    # GET
    def get(self):

        try:
            
            # Establish Connection
            conn = mysql.connect()
            cursor = conn.cursor()

            # Execute Query
            sql = "select * from user_credentials"
            cursor.execute(sql)
            
            # Fetch rows
            rows = cursor.fetchall()
            
            # Return response
            return make_response(jsonify({'success':True, 'error':None, 'message':rows}), 200)
        
        except Exception as error:
            
            # Report error
            print("[ERROR] ==>", error)
            return make_response(jsonify({'success':False, 'error':str(error), 'message':None}), 500)
    
    # PUT
    def put(self):

        try:
            
            # Establish Connection
            conn = mysql.connect()
            cursor = conn.cursor()

            # Define values to be inserted
            values = {
                'user_id' : str(uuid.uuid4()),
                'user_name' : 'Adisakshya Chauhan',
                'email' : 'adisakshya98@gmail.com',
                'hashed_password' : int(hashlib.sha1('this-ismy-password'.encode('utf-8')).hexdigest(), 16) % (10 ** 8)
            }

            # Execute Query
            sql = "INSERT INTO user_credentials (`user_id`, `user_name`, `user_email`, `password`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (values['user_id'], values['user_name'], values['email'], values['hashed_password']))

            # Commit connection
            conn.commit()
            
            # Return response
            return make_response(jsonify({'success':True, 'error':None, 'message':'inserted'}), 200)
        
        except Exception as error:
            
            # Report error
            print("[ERROR] ==>", error)
            return make_response(jsonify({'success':False, 'error':str(error), 'message':None}), 500)

# API Resources
api.add_resource(MySQL, '/')

# Driver Function
if __name__ == '__main__':
    
    port = int(os.environ.get("PORT", 5000))
    app.run(port=5000, host='0.0.0.0',debug=True)