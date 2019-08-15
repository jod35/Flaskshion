from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SubmitField,PasswordField,TextAreaField
from wtforms.validators import DataRequired,EqualTo,Email,Length

class SignUpform(FlaskForm):
    fname=StringField("First Name",validators=[DataRequired(),Length(min=1,max=40)])
    lname=StringField("Last Name",validators=[DataRequired(),Length(min=1,max=40)])
    username=StringField("Username",validators=[DataRequired(),Length(max=10)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField("Sign In")


class TopicForm(FlaskForm):
    topic=StringField("Topic",validators=[DataRequired(),Length(max=20)])
    content=TextAreaField("Content",validators=[DataRequired()])
    submit=SubmitField("Start the topic")

class CommentForm(FlaskForm):
    
    comment=TextAreaField("Content",validators=[DataRequired()])
    submit=SubmitField("Comment")