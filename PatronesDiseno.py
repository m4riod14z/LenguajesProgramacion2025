# Design Patterns: Como van a interacturar los distintos objetos del sistema


# Creational Patterns: Como se crean los objetos
# 1. Singleton: Permite que se cree solo una instancia de objeto

from abc import ABC, abstractmethod


# class NoSingleton:
#     pass

# class Singleton:

#     # Atributo de clase que guarda una referencia a la instancia una vez se crea
#     _instance = None

#     def __new__(cls, user, password):
#         if cls._instance is None:
#             # Crea una sola instancia de clase si esta no existe:
#             cls._instance = super(Singleton, cls).__new__(cls)
#             cls._instance.__setattr__("user", user)
#             cls._instance.__setattr__("password", password)
#         return cls._instance

#     def getUser(this):
#         return this.user
    
#     def getPassword(this):
#         return this.password
    
# # Ejemplo con un objeto que maneja sesion:
# sesion1 = Singleton("Diego", "abcd1234")
# sesion2 = Singleton("Diego2", "abcd456")
# print(f"{sesion1.getUser()}")
# print(f"{sesion2.getUser()}")

# objeto1 = Singleton()
# objeto2 = Singleton()

# objeto3 = NoSingleton()
# objeto4 = NoSingleton()

# # Objeto 1 y Objeto 2 son la misma instancia de clase, es decir, son el mismo objeto
# print(f"Objeto 1 es Objeto 2?: {objeto1 is objeto2}")
# print(f"El objeto 1 es: {objeto1}")
# print(f"El objeto 2 es: {objeto2}")

# print(f"Objeto 3 es Objeto 4?: {objeto3 is objeto4}")
# print(f"El objeto 3 es: {objeto3}")
# print(f"El objeto 4 es: {objeto4}")

# Ejercicio: Cree un logger o bitacora de eventos que use el patron Singleton


# 2. Abstract Factory: Permite crear familias de objetos relacionados sin especificar las subclases

# Clases abstractas
# Clases concretas
# Abstract Factory: Aqui se encuentra todo el control
# Concrete Factory
# Cliente

# Ejemplo para crear elementos de GUI
# class Button(ABC):
#     @abstractmethod
#     def click(this):
#         pass

# class Menu(ABC):
#     @abstractmethod
#     def open(this):
#         pass

# # Implementacion de las clases concretas (Windows):
# class WindowsUIButton(Button):
#     def click(this):
#         return "Me comporto como un boton de Windows"
    
# class WindowsUIMenu(Menu):
#     def open(this):
#         return "Me comporto como un menu de Windows"
    
# class LinuxUIButton(Button):
#     def click(this):
#         return "Me comporto como un boton de Linux"
    
# class LinuxUIMenu(Menu):
#     def open(this):
#         return "Me comporto como un menu de Linux"
    
# # Crear una sola Abstract Factory:
# # Es la que define como se crean las subclases
# class GUIAbstractFactory(ABC):
#     @abstractmethod
#     def createButton(this) -> Button:
#         pass

#     @abstractmethod
#     def createMenu(this) -> Button:
#         pass

# # Se crea una Concrete Factory para cada caso de uso:
# class WindowsFactory(GUIAbstractFactory):
#     def createButton(this) -> Button:
#         return WindowsUIButton()
    
#     def createMenu(this) -> Menu:
#         return WindowsUIMenu()
    
# class LinuxFactory(GUIAbstractFactory):
#     def createButton() -> Button:
#         return LinuxUIButton()
    
#     def createMenu() -> Menu:
#         return LinuxUIMenu()
    
# # Clase cliente consume el Abstract Factory
# def GUI_FactoryClient(os_type: str) -> GUIAbstractFactory:
#     if os_type == "Windows":
#         return WindowsFactory
#     elif os_type == "Linux":
#         return LinuxFactory
#     else:
#         raise ValueError("Sistema operativo no valido")
    
# # Uso del patron Abstract Factory:
# factory = GUI_FactoryClient("Windows") # Cambia a "Windows" por otra interfaz
# button = factory.createButton()
# menu = factory.createMenu()

# Ejercicio: Abstract Factory para crear enemigos en un videojuego: easy, middle, nightmare


# Structural: Como se relacionan, de forma estructural
# 3. Adapter: Es un patron que permite adaptar la comunicacion entre objetos que tienen interfaces distintas
# Ejemplo

# Clase incompatible que necesitamos adaptar:
class CelsiusTemperatureSensor:

    def __init__(this, temp):
        this.temp = temp

    def getTempCelsius(this):
        return this.temp

class FahrenheitTemperatureSensor:
    def getTempFahr(this):
        pass

# Clase adaptador entre las dos clases
# Se recibe como parametro la clase a la cual se va a adaptar la informacion de la clase incompatible
class TemperatureAdapter(FahrenheitTemperatureSensor):

    # Se inicializa con la clase incompatible
    def __init__(this, sensor):
        this.sensor = sensor

    # Funcion que adapta desde la clase no compatible para que el cliente la pueda consumir
    def getTempFahr(this):
        # Codigo que adapta desde la clase no compatible
        celsius = this.sensor.getTempCelsius()
        return celsius * (9/5) + 32
    
# Ejemplo de uso de la clase adaptadora
sensor = CelsiusTemperatureSensor(23)
adaptador = TemperatureAdapter(sensor)
print(f"La temperatura convertida es {adaptador.getTempFahr()}°F")


# 4. Decorator


# Behavioral Patterns: Como se comportan entre ellos y en el sistema, identifica patrones de comunicacion entre objetos
# 5. Strategy

# 6. Command
