import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)


class Atendente(object):
    def __init__(self, CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente):
        self.CpfAtendente = CpfAtendente
        self.NomeAtendente = NomeAtendente
        self.SobrenomeAtendente = SobrenomeAtendente
        self.RgAtendente = RgAtendente
        self.EnderecoAtendente = EnderecoAtendente
        self.SalarioAtendente = SalarioAtendente
        self.TelefoneAtendente = TelefoneAtendente


class Cliente(object):
    def __init__(self, CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, Cpfatendente, TelefoneCliente):
        self.CpfCliente = CpfCliente
        self.NomeCliente = NomeCliente
        self.SobrenomeCliente = SobrenomeCliente
        self.RgCliente = RgCliente
        self.EnderecoCliente = EnderecoCliente
        self.Cpfatendente = Cpfatendente
        self.TelefoneCliente = TelefoneCliente


class Manobrista(object):
    def __init__(self, CnhManobrista, NomeManobrista, SobrenomeManobrista, RgManobrista, EnderecoManobrista, SalarioManobrista, TelefoneManobrista):
        self.CnhManobrista = CnhManobrista
        self.NomeManobrista = NomeManobrista
        self.SobrenomeManobrista = SobrenomeManobrista
        self.RgManobrista = RgManobrista
        self.EnderecoManobrista = EnderecoManobrista
        self.SalarioManobrista = SalarioManobrista
        self.TelefoneManobrista = TelefoneManobrista


class Vaga(object):
    def __init__(self, NumeroVaga, Situacao):
        self.NumeroVaga = NumeroVaga
        self.Situacao = Situacao


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.3'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/cadastroatendente')
def cliente():
    return render_template('cadastroatendente.html')

@app.route('/cadastrocliente')
def cliente():
    return render_template('cadastrocliente.html')

@app.route('/gravaratendente', methods=['POST', 'GET'])
def cadastroatendente():
    Atendente = Atendente(request.form['CpfAtendente'],
                         request.form['NomeAtendente'],
                         request.form['SobrenomeAtendente'],
                         request.form['RgAtendente'],
                         request.form['EnderecoAtendente'],
                         request.form['SalarioAtendente'],
                         request.form['TelefoneAtendente'])

    if Atendente.CpfAtendente and Atendente.NomeAtendente and Atendente.SobrenomeAtendente and Atendente.RgAtendente and Atendente.EnderecoAtendente and Atendente.SalarioAtendente and Atendente.TelefoneAtendente:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Atendente (CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                           (Atendente.CpfAtendente, Atendente.NomeAtendente, Atendente.SobrenomeAtendente, Atendente.RgAtendente, Atendente.EnderecoAtendente, Atendente.SalarioAtendente, Atendente.TelefoneAtendente))
        conn.commit()
        return render_template('index.html')

@app.route('/cadastrocliente')
def cliente():
    return render_template('cadastrocliente.html')

@app.route('/cadastrocliente', methods=['POST', 'GET'])
def cadastrocliente():
    cpf = request.form[Cliente.CpfCliente]
    nome = request.form[Cliente.NomeCliente]
    sobrenome = request.form[Cliente.SobrenomeCliente]
    rg = request.form[Cliente.RgCliente]
    endereco = request.form[Cliente.EnderecoCliente]
    cpfatendente = request.form[Cliente.Cpfatendente]
    telefone = request.form[Cliente.TelefoneCliente]
    if cpf and nome and sobrenome and rg and endereco and cpfatendente and telefone:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Cliente (CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, Cpfatendente, TelefoneCliente) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (cpf, nome, sobrenome, rg, endereco, cpfatendente, telefone))
        conn.commit()
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host='0.0.0.0', port=port)
