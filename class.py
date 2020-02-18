import calendar
import requests
import time
import math
import mysql.connector
from mysql.connector import Error

PI = 3.14
GRAVITY = 9.8

MYSQL_HOST = 'http://127.0.0.1'
MYSQL_USER = 'maria'
MYSQL_PASSWORD = 'lamerestbelle'
MYSQL_DB = 'dsfsdf'



class MyClass:
	"This is my second class"
	a = 10

	database: {
	    'types': 'MySQL',
	    'versions': '5.7',
        'fields': {
            'sort_buffer_size': {'defaul': '32', 'unity': 'k', 'div':'2', 'type': 'TYPE_INT', 'required': 'true', 'min': 0, 'max': 4500},
            'join_buffer_size': {'defaul': '32', 'unity': 'k', 'div':'2', 'type': 'TYPE_INT', 'required': 'true', 'min': 0, 'max': 4500}
            }
 		}

	people = {'tanguy': {'name': 'John', 'age': '27', 'sex': 'Male'},
	          'mario': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}



	def func(self):
		print('Hello')

	def decremente(self):
		self.taggle = 'taggle'
		self.b = property(lambda self: self.a + 1)
		self.c = lambda self: self.a + 1
		print(self.a)
		print(self.b)
		print(self.c)
		print(self.taggle)


class ComplexNumber:
    "This is my second class"
    a = 10
    database: {
    'types': 'MySQL',
    'versions': '5.7',
    'fields': {
        'sort_buffer_size': {'defaul': '32', 'unity': 'k', 'div':'2', 'type': 'TYPE_INT', 'required': 'true', 'min': 0, 'max': 4500},
        'join_buffer_size': {'defaul': '32', 'unity': 'k', 'div':'2', 'type': 'TYPE_INT', 'required': 'true', 'min': 0, 'max': 4500}
        }
    }
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

    def func(self):
        print('Hello')

    def decremente(self):
        self.taggle = 'taggle'
        self.b = property(lambda self: self.a + 1)
        self.c = lambda self: self.a + 1
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.taggle)



# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5)
c2.attr = 10

# Output: (5, 0, 10)
print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'


# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)


# Output: 'This is my second class'
print(MyClass.__doc__)

print("hello")


a = MyClass()
a.decremente() 


# for url in urls:
#     start_time = time.time()
#     r = requests.get(url)
#     print( ((time.time() - start_time) * 1000) // 1)

MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'maria'
MYSQL_PASSWORD = 'lamerestbelle'
MYSQL_DB = 'ps1763'


class DB:
    "This is my DB class"
    a = 10
    database: {
    'types': 'MySQL',
    'versions': '5.7',
    'fields': {
        'sort_buffer_size': {'defaul': '32', 'unity': 'k', 'div':'2', 'type': 'TYPE_INT', 'required': 'true', 'min': 0, 'max': 4500},
        'join_buffer_size': {'defaul': '32', 'unity': 'k', 'div':'2', 'type': 'TYPE_INT', 'required': 'true', 'min': 0, 'max': 4500}
        }
    }
    def __init__(self,r = 0,i = 0, sql = None):
        self.connection = mysql.connector.connect(host=MYSQL_HOST,
                                             database=MYSQL_DB,
                                             user=MYSQL_USER,
                                             password=MYSQL_PASSWORD)
        self.cursor = self.connection.cursor()

    def execute(self, sql = None):
        print("start connexion")

        self.connection = mysql.connector.connect(host=MYSQL_HOST,
                                             database=MYSQL_DB,
                                             user=MYSQL_USER,
                                             password=MYSQL_PASSWORD)
        self.cursor = self.connection.cursor()

        try:
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                self.self.cursor.execute("SHOW DATABASES;")
                record = self.cursor.fetchone()
                print("You're connected to database: ", record)
            else:
                print("DB is not connected")
        except Error as e:
            print("Error while connecting to MySQL", e)
            
        finally:
            if (self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
                print("MySQL connection is closed")

print("start connexion")
con = DB()

print(con.a)
print(con.__doc__)
print(con.execute)
