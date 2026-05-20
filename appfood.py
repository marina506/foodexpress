from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")


@app.route("/lanche/<nome>")
def lanche(nome):

    if nome == "pizza":
        mensagem = "Pizza quentinha saindo do forno!"

    elif nome == "hamburguer":
        mensagem = "Hambúrguer artesanal delicioso!"

    elif nome == "batata":
        mensagem = "Batata frita crocante!"

    elif nome == "milkshake":
        mensagem = "Milkshake geladinho!"

    else:
        mensagem = "Lanche não encontrado."

    return render_template(
        "lanche.html",
        nome=nome,
        mensagem=mensagem
    )

@app.route("/cliente/<nome>/<cidade>")
def cliente(nome, cidade):

    if cidade == "Natal":
        mensagem = "Entrega disponível!"

    else:
        mensagem = "Entrega indisponível!"

    return render_template(
        "cliente.html",
        nome=nome,
        cidade=cidade,
        mensagem=mensagem
    )

app.run(debug=True)