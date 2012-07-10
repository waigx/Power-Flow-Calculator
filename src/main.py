#encoding:UTF-8  
'''
Created on 2012-6-28
Last updated on 2012-6-27

@author: Igor Wang 
@contact: igor@igorw.org
@version: 0.0
'''

import webapp2
import numpy as np
import pflib.gaussSeidel
import pflib.newtonRaphson


def testCal():
	a = np.mat ( [ [1,2+3j], [3,5] ], dtype=complex )
	return a.I

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write("""
<html>
	<head>
		<link rel="shortcut icon" href="/favicon.ico">
		<link rel="apple-touch-icon" href="/favicon.ico">
	</head>
	<body>
		""")
		self.response.write( "<pre><code>"+str(testCal())+"</code></pre>" )
		self.response.write("""
		<hr />
		<table width="100%">
			<tr valign="top">
				<td align="left">&copy; Igor Wang</td>
				<td align="right">
					<img src="https://developers.google.com/appengine/images/appengine-noborder-120x30.gif" 
alt="Powered by Google App Engine" />
				</td>
			</tr>
		</table>
	</body>
</html>	
		""")

app = webapp2.WSGIApplication(	[( '/' , MainPage )],
								debug=True )