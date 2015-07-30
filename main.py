from google.appengine.ext import ndb
from google.appengine.api import users
import webapp2
import jinja2
import os
import logging

class Person(ndb.Model):
    name_person = ndb.StringProperty(required= True)
    image = ndb.BlobProperty(required = False)
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
            self.redirect('/about')
        else:
            self.redirect(users.create_login_url(self.request.uri))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user_id = users.get_current_user().user_id()
        user_logout= users.create_logout_url ('/')
        category_data = Category.query().fetch()
        category_keys =[]
        for category in category_data:
            category_keys.append(category.key.id())
        template_vars = {'user_id': user_id, 'categories': category_data, "category_keys": category_keys, "user_logout" : user_logout}
        template = jinja2_environment.get_template('templates/index.html')
        self.response.write(template.render(template_vars))

class AddCategoryHandler(webapp2.RequestHandler):
    def post(self):
        category_Name = self.request.get('category_Name')
        user_id = users.get_current_user().user_id()
        category = Category(category_Name = category_Name, user_id = user_id)
        category.put()
        self.redirect('/home')

class AddPersonHandler(webapp2.RequestHandler):
    def get(self):
        category_id = self.request.get('category_id')
        user_logout= users.create_logout_url ('/')
        person_data = Person.query().fetch()
        template_vars = {'category_id': category_id, 'people': person_data, 'user_logout' : user_logout}
        template = jinja2_environment.get_template('templates/category.html')
        self.response.write(template.render(template_vars))
    def post(self):
        name_person = self.request.get('name_person')
        image = str(self.request.get('image'))
        paragraph = self.request.get('paragraph')
        category_id = self.request.get('category_id')
        person = Person(name_person = name_person, image = image, paragraph = paragraph, category_id = category_id )
        person.put()
        self.redirect('/add_person?category_id=' + category_id)

class DeleteCategoryHandler(webapp2.RequestHandler):
    def post(self):
        id_category = self.request.get('keyid')
        k = ndb.Key(Category, int(id_category))
        k.delete()
        self.redirect('/home')

class DeletePersonHandler(webapp2.RequestHandler):
    def post(self):
        id_people = self.request.get('ppl_id')
        k = ndb.Key(Person, int(id_people))
        k.delete()
        self.redirect('/add_person')


class TutorialHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template('templates/tutorial.html')
        self.response.write(template.render())

jinja2_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/home', MainHandler),
    ('/add_category', AddCategoryHandler),
    ('/add_person', AddPersonHandler),
    ('/delete_category', DeleteCategoryHandler),
    ('/delete_person', DeletePersonHandler),
    ('/about', TutorialHandler),
], debug=True)
