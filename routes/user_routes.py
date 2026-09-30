from flask import Blueprint, request, jsonify  
from flask_jwt_extended import jwt_required, get_jwt_identity  
from controllers.user_controller import UserController 

user_bp = Blueprint('users', __name__)

# REGISTO DE UTILIZADOR (POST)
@user_bp.route('/register', methods=['POST'])
def register():
    response, status = UserController.register_user(request.get_json())
    return jsonify(response), status

# LOGIN DE UTILIZADOR (POST)
@user_bp.route('/login', methods=['POST'])
def login():
    response, status = UserController.login_user(request.get_json())
    return jsonify(response), status

# OBTER PERFIL DO UTILIZADOR (GET)
@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    response, status = UserController.get_user(user_id)
    return jsonify(response), status

# ATUALIZAR PERFIL DO UTILIZADOR (PUT)
@user_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    response, status = UserController.update_user(user_id, request.get_json())
    return jsonify(response), status

# ELIMINAR PERFIL DO UTILIZADOR (DELETE)
@user_bp.route('/profile', methods=['DELETE'])
@jwt_required()
def delete_profile():
    user_id = get_jwt_identity()
    response, status = UserController.delete_user(user_id)
    return jsonify(response), status