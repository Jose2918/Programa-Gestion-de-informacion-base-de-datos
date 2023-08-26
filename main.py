import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QMessageBox
from Base_De_Datos import BaseDatos
from app import Ui_FlashInformation
from formPeli import Ui_formPeli
from formCine import Ui_formCine
from formSala import Ui_formSala
from formFunciones import Ui_formFunciones
from formBoleto import Ui_formBoleto
from formCliente import Ui_formCliente
from formTran import Ui_formTran
from formPromo import Ui_formPromo
from formCali import Ui_formCali
from forAsiento import Ui_formAsiento
from venta import Ui_formVenta
from formEmpleado import Ui_formEmpleado

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.base = BaseDatos()
        self.ui = Ui_FlashInformation()
        self.ui.setupUi(self)
        
        #MenuPelicula
        self.ui.actionPeliculas.triggered.connect(self.windowPeliculas)
        self.ui.actionCines.triggered.connect(self.windowCines)
        self.ui.actionSalas.triggered.connect(self.windowSalas)
        self.ui.actionFunciones.triggered.connect(self.windowFunciones)

        #MenuCliente
        self.ui.actionBoletos.triggered.connect(self.windowBoletos)
        self.ui.actionClientes.triggered.connect(self.windowCliente)
        self.ui.actionTransacciones.triggered.connect(self.windowTransacciones)
        self.ui.actionPromociones.triggered.connect(self.windowPromociones)
        self.ui.actionCalificaciones.triggered.connect(self.windowCalificaciones)
        self.ui.actionAsientos.triggered.connect(self.windowAsientos)

        #menu Venta
        self.ui.actionVentas.triggered.connect(self.windowVenta)
        #menu Empleado
        self.ui.actionEmpleadp.triggered.connect(self.windowEmpleado)


    #menu Peliculas
    def windowPeliculas(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formPeli()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()
        
        #informacion de pelicula
        def getFieldPeli():
            try:
                titulo = self.ui_new_window.tituloPeli.text()
                director = self.ui_new_window.directorPeli.text()
                genero = self.ui_new_window.generoPeli.text()
                duracion = self.ui_new_window.duracionPeli.text()
                sinopsis = self.ui_new_window.sinopsisPeli.toPlainText()
                fecha = self.ui_new_window.fechaPeli.text()
                self.base.pelicula(titulo, director, genero, duracion, sinopsis, fecha)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))

        self.ui_new_window.enviarPeli.clicked.connect(getFieldPeli)
        
    #menu cines
    def windowCines(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formCine()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()

        #obtener informacion cine
        def getFieldCine():
            try:
                nombre = self.ui_new_window.nombreCine.text()
                direccion = self.ui_new_window.direccionCine.text()
                ciudad = self.ui_new_window.ciudadCine.text()
                provincia = self.ui_new_window.provinciaCine.text()
                pais = self.ui_new_window.paisCine.text()
                capacidad = self.ui_new_window.capacidadCine.value()
                self.base.cine(nombre, direccion, ciudad, provincia, pais, capacidad)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))

        self.ui_new_window.enviarCine.clicked.connect(getFieldCine)

    #menu sala
    def windowSalas(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formSala()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()

        #obtener informacion sala
        def getFieldSala():
            try:
                numero = self.ui_new_window.numeroSala.value()
                capacidad = self.ui_new_window.capacidadSala.value()
        
                self.base.sala(Numero=numero,Capacidad= capacidad)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))
        
        self.ui_new_window.enviarSala.clicked.connect(getFieldSala)

    #menu funciones
    def windowFunciones(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formFunciones()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()

        #obtener informacion funciones
        def getFieldFunciones():
            try:
                fecha = self.ui_new_window.fechaFunciones.text()
                hora = self.ui_new_window.horaFunciones.text()
                self.base.funcion(fecha, hora)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))
        
        self.ui_new_window.enviarFunciones.clicked.connect(getFieldFunciones)
    
    #menu clientes
    def windowBoletos(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formBoleto()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()
       
        #obtener informacion boletos
        def getFieldBoleto(index):
            try:
                numeroAsiento = self.ui_new_window.asientoBoleto.text()
                precio = self.ui_new_window.precioBoleto.value()
                fecha = self.ui_new_window.fechaBoleto.text()
                metodoPago= self.ui_new_window.metodopaBoleto.itemText(index)
           
                self.base.boleto(numeroAsiento, precio, fecha, metodoPago)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))
        
        self.ui_new_window.enviarBoleto.clicked.connect(getFieldBoleto)
    
    def windowCliente(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formCliente()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()

        #obtener informacion cliente
        def getFieldCliente():
            try:
                nombre = self.ui_new_window.nombreCliente.text()
                apellido = self.ui_new_window.apellidoCliente.text()
                email = self.ui_new_window.emailCliente.text()
                telefono = self.ui_new_window.telCliente.text()
                direccion = self.ui_new_window.direccionCliente.text()
                
                self.base.cliente(nombre, apellido, email, telefono, direccion)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))    
        
        self.ui_new_window.enviarCliente.clicked.connect(getFieldCliente)
    
    #menu transacciones
    def windowTransacciones(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formTran()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()

        #obtener informacion transacciones
        def getFieldTransaccion():
            try:
                fecha = self.ui_new_window.fechaTran.text()
                hora = self.ui_new_window.horaTran.text()
                monto = self.ui_new_window.montoTran.value()
                
                self.base.transaccion(fecha, hora, monto)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))
        
        self.ui_new_window.enviarTran.clicked.connect(getFieldTransaccion)
    
    def windowPromociones(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formPromo()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()

        #obtener informacion promociones
        def getFieldPromo():
            try:
                nombre = self.ui_new_window.nombrePromo.text()
                descripcion = self.ui_new_window.descripcionPromo.toPlainText()
                fechaInit = self.ui_new_window.fechainiPromo.text()
                fechaEnd = self.ui_new_window.fechafinPromo.text()
                descuento = self.ui_new_window.descuentoPromo.value()
                self.base.promocion(nombre, descripcion, fechaInit, fechaEnd, descuento)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))
        
        self.ui_new_window.enviarPromo.clicked.connect(getFieldPromo)
    
    #menu calificaciones
    def windowCalificaciones(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formCali()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()

        #obtener informacion calificacion
        def getFieldCalificacion():
            try:
                nombre = self.ui_new_window.nombreCali.text()
                descripcion = self.ui_new_window.descripcionCali.toPlainText()

                self.base.calificacion(nombre, descripcion)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))
        
        self.ui_new_window.enviarCali.clicked.connect(getFieldCalificacion)
    
    #menu asientos
    def windowAsientos(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formAsiento()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()

        #obtener informacion asientos
        def getFieldAsiento():
            try:
                numero = self.ui_new_window.numeroAsiento.value()
                fila = self.ui_new_window.filaAsiento.text()
                disponibilidad = self.ui_new_window.disponibleAsiento.value()

                self.base.asiento(numero, fila, disponibilidad)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))
        
        self.ui_new_window.enviarAsiento.clicked.connect(getFieldAsiento)

    #menu Venta
    def windowVenta(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formVenta()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()

        #obtener informacion venta
        def getFieldVenta():
            try:
                total = self.ui_new_window.totalVenta.value()
                self.base.venta(total)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))
        
        self.ui_new_window.enviarVenta.clicked.connect(getFieldVenta)

    #menu Empleado
    def windowEmpleado(self):
        self.new_window = QMainWindow()
        self.ui_new_window = Ui_formEmpleado()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()

        #obtener informacion empleado
        def getFieldEmpleado():
            try:
                nombre = self.ui_new_window.nombreEmpleado.text()
                apellido = self.ui_new_window.apellidoEmpleado.text()
                cargo = self.ui_new_window.cargoEmpleado.text()
                email = self.ui_new_window.emailEmpleado.text()
                telefono= self.ui_new_window.telEmpleado.text()
                
                self.base.empleado(nombre, apellido, cargo, email, telefono)
                QMessageBox.information(None, "Éxito", "Enviado correctamente")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))
        
        self.ui_new_window.enviarEmpleado.clicked.connect(getFieldEmpleado)
    

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        QMessageBox.information(None, "Éxito", "Sesión iniciado correctamente")
        sys.exit(app.exec_())  
    except Exception as e:
        QMessageBox.critical(None, "Error", str(e))
    
    