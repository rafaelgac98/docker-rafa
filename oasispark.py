from crypt import methods
import os, cgi, cgitb
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/listaratendente/<int:pk>/', methods=['GET'])
def listaratendente(pk):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idAtendente, CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente from Atendente where idAtendente = ' + str(pk))
    data = cursor.fetchall()
    conn.commit()
    return render_template('listaatendente.html', datas=data, pk = pk)


@app.route('/deletaratendente/<int:pk>/', methods=['GET'])
def deletaratendente(pk):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('DELETE from Atendente where idAtendente = ' + str(pk))
    data = cursor.fetchall()
    conn.commit()
    return render_template('cadastroatendente.html', datas=data, pk = pk)


@app.route('/cliente')
def cliente():
    return render_template('cadastrocliente.html')


@app.route('/manobrista')
def manobrista():
    return render_template('cadastromanobrista.html')


@app.route('/vaga')
def vaga():
    return render_template('cadastrovaga.html')


@app.route('/veiculo')
def veiculo():
    return render_template('cadastroveiculo.html')






@app.route('/alteraratendente/<int:pk>/', methods=['POST', 'GET'])
def alteraratendente(pk):
    
    conn1 = mysql.connect()
    cursor1 = conn1.cursor()
    cursor1.execute('select idAtendente, CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente from Atendente where idAtendente = ' + str(pk))
    data = cursor1.fetchall()
    conn1.commit()
    #return render_template('listaatendente.html', datas=data, pk = pk)

    # cpfAtendente = request.form['cpfAtendente']
    # nomeAtendente = request.form['nomeAtendente']
    # sobrenomeAtendente = request.form['sobrenomeAtendente']
    # rgAtendente = request.form['rgAtendente']
    # enderecoAtendente = request.form['enderecoAtendente']
    # salarioAtendente = request.form['salarioAtendente']
    # telefoneAtendente = request.form['telefoneAtendente']

    # if cpfAtendente and nomeAtendente and sobrenomeAtendente and rgAtendente and enderecoAtendente and salarioAtendente and telefoneAtendente:
    #     conn = mysql.connect()
    #     cursor = conn.cursor()
    #     cursor.execute('UPDATE Atendente SET CpfAtendente=%s, NomeAtendente=%s, SobrenomeAtendente=%s, RgAtendente=%s, EnderecoAtendente=%s, SalarioAtendente=%s, TelefoneAtendente=%s WHERE idAtendente=%s',
    #                    (cpfAtendente, nomeAtendente, sobrenomeAtendente, rgAtendente, enderecoAtendente, salarioAtendente, str(pk)))
    #     conn.commit()

    return render_template('alteraatendente.html', datas=data, pk = pk)





@app.route('/gravaratendente', methods=['POST', 'GET'])
def gravaratendente():
    cpfatendente = request.form['cpfAtendente']
    nomeatendente = request.form['nomeAtendente']
    sobrenomeatendente = request.form['sobrenomeAtendente']
    rgatendente = request.form['rgAtendente']
    enderecoatendente = request.form['enderecoAtendente']
    salarioatendente = request.form['salarioAtendente']
    telefoneatendente = request.form['telefoneAtendente']
    if cpfatendente and nomeatendente and sobrenomeatendente and rgatendente and enderecoatendente and salarioatendente and telefoneatendente:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Atendente (CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente) values (%s, %s, %s, %s, %s, %s, %s)',
                       (cpfatendente, nomeatendente, sobrenomeatendente, rgatendente, enderecoatendente, salarioatendente, telefoneatendente))
        conn.commit()
    return render_template('cadastroatendente.html')


@app.route('/gravarcliente', methods=['POST', 'GET'])
def gravarcliente():
    cpfcliente = request.form['cpfcliente']
    nomecliente = request.form['nomecliente']
    sobrenomecliente = request.form['sobrenomecliente']
    rgcliente = request.form['rgcliente']
    enderecocliente = request.form['enderecocliente']
    idAtendente = request.form['cpfatendente']
    telefonecliente = request.form['telefonecliente']

    if cpfcliente and nomecliente and sobrenomecliente and rgcliente and enderecocliente and idAtendente and telefonecliente:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Cliente (CpfCliente, NomeCliente, SobrenomeCliente, RgCliente, EnderecoCliente, idAtendente, TelefoneCliente) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (cpfcliente, nomecliente, sobrenomecliente, rgcliente, enderecocliente, idAtendente, telefonecliente))
        conn.commit()
    return render_template('cadastrocliente.html')


@app.route('/gravarmanobrista', methods=['POST', 'GET'])
def gravarmanobrista():
    cnhmanobrista = request.form['cnhmanobrista']
    nomemanobrista = request.form['nomemanobrista']
    sobrenomemanobrista = request.form['sobrenomemanobrista']
    rgmanobrista = request.form['rgmanobrista']
    enderecomanobrista = request.form['enderecomanobrista']
    salariomanobrista = request.form['salariomanobrista']
    telefonemanobrista = request.form['telefonemanobrista']
    if cnhmanobrista and nomemanobrista and sobrenomemanobrista and rgmanobrista and enderecomanobrista and salariomanobrista and telefonemanobrista:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Manobrista (CnhManobrista, NomeManobrista, SobrenomeManobrista, RgManobrista, EnderecoManobrista, SalarioManobrista, TelefoneManobrista) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (cnhmanobrista, nomemanobrista, sobrenomemanobrista, rgmanobrista, enderecomanobrista, salariomanobrista, telefonemanobrista))
        conn.commit()
    return render_template('cadastromanobrista.html')


@app.route('/gravarvaga', methods=['POST', 'GET'])
def gravarvaga():
    numerovaga = request.form['numerovaga']
    situacaovaga = request.form['situacaovaga']
    if numerovaga and situacaovaga:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Vaga (NumeroVaga, Situacao) VALUES (%s, %s)',
                       (numerovaga, situacaovaga))
        conn.commit()
    return render_template('cadastrovaga.html')


@app.route('/gravarveiculo', methods=['POST', 'GET'])
def gravarveiculo():
    placaveiculo = request.form['placaveiculo']
    corveiculo = request.form['corveiculo']
    modeloveiculo = request.form['modeloveiculo']
    cpfcliente = request.form['cpfcliente']
    numerovaga = request.form['numerovaga']
    datahoraentrada = request.form['datahoraentrada']
    datahorasaida = request.form['datahorasaida']
    valor = request.form['valor']
    cpfatendente = request.form['cpfatendente']
    comprovante = request.form['comprovante']
    if placaveiculo and corveiculo and modeloveiculo and cpfcliente and numerovaga and datahoraentrada and datahorasaida and valor and cpfatendente and comprovante:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into Veiculo (Placa, Cor, Modelo, CpfCliente, NumeroVaga, DataHora_Entrada, DataHora_Saida, Valor, CpfAtendente, Comprovante) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (placaveiculo, corveiculo, modeloveiculo, cpfcliente, numerovaga, datahoraentrada, datahorasaida, valor, cpfatendente, comprovante))
        conn.commit()
    return render_template('cadastroveiculo.html')


@app.route('/atendente', methods=['POST', 'GET'])
def selectatendente():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select idAtendente, CpfAtendente, NomeAtendente, SobrenomeAtendente, RgAtendente, EnderecoAtendente, SalarioAtendente, TelefoneAtendente from Atendente')
    data = cursor.fetchall()
    conn.commit()
    return render_template('cadastroatendente.html',datas=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host='0.0.0.0', port=port)
