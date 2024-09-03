import re
from decimal import Decimal
def mostrar_paquetes_disponibles():
    # Mostramos como diccionario ciudades y los paquetes disponibles con el valor
    ciudades_hoteles = {
        "Cartagena": [
            {"hotel": "Hotel Caribe", "costo_noche": Decimal("119.999"), "hora_vuelo": "10:00 AM", "costo_vuelo_ida_regreso": Decimal("199.999"), "duracion": "3 días y 2 noches"},
            {"hotel": "Hotel Santa Teresa", "costo_noche": Decimal("119.999"), "hora_vuelo": "2:00 PM", "costo_vuelo_ida_regreso": Decimal("219.999"), "duracion": "4 días y 3 noches"}
        ],
        "Bogotá": [
            {"hotel": "Hotel Hilton", "costo_noche": Decimal("179.999"), "hora_vuelo": "8:00 AM", "costo_vuelo_ida_regreso": Decimal("180.349"), "duracion": "3 días y 2 noches"},
            {"hotel": "Hotel Bogotá Plaza", "costo_noche": Decimal("119.999"), "hora_vuelo": "12:00 PM", "costo_vuelo_ida_regreso": Decimal("200.588"), "duracion": "4 días y 3 noches"}
        ],
        "Medellín": [
            {"hotel": "Hotel Intercontinental", "costo_noche": Decimal("130.299"), "hora_vuelo": "11:00 AM", "costo_vuelo_ida_regreso": Decimal("290.999"), "duracion": "3 días y 2 noches"},
            {"hotel": "Hotel Dann Carlton", "costo_noche": Decimal("150.799"), "hora_vuelo": "3:00 PM", "costo_vuelo_ida_regreso": Decimal("279.999"), "duracion": "4 días y 3 noches"}
        ]
    }

    # Definimos las ciudades de destino disponibles
    ciudades_destino = list(ciudades_hoteles.keys())

    while True:
        print("\n--- SELECCIÓN DE PAQUETES TURÍSTICOS ---")
        
        # Selección de ciudad de origen
        ciudad_origen = input("Ingrese la ciudad de origen en Colombia: ").strip()
        print(f"Ciudad de Origen: {ciudad_origen}")

        # Selección de ciudad de destino con opciones numeradas
        print("\nSeleccione una ciudad de Destino:")
        for i, ciudad in enumerate(ciudades_destino, 1):
            print(f"{i}. {ciudad}")

        seleccion_destino = input("Ingrese el número de la ciudad de Destino: ")
        if seleccion_destino.isdigit():
            seleccion_destino = int(seleccion_destino)
            if 1 <= seleccion_destino <= len(ciudades_destino):
                destino_seleccionado = ciudades_destino[seleccion_destino - 1]
            else:
                print("Selección inválida. Intenta de nuevo.")
                continue  # Vuelve a comenzar el bucle si la selección de ciudad de destino es inválida
        else:
            print("Entrada inválida. Intenta de nuevo.")
            continue  # Vuelve a comenzar el bucle si la entrada no es un número

        # Mostrar paquetes disponibles en la ciudad de destino
        paquetes_destino = ciudades_hoteles[destino_seleccionado]
        print(f"\nPaquetes disponibles en {destino_seleccionado}:")
        for i, paquete in enumerate(paquetes_destino, 1):
            print(f"{i}. Hotel: {paquete['hotel']}, Duración: {paquete['duracion']}, Costo por noche: ${paquete['costo_noche']}, Hora de Vuelo: {paquete['hora_vuelo']}, Costo Vuelo Ida y Regreso: ${paquete['costo_vuelo_ida_regreso']}")

        # Selección de paquete
        seleccion_paquete = input("Ingrese el número del paquete que desea seleccionar: ")
        if seleccion_paquete.isdigit():
            seleccion_paquete = int(seleccion_paquete)
            if 1 <= seleccion_paquete <= len(paquetes_destino):
                paquete_seleccionado = paquetes_destino[seleccion_paquete - 1]
            else:
                print("Selección inválida. Intenta de nuevo.")
                continue  # Vuelve a comenzar el bucle si la selección de paquete es inválida
        else:
            print("Entrada inválida. Intenta de nuevo.")
            continue  # Vuelve a comenzar el bucle si la entrada no es un número

        # Extraer duración de días y noches usando expresión regular
        duracion = paquete_seleccionado['duracion']
        match = re.search(r'(\d+) días y (\d+) noches', duracion)
        if match:
            duracion_dias = int(match.group(1))
            duracion_noches = int(match.group(2))
        else:
            print("Formato de duración del paquete no válido.")
            continue  # Vuelve a comenzar el bucle si el formato de duración es inválido

        # Calcular costo total
        costo_hotel_total = paquete_seleccionado['costo_noche'] * duracion_noches
        costo_vuelo_total = paquete_seleccionado['costo_vuelo_ida_regreso']
        costo_total = costo_hotel_total + costo_vuelo_total

        # Mostrar resumen del paquete seleccionado
        print("\n--- RESUMEN DEL PAQUETE ---")
        print(f"Ciudad de Origen: {ciudad_origen}")
        print(f"Ciudad de Destino: {destino_seleccionado}")
        print(f"Hotel: {paquete_seleccionado['hotel']}")
        print(f"Duración: {paquete_seleccionado['duracion']}")
        print(f"Costo por Noche: ${paquete_seleccionado['costo_noche']}")
        print(f"Costo Total del Hotel: ${costo_hotel_total}")
        print(f"Costo Total del Vuelo (Ida y Regreso): ${costo_vuelo_total}")
        print(f"Costo Total del Paquete: ${costo_total}")
        print(f"Hora de Vuelo: {paquete_seleccionado['hora_vuelo']}")

        # Opción para regresar al menú principal o salir
        respuesta = input("\n¿Deseas volver atras? (s/n): ").strip().lower()
        if respuesta == 'n':
            print("Paquete seleccionado con EXITO, Gracias por tu consulta. ")
            break  # Sale del bucle y termina la función

        # Si la respuesta es 's', el bucle se repite, permitiendo seleccionar otro paquete
