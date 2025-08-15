from ninja import NinjaAPI
from .models import User, RegistroSaude, Consulta
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
import json

from .schemas import UserSchema, RegistroSchema, ConsultaSchema

api = NinjaAPI()

# Endpoints do CRUD de Usuários
@api.post('usuario/') # Cria novo usuário
def cria_usuario(request, user: UserSchema):
    user_dict = user.dict()
    user = User(**user_dict)
    user.save()
    return user

@api.put('usuario/{id}') # Atualiza informações de um usuário especifico
def atualiza_usuario(request, id: int, user: UserSchema):
    user = get_object_or_404(User, id=id)
    for atributo, valor in user.dict().items():
        setattr(user, atributo, valor)
    user.save()
    return {"success": True}

# Endpoints do CRUD de Registros de Saúde
@api.get('registros/') # Lista todos os registros de saúde cadastrados
def lista_registros(request):
    registros = RegistroSaude.objects.all()
    for r in registros:
        response = [{
            'id': r.id, 
            'usuario': r.usuario,
            'data': r.data_registro, 
            'glicemia': r.glicemia, 
            'pressao_sistolica': r.pressao_sistolica, 
            'pessao_diastolica': r.pressao_diastolica, 
            'peso': r.peso, 
            'frequencia_cardiaca': r.frequencia_cardiaca
        }]
    return response

@api.post('registros/') # Cria um novo Registro de saúde
def cria_registro(request, registro: RegistroSchema):
    registro_dict = registro.dict()
    registro = RegistroSaude(**registro_dict)
    registro.save()
    return registro

@api.put('registro/{id}') # Atualiza registro de saúde especifico
def atualiza_registro(request, id: int, registro: RegistroSchema):
    registro = get_object_or_404(RegistroSaude, id=id)
    for atributo, valor in registro.dict().item():
        setattr(registro, atributo, valor)
    registro.save()
    return {"success": True}

@api.delete('registro/{id}') # Deleta registro de saúde especifico
def deleta_registro(request, id: int): 
    registro = get_object_or_404(RegistroSaude, id=id)
    registro.delete()
    return {"success": True}

# Endpoints da criação e listagem de Consultas
@api.get('consultas/')
def lista_consultas(request):
    consultas = Consulta.objects.all()
    for c in consultas:
        response = [{
            'id': c.id,
            'solicitante': c.solicitante,
            'data_solicitacao': c.data_solicitacao,
            'titulo': c.titulo,
            'especialidade': c.especialidade,
            'medico': c.medico,
            'data_atendimento': c.data_atendimento,
            'hora_atendimento': c.hora_atendimento,
            'observacao': c.observacao,
        }]
    return response

@api.post('consultas/')
def cria_consulta(request, consulta: ConsultaSchema):
    consulta_dict = consulta.dict()
    consulta = Consulta(**consulta_dict)
    consulta.save()
    return consulta