from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/index/<info>')
def index(info):
    return 'new %s app' % info

@app.route('/room/<int:roomID>')
def room(roomID):
    return 'This is room %d' % roomID

@app.route('/floor/<int:roomID>')
def floor(roomID):
    if roomID == 5:
        return redirect(url_for('index', info = 'dungeon'))
    else:
        return redirect(url_for('room', roomID = roomID))

@app.route('/version/<float:verNo>')
def version(verNo):
    return 'Version Number %f' % verNo

if __name__ == '__main__':
    app.run(debug = True)