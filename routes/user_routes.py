from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.user_controller import UserController

user_bp = Blueprint('users', __name__)

# (Apenas mantém as rotas de login e register já existentes aqui)

# OBTER PERFIL DO UTILIZADOR (GET)
@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    return jsonify(UserController.get_user_by_id(user_id))

# ATUALIZAR UTILIZADOR (PUT)
@user_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()
    return jsonify(UserController.update_user(user_id, data))

# ELIMINAR UTILIZADOR (DELETE)
@user_bp.route('/profile', methods=['DELETE'])
@jwt_required()
def delete_profile():
    user_id = get_jwt_identity()
    return jsonify(UserController.delete_user(user_id))

from flask_jwt_extended import jwt_required, get_jwt_identity

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    response, status = UserController.get_user(user_id)
    return jsonify(response), status

@user_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    response, status = UserController.update_user(user_id, request.get_json())
    return jsonify(response), status

@user_bp.route('/profile', methods=['DELETE'])
@jwt_required()
def delete_profile():
    user_id = get_jwt_identity()
    response, status = UserController.delete_user(user_id)
    return jsonify(response), status