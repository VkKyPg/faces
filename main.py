#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.ext import ndb
from google.appengine.api import users
import webapp2
import jinja2
import os

class Person(ndb.Model):
    name = ndb.StringProperty(required= True)
    image = ndb.BlobProperty(required = False)
    paragraph = ndb.TextProperty(required = False)

class Category(ndb.Model):
    categoryName = ndb.StringProperty(required=True)
    people = ndb.StructuredProperty(Person, repeated)

class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    categories = ndb.StructuredProperty(Category, repeated= True)

class loadCategoryPage(webapp2.RequestHandler):
    def get(self):
        query = Category
        instagram2 = []
        id_category = self.request.get()
        id_people = self.response.get()
        instagram2.append()

class LoginHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja2_environment.get_template("templates/index.html")
        self.response.write(template.render())
        user = users.get_current_user()

        template = jinja2_environment.get_template("templates/login.html")
        user= users.get_current_user()

        if user:
            greeting = ('Welcome, %s! (<a href=%s>sign_out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting= ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/'))
        self.response.write('<html><body>%s</body></html>' % greeting)

class CreateUser(webapp2.RequestHandler):
    def get(self):
        template= jinja2_environment.get_template("/templates/user.html")
        self.response.write(template.render())

class AddUserHandler(webapp2.RequestHandler):
    def post(self):
        name= self.request.get('name')
        user= User(name=name)
        user.put()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template("templates/index.html")
        self.response.write(template.render())

class CreateCategoryHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template('/templates/index.html')
        self.response.write(template.render())

class AddCategoryHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('categoryName')
        category = Category(name=name)
        category.put()
        self.response.write("Category was created")


class CreatePersonHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template('/templates/category.html')
        self.response.write(template.render())

class AddPersonHandler(webapp2.RequestHandler):
        def post(self):
            name=self.request.get('name')
            person = Person(name=name)
            person.put()
            self.response.write(person.name + ' was created')
            self.response.write('<a href = /create_person> Create another Person </a>')
            self.response.write('<a href = /> Back to Homepage </a>')
            self.response.write('<a href = /category> Back to Category </a>')

class AddUserHandler(webapp2.RequestHandler):
    def post(self):
        name= self.request.get('name')
        user= User(name=name)
        user.put()

jinja2_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/create_person', CreatePersonHandler),
    ('/add_person', AddPersonHandler),
    ('/category', CreateCategoryHandler),
    ('/login', LoginHandler),
], debug=True)
