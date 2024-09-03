import paquete
import crear_paquete

def imprimir_titulo():
    # IMPRIMIMOS título de la agencia de viajes
    titulo = "AGENCIA DE VIAJE PIO TOURS"
    print(titulo)
    print("=" * len(titulo))

def mostrar_mensaje_bienvenida():
    # Mostramos el mensaje de bienvenida
    print("BIENVENIDO VIAJERO PIO, ¿DESEAS VER NUESTRO MENÚ? (S/N)")
    respuesta = input("").strip().lower()
    return respuesta

def registro_usuarios():
    # Solicitamos la cantidad de personas y se registra la información gestion de BD 
    cantidad_personas = input("¿Cuántas personas van a viajar? ")

    if cantidad_personas.isdigit() and int(cantidad_personas) > 0:
        cantidad_personas = int(cantidad_personas)
    else:
        print("Número inválido. Intenta de nuevo.")
        return registro_usuarios()  # Si el dato es invalido regresar a la linea 18

    usuarios = []
    for i in range(cantidad_personas):
        print(f"\nRegistrando a la persona {i+1}:")
        nombre = input("Nombre: ")
        cc = input("Cédula: ")
        if cc.isdigit():
            usuarios.append({"Nombre": nombre, "CC": cc})
            print(f"Registro EXITOSO, Sr. '{nombre}', identificado con la cédula '{cc}'")
        else:
            print("Cédula inválida. Registro cancelado")
    
    input("Presione Enter para continuar...")
    return usuarios


def imprimir_menu():
    # Imprime las opciones del menú
    print("NUESTRO MENÚ")
    print("1. Paquetes turísticos Disponibles")
    print("2. Crear paquetes turísticos")

def manejar_opcion_menu():
    # Solicita la opción deseada y maneja la entrada del usuario
    print("¿Qué opción deseas Escoger?")
    opcion = input("").strip()
    
    if opcion == "1":
        # Llama a la función desde el módulo paquete
        paquete.mostrar_paquetes_disponibles()
    elif opcion == "2":
        crear_paquete.crear_paquete_turistico()
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

def main():
    # Función principal que controla el flujo del programa
    imprimir_titulo()
    respuesta = mostrar_mensaje_bienvenida()
    
    if respuesta == "s":
        registro_usuarios()
        imprimir_menu()
        manejar_opcion_menu()
    else:
        print("Finalización de consulta")

if __name__ == "__main__":
    main()
