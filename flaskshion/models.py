from flaskshion import db,admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin
from flaskshion import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    fname=db.Column(db.String(255),nullable=False)
    lname=db.Column(db.String(255),nullable=False)
    username=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(255),nullable=False)
    passwd=db.Column(db.Text(),nullable=False)
    topics=db.relationship('Topic',backref='author',lazy=True)
    comments=db.relationship('Comment',backref='commentor',lazy=True)


    def __repr__(self):
        return '{}'.format(self.fname)

class UserView(ModelView):
    form_columns=['id','fname','lname','username','email','passwd']

class Topic(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(255),nullable=False,unique=True)
    date_created=db.Column(db.DateTime(),default=datetime.utcnow)
    content=db.Column(db.Text(),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    

    def __repr__(self):
        return '[Topic {}]'.format(self.title)

class TopicView(ModelView):
    form_columns=['id','title','date_created','content']
class Comment(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    comment=db.Column(db.Text(),nullable=False)
    commentor_id=db.Column(db.Integer(),db.ForeignKey('user.id'))

    def __repr__(self):
        return '{}'.format(self.comment)

class CommentView(ModelView):
    form_columns=['id','comment']

admin.add_view(UserView(User,db.session))
admin.add_view(TopicView(Topic,db.session))
admin.add_view(CommentView(Comment,db.session))