#importar la biblioteca de flask
#from flask import Flask
from flask import Flask,render_template
#render_template me permite retornar archivos html

#llamar al archivo principal desde una funcion
app = Flask(__name__)#nos permite crear las rutas para las diferentes paginas del sitio web
@app.route('/')
def inicio():
    #return 'Hola Mundo desde UPVT'
    return render_template('index.html')
#crear otra ruta
@app.route('/acercade')
def acercade():
  #return 'Muestra informacion acerca del proyecto'
 return render_template('acerca.html')

@app.route('/n_cliente')
def n_cliente():
  #return 'Muestra informacion acerca del proyecto'
 return render_template('n_cliente.html')

#ACTIVAR LA VALIDACION PARA QUE LA PAGINA SE QUEDE EJECUTANDO EN EL SERVIDOR
if __name__ == '__main__':
    app.run(debug=True)
    #OPCION PARA QUE SE REINICIE CADA QUE CAMBIO ALGO EN LA PAGINA