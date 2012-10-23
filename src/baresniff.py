import webapp2
import simplejson
import logging
import json

from google.appengine.ext import db
from google.appengine.api import users

log = logging.getLogger('webapp')

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
        <html>
           <body>
              Welcome to baresniff : try api's 
           </body>
            </html>""")

class Place(db.Model):
    location = db.StringProperty(multiline=True)

class User(db.Model):
    name = db.StringProperty()
    sex = db.BooleanProperty()

class AuditTrail(db.Model):
    createdBy = User()
    modifiedBy = User()
    createdAt = db.DateTimeProperty(auto_now_add=True)
    modifiedAt = db.DateTimeProperty(auto_now_add=True)

class Activity(db.Model):
    action = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    place = Place()
    auditTrail = AuditTrail()
    
    def to_dict(self):
       return dict([(p, unicode(getattr(self, p))) for p in self.properties()])

def baresniff_key(baresniff_name=None):
    """creating db key """
    return db.Key.from_path('Baresniff', baresniff_name or 'thisisit')

class RootHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>This is baresniff home page</pre></body></html>')

class ActivitiesHandler(webapp2.RequestHandler):
    
    def get(self):

        # Get all the activities
        activity_query = Activity.all()
        for w in activity_query.run():
            print w.action
        
        #activities = activity_query.fetch(10, 0)
        
        simpactivities = db.GqlQuery("SELECT * "
                "FROM Activity "
                "WHERE ANCESTOR IS :1 ",
                baresniff_key())
        
        #print(activities.count(10), " activities found")
        print(simpactivities.count(10), " simp activities found")
        
        #for activity in activities:
            #print(activity.place.location)
            
        self.response.write(json.dumps([p.to_dict() for p in simpactivities]))   

    def post(self):

        userdict = simplejson.loads(self.request.body)
        activity = Activity(parent=baresniff_key(),**userdict)
        
        #print(activity.action)
        #print(activity.place.location)
        
        print("%s is the id of activity", str(activity.put().id()))
        
        #self.request.rawpost_data
        
        #Returns the ID that was created
        self.response.write(str(activity.put().id()))
        
        #post the activity
        activity.put()
        self.response.out.write(activity.parent_key())

    def delete(self):
        Activity.delete(self)
        
class testclass():
    def testmethod(self, *args,**kwargs):
        print(args)
        



class ActivityHandler(webapp2.RequestHandler):
    def get(self,product_id):
        self.response.out.write('<html><body>')
        
        # Get all the activities
        activity = db.GqlQuery("SELECT * "
                "FROM Activity "
                "WHERE ANCESTOR IS :1 "
                "ORDER BY date DESC LIMIT 10",
                baresniff_key())
        
        self.response.out.write(product_id)
        self.response.out.write('</body></html>')

    def put(self,product_id):
        self.response.out.write('<html><body>')
        
        # Get all the activities
        activity = db.GqlQuery("SELECT * "
                "FROM Activity "
                "WHERE ANCESTOR IS :1 "
                "ORDER BY date DESC LIMIT 10",
                baresniff_key())
        
        self.response.out.write(product_id)
        self.response.out.write('</body></html>')

    def delete(self,product_id):
        self.response.out.write('<html><body> deleting activity : <pre>')
        self.response.out.write(product_id)
        self.response.out.write('</pre></body></html>')


app = webapp2.WSGIApplication([('/', MainPage),
                   ('/baresniff',RootHandler),
                   ('/baresniff/activities',ActivitiesHandler),
                   ('/baresniff/activities/(\d+)',ActivityHandler)],
                   debug=True)
