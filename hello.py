from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/index/<info>')
def index(info):
    return 'new %s app' % info

@app.route('/start')
def start():
    return render_template('login.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('index', info = user))
    else:
        user = request.args.get('nm')
        print(user)
        user = "junk"
        return redirect(url_for('index', info = user))

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