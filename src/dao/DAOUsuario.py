import pymysql

class DAOUsuario:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_poo" )
        # return pymysql.connect(host="localhost",user="userapp2",password="$$Utec2211$$",db="db_poo" )

    def read(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute("SELECT * FROM usuario order by nombre asc")
            else:
                cursor.execute("SELECT * FROM usuario where id = %s order by nombre asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
    def read_prod(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute("SELECT * FROM productos order by producto asc")
            else:
                cursor.execute("SELECT * FROM productos where id = %s order by producto asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
    
    def read_ventas(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute("SELECT * FROM ventas order by nombre asc")
            else:
                cursor.execute("SELECT * FROM ventas where id = %s order by nombre asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def read_reg(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute("SELECT * FROM register order by nombre asc")
            else:
                cursor.execute("SELECT * FROM register where id = %s order by nombre asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def read_pedidos(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute("SELECT * FROM pedidos order by producto asc")
            else:
                cursor.execute("SELECT * FROM pedidos where id = %s order by producro asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()


    def insert(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO usuario(nombre,telefono,email) VALUES(%s, %s, %s)", (data['nombre'],data['telefono'],data['email'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    
    def insert_Venta(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO ventas(nombre,categoria,cantidad,cliente,estado) VALUES(%s, %s, %s,%s,%s)", (data['nombre'],data['categoria'],data['cantidad'],data['cliente'],data['estado']))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    def insert_prod(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO productos(producto,categoria,stock) VALUES(%s, %s, %s)", (data['producto'],data['categoria'],data['stock'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def insert_reg(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO register(nombre,contra1,contra2,telefono,email) VALUES(%s, %s, %s,%s,%s)", (data['nombre'],data['contra1'],data['contra2'],data['telefono'],data['email']))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE register set nombre = %s, telefono = %s, email = %s where id = %s", (data['nombre'],data['telefono'],data['email'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM register where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    def update2(self, id, data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE usuario set nombre = %s, telefono = %s, email = %s where id = %s", (data['nombre'],data['telefono'],data['email'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete2(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM usuario where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    def updateVenta(self, id, data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE ventas set nombre = %s, categoria = %s, cantidad = %s, cliente = %s, estado = %s where id = %s", (data['nombre'],data['categoria'],data['cantidad'],data['cliente'],data['estado'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def deleteVenta(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM ventas where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    def updateProd(self, id, data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE productos set producto = %s, categoria = %s, stock = %s where id = %s", (data['producto'],data['categoria'],data['stock'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def deleteProd(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM productos where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
