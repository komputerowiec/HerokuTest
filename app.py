from flask import Flask
from str2bool import str2bool
import os, datetime
import psutil

app = Flask(__name__)

start_time = datetime.datetime.now()

@app.route("/")
def hello():
    return "Hello World: " + os.environ['PORT']

@app.route("/write/<message>")
def write(message='no message'):
    with open('workfile', 'w') as f:
        f.write(message)
    return "Message {} stored on disk".format(message)

@app.route("/read")
def read():
    try:
        with open('workfile', 'r') as f:
            message = f.read()
        return "Message {} retrieved from disk".format(message)
    except IOError:
        return "NO DATA ON DISK"

@app.route("/memory")
def memory():
    return str(psutil.virtual_memory())

@app.route("/start-time")
def starttime():
    return str(start_time)

@app.route("/uptime")
def uptime():
    curr_time = datetime.datetime.now()
    uptime = curr_time - start_time
    return str(uptime)

app.run(
    debug=str2bool(os.environ.get('DEBUG', 'false')),
    host=os.environ.get('LISTEN_ADDR', '0.0.0.0'),
    port=int(os.environ.get('PORT', '5000')),
    use_reloader=True
)
