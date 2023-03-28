
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
conn = snowflake.connector.connect(
    account=account_name,
    user=username,
    password=password,
    warehouse=warehouse_name,
    database=database_name,
    schema=schema_name
)

#default route
@app.route('/')
def default_route():
    return "<p>welcome to the page and</p>"

# route to execute a query
@app.route('/select', methods=['GET'])
def query():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM table2')
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
