from flask import jsonify, g
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.libs.error_code import NotFound, DeleteSuccess, AuthFailed
from app.models.user import User, db

api = Redprint('user')


# class KOA:
#     name = 'koa'
#     age = 18
#
#     def __init__(self):
#         self.gender = 'gemal'
#
#     def keys(self):
#         return ['name', 'age']
#
#     def __getitem__(self, item):
#         return getattr(self, item)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # 管理员
    # is_admin = g.user.is_admin
    # if not is_admin:
    #     raise AuthFailed()
    user = User.query.filter_by(id=uid).first_or_404()
    # if not user:
    #     raise NotFound()
    # r = {
    #     'nickanme': user.nickname,
    #     'email': user.email
    # }
    return jsonify(user)


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
    # 管理员删除用户接口
    pass


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    # 普通用户
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    # g线程隔离
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('/<int:uid>', methods=['PUT'])
@auth.login_required
def update_user(uid):
    return 'i am koa'
