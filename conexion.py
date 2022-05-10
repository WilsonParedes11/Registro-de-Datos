#-----@Wilson11-----#
import mysql.connector 

class registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='base_datos', 
                                            user = 'root',
                                            password ='')
    
    def insertar_contacto(self,codigo,nombre,telefono,correo,direccion):

        cur=self.conexion.cursor()
        sql='''INSERT INTO contacto (CODIGO,NOMBRE,TELEFONO,CORREO,DIRECCION)
        VALUES ('{}','{}','{}','{}','{}')'''.format(codigo,nombre,telefono,correo,direccion)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
    
    def actualizar(self,codigo,nombre,telefono,correo,direccion):

        cur=self.conexion.cursor()
        sql='''UPDATE contacto SET CODIGO='{}',NOMBRE='{}',TELEFONO='{}',CORREO='{}',DIRECCION='{}'
        WHERE nombre ='{}' '''.format(codigo,nombre,telefono,correo,direccion,nombre)
        cur.execute(sql)
        a=cur.rowcount
        self.conexion.commit()
        cur.close()
        return a

    def elimina_contacto(self,nombre):

        cur=self.conexion.cursor()
        sql='''DELETE FROM contacto WHERE NOMBRE = {} '''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def busca_contacto(self,nombre):

        cur=self.conexion.cursor()
        sql="SELECT * FROM contacto WHERE NOMBRE = {} ".format(nombre)
        cur.execute(sql)
        nombrex=cur.fetchall()
        cur.close()
        return nombrex

    def mostrar_contacto(self):

        cur=self.conexion.cursor()
        sql="SELECT * FROM contacto"
        cur.execute(sql)
        registro=cur.fetchall()
        return registro

    
    
    




