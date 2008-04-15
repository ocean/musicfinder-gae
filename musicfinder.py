#!/usr/bin/env python
# encoding: utf-8
"""
musicfinder.py

Created by Drew Robinson on 2008-04-15.
Copyright (c) 2008 FYG. All rights reserved.
"""

import cgi
import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp

class Search(webapp.RequestHandler):
  def get(self):
    self.response.out.write("""
      <html>
        <body>
          <form action="/search" method="post">
            <div><input type="text" name="content"></input></div>
            <div><input type="submit" value="Search"></div>
          </form>
        </body>
      </html>""")


class Results(webapp.RequestHandler):
  def post(self):
    self.response.out.write('<html><body>You searched for:<pre>')
    self.response.out.write(cgi.escape(self.request.get('content')))
    self.response.out.write('</pre></body></html>')

def main():
  application = webapp.WSGIApplication(
                                       [('/', Search),
                                        ('/search', Results)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()

