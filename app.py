from flask import Flask, render_template, request, url_for, redirect

app=Flask(__name__)

@app.before_request
def before_request():
   print("Antes de la peticion...")

@app.after_request
def after_request(response):
   print("Despues de la peticion")
   return response

@app.route('/')
def index():
   # return "<h1>UskoKruM2010 - Tutorial!</h1>"
   cursos = ['PHP','Python','Java','Kotlin','Dart','JavaScript']
   data = {
      'titulo': 'Index123',
      'bienvenida': 'Saludos!',
      'cursos': cursos,
      'numero_cursos': len(cursos)
   }
   return render_template('index.html',data=data)

@app.route('/contacto/<nombre>/<int:edad>') # <nombre> esto indica que es un parametro que ira dentro de la URL.
def contacto(nombre,edad): # colocamos el mismo nombre que en el parametro de arriba.
   data = {
      'titulo': 'Contacto',
      'nombre': nombre,
      'edad': edad
   }
   return render_template('contacto.html', data=data)   

def query_string():
   print(request)
   print(request.args)
   print(request.args.get('param1'))
   print(request.args.get('param2'))
   return "Ok"

def pagina_no_encontrada(error):
   # return render_template('404.html'), 404
   return redirect(url_for('index'))

if __name__=='__main__':
   app.add_url_rule('/query_string',view_func=query_string)
   app.register_error_handler(404,pagina_no_encontrada)
   app.run(debug=True,port=5000) # en lugar de 5000 podesmos colocar cualquier numero.
