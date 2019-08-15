from . import app,db
from flask import render_template,redirect,request,flash
from flaskshion.forms import SignUpform,LoginForm,TopicForm,CommentForm
from  flaskshion.models import User,Topic,Comment
from flask_bcrypt import Bcrypt
from flask_login import current_user,login_user,logout_user,login_required

bcrypt=Bcrypt(app)



@app.route('/')
def index():
   topics=Topic.query.all()
   return render_template('index.html',topics=topics)


@app.route('/signup')
def SignUp():
   form=SignUpform()
   return render_template('sign.html',form=form,title="Sign Up")

@app.route('/adduser',methods=['GET', 'POST'])
def SignUser():
   if request.method =='POST':
      fname=request.form.get('fname')
      lname=request.form.get('lname')
      username=request.form.get('username')
      email=request.form.get('email')
      password=request.form.get('password')
      p=bcrypt.generate_password_hash(password)

      new_user=User(fname=fname,lname=lname,username=username,email=email,passwd=p)

      db.session.add(new_user)
      try:
         db.session.commit()
         flash('Account created for user %s. You can now Sign In!'%fname)
         return redirect('/signup')
      except:
         flash('There has been a problem submitting you form.')
         return redirect('/signup')

      return redirect('/signup')


@app.route('/login', methods=['POST','GET'])
def LoginUser():
    form=LoginForm()
   

    return render_template('login.html',form=form)


@app.route('/loginuser', methods=['POST'])
def Login():
    form=LoginForm()
    email=request.form.get('email')
    password=request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.passwd,password):
        login_user(user)
        return redirect('/')
    return render_template('login.html',form=form) 

@app.route('/logout')
def LogOutUser():
   logout_user()
   return redirect('/login')



@app.route('/topics',methods=['GET', 'POST'])
@login_required
def UsersTopics():
   form=TopicForm()
   topics=Topic.query.filter_by(author=current_user)
   if request.method=='POST':
      title=request.form.get('topic')
      content=request.form.get('content')
      new_topic=Topic(title=title,content=content,author=current_user)
      try:
         db.session.add(new_topic)
         db.session.commit()
         flash('Topic created successfully')
         return redirect('/topics')
      except:
         flash('Topic not created, There might be a problem')
         return redirect('/topics')
         
   return render_template('topics.html',form=form,topics=topics)

@app.route('/topics/comment/<int:id>', methods=['POST','GET'])
def CommentTopic(id):
    form=CommentForm()
    topic=Topic.query.get_or_404(id)

    return render_template('comment.html',form=form,topic=topic)