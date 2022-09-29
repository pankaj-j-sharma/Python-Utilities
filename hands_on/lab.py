# Question:

# Design ITAM system?(IT asset management)

# Users:
# Phase1 :
# Hardware assets : Laptop, Headphones,etc
# Software: email, vpn,etc
# Phase 2: get access 10 apps - 7 apps for all devs

# Candidate raise request to certain softwares
# Raise ticket to admin
# Access
# Phase 3:
# On demand


# Characters with in the application:

# Funcional requirements:
# Users:
# Employees
# Itadmins

# Assets
# Software assets
# Hardware assets

# Business Processes:
# On boarding
# Offboarding

# User logs in -
# ITAdmin-
# 	Create user
# 	Assign role / dept
# 	Start Onboarding
# 		Allocate hardware assets - done
# Allocate software assets as per the role/dept
# Notify the employer and employee once standard allocation done

# Find User
# Start Offboarding
# 	Deallocate softwares
# 	Deallocate hardware assets
# 	Notify employer assets recovered
# 	Make the user dormant/delete

# Employee
# 	Checks the process status - onboarding complete
# 	View the allocated assets , sw , hw
# 	Request for additional assets - subject to approval
# 	Request for removal of sw assets


# User_Types:
# 	Id : int
# 	Title : string
# 	Description : string

# All_Users
# Id : int
# Name : string
# Employee_id : string
# Active : bool
# 	Type : foreign key -> User_Types
# 	Start_date : date
# 	Dob : date

# Software_Assets
# Id:int
# Licenceno: string
# ValidFrom : date
# ValidTo : date
# Active: bool
# Title : string
# Description : string
# Version : string
# Build : string
# Issuer : string
# UserTypeId: ForeignKey -> User_Types

# Hardware_Assets
# 	Id : int
# 	Title : string
# 	Description : string
# 	ModelNo: string
# 	SerialNo: string
# 	ProcuredDate : date
# 	InWarranty: bool
# 	Manufacturer:string
# 	Allocated:bool
# User_Assets
# 	Id:int
# 	Userid -> ForeignKey id -> All_Users
# 		Asset_Id -> ForeignKey id -> All_Assets
# CreatedDate : date
#  isActivc:bool
# updatedBy:string


# Requirements
# Types of assets - Software , Hardware
# Inventory management - admin portal ?? updating/adding
# Inventory stock count - available
# Notification sent for low inventory as per threshold
# In Warranty / out of warranty
# Users or owners


# from flask import Flask, session, request
# from werkzeug.utils import secure_filename
# import os
# from markupsafe import escape

# app = Flask(__name__)


# @app.route("/")
# def test():
#     app.logger.debug(f'request -> {request}')
#     return "hey this is test"


# @app.route("/<name>")
# def hello(name):
#     return "hello {name}".format(name=escape(name))


# @app.route('/use_session')
# def use_session():
#     if 'song' not in session:
#         session['songs'] = {'title': 'Tapestry', 'singer': 'Bruno Major'}


# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     app.logger.debug('request ', request)
#     if request.method == 'POST':
#         file = request.files['the_file']
#         file.save(os.path.join(os.getcwd(), file.filename))
#         file.save(os.path.join(os.getcwd(), secure_filename(file.filename)))


# if __name__ == '__main__':
#     app.run(host="localhost", port=8080, debug=True)

# # class MyLab:
# #     def __init__(self, name):
# #         self.__name = name
# #         self._protected = name


# # mylab = MyLab('new hands on')
# # print(dir(mylab))
# # print(mylab._protected)
# # print(mylab.__init__('new'))

# class Parent:
#     def __init__(self):
#         self.name='Pankaj'
#         self.last='Sharma'

#     def __init_subclass__(cls):
#         print(cls.__name__,'cannot inherit')
#         raise Exception("unable to inherit")


# class Children(Parent):
#     def __init__(self):
#         self.name='Pankaj jr'
#         self.last='Sharma jr'

# child = Children()

# set_new = {'1','pan',(1,2,3,4,5)}

# def dirReduc(arr):
#     dir_lookup = {'EAST':'WEST','NORTH':'SOUTH','WEST':'EAST','SOUTH':'NORTH'}
#     tmp = arr[:]
#     i = 0
#     while True:
#         cleared = False
#         i =0
#         while i<len(arr)-1:
#             if dir_lookup[arr[i]] == arr[i+1]:
#                 del arr[i]
#                 del arr[i]
#                 cleared=True
#             else:
#                 i+=1
#         if not cleared:
#             break
#     return arr


# if __name__=='__main__':
#     print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))


# def zero(fn=None):
#     if fn:
#         return fn(0)
#     else:
#         return 0

# def one(fn=None):
#     if fn:
#         return fn(1)
#     else:
#         return 1

# def two(fn=None):
#     if fn:
#         return fn(2)
#     else:
#         return 2

# def three(fn=None): 
#     if fn:
#         return fn(3)
#     else:
#         return 3

# def four(fn=None): 
#     if fn:
#         return fn(4)
#     else:
#         return 4

# def five(fn=None): 
#     if fn:
#         return fn(5)
#     else:
#         return 5

# def six(fn=None):
#     if fn:
#         return fn(6)
#     else:
#         return 6

# def seven(fn=None):
#     if fn:
#         return fn(7)
#     else:
#         return 7

# def eight(fn=None):
#     if fn:
#         return fn(8)
#     else:
#         return 8

# def nine(fn=None): 
#     if fn:
#         return fn(9)
#     else:
#         return 9

# def plus(num): 
#     return lambda a:a+num

# def minus(num):
#     return lambda a:a-num

# def times(num): 
#     return lambda a:a*num

# def divided_by(num): 
#     return lambda a:a//num

# if __name__=='__main__':
#     print(eight(minus(three())))


# def rot13(message):
#     response = []
#     for literal in message:
#         ord_literal = ord(literal)
#         if ord(literal) >= ord('A') and ord(literal) <= ord('Z'):
#             ord_literal = ord(literal)+13 if ord(literal)+13 <=ord('Z') else (ord(literal)+13 - ord('Z'))+ord('A')-1
#         elif ord(literal) >= ord('a') and ord(literal) <= ord('z'):
#             ord_literal = ord(literal)+13 if ord(literal)+13 <=ord('z') else (ord(literal)+13 - ord('z'))+ord('a')-1
#         response.append(chr(ord_literal))
#
#     return ''.join(response)
#
# if __name__=='__main__':
#     print(rot13('test'))

# def productFib(prod):
#     fibs = [0, 1]
#     while True :
#         current_product = fibs[-2]*fibs[-1]
#         if current_product >= prod:
#             break
#         last_ele = fibs[-2]+fibs[-1]
#         fibs.append(last_ele)
#
#     return [fibs[-2], fibs[-1], current_product == prod]
#
# if __name__=='__main__':
#     print(productFib(5895))

# def cakes(recipe, available):
#     number_of_cakes = 0
#     ingredients_available = True
#     while ingredients_available:
#         for ingredient in recipe:
#             if not ingredient in available or available[ingredient]<recipe[ingredient]:
#                 ingredients_available = False
#                 return number_of_cakes
#             else:
#                 available[ingredient] -= recipe[ingredient]
#         number_of_cakes += 1
#     return number_of_cakes
#
# if __name__=='__main__':
#     recipe = {"flour": 500, "sugar": 200, "eggs": 1}
#     available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
#     print(cakes(recipe,available))

# # Kadane's Algorithm
# def max_sequence(arr):
#     m_sum = 0
#     c_sum = 0
#     for num in arr:
#         c_sum+=num
#         if c_sum > m_sum:
#             m_sum = c_sum
#         if c_sum < 0 :
#             c_sum = 0    
#     return m_sum

# if __name__=='__main__':
#     print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

# def generate_hashtag(s):
#     input_string = s.replace(' ', ' ').strip()
#     input_string = ''.join([st.capitalize() for st in input_string.split(' ')])
#     response = '#'+input_string if input_string and len(input_string) < 140 else False
#     return response
#
# if __name__=='__main__':
#     print(generate_hashtag('   coded   '))

# def order_weight(strng):
#     return ' '.join(sorted(strng.replace("  "," ").split(" "),key=lambda x: (sum([int(l) for l in list(x)]),str(x))))
#
# if __name__=='__main__':
#     print(order_weight("103 123 4444 99 2000 90 180"))

# def first_non_repeating_letter(string):
#     dct_chrs={}
#     for s in string:
#         if s.lower() in dct_chrs :
#             dct_chrs[s.lower()]+=1
#         elif s.upper() in dct_chrs:
#             dct_chrs[s.upper()] += 1
#         else:
#             dct_chrs[s]=1
#
#     result = [chr for chr in dct_chrs if dct_chrs[chr]==1]
#     result = result[0] if result else ""
#     return result
#
# if __name__=='__main__':
#     print(first_non_repeating_letter("Go hang a salami, I\'m a lasagna hog!"))

# import re
# def increment_string(strng):
#     str_digits = re.findall(r'\d+$', strng)
#     str_digits = str_digits[0] if str_digits else None
#     if str_digits:
#         digits = int(str_digits)+1
#     else:
#         digits = 1
#     strng = strng.replace(str_digits,str(digits).rjust(len(str_digits), '0')) if str_digits else strng+str(digits)
#     return strng
#
# if __name__=='__main__':
#     print(increment_string("foobar00"))


# def rgb(r, g, b):
#     if r<0:
#         r =0
#     elif r>255:
#         r=255
#     if g<0:
#         g =0
#     elif g>255:
#         g=255
#     if b<0:
#         b =0
#     elif b>255:
#         b=255
#
#     return '%02X%02X%02X' % (r,g,b)
#
# if __name__=='__main__':
#     print(rgb(-20,275,125))
#     print(rgb(1,2,3))

# from collections import  Counter
#
# def scramble(s1, s2):
#     dct_s1=Counter(s1)
#     dct_s2 = Counter(s2)
#     return dct_s2-dct_s1
#
# if __name__=='__main__':
#     print(scramble('cedewaraaossoqqyt', 'codewarsmmmmmmmm'))

# def pig_it(text):
#     return ' '.join([word[1:]+str(word[0])+'ay' if word.isalpha() else word for word in text.split(' ') ])
#
# if __name__=='__main__':
#     print(pig_it('Hello world !'))


# def zeros(n):
#     number_of_zeros = 0
#     for i in range(1,n):
#         tmp = n // (5**i)
#         number_of_zeros+=tmp
#         if tmp <5:
#             break
#     return number_of_zeros
#
# if __name__=='__main__':
#     print(zeros(6),1)
#     print(zeros(30), 7)
#



