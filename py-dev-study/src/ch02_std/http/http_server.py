'''
Created on Apr 14, 2015

@author: dev

Python内置了一个简单的HTTP服务器，
python -m SimpleHTTPServer 80
后面的80端口是可选的，不填会采用缺省端口8000。注意，这会将当前所在的文件夹设置为默认的Web目录，试着在浏览器敲入本机地址：
http://localhost:80

Python版FTP服务器

pip install pyftpdlib
python -m pyftpdlib -p 21
后面的21端口依然是可选的，不填会随机一个，被占用的端口将跳过。在浏览器敲入本机地址：
ftp://localhost:21
'''
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()