from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY_SECRET_KEY'

class SimpleForm(FlaskForm):
    breed = StringField('What breed are you?')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(session['breed'])

        return redirect(url_for('index'))
    
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
