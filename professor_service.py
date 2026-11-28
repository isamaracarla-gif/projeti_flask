lista_professor = [
    {"id": 1, "nome": "Marcos Oliveira",
     "email": "marcos@exemplo.com", "titulação": "Mestre"},
    {"id": 2, "nome": "Paula Ribeiro",
     "email": "paula@exemplo.com", "titulação": "Doutora"},
    {"id": 3, "nome": "Renato Alves",
     "email": "renato@exemplo.com", "titulação": "Especialista"},
]


def listar():
    return lista_professor

def cadastrar(nome, carga, semestre):
    if len(lista_professor) == 0:
        novo_id = 1
    else:
        ultimo = lista_professor[-1]
        novo_id = ultimo["id"] + 1
    professor = {"id": novo_id, "nome": nome,
             "carga": carga, "semestre": semestre}
    lista_professor.append(professor)
    return professor