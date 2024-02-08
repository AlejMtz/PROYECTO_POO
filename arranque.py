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

@app.route('/n_producto')
def n_producto():
 return render_template('n_producto.html')

@app.route('/g_producto')
def g_producto():
 return render_template('g_producto.html')

@app.route('/n_cliente')
def n_cliente():
 return render_template('n_cliente.html')

@app.route('/g_cliente')
def g_cliente():
 return render_template('g_cliente.html')

@app.route('/n_proveedor')
def n_proveedor():
 return render_template('n_proveedor.html')

@app.route('/g_proveedor')
def g_proveedor():
 return render_template('g_proveedor.html')

@app.route('/n_venta')
def n_venta():
 return render_template('n_venta.html')

@app.route('/n_usuario')
def n_usuario():
 return render_template('n_usuario.html')

@app.route('/g_usuario')
def g_usuario():
 return render_template('g_usuario.html')

#ACTIVAR LA VALIDACION PARA QUE LA PAGINA SE QUEDE EJECUTANDO EN EL SERVIDOR
if __name__ == '__main__':
    app.run(debug=True)
    #OPCION PARA QUE SE REINICIE CADA QUE CAMBIO ALGO EN LA PAGINA