from flask import Flask, render_template, redirect, flash

from conf import flaskConf
from pkg.forms import LoginForm

app = Flask(__name__)
app.config.from_object(flaskConf)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])

if __name__ == '__main__':
    app.run()