#encoding:UTF-8  
'''
Created on 2012-6-28
Last updated on 2012-6-27

@author: Igor Wang 
@contact: igor@igorw.org
@version: 0.0
'''

import webapp2
import jinja2
import os
import numpy as np

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

def isMobileDevice( ua ):
    isM = False
    if 'Mobile' in ua:
        isM = True
    return isM

class MainPage(webapp2.RequestHandler):
    def get(self):
        
        #if isMobileDevice(str(self.request.headers['User-Agent'])):
        #   self.redirect('/m/')
        
        index = jinja_environment.get_template('pages/index.html')
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(index.render())

class MainPageM(webapp2.RequestHandler):
    def get(self):
        
        index = jinja_environment.get_template('pages/m/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(index.render())

class MainPagem(webapp2.RequestHandler):
    def get(self):
        
        self.redirect('/m/')
        
app = webapp2.WSGIApplication([ (   '/'     ,MainPage   ),
                                (   '/m'    ,MainPagem  ),
                                (   '/m/'   ,MainPageM  )],
								debug=True )