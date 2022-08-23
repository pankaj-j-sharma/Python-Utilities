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
