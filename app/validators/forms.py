from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import DataRequired, length, Email, Regexp

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[DataRequired(message='用户名不能为空'), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        """
        验证自定义枚举类型
        :param value:
        :return:
        """
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client

# class ClientForm(Form):
#     account = StringField(validators=[DataRequired(message='不允许为空'), length(
#         min=5, max=32
#     )])
#     secret = StringField()
#     type = IntegerField(validators=[DataRequired()])

#     def validate_type(self, value):
#         try:
#             client = ClientTypeEnum(value.data)
#         except ValueError as e:
#             raise e
#         self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='Invalid email')])
    secret = StringField(validators=[DataRequired(), Regexp(r'^[A-Za-z0-9_*&$#@]{6, 22}$')])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()


class SearchBookForm(Form):
    q = StringField(validators=[DataRequired()])


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])