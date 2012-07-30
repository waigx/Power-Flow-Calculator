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

def testCal():
	a = np.mat ( [ [1,2+3j], [3,5] ], dtype=complex )
	return a.I

class MainPage(webapp2.RequestHandler):
	def get(self):
		
		index = jinja_environment.get_template('index.html')
		
		self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write(index.render())

app = webapp2.WSGIApplication(	[( '/' , MainPage )],
								debug=True )