from google.appengine.ext import ndb
from google.appengine.api import users
import webapp2
import jinja2
import os
import logging

class Person(ndb.Model):
    name_person = ndb.StringProperty(required= True)
    image = ndb.StringProperty(required = False)
    paragraph = ndb.StringProperty(required = False)
    category_id = ndb.StringProperty(required = False)

class Category(ndb.Model):
    category_Name = ndb.StringProperty(required=True)
    people = ndb.StructuredProperty(Person, repeated = True, required = False)
    user_id = ndb.StringProperty(required = True)

class User(ndb.Model):
    name_id = ndb.StringProperty(required=True)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            name_id = user.user_id()
            user = User(name_id = name_id)
            user.put()
            self.redirect('/home')
        else:
            self.redirect(users.create_login_url(self.request.uri))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template("templates/index.html")
        self.response.write(template.render())

class AddCategoryHandler(webapp2.RequestHandler):
    def post(self):
        category_Name = self.request.get('category_Name')
        user_id = users.get_current_user().user_id()
        category = Category(category_Name = category_Name, user_id = user_id)
        category_data = Category.query().fetch()
        category.put()
        category_data.append(category)
        template_vars = {'user_id': user_id, 'categories': category_data}
        template = jinja2_environment.get_template('templates/index.html')
        self.response.write(template.render(template_vars))

class AddPersonHandler(webapp2.RequestHandler):
    def get(self):
        category_id = self.request.get('category_id')
        temp_vars = {'category_id': category_id}
        template = jinja2_environment.get_template('templates/category.html')
        self.response.write(template.render(temp_vars))
    def post(self):
        name_person = self.request.get('name_person')
        image = self.request.get('image')
        paragraph = self.request.get('paragraph')
        category_id = self.request.get('category_id')
        if name_person.strip() == "":
            name_person = "Anonymous"
        person = Person(name_person = name_person, image = image, paragraph = paragraph, category_id = category_id )
        person_data = Person.query().fetch()
        person.put()
        person_data.append(person)
        template_vars = {'category_id': category_id, 'people':person_data}
        template = jinja2_environment.get_template('templates/category.html')
        self.response.write(template.render(template_vars))


jinja2_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/home', MainHandler),
    ('/add_category', AddCategoryHandler),
    ('/add_person', AddPersonHandler),
], debug=True)
