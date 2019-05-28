from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_form_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    # identity 用户id
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generater_user_token(identity['uid'], form.type.data, identity['scope'], expiration)
    t = {
        "token": token.decode('ascii')
    }
    return jsonify(t), 201


def generater_user_token(uid, account_type, scope=None, expiration=7200):
    """"
    生成token, token中需要携带一些信息, 比如用户的id, type, token过期时间
    """
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        "uid": uid,
        "type": account_type.value,
        "scope": scope
    })
