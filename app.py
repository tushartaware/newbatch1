from ﬂask import Flask
import socket
import datetime
app = Flask(__name__)
@app.route('/')
def hello_world():
  hostname = socket.gethostname()
  time = datetime.datetime.now().strftime("%m/%d/%Y,%H:%M:%S")
  return 'Welcome TUSHAR from '+hostname+' , at '+time

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
