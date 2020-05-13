from flask import Flask
app = Flask(__name__)

@app.route('/index/<info>')
def index(info):
    return 'new %s app' % info

@app.route('/room/<int:roomID>')
def room(roomID):
    return 'This is room %d' % roomID

@app.route('/version/<float:verNo>')
def version(verNo):
    return 'Version Number %f' % verNo

if __name__ == '__main__':
    app.run()