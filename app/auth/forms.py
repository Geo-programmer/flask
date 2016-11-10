# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    email = StringField('邮箱地址', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('登录密码', validators=[Required()])
    remember_me = BooleanField('记住登录状态')
    submit = SubmitField('登录')


class RegistrationForm(Form):
    email = StringField('邮箱地址', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField('请输入用户名', validators=[Required(), Length(1, 64)])
    password = PasswordField('请输入您的密码', validators=[
        Required(), EqualTo('password2', message='密码必须匹配')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱地址已使用')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已使用')


class ChangePasswordForm(Form):
    old_password = PasswordField('旧密码', validators=[Required()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='密码必须匹配')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('确认更改')


class PasswordResetRequestForm(Form):
    email = StringField('邮箱地址', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField('重设密码')


class PasswordResetForm(Form):
    email = StringField('邮箱地址', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='密码必须匹配')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('确认更改')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('未知邮箱地址')


class ChangeEmailForm(Form):
    email = StringField('新邮箱地址', validators=[Required(), Length(1, 64),
                                                 Email()])
    password = PasswordField('请输入密码', validators=[Required()])
    submit = SubmitField('确认更改')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱地址已使用')
