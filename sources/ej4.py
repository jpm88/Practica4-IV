#!/usr/bin/python
# -*-coding: utf-8 -*-

import web
from web import form
from web.contrib.template import render_mako
import dbm
from mako.template import Template
import sys
import pymongo
import feedparser
import tweepy


paginas=[]
paginas.insert(0,"Vacia")
paginas.insert(1,"Vacia")
paginas.insert(2,"Vacia")

        
urls = (
    '/*', 'index',
    '/formulario', 'formulario',
	 '/modifica', 'modifica',
	 '/desconectar', 'desconectar',	
	 '/pagina1', 'pagina1',	
	 '/pagina2', 'pagina2',
	 '/pagina3', 'pagina3',
	 '/pagina4', 'pagina4',
	 '/graficos', 'graficos',
	 '/rss', 'rss',
	 '/mapa', 'mapa',
	 '/twitter', 'twitter',
)
app = web.application(urls, globals())

###########TWITTER#############
 
def twitterfuncion(q):

	# Consumer keys and access tokens, used for OAuth
	consumer_key = 'rmuzf54RNldaNqPAio5Osg'
	consumer_secret = 'oF8EcGF029xujron9u8qjnfyl7MZDs0aFshkDEYI'
	access_token = '794094740-4ehh0GMWSsIhju5g4f3cZvq5DFwEpGqxNoTTxK6h'
	access_token_secret = 'Bhqf4zdb4sESerWc939JuptnEwUqFznwmxhbDOkC80vjE'
	# OAuth process, using the keys and tokens
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	# Creation of the actual interface, using authentication
	api = tweepy.API(auth)
	
	
	
	conta = 0	
	t=[]
	
	
	for tweet in tweepy.Cursor(api.search,
                           q,
			   geocode="40,4,800km",
                           rpp=2,
			   count=0,
                           result_type="recent",
                           include_entities=True,
                           lang="es").items():
   	
	 if tweet.geo:		
		lan, lon = tweet.geo['coordinates']
		t.append([lan,lon,tweet.user.screen_name, tweet.text])
		conta = conta +1
	 	
	 if conta >= 5 :
			return t
	return t
	 




if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'usuario':''})
    web.config._session = session
else:
    session = web.config._session


###########mongodb#############

# Connection to Mongo DB
try:
    conn=pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 

db = conn.RegistroUsurarios

usuarios = db.usuarios

#Creando la conexión por defecto
#conexion = Connection()
 
#Definiendo la BD que vamos a usar. En caso de no existir, se crea automágicamente al insertar el primer registro
#db = conexion.bdRegistroUsuarios
 
#Se ingresa la información en estilo JSON (los mismos datos de arriba) y se guarda en una variable
#alumno1 = {"Alumno": "Mario Andrés Cares Cabezas", "Dirección": "El Canelo 2652, Iquique, Chile", "Fecha Nacimiento": "1990-05-16", "Carrera": "Ing. Informática", "Semestre Actual": 8, "Ramos": ["Adm. Recursos Humanos", "Economía", "Proyecto Final", "Aud. Computacional"]}
 
#Guardamos el alumno
#db.alumnos.save(alumno1)
 
#Leemos los alumnos ingresados
#cursor = db.alumnos.find()
#for alumno in cursor:
#print alumno


######################


render = web.template.render('./static/')

def contra_correcta (usuario):
        return usuario


def comprueba_identificacion ():
        usuario = session.usuario
        return usuario

def noticias():
	noticia1 = ""
	noticia2 = ""
	noticia3 = ""
	noticia4 = ""
	noticia5 = ""

	conte1 = ""
	conte2 = ""
	conte3 = ""
	conte4 = ""
	conte5 = ""		

	d = feedparser.parse(r'http://eu.square-enix.com/es/rss.xml')
	
	# Titulos
	noticia1 = d.entries[0].title
	noticia2 = d.entries[1].title
	noticia3 = d.entries[2].title
	noticia4 = d.entries[3].title
	noticia5 = d.entries[4].title

	# Contenido
	conte1= d.entries[0].summary
	conte2= d.entries[1].summary
	conte3= d.entries[2].summary
	conte4= d.entries[3].summary
	conte5= d.entries[4].summary


	#noticias[i][2] = d.entries[i].id
	
	noticias1 = [noticia1, conte1, noticia2, conte2, noticia3, conte3, noticia4, conte4, noticia5, conte5]

	return noticias1


formularioDatos = form.Form( 
    form.Textbox("nombre", form.notnull,form.Validator('No vacio', lambda x:x!=""), description = "Nombre:", value=""),
	 form.Textbox("apellido1", form.notnull,form.Validator('No vacio', lambda x:x!=""), description = "Primer apellido:", value=""),
	 form.Textbox("apellido2", form.notnull, form.Validator('No vacio', lambda x:x!=""), description = "Segundo apellido:", value=""),
	 form.Textbox("correo", form.notnull, form.regexp('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', "Formato incorrecto"), description = "Correo Electronico:", value=""),
	 form.Textbox("dni", form.notnull, description = "DNI:", value=""),
	 form.Dropdown('dia', ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31' ])	, 
	 form.Dropdown('mes', ['1','2','3','4','5','6','7','8','9','10','11','12' ])	,
	 form.Dropdown('year', ['1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994' ])	,
	 form.Textarea("direccion", form.notnull, form.Validator('No vacio', lambda x:x!=""),description = "Direccion:", value=""),
	 form.Password("contrasena", form.Validator('5 caracteres', lambda x: len(x)>=5),description = "Contrasena:", value=""),
	 form.Password("repite", form.notnull, form.notnull, form.Validator('No vacio', lambda x:x!=None),description = "Repite Contrasena:", value=""),	 
	 form.Radio("pago", [('contra' ,'Contra reembolso'),('visa' ,'Visa')] ), 
	 form.Checkbox("clausulas", description = "Acepta todas las clausulas", value=""),

    form.Button("Enviar"),
	  validators = [form.Validator("No coinciden las contraseñas", lambda x: x.contrasena == x.repite), form.Validator("Error fecha.", lambda x: (((int(x.mes) == 2) and ((int(x.dia) <= 28) and ((int(x.year) % 4) != 0) or (int(x.dia) <= 29) and ((int(x.year) % 4) == 0))) or ((int(x.dia) <= 30) and ((int(x.mes) == 4) or (int(x.mes) == 6) or (int(x.mes) == 9) or (int(x.mes) == 11)))))] 
) 



formacceso = form.Form( 
	form.Textbox("usuario",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Usuario:"),
	form.Password("contra",form.notnull, form.Validator('No vacio', lambda x:x!=None),description = "Contraseña:"),
	form.Button("Enviar"),
		)

formtwi = form.Form( 
	form.Textbox("busqueda",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Tweets que desea buscar:"),
	form.Button("Enviar"),
		)

formmapa = form.Form( 
	form.Textbox("latitud",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Latitud:"),
	form.Textbox("longitud",form.notnull, form.Validator('No vacio', lambda x:x!=None),description = "Longitud:"),
	form.Button("Enviar"),
		)


formmodifica = form.Form( 
	form.Textbox("usuario",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Usuario:"),
	form.Textbox("dni",form.notnull, form.Validator('No vacio', lambda x:x!=None),description = "Dni:"),
	form.Button("Enviar"),
		)

formgrafico = form.Form( 
	form.Textbox("enero",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Enero:"),
	form.Textbox("febrero",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Febrero:"),
	form.Textbox("marzo",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Marzo:"),
	form.Textbox("abril",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Abril:"),
	form.Textbox("mayo",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Mayo:"),
	form.Textbox("junio",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Junio:"),
	form.Textbox("julio",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Julio:"),
	form.Textbox("agosto",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Agosto:"),
	form.Textbox("septiembre",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Septiembre:"),
	form.Textbox("octubre",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Octubre:"),
	form.Textbox("noviembre",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Noviembre:"),
	form.Textbox("diciembre",form.notnull, form.Validator('No vacio', lambda x:x!=None), description = "Diciembre:"),
	form.Dropdown('tipo', ['PieChart','Histogram' ])	,
	form.Button("Enviar"),
		)



class index:
	def GET(self):
			
			usuario = comprueba_identificacion ()
			

			formu = formacceso	

			if usuario:				
				return render.indexlog(usuario=usuario)
			else:
				return render.index(formu)

	def POST(self): 

		usuario = comprueba_identificacion ()	
		twitterfuncion("Camion")	

		formu = formacceso
                if not formu.validates ():
                        return render.index(formu) 
		i = web.input()
                usuario = i.usuario
                contra = i.contra

		
                if contra == contra_correcta(usuario):
                        session.usuario = usuario
                        return render.indexlog(usuario=usuario)
		else:

			return render.index(formu)


class desconectar:
        def GET(self):
        		
				session.kill()
								   
				return web.seeother('/')  

class pagina1:
        def GET(self):
        		
				usuario = comprueba_identificacion ()
				paginas[2]=paginas[1]
				paginas[1]=paginas[0]
				paginas[0]='pagina1' 
								   
				return render.pagina1(usuario, paginas)

class pagina2:
        def GET(self):
        	
				usuario = comprueba_identificacion ()	
				paginas[2]=paginas[1]
				paginas[1]=paginas[0]
				paginas[0]='pagina2'
								   
				return render.pagina2(usuario, paginas)

class pagina3:
        def GET(self):
        	
				usuario = comprueba_identificacion ()	
				paginas[2]=paginas[1]
				paginas[1]=paginas[0]
				paginas[0]='pagina3'
								   
				return render.pagina3(usuario, paginas)

class pagina4:
        def GET(self):
        		
				usuario = comprueba_identificacion ()
				paginas[2]=paginas[1]
				paginas[1]=paginas[0]
				paginas[0]='pagina4'
								   
				return render.pagina4(usuario, paginas)


class formulario:
	def GET(self):
		
		
		form = formularioDatos()
		return render.formulario(form)
		
	

	def POST(self):

		form = formularioDatos()

		if not form.validates():
			mensaje='Error. Datos incorrectos'			
			return render.formulario(form)		
		else:	
			usuario1 = {'Nombre': form.d.nombre, "Apellido1": form.d.apellido1,"Apellido2": form.d.apellido2, "Correo": form.d.correo, "DNI": form.d.dni, "Dia": form.d.dia, "Mes": form.d.mes, "Year": form.d.year, "Direccion": form.d.direccion, "Contrasena": form.d.contrasena, "Pago": form.d.pago}
			 
			#Guardamos el usuario
			usuarios.insert(usuario1)

			mensaje='Usuario introducido correctamente'			
			return render.formulario2(mensaje)



class modifica:
	def GET(self):
		
		
		#form2 = formmodifica()
		#return render.modifica(form2)
		form = formularioDatos()
		
		p_usu = usuarios.find_one({'Nombre':session.usuario})
		#print p_usu
		
		form.nombre.value = p_usu['Nombre']
		form.apellido1.value = p_usu['Apellido1']
		form.apellido2.value = p_usu['Apellido2']
		form.correo.value = p_usu['Correo']
		form.dni.value = p_usu['DNI']
		form.dia.value = p_usu['Dia']
		form.mes.value = p_usu['Mes']
		form.year.value = p_usu['Year']	 
		form.direccion.value = p_usu['Direccion']		
		form.pago.value=p_usu['Pago']  
			 			
		return render.formulario(form)
		
	

	def POST(self):

		form = formularioDatos()

		if not form.validates():
			mensaje='Error. Datos incorrectos'			
			return render.formulario(form)		
		else:

			 usuarios.update({"Nombre" : session.usuario},{"Nombre": form.d.nombre, "Apellido1": form.d.apellido1, "Apellido2": form.d.apellido2, "Correo": form.d.correo, "DNI": form.d.dni, "Dia": form.d.dia, "Mes": form.d.mes, "Year": form.d.year, "Direccion": form.d.direccion, "Contrasena": form.d.contrasena, "Pago": form.d.pago});
			 
			 mensaje='Datos modificados correctamente'			
			 return render.formulario2(mensaje)






class graficos:
	def GET(self):
		
		
		form = formgrafico()
		return render.formulario(form)
		
	

	def POST(self):

		form = formgrafico()

		if not form.validates():
			mensaje='Error. Datos incorrectos'			
			return render.formulario(form)		
		else:	
			datos=[]
	
			datos.insert(0,form.d.enero)
			datos.insert(1,form.d.febrero)
			datos.insert(2,form.d.marzo)
			datos.insert(3,form.d.abril)
			datos.insert(4,form.d.mayo)
			datos.insert(5,form.d.junio)
			datos.insert(6,form.d.julio)
			datos.insert(7,form.d.agosto)
			datos.insert(8,form.d.septiembre)
			datos.insert(9,form.d.octubre)
			datos.insert(10,form.d.noviembre)
			datos.insert(11,form.d.diciembre)
			tipo=form.d.tipo
			
			print datos[7]

						
			return render.graficos(datos,tipo)



class rss:	

	def GET(self):
	
		noti = noticias()
		return render.rss(noti)


class mapa:
	def GET(self):
		
		
		form = formmapa()
		return render.formulario(form)
		
	

	def POST(self):

		form = formmapa()

		if not form.validates():
			mensaje='Error. Datos incorrectos'			
			return render.formulario(form)		
		else:	
			datos=[]
	
			datos.insert(0,form.d.latitud)
			datos.insert(1,form.d.longitud)
			
			

						
			return render.mapa(datos)


class twitter:
	def GET(self):
		
		
		form = formtwi()
		return render.formulario(form)
		
	

	def POST(self):

		form = formtwi()

		if not form.validates():
			mensaje='Error. Datos incorrectos'			
			return render.formulario(form)		
		else:	
			datos=[]
	
			datos = twitterfuncion(form.d.busqueda)			

						
			return render.twitter(datos)

	

if __name__ == "__main__":
    app.run()
