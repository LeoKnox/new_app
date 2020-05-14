from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/index/<info>')
def index(info):
    return render_template('index.html', info=info)

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

@app.route('/level/<int:roomID>')
def level(roomID):
    return render_template('level.html', roomID=roomID)

@app.route('/rooms')
def rooms():
    #dict = {'entry':5,'storage':7,'prison':8}
    dict = {'entry':[5, 5], 'storage':[8, 8], 'prison':[10, 10]}
    return render_template('rooms.html', rooms = dict)

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