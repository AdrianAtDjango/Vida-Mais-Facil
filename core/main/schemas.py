from ninja import ModelSchema
from .models import User, RegistroSaude, Consulta

class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = [
            'email',
            'nome',
            'sobrenome',
            'sexo',
            'rua',
            'numero',
            'bairro',
        ]

class RegistroSchema(ModelSchema):
    class Config:
        model = RegistroSaude
        model_fields = [
            'usuario',
            'glicemia',
            'pressao_sistolica',
            'pressao_diastolica',
            'peso',
            'frequencia_cardiaca',
        ]

class ConsultaSchema(ModelSchema):
    class Config:
        model = Consulta
        model_fields = [
            'solicitante',
            'titulo',
            'especialidade',
            'medico',
            'data_atendimento',
            'hora_atendimento',
            'observacao',
        ]