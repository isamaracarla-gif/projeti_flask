lista_professor = [
    {"id": 1, "nome": "Marcos Oliveira",
         "e-mail": "marcos@exemplo.com", "titulção": "Mestre"},
    {"id": 2, "nome": "Paula Ribeiro",
             "e-mail": "paula@exemplo.com", "titulação": "Doutora"},
    {"id": 3, "nome": "Renato Alves",
                 "e-mail": "renato@exemplo.com", "titulação": "Especialista"},
]
def listar():
    return lista_professor

def cadastrar(nome, email, titulação):
    if len(lista_professor) == 0:
        novo_id = 1
    else:
        ultimo = lista_professor[-1]
        novo_id = ultimo["id"] + 1
    professor = {"id": novo_id, "nome": nome,
             "email": email, "titulação": titulação}
    lista_professor.append(professor)
    return professor