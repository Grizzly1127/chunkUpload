#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado.web
#from handlers.home import BaseHandler

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home/index.html', error=None, email='')