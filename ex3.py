from flask import Flask, render_template
from forms import RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)
