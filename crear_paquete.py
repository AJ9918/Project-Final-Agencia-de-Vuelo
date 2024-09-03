from decimal import Decimal

def mostrar_opciones_ciudad():
    ciudades_hoteles = {
        "Cartagena": ["Hotel Caribe", "Hotel Santa Teresa", "Hotel San Pedro"],
        "Bogotá": ["Hotel Hilton", "Hotel Bogotá Plaza", "Hotel Casa Deco"],
        "Medellín": ["Hotel Intercontinental", "Hotel Dann Carlton", "Hotel Poblado"]
    }

    print("\n--- CREACIÓN DE PAQUETE TURÍSTICO ---")

    ciudad_origen = input("Ingrese la ciudad de origen: ")

    print("\nSeleccione una ciudad de destino:")
    for i, ciudad in enumerate(ciudades_hoteles.keys(), 1):
        print(f"{i}. {ciudad}")

    seleccion_destino = input("Ingrese el número de la ciudad de destino que desea escoger: ")
    if seleccion_destino.isdigit():
        seleccion_destino = int(seleccion_destino)
        if 1 <= seleccion_destino <= len(ciudades_hoteles):
            ciudad_destino = list(ciudades_hoteles.keys())[seleccion_destino - 1]
            hoteles = ciudades_hoteles[ciudad_destino]
        else:
            print("Selección inválida. Intenta de nuevo.")
            return mostrar_opciones_ciudad()
    else:
        print("Entrada inválida. Intenta de nuevo.")
        return mostrar_opciones_ciudad()

    print(f"\nHoteles disponibles en {ciudad_destino}:")
    for i, hotel in enumerate(hoteles, 1):
        print(f"{i}. {hotel}")

    seleccion_hotel = input("Ingrese el número del hotel que desea escoger: ")
    if seleccion_hotel.isdigit():
        seleccion_hotel = int(seleccion_hotel)
        if 1 <= seleccion_hotel <= len(hoteles):
            hotel_elegido = hoteles[seleccion_hotel - 1]
        else:
            print("Selección de hotel inválida. Se seleccionará el primer hotel disponible.")
            hotel_elegido = hoteles[0]
    else:
        print("Entrada inválida. Se seleccionará el primer hotel disponible.")
        hotel_elegido = hoteles[0]

    return ciudad_origen, ciudad_destino, hotel_elegido

def crear_paquete_turistico():
    ciudad_origen, ciudad_destino, hotel_elegido = mostrar_opciones_ciudad()

    duraciones = [
        {"duracion": "3 días y 2 noches", "costo": 500.633},
        {"duracion": "4 días y 3 noches", "costo": 700.399}
    ]

    print("\nSeleccione la duración del paquete:")
    for i, duracion in enumerate(duraciones, 1):
        print(f"{i}. {duracion['duracion']} - Costo: ${duracion['costo']}")

    seleccion_duracion = input("Ingrese el número de la duración que desea escoger: ")
    if seleccion_duracion.isdigit():
        seleccion_duracion = int(seleccion_duracion)
        if 1 <= seleccion_duracion <= len(duraciones):
            duracion_seleccionada = duraciones[seleccion_duracion - 1]
        else:
            print("Selección inválida. Se seleccionará la primera opción.")
            duracion_seleccionada = duraciones[0]
    else:
        print("Entrada inválida. Se seleccionará la primera opción.")
        duracion_seleccionada = duraciones[0]

    costo_vuelo_ida_regreso = Decimal("289.999")
    costo_vuelo_solo_ida = Decimal("149.999")

    ida_regreso = input("¿El vuelo es ida y regreso? (s/n): ").strip().lower()
    if ida_regreso == 's':
        costo_vuelo = costo_vuelo_ida_regreso
    elif ida_regreso == 'n':
        costo_vuelo = costo_vuelo_solo_ida
    else:
        print("Entrada inválida. Se asignará un costo de vuelo ida y regreso.")
        costo_vuelo = costo_vuelo_ida_regreso

    costo_paquete = Decimal(duracion_seleccionada["costo"])

    # Convertir a float y formatear a 3 decimales
    costo_paquete = float(costo_paquete)
    costo_vuelo = float(costo_vuelo)
    costo_total = costo_paquete + costo_vuelo

    paquete_turistico = {
        "ciudad_origen": ciudad_origen,
        "ciudad_destino": ciudad_destino,
        "hotel": hotel_elegido,
        "duracion": duracion_seleccionada["duracion"],
        "costo_paquete": costo_paquete,
        "costo_vuelo": costo_vuelo,
        "costo_total": costo_total
    }

    print("\n--- RESUMEN DEL PAQUETE CREADO ---")
    print(f"Ciudad de Origen: {paquete_turistico['ciudad_origen']}")
    print(f"Ciudad de Destino: {paquete_turistico['ciudad_destino']}")
    print(f"Hotel Seleccionado: {paquete_turistico['hotel']}")
    print(f"Duración del Paquete: {paquete_turistico['duracion']}")
    print(f"Costo del Paquete: ${paquete_turistico['costo_paquete']:.3f}")
    print(f"Costo del Vuelo: ${paquete_turistico['costo_vuelo']:.3f}")
    print(f"Costo Total del Paquete (incluido vuelo): ${paquete_turistico['costo_total']:.3f}")

    input("\nPresione Enter para volver al menú principal...")


