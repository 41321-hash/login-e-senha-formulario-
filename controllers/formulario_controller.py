from models.formulario_model import FormularioModel  

class FormularioController:

    @staticmethod
    def create_formulario(user_id, data):
        nome = data.get('nome')  
        email = data.get('email') 
        data_nascimento = data.get('data_nascimento') 
        cpf = data.get('cpf')  
        genero = data.get('genero')  

        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatórios"}, 400  

        formulario = FormularioModel.create_formulario(user_id, nome, email, data_nascimento, cpf, genero)
        if formulario:
            return {"message": "Formulário criado com sucesso"}, 201
        return {"error": "Erro ao criar formulário"}, 500

    @staticmethod
    def get_formularios(user_id):
        formularios = FormularioModel.get_formularios_by_user(user_id)
        return formularios, 200

    @staticmethod
    def update_formulario(form_id, user_id, data):
        nome = data.get('nome')  
        email = data.get('email') 
        data_nascimento = data.get('data_nascimento') 
        cpf = data.get('cpf')  
        genero = data.get('genero')  

        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatórios"}, 400

        if FormularioModel.update_formulario(form_id, user_id, nome, email, data_nascimento, cpf, genero):
            return {"message": "Formulário atualizado com sucesso"}, 200
        return {"error": "Formulário não encontrado ou sem permissão"}, 404

    @staticmethod
    def delete_formulario(form_id, user_id):
        if FormularioModel.delete_formulario(form_id, user_id):
            return {"message": "Formulário eliminado com sucesso"}, 200
        return {"error": "Formulário não encontrado ou sem permissão"}, 404