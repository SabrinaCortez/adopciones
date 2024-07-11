from flask import Flask,render_template, request, redirect
from controller import *

app = Flask(__name__)


@app.route('/')
def getIndex():
    title="Index"
    # conexion = probar_Conexion()
    # print (conexion)
    return render_template("index.html",title=title)

@app.route('/contacto')
def dataContacto():
    title="Contacto"
    return render_template("contacto.html",title=title)

@app.route('/perros')
def dataPerros():
    title="Perros"
    perros = obtener_AnimalesPublicados('PE')
    return render_template("perros.html",title=title,perros=perros)

@app.route('/gatos')
def dataGatos():
    title="Gatos"
    gatos = obtener_AnimalesPublicados('GA')
    return render_template("gatos.html",title=title,gatos=gatos)

@app.route('/nosotros')
def dataNosotros():
    title="Nosotros"
    return render_template("nosotros.html",title=title)

@app.route('/donar')
def dataDonar():
    title="Donar"
    return render_template("donar.html",title=title)

@app.route('/formAdopsion')
def dataForm():
    title="Formulario de adopcion"
    tipoEstados = obtener_TipoEstado()
    tipoAnimales = obtener_TipoAnimales()
    publicados = obtener_AnimalesPublicadosNombres()
    # for row in publicados:
    #        print(row)
    return render_template("formAdopcion.html",title=title,tipoEstados=tipoEstados,tipoAnimales=tipoAnimales,publicados=publicados)

@app.route('/transito')
def dataTransito():
    title="Transito"
    perros = obtener_AnimalesEnTransito('PE')
    gatos = obtener_AnimalesEnTransito('GA')
    return render_template("transito.html",title=title,perros= perros,gatos =gatos )


    # Ruta para procesar el formulario
@app.route('/formularioAdopcionGrabar', methods = ['POST'])
def formularioAdopcion_Grabar():
    # Obtener el valor seleccionado del combo box
    tipoanimal = request.form['tipoanimal']
    idAnimales = request.form['idAnimales']
    tipoestado = request.form['tipoestado']
    cNombreyApellido = request.form['cNombreyApellido']
    cDNI = request.form['cDNI']
    cCorreo = request.form['cCorreo']
    cLinkInstagram = request.form.get('cTelefono')
    cTelefono = request.form.get('cTelefono')
    dFechaNacimiento = request.form.get('dFechaNacimiento ')
    cCasaDepartamento = request.form.get('cCasaDepartamento')
    print('Grabamos la adopcion')
    adoptante_nuevo(cDNI,cNombreyApellido,cCorreo,cLinkInstagram,cTelefono,dFechaNacimiento,cCasaDepartamento)
    estado_Actualizar (idAnimales , cDNI,tipoestado)
    # Aquí puedes realizar acciones con el valor seleccionado, como consultas adicionales o redireccionamientos
    # {cCasaDepartamento}{dFechaNacimiento} {cTelefono}{cLinkInstagram}
    print  (f"El tipo de animal seleccionado tiene el ID:  {cCasaDepartamento}{dFechaNacimiento} {cTelefono}{cLinkInstagram}{cCorreo} {cDNI}{cNombreyApellido} {idAnimales} {tipoanimal} {tipoestado}")
    return redirect("/")
#f"El tipo de animal seleccionado tiene el ID:{cCasaDepartamento}{dFechaNacimiento}{cTelefono} {cNombreyApellido} {idAnimales} {tipoanimal} {tipoestado}"
