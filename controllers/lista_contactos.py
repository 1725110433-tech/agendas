from csv import reader


class ListaContactos:

    def conectar(self):
    def obtenerContactos(self):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            return conexion
        except Exception as error:
            print(f"ERROR 100: {error.args}")
            return None

    def listaContactos(self):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()
            sql = "SELECT * FROM contactos"
            sql = "SELECT * FROM contactos;"
            cursor.execute(sql)
            contactos = cursor.fetchall()
            return contactos
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                contacto = {
                    "id_contacto":fila[0],
                    "nombre":fila[1],
                    "primer_apellido":fila[2],
                    "segundo_apellido":fila[3],
                    "email":fila[4],
                    "telefono":fila[5]
                }
                datos.append(contacto)

            conexion.close()
            print(datos)
            return datos
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return None
            return []

    def GET(self):
        print(self.listaContactos())
        return render.lista_contactos()
        contactos = self.obtenerContactos()
        return render.lista_contactos(contactos)