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
import json

class Person(ndb.Model):
    name_person = ndb.StringProperty(required= True)
    image = ndb.BlobProperty(required = False)
    paragraph = ndb.StringProperty(required = False)

class Category(ndb.Model):
    category_Name = ndb.StringProperty(required=True)
    people = ndb.StructuredProperty(Person, repeated = True)


class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    # categories = ndb.LocalStructuredProperty(Category, repeated = True)


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template= jinja2_environment.get_template("/templates/user.html")
            self.response.write(template.render())
        else:
            greeting = ('<a href= "%s"> Sign in or register</a>.' % users.create_login_url('/'))
            self.response.write('<html><body>%s</body></html>' % greeting)

class AddUserHandler(webapp2.RequestHandler):
    def post(self):
        name= self.request.get('name')
        user = User(name=name)
        user.put()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template("/templates/index.html")
        self.response.write(template.render())

class CreateCategoryHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template('/templates/index.html')
        self.response.write(template.render())

class AddCategoryHandler(webapp2.RequestHandler):
    def post(self):
        category_Name = self.request.get('category_Name')
        category = Category(category_Name = category_Name)
        category.put()
        template_vars = {'category': category}
        template = jinja2_environment.get_template('category.html')
        self.response.write(template.render(template_vars))

class CreatePersonHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template('/templates/category.html')
        self.response.write(template.render())

class AddPersonHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        name_person = self.request.get('name_person')
        image = str(self.request.get('image'))
        paragraph = self.request.get('paragraph')
        person = Person(name_person= name_person, image = image, paragraph = paragraph)
        person.put()
        template_vars = {'person': person}
        template = jinja2_environment.get_template('templates/category.html')
        self.response.write(template.render(template_vars))
        self.response.write(person.name_person + ' was created')
        self.response.write('<a href = /create_person> Create another Person </a>')
        self.response.write('<a href = /> Back to Homepage </a>')
        self.response.write('<a href = /category> Back to Category </a>')

jinja2_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/add_user', AddUserHandler),
    ('/category', CreateCategoryHandler),
    ('/add_category', AddCategoryHandler ),
    ('/create_person', CreatePersonHandler),
    ('/add_person', AddPersonHandler),

], debug=True)
