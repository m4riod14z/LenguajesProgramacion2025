# S - Single responsibility: Se crean clases solo para una tarea especifica

# Clases en Python:
# - Atributos: Clase (Static): se pueden usar sin instanciar la clase 
#              Instancia: Propios del objeto, necesita instancia, comunes a todos los objetos de la clase
# - Metodos

class reportGenerator:

    # Metodo de instanciación:
    def __init__(this, data):
        # self.data es un atributo de instancia:
        this.data = data

    # Todos los metodos donde se use un atributo de instancia, debe tener como primer parametro
    # una referencia a la instancia
    def generateReport(this):
        return f"Generando reporte: {this.data}"
    

# Esta clase tiene la responsabilidad unica de guardar un reporte:
class ReportSaver():
    
    def saveToFile(this, report, filename):
        with open(filename, "w") as reportFile:
            reportFile.write(report)


# Esta clase tendria la responsabilidad unica de imprimir el reporte:
class reportPrinter:
    pass


# ¿Cómo se usan?
reportData = reportGenerator("Estos son los datos del reporte: xdxdxdxd").generateReport()
reportSaver = ReportSaver()
reportSaver.saveToFile(reportData, "nuevoReporte.txt")

# O - Open for Extension                      
#     Closed for Modification: Permite añadir funcionas y heredarlas, pero no modificarlas

# Mantenible, Escalable, Testeable, Configurable, Reutilizable, Extensible

# Se usan clases abstractas para no modificar los descuentos

from abc import ABC, abstractmethod
class Discount(ABC):
    
    @abstractmethod
    def applyDiscount(this, price):
        # Se pone la instruccion "pass" porque una clase abstracta no implementa funcionalidades,
        # lo hacen las clases hijas
        pass

# Aplica descuento del 20%
class FrecuentClientDiscount(Discount):
    def applyDiscount(this, price):
        this.discount = 0.8
        return super().applyDiscount(price*this.discount)
    

class VipDiscount(Discount):
    def applyDiscount(this, price):
        this.discount = 0.5
        return super().applyDiscount(price)
    
# L - Liskov Substitution Principle: Una clase derivada puede sustituir a una clase base sin afectar el comportamiento del sistema
# Los subtipos pueden ser usados en reemplazo de sus clases base sin afectar la funcionalidad (Interfaces o Clases abstractas)

class Rectangle:

    def __init__(self, width, height):
        self.widht = width
        self.height = height

    def set_width(self, width):
        self.widht = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.widht * self.height
    

class Square(Rectangle):

    # Vulnera el principio LSP: Ya que no se puede usar un cuadrado como un rectangulo
    def set_width(self, width):
        self.height = width
        self.widht = width

    def set_height(self, height):
        self.height = height
        self.widht = height

# No se puede usar Square en reemplazo de Rectangle, porque los metodos son distintos a los de la clase base:
# La solucion es implementar una clase abstracta shape, de la cual Square y Rectangle, hereden

class Shape(ABC):

    @abstractmethod
    # La implementacion se le deja a las subclases
    def area(self):
        pass

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height
    
class Square(Shape):

    def __init__(this, side):
        this.side = side

    def area(this):
        return this.side**2
    
# ¿Por qué respeta el principio LSP?: Ambos heredan la misma forma (shape) 

# I - Interface Segregation Principle (ISP): Clientes no deben depender de metodos que no usan, segregar es separar en interfaces solo los metodos que se van a usar
# Está relacionado con el principio S
# Tipos de impresion

class Printer(ABC):

    @abstractmethod
    def print(this, document):
        pass

    @abstractmethod
    def fax(this, document):
        pass

    @abstractmethod
    def scan(this, document):
        pass

# Impresora moderna
class HQPrinter(Printer):
    
    def print(this, document):
        return super().print(document)
    
    def scan(this, document):
        return super().scan(document)
    
    def fax(this, document): # Vulnera el principio ISP
        raise NotImplementedError("Las impresoras modernas no envian fax")

# Impresora antigua, de baja calidad
class LQPrinter(Printer):
    
    def print(this, document):
        return super().print(document)
    
    def scan(this, document):
        return super().scan(document)
    
    def fax(this, document):
        return super().fax(document)

# Solucion
# Primero se deja la clase impresora tal y como está y se separa la funcion fax en otra interfaz
# Segrego las funcionalidades en dos interfaces o clases separadas

class Printer(ABC):

    @abstractmethod
    def print(this, document):
        pass

    @abstractmethod
    def scan(this, document):
        pass

class Fax(ABC):

    @abstractmethod
    def Fax(this, document):
        pass

class HQPrinter(Printer):
    
    def print(this, document):
        return super().print(document)
    
    def scan(this, document):
        return super().scan(document)
    
class LQPrinter(Printer, Fax):
    
    def print(this, document):
        return super().print(document)
    
    def scan(this, document):
        return super().scan(document)
    
    def Fax(this, document):
        return super().Fax(document)


# D - Dependency Inversion Principle (DIP): Las abstracciones no deben depender de los detalles
#                                           Los detalles dependen de las abstracciones

class FrontEnd:

    def __init__(this, back_end):
        this.back_end = back_end

    def show_data(this):
        data = this.back_end.getData()
        print(f"Mostrando info en el front end: {data}")

class BackEnd:

    def getData():
        return "Esta info viene de la base de datos..."
    
# Correción: Se separa el back end para segregar funcionalidades:

class FrontEnd:

    def __init__(this, dataSource):
        this.dataSource = dataSource

    def show_data(this):
        data = this.dataSource.getData()
        print(f"Mostrando info en el front end: {data}")

class DataSource(ABC):

    @abstractmethod
    def getData(this):
        pass

class SQLDataBase(DataSource):

    def getData(this):
        return "Datos de una base de datos relacional"
    
class DocumentDataBase(DataSource):

    def getData(this):
        return "Datos de una base de datos documental"
    
class API(DataSource):

    def getData(this):
        return "Datos que vienen de una API"