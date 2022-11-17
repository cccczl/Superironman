#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = f"<h1>Hello, {environ['PATH_INFO'][1:] or 'web'}!</h1>"
    return [body.encode('utf-8')]
