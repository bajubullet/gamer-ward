from google.appengine.ext import ndb


GAME_CHOICES = (
  'CS 1.6',
  'DOTA',
  'FIFA',
  'NFS',
  'COD',
  'OTHER'
)

class UserInfo(ndb.Model):
  user = UserProperty(required=True)
  location = ndb.GeoPtProperty(required=True)
  phone = ndb.IntegerProperty()
  games_interested_in = ndb.StringProperty(repeated=True, choices=GAME_CHOICES)
  date_joined = ndb.DateTimeProperty(auto_now_add=True)

  @classmethod
  def all(cls):
    return cls.query()
