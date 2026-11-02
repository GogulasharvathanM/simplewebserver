from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title> Laptop Configration Details </title>
    </head>
    <body  bgcolor="">
        <center>
            <h2> Gogulasharvathan M </h2>
            <h3>26018286</h3>
        
        <table border="8"
        cellspacing="2"
        cellpadding="15">
        <caption> <h1>Student Laptop Information<h1> </caption>

         <tr>
            <th>Device Name</th>
            <th>Processor</th>
            <th>Installed RAM</th>
            <th>Graphics Card</th>
            <th>Storage</th>
            <th>Device Id</th>
            <th>Product Id</th>
           <th>System Type</th>
           <th>Pen and Touch</th> </tr>
        <tr>
            <td>TL15-53M-G2</td>
            <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
            <td>16.0 GB (15.7 GB usable)</td>
            <td>Intel(R) Graphics (128 MB)</td>
            <td>131 GB of 477 GB used</td>
            <td>87AA3287-A8AD-42F6-A565-72EEA5673D02</td>
            <td>00342-42943-38934-AAOEM</td>
            <td>64-bit operating system, x64-based processor</td>
            <td>No pen or touch input is available for this display</td>
        </tr>
        
        </center>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()