from flask import Flask,make_response,redirect,request,render_template,session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
app=Flask(__name__)
bootstrap=Bootstrap(app)
app.config['SECRET_KEY']='SUPER SECRETO'

todos=['Comer','Dormir','Programar']

class LoginForm(FlaskForm):
    name=StringField('User name',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Send')



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.errorhandler(500)
def didnt_completed(error):
    return render_template('500.html',error=error)


@app.route('/')
def index():
    user_ip=request.remote_addr
    response=make_response(redirect('/hello'))
    session['user_ip']=user_ip
    return response

@app.route('/hello')
def hello():
    user_ip=request.remote_addr
    login_form=LoginForm()
    context={
        'user_ip':user_ip,
        'todos':todos,
        'login_form':login_form
    }
    return render_template('hello.html',**context)