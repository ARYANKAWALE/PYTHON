import cgi

# Get form data
data = cgi.FieldStorage()
make = data.getvalue('make')
model = data.getvalue('model')

# Send response to browser
print('Content-type:text/html\r\n\r\n')
print('<!DOCTYPE HTML>')
print('<html lang="en">')
print('<head><meta charset="UTF-8"><title>Python Response</title></head>')
print('<body>')
print(f'<h1>{make} {model}</h1>')
print('<a href="post.html">Back</a>')
print('</body></html>')