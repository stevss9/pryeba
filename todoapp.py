#Importamos las librerias
from flask import Flask, redirect, render_template, request, url_for, flash

#Objeto para inicilizar la aplicacion
app = Flask(__name__, template_folder='templates')

#Clave  de la app
app.secret_key = '090700'

#Array donde almacenaremos los datos
task_list = []
task_listc = []
task_listt = []
task_lista = []

#Controlador de la ruta inicial
@app.route('/')
def index():
    return render_template('index.html', task_list=task_list)

@app.route('/cliente/')
def cliente():
    return render_template('cliente.html', task_listc=task_listc)

@app.route('/tienda/')
def tienda():
    return render_template('tienda.html', task_listt=task_listt)

@app.route('/admin/')
def admin():
    return render_template('admin.html', task_lisa=task_lista)

#Controlador de la ruta de envio de datos
@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        task_name = request.form['task_name']
        task_phone = request.form['task_phone']
        task_status = request.form['task_status']


        if task_name == '' or task_phone == '':            
            return redirect(url_for('cliente'))
        else:
            task_list.append({'task_name': task_name, 'task_phone': task_phone, 'task_status': task_status })
            return redirect(url_for('cliente'))

#Controlador de la ruta para delete los datos de la tabla
@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':        
        if task_listc == []:
            return redirect(url_for('cliente'))
        else:
            task_listc.clear()
            return redirect(url_for('cliente'))

#Main de la app
if __name__ == '__main__':
    app.run(debug=True)