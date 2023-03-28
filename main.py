
from flask import Flask, jsonify, request
import snowflake.connector

app = Flask(__name__)

# Set Snowflake credentials
account_name = 'ewhcreo-ot80498'
username = 'benten63'
password = 'Benten@63'
warehouse_name = 'COMPUTE_WH'
database_name = 'MYTESTDB'
schema_name = 'MYSCHEMA'

# Connect to Snowflake


#default route
@app.route('/')
def default_route():
    return "<p>welcome to the page </p>"






if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
