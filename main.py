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


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user= users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href=%s>sign_out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting= ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/'))
        self.response.write('<html><body>%s</body></html>' % greeting)

class Category(ndb.Model):
    name = ndb.StringProperty(required=True)
    id_list_of_people = ndb.IntegerProperty(repeated=True)

class Person(ndb.Model):
    name_person = ndb.StringProperty(required= True)
    image = ndb.BlobProperty(required = True)
    paragraph = ndb.TextProperty(required = False)


class CreatePersonHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template('/templates/category.html')
        self.response.write(template.render())

class AddPersonHandler(webapp2.RequestHandler):
    def post(self):
        name_person = self.request.get('name_person')
        image = self.request.get('image')
        paragraph = self.request.get('paragraph')
        person = Person(name_person = name_person, image = image, paragraph = paragraph)
        person.put()

class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    id_list_of_categories= ndb.StringProperty(repeated=True)

class CreateUser(webapp2.RequestHandler):
    def get(self):
        template= jinja2_environment.get_template("/templates/user.html")
        self.response.write(template.render())

class AddUserHandler(webapp2.RequestHandler):
    def post(self):
        name= self.request.get('name')
        user= User(name=name)
        user.put()

jinja2_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/create_user', CreateUser),
    ('/add_user', AddUserHandler),
    ('/create_person', CreatePersonHandler),
    ('/add_person', AddPersonHandler),
], debug=True)
