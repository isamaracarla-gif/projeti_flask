import email

from flask import Flask, render_template, request, redirect
import aluno_service
import curso_service
import disciplina_service
import professor_service
app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html", titulo="Minha primeira aplicação Flask")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/ola/<nome>")
def ola(nome):
    return render_template("ola.html", nome=nome)

@app.route("/idade/<int:idade>")
def idade(idade):
    return render_template("idade.html", idade=idade)

@app.route("/disciplinas")
def disciplinas():
    lista = ["Programação Web", "Banco de Dados",
             "Redes", "Inglês Técnico"]
    return render_template("disciplinas.html",
                           disciplinas=lista)

@app.route("/tabuada/<int:n>")
def tabuada(n):
    return render_template("tabuada.html", n=n)

@app.route("/tabuadas")
def tabuadas():
    return render_template("tabuadas.html")

@app.route("/aluno/")
def listar_alunos():
    alunos = aluno_service.listar()
    return render_template("aluno/listar.html", alunos=alunos)

@app.route("/curso/")
def listar_cursos():
    cursos = curso_service.listar()
    return render_template("curso/listar.html", cursos=cursos)

@app.route("/aluno/novo")
def novo_aluno():
    return render_template("aluno/form.html", aluno=None)

@app.route("/aluno/salvar", methods=["POST"])
def salvar_aluno():
    id_aluno = request.form["id"]
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    cidade = request.form["cidade"]
    if id_aluno == "":
        aluno_service.cadastrar(nome, telefone, cidade)
    return redirect("/aluno/")

@app.route("/curso/novo")
def novo_curso():
    return render_template("curso/form.html",curso=None)

@app.route("/curso/salvar", methods=["POST"])
def salvar_curso():
    id_curso = request.form["id"]
    nome = request.form["nome"]
    area = request.form["area"]
    if id_curso == "":
       curso_service.cadastrar(nome, area)
    return redirect("/curso/")


@app.route("/disciplina/")
def listar_disciplina():
    disciplina = disciplina_service.listar()
    return render_template("disciplina/listar.html", disciplina=disciplina)

@app.route("/disciplina/novo")
def novo_disciplina():
    return render_template("disciplina/form.html",disciplina=None)

@app.route("/disciplina/salvar", methods=["POST"])
def salvar_disciplina():
    id_disciplina = request.form["id"]
    nome = request.form["nome"]
    carga = request.form["carga"]
    semestre = request.form["semestre"]
    if id_disciplina == "":
       disciplina_service.cadastrar(nome, carga, semestre)
    return redirect("/disciplina/")

@app.route("/professor/")
def listar_professor():
    professor = professor_service.listar()
    return render_template("professor/listar.html", professor=professor)

@app.route("/professor/novo")
def novo_professor():
    return render_template("professor/form.html",professor=None)

@app.route("/professor/salvar", methods=["POST"])
def salvar_professor():
    id_professor = request.form["id"]
    nome = request.form["nome"]
    email = request.form["email"]
    titulação = request.form["titulação"]
    if id_professor == "":
      professor_service.cadastrar(nome, email, titulação)
    return redirect("/professor/")










#Sempre no final do arquivo.
if __name__ == "__main__":
    # host=0.0.0.0 permite o encaminhamento da porta no Codespaces.
    app.run(host="0.0.0.0", port=5000, debug=True)
