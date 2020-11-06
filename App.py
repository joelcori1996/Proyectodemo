from flask import Flask, render_template, request, redirect, url_for,flash
from flask_mysqldb import MySQL


#MySQL conexion
app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'joel1010'
# app.config['MYSQL_DB'] = 'proyecto'


##
app.config['MYSQL_HOST'] = 'klbcedmmqp7w17ik.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'fvvu4v5mdlms6hri'
app.config['MYSQL_PASSWORD'] = 'b0dap63709nnejsf'
app.config['MYSQL_DB'] = 'vejbs8y4r6k6szj3'

##

#Configuraciones
app.secret_key='mysecretkey'

mysql = MySQL(app)


@app.route('/')
def Index():
    conn = mysql.connection.cursor()  
    conn.execute('SELECT * FROM contactos')
    data = conn.fetchall()
 
    return render_template('Index.html', contact=data)

@app.route('/Agregar_Contacto', methods=['POST'])
def Agregar_Contacto():
    if request.method =='POST' :
        Nombre = request.form['txtNombre']
        Telefono = request.form['txtTelefono']
        Email = request.form['txtEmail']     
        conn = mysql.connection.cursor()  
        conn.execute('INSERT INTO contactos (Nombre,Telefono,Email) VALUES (%s, %s, %s)', (Nombre.upper(),Telefono,Email))
        mysql.connection.commit()
    
    flash('Se Agregó correctamente')
    return redirect(url_for('Index'))

@app.route('/Editar_Contacto/<ContactoId>')
def Editar_Contacto(ContactoId):
    conn = mysql.connection.cursor()  
    conn.execute('SELECT * FROM contactos WHERE ContactoId = %s',(ContactoId) )
    data = conn.fetchall()
    return render_template('Editar.html', contact=data[0])

@app.route('/Actualizar/<Id>', methods=['POST'])
def Actualizar_Contacto(Id):
    if request.method =='POST' :
        Nombre = request.form['txtNombre']
        Telefono = request.form['txtTelefono']
        Email = request.form['txtEmail']     
        conn = mysql.connection.cursor()  
        conn.execute('''UPDATE  contactos  SET 
        Nombre = %s,
        Telefono = %s,
        Email=%s
        WHERE  ContactoId=%s''', (Nombre,Telefono,Email,Id))
        mysql.connection.commit()
        flash('Contacto Actualizado')
    return redirect(url_for('Index'))

@app.route('/Eliminar_Contacto/<string:ContactoId>')
def Eliminar_Contacto(ContactoId):
    conn = mysql.connection.cursor()  
    conn.execute('DELETE FROM contactos WHERE ContactoId={0}'.format(ContactoId))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('Index'))



if __name__ == '__main__':
    app.run(port=3000,debug=True)


