#!/usr/bin/env python
from __future__ import unicode_literals
from http.server import BaseHTTPRequestHandler, HTTPServer
import youtube_dl
ydl_opts = {
    'outtmpl': './%(id)s.%(ext)s',

    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message1 = "<html><head>  <meta charset=\"UTF-8\"></head><body><form method=\"POST\">"
        message2 = message1 + "<input type=\"text\" name=\"emlak\"><button type=\"submit\"> Gonder </button> "
        message3 = message2 + "</form></body> </html>";
        # Write content as utf-8 data
        self.wfile.write(bytes(message3 ,"utf8"))
        return
  def do_POST(self):
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        selta=post_data.decode('utf-8').split("=")[1]
        selta=selta.replace("%2F", "/")
        selta=selta.replace("%3A",":")
        selta=selta.replace("%3F","?")
        selta=selta.replace("%3D","=")
        vid=selta.split("v=")[1]
        print(selta)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            #ydl.download([selta])
             info_dict = ydl.extract_info(selta, download=True)
             print(info_dict.get('title', None))
             with open("liste.txt","a") as myfile:
                  myfile.write(info_dict.get('title',None )+";"+vid+".mp3\n")
        self.wfile.write(bytes('<a href="http://31.14.134.50/download/'+vid+"\">Download Click </a>", "utf8"))
def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
