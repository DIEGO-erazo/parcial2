from modelos import Motocicleta, Automovil

def ejecutar_demostracion():
    # Creación de al menos cuatro servicios de diferentes tipos
    servicios = [
        Motocicleta(conductor="Carlos Pérez", identificador="M-12345", distancia=12.5, tarifa_base=2.00),
        Automovil(conductor="María López", identificador="P-98765", distancia=12.5, tarifa_base=3.50),
        Motocicleta(conductor="Jorge Ramírez", identificador="M-67890", distancia=5.0, tarifa_base=1.50),
        Automovil(conductor="Ana Rodríguez", identificador="P-54321", distancia=22.0, tarifa_base=4.00)
    ]

    print("=== RESUMEN DE SERVICIOS DE TRANSPORTE (DEMOSTRACIÓN DE POLIMORFISMO) ===\n")
    
    # Procesamiento desde una misma colección utilizando polimorfismo
    for servicio in servicios:
        print(servicio.mostrar_resumen())

if __name__ == "__main__":
    ejecutar_demostracion()