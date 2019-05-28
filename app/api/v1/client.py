from flask import request
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError, ClientSuccess
from app.models.user import User

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    """
    创建用户
    :return:
    """
    # data = request.json
    # data = request.args.to_dict()
    form = ClientForm().validate_form_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_client_by_email
    }
    promise[form.type.data]()
    return ClientSuccess()


def __register_client_by_email():
    form = UserEmailForm().validate_form_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
