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

# O - Open for Extension                      Mantenible, Escalable, Testeable, Configurable
#     Closed for Modification

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
    
# L - Liskov Substitution Principle: Una clase derivada puede sustituir a una clase base sin afectar el comportamiento
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

    # Viola el principio LSP:
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
    
# ¿Por qué respeta el principio LSP?