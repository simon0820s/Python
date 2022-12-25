from flask import Flask,make_response,redirect,request,render_template
app=Flask(__name__)

todos=['TODO 1','TODO 2','TODO 3']

@app.route('/')
def index():
    user_ip=request.remote_addr
    response=make_response(redirect('/ip'))
    response.set_cookie('user_ip',user_ip)

    return response
@app.route('/ip')
def ip():
    user_ip=request.cookies.get('user_ip')
    context={
        'user_ip':user_ip,
        'todos':todos
    }
    return render_template('hello.html',**context)