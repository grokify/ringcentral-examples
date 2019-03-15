import sys
from bottle import route, run
from bottle import request, response

@route('/webhook', method='POST')
def handlewebhook():
    vtHeader = 'Validation-Token'
    vt = request.get_header(vtHeader)
    if vt is not None and len(vt) > 0:
       response.set_header(vtHeader, vt)
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)

run(host='localhost', port=8080)