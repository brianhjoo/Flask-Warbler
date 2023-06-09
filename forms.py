from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField(
        'Username',
        validators=[DataRequired()],
    )

    email = StringField(
        'E-mail',
        validators=[DataRequired(), Email()],
    )

    password = PasswordField(
        'Password',
        validators=[Length(min=6)],
    )

    image_url = StringField(
        '(Optional) Image URL',
    )


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(
        'Username',
        validators=[DataRequired()],
    )

    password = PasswordField(
        'Password',
        validators=[Length(min=6)],
    )


class EditForm(FlaskForm):
    """Edit form."""

    username = StringField(
        'Username',
        validators=[Optional()]
    )

    email = StringField(
        'E-mail',
        validators=[Optional(), Email()]
    )

    image_url = StringField(
        '(Optional) Image URL',
        validators=[Optional()]
    )

    header_image_url = StringField(
        '(Optional) Header Image URL',
        validators=[Optional()]
    )

    bio = TextAreaField(
        '(Optional) Bio',
        validators=[Optional()]
    )

    password = PasswordField(
        'Password',
        validators=[Length(min=6)]
    )


class CSRF_Form(FlaskForm):
    """For CSRF protection"""
