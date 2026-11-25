lista_disciplina = [
    {"id": 1, "nome": "Programação Web",
         "carga": "80", "semestre": "3"},
    {"id": 2, "nome": "Banco de Dados",
             "carga": "60", "semestre": "2"},
    {"id": 3, "nome": "Engenharia de Software",
                 "carga": "60", "semestre": "4"},
]
def listar():
    return lista_disciplina

def cadastrar(nome, carga, semestre):
    if len(lista_disciplina) == 0:
        novo_id = 1
    else:
        ultimo = lista_disciplina[-1]
        novo_id = ultimo["id"] + 1
    disciplina = {"id": novo_id, "nome": nome,
             "carga": carga, "semestre": semestre}
    lista_disciplina.append(disciplina)
    return disciplina