from flask import Flask
from flask import request, redirect, url_for
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL
#from flask_ngrok import run_with_ngrok

app = Flask(__name__, static_url_path='/static')
CORS(app)
#run_with_ngrok(app)

# connecion_string = {'host':"147.232.40.14", 'user':"tv635vg", 'passwd':"Airi8Eiw", 'database':"tv635vg"}
# connecion_string = {'host':"147.232.40.14", 'user':"sg624ew", 'passwd':"moor8eiW", 'database':"sg624ew"}

@app.route('/GetOrders', methods=['GET'])
def GetOrders():
  with open ('content/OrderGetTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  myDb.close()

  return jsonify(result),200

@app.route('/GetOrders/<id>', methods=['GET'])
def GetIdOrder(id):
  with open ('content/OrderByIdGetTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql+id)
  result = cursor.fetchall()
  cursor.close()
  myDb.close()
  return jsonify(result),200

@app.route('/GetProducts', methods=['GET'])
def GetProducts():
  with open ('content/ProductGetTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  myDb.close()
  return jsonify(result),200

@app.route('/imgs/<filename>', methods=['GET'])
def display_image(filename):
	return redirect(url_for('static', filename='imgs/' + filename), code=301)

@app.route('/GetCustomers', methods=['GET'])
def GetCustomers():
  with open ('content/CustomerGetTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  myDb.close()
  return jsonify(result),200

@app.route('/CreateOrder', methods=["POST"])
def CreateOrder():
  data = request.get_json(force=True)
  order_dict = dict(data)
  with open ('content/OrderInsertTable.ddl') as ddl_file:
    sql = ddl_file.read()
    sql = sql[:-1] + "'{}','{}','{}','{}')"
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql.format(order_dict["orders_ID"], order_dict["product_ID"],order_dict["customer_ID"],order_dict["orders_quantity"]))
  myDb.commit()
  cursor.close()
  myDb.close()
  return jsonify("Created"),201


@app.route('/CreateCustomer', methods=["POST"])
def CreateCustomer():
  data = request.get_json(force=True)
  customer_dict = dict(data)
  with open ('content/CustomerInsertTable.ddl') as ddl_file:
    sql = ddl_file.read()
    sql = sql[:-1] + "'{}','{}','{}','{}','{}','{}')"
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql.format(customer_dict["customer_ID"], customer_dict["customer_firstName"],customer_dict["customer_lastName"],customer_dict["customer_phone"],customer_dict["customer_email"],customer_dict["customer_address"]))
  myDb.commit()
  cursor.close()
  myDb.close()
  return jsonify("Created"),201

@app.route('/CreateProduct', methods=["POST"])
def CreateProduct():
  data = request.get_json(force=True)
  product_dict = dict(data)
  with open ('content/ProductInsertTable.ddl') as ddl_file:
    sql = ddl_file.read()
    sql = sql[:-1] + "'{}','{}','{}','{}')"
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql.format(product_dict["product_ID"], product_dict["product_name"], product_dict["product_price"], product_dict["product_pieces_WH"]))
  myDb.commit()
  cursor.close()
  myDb.close()
  return jsonify("Created"),201

@app.route('/UpdateOrder/<id>', methods=['PUT'])
def UpdateOrder(id):
  data = request.get_json(force=True)
  order_dict = dict(data)
  with open ('content/OrderUpdateTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql.format(order_dict["orders_ID"], order_dict["product_ID"],order_dict["customer_ID"],order_dict["orders_quantity"],order_dict["orders_ID"]))
  myDb.commit()
  cursor.close()
  myDb.close()
  return jsonify("Updated"),200

@app.route('/UpdateCustomer/<id>', methods=['PUT'])
def UpdateCustomer(id):
  data = request.get_json(force=True)
  customer_dict = dict(data)
  with open ('content/CustomerUpdateTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql.format(customer_dict["customer_ID"], customer_dict["customer_firstName"],customer_dict["customer_lastName"],customer_dict["customer_phone"],customer_dict["customer_email"],customer_dict["customer_address"],customer_dict["customer_ID"]))
  myDb.commit()
  cursor.close()
  myDb.close()
  return jsonify("Updated"),200

@app.route('/UpdateProduct/<id>', methods=['PUT'])
def UpdateProduct(id):
  data = request.get_json(force=True)
  product_dict = dict(data)
  with open ('content/ProductUpdateTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql.format(product_dict["product_ID"], product_dict["product_name"],product_dict["product_price"],product_dict["product_pieces_WH"],product_dict["product_ID"]))
  myDb.commit()
  cursor.close()
  myDb.close()
  return jsonify("Updated"),200


@app.route('/DeleteOrder/<id>', methods=['DELETE'])
def DeleteOrder(id):
	with open ('content/OrderDeleteTable.ddl') as ddl_file:
		sql = ddl_file.read()
		sql = sql + "'{}'"
	myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
	cursor = myDb.cursor()
	cursor.execute(sql.format(id))
	myDb.commit()
	cursor.close()
	myDb.close()
	return jsonify("Deleted"),204

@app.route('/DeleteCustomer/<id>', methods=['DELETE'])
def DeleteCustomer(id):
	with open ('content/CustomerDeleteTable.ddl') as ddl_file:
		sql = ddl_file.read()
		sql = sql + "'{}'"
	myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
	cursor = myDb.cursor()
	cursor.execute(sql.format(id))
	myDb.commit()
	cursor.close()
	myDb.close()
	return jsonify("Deleted"),204

@app.route('/DeleteProduct/<id>', methods=['DELETE'])
def DeleteProduct(id):
	with open ('content/ProductDeleteTable.ddl') as ddl_file:
		sql = ddl_file.read()
		sql = sql + "'{}'"
	myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
	cursor = myDb.cursor()
	cursor.execute(sql.format(id))
	myDb.commit()
	cursor.close()
	myDb.close()
	return jsonify("Deleted"),204

if __name__ == "__main__":
    app.run()
