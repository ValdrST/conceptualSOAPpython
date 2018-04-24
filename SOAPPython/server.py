import SOAPpy
from sqlalchemy import create_engine


def getEmployees():
	conn = db_connect.connect()
	query = conn.execute("select * from employees")
	return [i[0] for i in query.cursor.fetchall()]
    
def postEmployees():
	conn = db_connect.connect()
	LastName = request.json['LastName']
	FirstName = request.json['FirstName']
	Title = request.json['Title']
	ReportsTo = request.json['ReportsTo']
	BirthDate = request.json['BirthDate']
	HireDate = request.json['HireDate']
	Address = request.json['Address']
	City = request.json['City']
	State = request.json['State']
	Country = request.json['Country']
	PostalCode = request.json['PostalCode']
	Phone = request.json['Phone']
	Fax = request.json['Fax']
	Email = request.json['Email']
	query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
	'{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
	'{13}')".format(LastName,FirstName,Title,ReportsTo, BirthDate, HireDate, Address, City, State, Country, PostalCode, Phone, Fax,Email))
	return 'success'

def getById(id):
	conn = db_connect.connect()
	query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
	result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
	return result

db_connect=create_engine('sqlite:///chinook.db')
server = SOAPpy.SOAPServer(("0.0.0.0", 5001))
server.registerFunction(getEmployees)
server.registerFunction(postEmployees)
server.registerFunction(getById)
server.serve_forever()