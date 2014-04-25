import os
import webapp2
import jinja2

from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
      user = users.get_current_user()
      if user:
        template_values = {
          'auth_url': users.CreateLogoutURL(self.request.uri),
          'auth_text': 'Sign out',
          'user_email': user.email(),
          'user_nickname': user.nickname(),
        }
      else:
        template_values = {
          'auth_url': users.CreateLoginURL(self.request.uri),
          'auth_text': 'Sign in',
          'user_email': '',
          'user_nickname': '',
        }
      template = JINJA_ENVIRONMENT.get_template('index.html')
      self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
