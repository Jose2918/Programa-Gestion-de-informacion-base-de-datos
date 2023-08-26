import mysql.connector

class BaseDatos:
    def __init__(self):
        self.con = mysql.connector.connect(
            host= "127.0.0.1",
            user="root",
            password="cisco",
            database="taquilla"
        )
    #funciones de querys
    def pelicula(self,titulo, director, genero, duracion, sinopsis, fechaLanzamiento):
        query = ('INSERT INTO peliculas(Titulo, Director, Genero, Duracion, Sinopsis, Fecha_Lanzamiento) values (%s,%s,%s,%s,%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(titulo, director, genero, duracion, sinopsis, fechaLanzamiento))
        self.idPeli = mycursor.lastrowid
        self.con.commit()
    
    def cine(self, Nombre, Direccion, Ciudad, Provincia, Pais, Capacidad_total):
        query = ('INSERT INTO cines(Nombre, Direccion, Ciudad, Provincia, Pais, Capacidad_total) values (%s,%s,%s,%s,%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(Nombre, Direccion, Ciudad, Provincia, Pais, Capacidad_total))
        self.idCine = mycursor.lastrowid
        self.con.commit()
    
    def sala(self,Numero, Capacidad):
        query = ('INSERT INTO Salas(ID_cine, Numero, Capacidad) values (%s,%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(self.idCine, Numero, Capacidad))
        self.idSala = mycursor.lastrowid
        self.con.commit()

    def funcion(self, fecha, hora):
        query = ('INSERT INTO funciones (ID_Pelicula, ID_Sala, Fecha, Hora) values (%s,%s,%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(self.idPeli,self.idSala,fecha, hora))
        self.idFuncion = mycursor.lastrowid
        self.con.commit()

    def boleto(self, Numero_asiento, Precio, Fecha_compra, Metodo_pago):
        query = ('INSERT INTO boletos(ID_Funcion, Numero_asiento, Precio, Fecha_compra, Metodo_pago) values (%s,%s,%s,%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(self.idFuncion,Numero_asiento, Precio, Fecha_compra, Metodo_pago))
        self.idBoleto = mycursor.lastrowid
        self.con.commit()
    
    def cliente(self, Nombre, Apellido, Correo_electronico, Telefono, Direccion):
        query = ('INSERT INTO clientes(Nombre, Apellido, Correo_electronico, Telefono, Direccion) values (%s,%s,%s,%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(Nombre, Apellido, Correo_electronico, Telefono, Direccion))
        self.idCliente = mycursor.lastrowid
        self.con.commit()
    
    def transaccion(self, Fecha, Hora, Monto):
        query = ('INSERT INTO transacciones(ID_Boleto,ID_Cliente,Fecha, Hora, Monto) values (%s,%s,%s,%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(self.idBoleto,self.idCliente,Fecha, Hora, Monto))
        self.idTran = mycursor.lastrowid
        self.con.commit()

    def promocion(self, Nombre, Descripcion, Fecha_inicio, Fecha_fin, descuento):
        query = ('INSERT INTO promociones(Nombre, Descripcion, Fecha_inicio, Fecha_fin, descuento) values (%s,%s,%s,%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(Nombre, Descripcion, Fecha_inicio, Fecha_fin, descuento))
        self.idPromo = mycursor.lastrowid
        self.con.commit()
    
    def calificacion(self, Nombre, Descripcion):
        query = ('INSERT INTO calificaciones(Nombre, Descripcion) values (%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(Nombre, Descripcion))
        self.con.commit()
    
    def asiento(self, Numero, Fila, Disponibilidad):
        query = ('INSERT INTO asientos(ID_Sala, Numero, Fila, Disponibilidad) values (%s,%s,%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(self.idSala, Numero, Fila, Disponibilidad))
        self.con.commit()
    
    def venta(self, Total):
        query = ('INSERT INTO ventas(ID_Transaccion, ID_Promocion, Total) values (%s,%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(self.idTran,self.idPromo,Total))
        self.con.commit()
    
    def empleado(self, Nombre, Apellido, Cargo, Email, Telefono):
        query = ('INSERT INTO empleados(Nombre, Apellido, Cargo, Correo_electronico, Telefono) values (%s,%s,%s,%s,%s);')
        mycursor = self.con.cursor()
        mycursor.execute(query,(Nombre, Apellido, Cargo, Email, Telefono))
        self.con.commit()