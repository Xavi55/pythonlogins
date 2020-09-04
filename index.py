from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key='secret01'


@app.route('/')
def index():
    try:
        if session['username']:
            return '''Logged in as {} <br>
            Logout out <a href="/logout">here</a>
            '''.format(session['username'])
    except Exception as e:
        return '''You are not logged in<br>
                Click <a href="/login">here</a> to log in.
                '''

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    
    return '''
	
   <form action = "" method = "post">
      <p><input type = text name =username /></p>
      <p<<input type = submit value=Login /></p>
   </form>
	
   '''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    Flask.run(app)