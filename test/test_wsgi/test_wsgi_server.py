#coding=utf-8
#@Author:Administrator
#@date:2019/11/19   17:36

from wsgiref.simple_server import make_server

def home_func(environ):
    with open('test_wsgi_home.html','rb') as f:
        data = f.read()

        return [data]

def login_func():
    pass

def routers():
    urlpatterns = (
        ('/home',home_func),
        ('/login',login_func)
    )
    return urlpatterns


def application(environ, start_response):
    print(environ['PATH_INFO'])
    path = environ['PATH_INFO']     # '/home'
    start_response('200 OK',[('Content-Type','text/html')])

    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return ['<h1>404<h1>'.encode('utf8')]

httpd = make_server('',8090,application)
print('Servering HTTP on port 8090...')

httpd.serve_forever()
