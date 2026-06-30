import web
import sqlite3

render = web.template.render('views', nase='layout')

class VerContacto:

    def GET (self,id_contacto):
        print(f"ID_CONTACTO: {id_contacto}")
        return render.ver_contacto()