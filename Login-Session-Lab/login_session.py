from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['POST','GET']) # What methods are needed?
def home():
	if request.method=="GET":
		return render_template('home.html')
	else:
		try:
			login_session['quote'] = request.form['quote']
			login_session['author'] = request.form['author']
			login_session['age'] = int(request.form['age'])
			return redirect(url_for('thanks'))
		except:
			return redirect(url_for('error'))

@app.route('/error',methods=['GET','POST']	)
def error():

        return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', login_session=login_session) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)