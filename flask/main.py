from flask import Flask,make_response,redirect,request,render_template,session
from flask_bootstrap import Bootstrap
app=Flask(__name__)
bootstrap=Bootstrap(app)
app.config['SECRET_KEY']='SUPER SECRETO'

todos=['Comer','Dormir','Programar']
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.errorhandler(500)
def didnt_completed(error):
    return render_template('500.html',error=error)


@app.route('/')
def index():
    user_ip=request.remote_addr
    response=make_response(redirect('/welcome'))
    session['user_ip']=user_ip
    return response
@app.route('/welcome')
def welcome():
    user_ip=session.get['user_ip']
    context={
        'user_ip':user_ip,
        'todos':todos
    }
    return render_template('hello.html',**context)