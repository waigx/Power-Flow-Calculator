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
import core.newtonRaphson as nr
import time
import numpy as np

Language = 0

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

pageInfo = {
    'Version'       :'0.0.0 (Alpha)'    ,
    'LastUpdate'    :'Aug. 8, 2012'     ,
    'Language'      :Language           ,
}

def languageChanged( request ):
    if request.query_string == 'en':
        Language = 0
    if request.query_string == 'cn':
        Language = 1
    
    pageInfo.update({
    'Language'    :Language             ,
    })
    
        
def isMobileDevice( ua ):
    isM = False
    if 'Mobile' in ua:
        isM = True
    return isM

def powerflowcal( inputData ):

    result = nr.newtonRaphson( inputData['Y'] , inputData['S'] , inputData['UPri'] , inputData['UAcc'] , inputData['accu'] , inputData['echoLevel'] , inputData['maxIteration'] )

    return result

class MainPage(webapp2.RequestHandler):
    def get(self):
        
        #if isMobileDevice(str(self.request.headers['User-Agent'])):
        #   self.redirect('/m/')
                
        if self.request.query_string:
            languageChanged(self.request)
            self.redirect(self.request.path)  
        
        index = jinja_environment.get_template('pages/index.html')

        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(index.render( pageInfo ))

class MainPageM(webapp2.RequestHandler):
    def get(self):
        
        if self.request.query_string:
            languageChanged(self.request)
            self.redirect(self.request.path)        
        
        index = jinja_environment.get_template('pages/m/index.html')
                
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(index.render( pageInfo ))

class MainPagem(webapp2.RequestHandler):
    def get(self):
        
        self.redirect('/m/')

class ReturnResult(webapp2.RequestHandler):
    def post(self):
        currentTime = time.time()
        
        if self.request.query_string:
            languageChanged(self.request)
            self.redirect(self.request.path)
        
        resultPage = jinja_environment.get_template('pages/result.html')
        self.response.headers['Content-Type'] = 'text/html'
        
        Y = np.matrix("".join(str(self.request.get('Y')).split()),dtype=np.complex)
        S = np.matrix("".join(str(self.request.get('S')).split()),dtype=np.complex)
        UPri = np.matrix("".join(str(self.request.get('UPri')).split()),dtype=np.complex)
        UAcc = np.matrix("".join(str(self.request.get('UAcc')).split()),dtype=np.complex)
        accu = float(self.request.get('accu'))
        echoLevel = int(self.request.get('echoLevel'))
        maxIteration = float(self.request.get('maxIteration'))
        
        inputData = {
            'Y'             :Y              ,
            'S'             :S              ,
            'UPri'          :UPri           ,
            'UAcc'          :UAcc           ,
            'accu'          :accu           ,
            'echoLevel'     :echoLevel      ,
            'maxIteration'  :maxIteration   ,
        }
        
        [result,debuginfo] = powerflowcal(inputData)
        
        timeUseage = time.time() - currentTime
        
        resultObject = {
            'output'        :debuginfo      ,
            'result'        :result         ,
            'echoLevel'     :1              ,
            'timeUseage'    :timeUseage     ,
        }
        
        resultObject.update(pageInfo)
        
        self.response.out.write(resultPage.render( resultObject ))
        
class AboutPage(webapp2.RequestHandler):
    def get(self):
        
        if self.request.query_string:
            languageChanged(self.request)
            self.redirect(self.request.path)
        
        index = jinja_environment.get_template('pages/about.html')
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(index.render( pageInfo ))

class HelpPage(webapp2.RequestHandler):
    def get(self):
        
        if self.request.query_string:
            languageChanged(self.request)
            self.redirect(self.request.path)
        
        index = jinja_environment.get_template('pages/help.html')
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(index.render( pageInfo ))

class AboutPageM(webapp2.RequestHandler):
    def get(self):
        
        if self.request.query_string:
            languageChanged(self.request)
            self.redirect(self.request.path)
        
        index = jinja_environment.get_template('pages/m/about.html')

        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(index.render( pageInfo ))
        
app = webapp2.WSGIApplication([ (   '/'             ,MainPage           ),
                                (   '/result'       ,ReturnResult       ),
                                (   '/about/'       ,AboutPage          ),
                                (   '/help/'        ,HelpPage           ),
                                (   '/m'            ,MainPagem          ),
                                (   '/m/'           ,MainPageM          ),
                                (   '/m/about/'     ,AboutPageM         )],
								debug=True )