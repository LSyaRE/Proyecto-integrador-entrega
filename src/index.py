from flask import Flask, render_template, request,redirect ,url_for, flash
import psycopg2
#conexionBD
PSQL_Host = "localhost"
PSQL_Port = "5432"
PSQL_User = "postgres"
PSQL_Pass = "Porawiin.1"
PSQL_DB = "proyecto1"

conection_adress= """
host=%s port=%s user=%s password= %s dbname=%s 
""" %(PSQL_Host,PSQL_Port,PSQL_User,PSQL_Pass,PSQL_DB)

connection= psycopg2.connect(conection_adress)

c=connection.cursor()




app= Flask(__name__)
app.secret_key= 'mysecretkey'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/album')
def album():
    return render_template('album.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/add_contacto', methods=['POST'])
def add_contacto():
    if request.method == 'POST':
        name = request.form['name']
        Sname = request.form['Sname']
        email = request.form['email']
        asunt= request.form['asunt']
        message = request.form['message']
        flash('Datos Enviados correctamente')
    personas= c.execute('INSERT INTO personas(nom_personas,ape_personas,email_personas) VALUES (%s,%s,%s)', (name,Sname,email))
    
    connection.commit()
    contacto= c.execute('INSERT INTO contacto(asunto,mensaje) VALUES (%s,%s)', (asunt,message))
    connection.commit()

    return redirect(url_for('contacto'))
if __name__ == '__main__':
    app.run(debug=True)