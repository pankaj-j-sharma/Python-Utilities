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


# def get_transpose(matrix):

#     transpose_matrix=[]
#     for row in range(len(matrix)):
#         for column in range(len(matrix[row])):
#             if column>=len(transpose_matrix):
#                 transpose_matrix.append([matrix[row][column]])
#             else:                
#                 transpose_matrix[column].append(matrix[row][column])
#     return transpose_matrix


# matrix = [[1, 2], [3,4], [5,6], [7,8]]
# print(get_transpose(matrix))

# def get_transpose(matrix):
#     transpose_matrix=[[0 for j in range(len(matrix)) ] for i in range(len(matrix[0]))]

#     for row in range(len(matrix)):
#         for column in range(len(row)):
#             transpose_matrix[column][row]=matrix[row][column]

#     return transpose_matrix

# matrix = [[1, 2], [3,4], [5,6], [7,8]]
# print(get_transpose(matrix))


# def some_func(default_arg=[]):
#     default_arg.append("some_string")
#     return default_arg

# print(some_func())
# print(some_func())

# list1 = [10, -21, -4, 45, 66, 93, -11]
# print(list(map(lambda x: x<0, list1)))

# a = [1, 2, 3, 4]
# b = a
# a = a + [5, 6, 7, 8]
# print(a)
# print(b)


# a = 1

# def some_func():
#     return a

# def another_func():
#     a += 1
#     return a

    
# print(some_func())
# print(another_func())

# e = 7
# try:
#     raise Exception()
# except Exception as e:
#     pass
# print(e)

# from django.db import models
# class User(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     city = models.CharField(max_length=255)
# orm query to find average age 

# # Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.
# # ArrayList = [-8, -5, -4,-3, -1,0, 2, 1, 5, 6, 8, 10]
# # Explanation: The triplets with zero-sum are
# # 0 + -1 + 1 = 0 and 2 + -3 + 1 = 0
# # Eligible/expected output:
# # (0 -1 1)(2 -3 1)(-8 8 0)etc


# def find_triplets(input_list):
#     running_sum=0
#     input_list
#     result=[]
#     for i in range(0,len(input_list)):
#         for j in range(i+1,len(input_list)):
#             third_num = 0-sum([input_list[i],input_list[j]])
#             for k in range(j+1,len(input_list)):
#                 if sum([input_list[i],input_list[j],input_list[k]])==0:
#                     result.append((input_list[i],input_list[j],input_list[k]))                    
#     return result


# def find_triplets_opt(input_list):
#     inputs = set(input_list)
#     result=[]
#     num_list=[]
    
#     while True:
#         for num in inputs:
#             if len(num_list)<2:
#                 num_list.append(num)            
#             else:
#                 if (0 - sum(num_list)) in inputs:
#                     result.append((*num_list,0 - sum(num_list)))
#                     num_list.clear()
        
#     return result


# if __name__=='__main__':
#     # print(find_triplets([-8, -5, -4,-3, -1,0, 2, 1, 5, 6, 8, 10]))
#     print(find_triplets_opt([-8, -5, -4,-3, -1,0, 2, 1, 5, 6, 8, 10]))


# from statistics import median
# import pandas as pd
# import numpy as np

# def class_grades(students):
#     """
#     :param students: (list) Each element of the list is another list with the 
#       following elements: Student name (string), class name (string), student grade (int).
#     :returns: (list) Each element is a list with the following 
#       elements: Class name (string), median grade for students in the class (float).
#     """
#     results = []
#     df=pd.DataFrame(students,columns=['Name','Class','Grades'])
#     results = df.groupby(['Class']).median()
#     # print(results)
#     return results

# students = [["Ana Stevens", "1a", 5], ["Mark Stevens", "1a", 4], ["Jon Jones", "1a", 2], ["Bob Kent", "1b", 4]]
# print(class_grades(students))


# def find_unique_numbers(numbers):
    
#     return None

# if __name__ == "__main__":
#     print(find_unique_numbers([1, 2, 1, 3]))


# from enum import Enum

# class Side(Enum):
#     none = 0
#     left = 1
#     right = 2

# class ChainLink:

#     def __init__(self):
#         self._left = None
#         self._right = None

#     def append(self, link):
#         if self._right is not None: 
#             raise Exception('Link already connected!')
#         self._right = link
#         link._left = self

#     def longer_side(self):
#         counter_right=0
#         counter_left=0

#         while self._right:
#             self = self._right
#             counter_right+=1

#         while self._left:
#             self = self._left
#             counter_left+=1

#         print(counter_right,' ',counter_left)
#         return None

# if __name__ == "__main__":
#     left = ChainLink()
#     middle = ChainLink()
#     right = ChainLink()
#     left.append(middle)
#     middle.append(right)
#     print(middle)
#     print(left.longer_side() == Side.right)

# import numbers


# class MovingTotal:

#     def __init__(self):
#         self.numbers=[]
#         self.moving_total=[]

#     def append(self, numbers):
#         """
#         :param numbers: (list) The list of numbers.
#         """
#         self.numbers.extend(numbers)
#         for i in range(max(len(self.numbers)-2,0)):
#             self.moving_total.append(sum([self.numbers[i],self.numbers[i+1],self.numbers[i+2]]))


#     def contains(self, total):
#         """
#         :param total: (int) The total to check for.
#         :returns: (bool) If MovingTotal contains the total.
#         """
#         for mv_tot in self.moving_total:
#             if total == mv_tot:
#                 return True
#         return False
    
# if __name__ == "__main__":
#     movingtotal = MovingTotal()
    
#     movingtotal.append([1, 2, 3, 4])
#     print(movingtotal.contains(6))
#     print(movingtotal.contains(9))
#     print(movingtotal.contains(12))
#     print(movingtotal.contains(7))
    
#     movingtotal.append([5])
#     print(movingtotal.contains(6))
#     print(movingtotal.contains(9))
#     print(movingtotal.contains(12))
#     print(movingtotal.contains(7))



# class MovingTotal:


#     def __init__(self):
#         self.numbers=[]
        
#     def append(self, numbers):
#         """
#         :param numbers: (list) The list of numbers.
#         """
#         self.numbers.extend(numbers)

#     def contains(self, total):
#         """
#         :param total: (int) The total to check for.
#         :returns: (bool) If MovingTotal contains the total.
#         """
#         for i in range(max(len(self.numbers)-2,0)):
#             if total == sum([self.numbers[i],self.numbers[i+1],self.numbers[i+2]]):
#                 return True
#         return False
    
    
# if __name__ == "__main__":
#     movingtotal = MovingTotal()
    
#     movingtotal.append([1, 2, 3, 4])
#     print(movingtotal.contains(6))
#     print(movingtotal.contains(9))
#     print(movingtotal.contains(12))
#     print(movingtotal.contains(7))
    
#     movingtotal.append([5])
#     print(movingtotal.contains(6))
#     print(movingtotal.contains(9))
#     print(movingtotal.contains(12))
#     print(movingtotal.contains(7))    


# from typing import Dict, Tuple, Callable, Iterable

# import numpy 

# def model_quadratic(model_parameters: dict):
#     """
#     This is a quadratic model with a minimum at a=0.5, b=0.75, c=0.25.
#     """
#     a = model_parameters['a']
#     b = model_parameters['b']
#     c = model_parameters['c']

#     return 1.75 + (a - 0.5) ** 2 + (b - 0.75) ** 2 + (c - 0.25) ** 2


# class Problem:
#     @staticmethod
#     def grid_search(search_space: Dict[str, Iterable],
#                     scoring_func: Callable[[Dict[str, float]], float]) -> Tuple[float, Dict[str, float]]:
#         """
#         This function accepts a search space, which is a dictionary of arrays.

#         For each key in the dictionary, the respective array holds the numbers in the search space that should be
#         tested for.

#         This function also accepts a scoring_func, which is a scoring function which will return a float score given a
#         certain set of parameters.  The set of parameters is given as a simple dictionary. As an example, see
#         model_quadratic above.
#         """
#         a= search_space['a']
#         b= search_space['b']
#         c= search_space['c']
        
#         cartesian = numpy.transpose([numpy.tile(a, len(b)), numpy.repeat(b, len(a))])
#         final_cartesian = numpy.transpose([numpy.tile(c, len(c)), numpy.repeat(cartesian, len(cartesian))])

#         print('cartesian',final_cartesian)
#         return 1.75, {'a': 0.5, 'b': 0.75, 'c': 0.25}


# print(Problem.grid_search({
#     'a': numpy.arange(0.0, 1.0, 0.05),
#     'b': numpy.arange(0.0, 1.0, 0.05),
#     'c': numpy.arange(0.0, 1.0, 0.05),
# }, model_quadratic))

# from collections import Counter
# import pandas as pd


# def nth_lowest_selling(sales, n):
#     """
#     :param elements: (list) List of book sales.
#     :param n: (int) The n-th lowest selling element the function should return.
#     :returns: (int) The n-th lowest selling book id in the book sales list.
#     """
#     data = pd.Series(sales).value_counts().sort_values().nsmallest(n,keep='first').last_valid_index()
#     # print(data)
#     return data

# if __name__ == "__main__":
#     print(nth_lowest_selling([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))


# class Student:
#     def __init__(self,**kwargs):

#         a=kwargs.get('a')
#         b=...
#         c=...
#         d=...

# str ="HelloWorld"
# str[-2::-2]        

# num =1
# print(num) 
# num2 = num 
# print(num,num2 , id(num),id(num2)) 
# num=3 
# print(num,num2 , id(num),id(num2)) 


# # 1..Pyhton program to replace first occurance of vowels with '-'in a string ,without using dictinaries
# # 2. python program to have count of alphabets ,digits and special characters without using dictionaries

# # 'practice ' => 'pr-ctice'

# def count_types(input):
#     alphabets=0
#     digits=0
#     special_chars=0
#     for i in input:
#         if i.isalpha():
#            alphabets+=1
#         elif i.isnumeric():
#            digits+=1     
#         else :
#             special_chars+=1
#     return alphabets,digits,special_chars


# def replace_vowels(input):
#     vowels = ['a','e','i','o','u']
#     inp_lst = input.split()
#     for i,s in enumerate(inp_lst):
#         if s in vowels:
#             input[i]='-'
#             break 
#     print(inp_lst)
#     return ''.join(inp_lst)

# # print(replace_vowels('practice'))    

# alphabets,digits,special_chars = count_types('pr#c11t1i ce')
# print('alphabets',alphabets)
# print('digits',digits)
# print('special characters',special_chars)



# a = [4, 1, 2, 9, 12, 11]

# for i in range(len(a)-1):
#     for j in range(i, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]

# print(a)

# 2, 4, 8, 16, 32, 64, 128, 256
# 1, 2, 3, 4, 5, 6, 7, 8

# how do you analyse and improve memory performance
# dynamic programming
# how is hash calculated
# design a Dictionary class
# process and a thread in python
# how do you stop a class ineritance
# matrix manipulation , recursion

# flask
# signals in django

# __init_subclass__
# partial functions
# quorum value nosql data
# CAP theoram
# Centry
# CORS headers for DRF
# custom json renderer
# JWT authentication , auth token and refresh token
# secure scret key approaches uuid.uuid4().hex , os.urandom(12) , secrets.token_urlsafe(12)
# JWT token expiration time helps in generating a diffrent token everytime we reauthenticate
# The MIDDLEWARE list is like an onion so each request passes through from top to bottom and
# response is in reverse order (bottom to up).
# middlewares in flask
# implementing 2.7 features of dictionary in python 3.7 where keys are not stored in an order i.e.
# how is Ordereddcit implemented in python ( doubly linked list)
# python rq , asynchronous taks python
# celery

# 1..Pyhton program to replace first occurance of vowels with '-'in a string ,without using dictinaries
# 2. python program to have count of alphabets ,digits and special characters without using dictionaries
# 'practice ' => 'pr-ctice'
# all django exceptions 
# python inheritance 
# microservices benefits 
# usefulness of ec2 
# how do you make call to S3 

# defining entry point of an application def main() and __main__
# adding a mutable datastructure inside a tuple causes tuple immutability to break
# accessing private variable outside of the class _ClassName__variablename
# creating default for dictionary 'defaultdict'
# working of a named argument what if I send one named in between
# reversing a string  str="HelloWorld"  => str[-2::-2] 
# what happens if a.py imports from b.py and c.py and after 
# one execution I delete b.py and then run a.py 
# will it error 

#  JPMC level 1 24/08/2022
# class TestClass:
#     _object_counter=0
#     def __init__(self):
#         TestClass._object_counter+=1

#     @classmethod
#     def get_no_of_objects(cls):
#         return TestClass._object_counter

# cls1 = TestClass()
# cls2 = TestClass()
# cls3 = TestClass()

# print(TestClass.get_no_of_objects())


# import pandas as pd 

# df = pd.DataFrame([{'Type':'Bird','Name':'Sparrow'},{'Type':'Animal','Name':'Dog'}])
# # print(df.head())

# print(df[df['Type']=='Bird'])

# list1= [5,4,3,2,1]

# for i in range(0,len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i] 

# print(list1)

# dct1={'a':1,'b':2,'c':5}
# dct2={'b':2,'c':5,'d':6}

# for k in dct1:
#     if k in dct2:
#         dct2[k]+=dct1[k]
#     else:
#         dct2[k]=dct1[k]
# print(dct2)


# def logger(f):
#     def wrapper(*args,**kwargs):
#         print('fn started',f.__name__)
#         result = f(*args,**kwargs)
#         print(result)
#         return result
#     return wrapper

# @logger
# def add(a,b):
#     return a+b    

# Provided is the list of string and each string is a combination of
# - search keyword
# - count of occurrence
# - string to search from

# Input:

# ['a 1: ashish',
# 'aa 2: aassddaacc',
# 'c 5: bat',
# 'z 2: zebra']

# Validation:

# 'a 1: ashish' : valid
# 'aa 2: aassddaacc' : valid
# 'c 5: bat' : invalid
# 'z 2: zebra' : invalid



# Output:

# Return a list of valid and invalid strings based on conditions satisfied

# ['valid', 'valid', 'invalid', 'invalid']

# def find_valid_string(list_input):
#     response = []
#     for str in list_input:
#         str_split = str.split(':')
#         search_keyword,count  = (str_split[0].split(' '))
#         search_string = str_split[-1]
#         # print('search_keyword',search_keyword,'str count',count,'search_string',search_string,'lst count',search_string.count(search_keyword))

#         if search_string.count(search_keyword) == int(count):
#             response.append('valid')
#         else:
#             response.append('invalid')
#     return response

# print(find_valid_string(['a 1: ashish','aa 2: aassddaacc','c 5: bat','z 2: zebra']))

# list1 = [1,2,3,4,5,[8,9]]
# list2 = list1 # shallow
# list3 = list1.copy()
# list4 = list1[:] 
# list4[-1]=10
# print(list1,list4)

# for i in [1,2,2,2]:
#     print(1)
# else:
#     print('else')

# def gen_elements(num):
#     for ele in range(num):
#         yield ele

# print([i for i in gen_elements(10)])

# class A :
#     def __init__(self,str_data):
#         self.data = str_data
#         self.name = ''


#     def __add__(self,obj):
#         if isinstance(self.data,str) or isinstance(obj.data,str) :
#             raise 'String Not allowed '            
#         return int(self.data)+ obj.data 




# obj1 = A("a")
# obj2 = A(20)

# print(obj1 + obj2)




# Problem statement 1 :


# Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.
# ArrayList = [-8, -5, -4,-3, -1,0, 2, 1, 5, 6, 8, 10]
# Explanation: The triplets with zero-sum are
# 0 + -1 + 1 = 0 and 2 + -3 + 1 = 0
# Eligible/expected output:
# (0 -1 1)(2 -3 1)(-8 8 0)etc
# Not eligible :
# (-4,2,2)
# (-2,1,1)
# (8, -2,2)
# (0 -1 1) ,(1 0 -1)
# ArrayList = {-8, -5, -4,-3, -1,0, 2, 1, 5, 6, 8, 10}


# Problem statement 2:

# A list of strings. Remember that spaces count as characters. So, "abc" and “cab” are technically anagrams, since "abc" and“cab” Output

# A list of lists where all pairs of anagrams grouped together

# {“cat”, “dog”, “tac”, “god”, “act”, “abc”, “cab”, “fed”, “def”}
# ##A list of strings. Remember that spaces count as characters.
# ##So, " abc" and “cab” are technically anagrams, 
# "abc" and“cab ” are not anagrams there is a space


# Problem statement 3:

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]


# Problem statement3:

# ​​You are given an integer array nums that is sorted in non-decreasing order.
# Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:
# Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
# All subsequences have a length of 3 or more.
# Return true if you can split nums according to the above conditions, or false otherwise.
# A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).
#  Example 1:
# Input: nums = [1,2,3,3,4,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,5] --> 1, 2, 3
# [1,2,3,3,4,5] --> 3, 4, 5

# Example 2:
# Input: nums = [1,2,3,3,4,4,5,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5


# Example 3:
# Input: nums = [1,2,3,4,4,5]
# Output: false
# Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.


# Problem statement 3:


# Check if array can be divided into two subsequences merging whom makes Array sorted


# Given an integer array A[] of size N, the task is to check if the array can be divided into two subsequences such that appending one of them at the end of the other makes the array sorted.
# A sub-sequence is a sequence that can be obtained from the array by deleting some or no elements from it. It may or may not be a continuous part of an array.
# Examples:
# Input: arr[] = {1, 4, 5, 2, 3, 4}
# Output: Yes
# Explanation :
# First Sub-Sequence (P) :  {1, 2, 3, 4};
# Second Sub-Sequence (Q) : {4, 5};
# Merging both Sub-Sequence Gives Sorted Array: 
# P+Q = {1, 2, 3, 4} + {4, 5} = {1, 2, 3, 4, 4, 5}
# Input: arr[] = {1, 4, 6, 3, 5}
# Output: No


# In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, the second transaction can only start after the first one is complete (Buy->sell->Buy->sell). Given stock prices throughout the day, find out the maximum profit that a share trader could have made.
# Examples: 
# Input:   price[] = {10, 22, 5, 75, 65, 80}
# Output:  87
# Trader earns 87 as sum of 12, 75 
# Buy at 10, sell at 22, 
# Buy at 5 and sell at 80
# Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
# Output:  100
# Trader earns 100 as sum of 28 and 72
# Buy at price 2, sell at 30, buy at 8 and sell at 80
# Input:   price[] = {100, 30, 15, 10, 8, 25, 80};
# Output:  72
# Buy at price 8 and sell at 80.
# Input:   price[] = {90, 80, 70, 60, 50}
# Output:  0
# Not possible to earn.


#         while(lo<hi &&(num[lo]==num[lo+1])) lo++
    
# Problem statement 2:

# Given two linked lists, insert nodes of second list into first list at alternate positions of first list. 
# For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list should only be inserted when there are positions available. For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.
# Use of extra space is not allowed (Not allowed to create additional nodes), i.e., insertion must be done in-place. Expected time complexity is O(n) where n is number of nodes in first list.


# A = [5,7,17,13,11]
# B = [12,10,2,4,6]
# C = [a0,b0]




# Problem 3:

# Given a linked list, check if the linked list has loop or not. Below diagram shows a linked list with a loop. 
 


# A = [1,2,3,4,5,2]
 


# LLD Stock market 

# 1.) Buy
# 2. Sell
# 3. Cancel Request


# Request: 
# User Details. 
# Timestamp requested. 
# Stock (MSFT)
# Amount
# Price
# Boolean buy / sell

# Stock = Class
# Timeseries<Price> price; 
# String stockName; 
# String id; 

# User: Person
# 	Name
# 	Email 

# RequestInSystem
# 	kalfaMappingId; 
# 	UserId;

# User Accounts: Person -> (Adapter patter)
# 	User userDetails; 
# 	Collection<Stock> owned; 
# 	Collection<RequestInSystem> requests; 



# DB Design. 

# Transaction
# 	ID - PK ,AI
# 	PriceBoughtAt
# 	User - FK
# 	TransactionId
# 	Stock - FK
# 	Quantity
# 	TimestampCreated
# 	TimestampUpdated

# User
# 	UserID - PK, AI
# 	UserEmail - 
# 	Name
# 	KYC - FK
# 	AccountStatus - ENUM
# 	Password

# Stock
# 	ID - PK, AI (5000)
# 	StockName
# 	Listing - FK

# Listing 
# 	Id - PK, AI
# 	StockExchange - NSE, BSE, 
# 	LastKnownPrice - 
	
	
	


# StockPrice - Volatile (InMemory)
# 	ID - PK
# 	DBId - FK
# 	BlockingQueue<LastKnownPrice> 


# Given a string sequence say “abbbccdeaab” replace sequentially repeating characters with a single character and return the string “abcdeab”.
# Input:
# 	“abbbccdeaab”

# Output:
# 	“abcdeab”

# 1. iterate one by one 
# 2. store the current char in list
# 3. if the element already present then skip
# 4. return

# def replace_sequential_characters(data):
#     elements=[]
#     for lt in data:
#         if elements and lt == elements[-1]:
#             continue
#         else:
#             elements.append(lt)
#     return "".join(elements)

# print(replace_sequential_characters("abbbccdeaab"))


# Check if there is any subarray with 0 sum. If yes, can you list these subarrays:

# Input: [4, 2, -3, 1, 6, -6, -1]
# Output: [2,-3,1], [2, -3, 1, 6, -6] ,[1,6,-6,-1], [6,-6]

# 1. initialise current_sum=0
# 2. iterate on first element , then add 

# def find_subarray(data):
#     sub_arr=[]
#     current_sum=0
#     for i,num1 in enumerate(data):
#         current_sum = 0
#         for j,num2 in enumerate(data):
#             current_sum+=num2            
#             if current_sum==0:
#                 tmp = data[:j]
#                 print(tmp)
#                 sub_arr.append(data[:j])
#                 break
#     return sub_arr

# print(find_subarray([4, 2, -3, 1, 6, -6, -1]))  


# event driven architecture vs pub - sub based architecture
# saml or sso authentication mechanism
# django signals 
# aws glue vs lambda 
# abstraction
# extension methods 

# a = [4, 1, 2, 9, 12, 11]

# for i in range(len(a)-1):
#     for j in range(i, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]

# print(a)

# 2, 4, 8, 16, 32, 64, 128, 256
# 1, 2, 3, 4, 5, 6, 7, 8

# how do you analyse and improve memory performance
# dynamic programming
# how is hash calculated
# design a Dictionary class
# process and a thread in python
# how do you stop a class ineritance
# matrix manipulation , recursion

# flask
# signals in django

# __init_subclass__


# # employee -> id,name
# # dept -> id , name 
# # employee_dept -> id,emp_id,dept_id

# # all employees for dept 
# select * 
# from 
# employee emp 
#     inner join 
# employee_dept ed 
# on emp.id=ed.emp_id
# where 
# ed.dept_id is not null 
# and 
# ed.dept_id = 1 

# # all dept for an employee 
# select * 
# from 
# dept dt 
#     inner join 
# employee_dept ed 
# on dt.id=ed.dept_id
# where dt.emp_id = 1 


# import pytest
# import main

# check for pep8 standards
# pip install pep8
# pip install pycodestyle

# check for pylint style
# pylint ./Interviews

# check for pytest 
# pytest test.py


# @pytest.fixture
# def setup_class():
#     return main.Human("Ciri",18,"female")

# def test_speak(setup_class) :
#     assert setup_class.speak()== "Hello everyone! I am Ciri"   

# def test_bring_food(setup_class,mocker) :
#     mock_patch = mocker.patch("main.requests.get")
#     mock_patch.return_value.status_code=200
#     assert setup_class.bring_food()== 200   

# def test_eat(setup_class) :
#     assert setup_class.eat("momos")== "I love to eat momos!!!" 



# '''main module for Human class'''
# import requests

# class Human:
#     '''Human class '''
#     #class attribute
#     species = "Homo Sapiens"
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     #Instance Method
#     def speak(self):
#         '''function for speak'''
#         return f"Hello everyone! I am {self.name}"

#     def bring_food(self):
#         '''function for bring food'''
#         print("bring food called")
#         google = requests.get("http://127.0.0.1:8001/?search="+self.name,timeout=60)
#         return google.status_code

#     #Instance Method
#     def eat(self, favourite_dish):
#         '''function for eat'''
#         return f"I love to eat {favourite_dish}!!!"


# if __name__=='__main__':
#     x = Human("Ciri",18,"female")
#     print(x.speak())
#     print(x.eat("momos"))
#     print(x.bring_food())


# class MockResponseExisting: # 1

#     def __init__(self) -> None:
#         self.status_code=200

#     @staticmethod
#     def json():
#         return {'success':True} 


# class TestHuman:

#     @pytest.fixture
#     def setup_human(self):
#         return main.Human("Ciri",18,"female")

#     def test_bring_food_mocker(self,setup_human,mocker) :
#         mock_patch = mocker.patch("main.requests.get")
#         mock_patch.return_value.status_code=200
#         assert setup_human.bring_food()== 200   

#     def test_bring_food_monkeypatch(self,setup_human,monkeypatch) :

#         def mock_get(*args, **kwargs):
#             return MockResponseExisting() 

#         monkeypatch.setattr(main.requests, "get", mock_get)
#         assert setup_human.bring_food()== 200   

#     def test_bring_food_complete_patch(self,setup_human,mocker) :
#         mocker.patch("main.Human.bring_food",return_value=200)
#         assert setup_human.bring_food()== 200   

#     def test_eat(self,setup_human) :
#         assert setup_human.eat("momos")== "I love to eat momos!!!" 

#     def test_init(self):        
#         human_obj = main.Human("pankaj",18,"male")
#         assert human_obj.name =="pankaj"
#         assert human_obj.age ==18
#         assert human_obj.gender =="male"

#     def test_speak(self,setup_human) :
#         assert setup_human.speak()== "Hello everyone! I am Ciri"         