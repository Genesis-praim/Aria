from conocimiento_almacenamiento import crear_sistema_conocimiento

def test_sistema_conocimiento():
    sistema = crear_sistema_conocimiento()

    # Agregar conocimiento específico
    sistema.agregar_conocimiento("Ciencias Naturales", "Biología", "Botánica", "Las plantas realizan fotosíntesis para producir energía.")
    sistema.agregar_conocimiento("Ingeniería", "Ingeniería de Software", "Desarrollo de Software", "El ciclo de vida del software incluye análisis, diseño, implementación y pruebas.")
    sistema.agregar_conocimiento("Medicina", "Medicina General", "Anatomía", "El corazón es un órgano vital que bombea sangre.")
    sistema.agregar_conocimiento("Derecho", "Derecho Civil", "Contratos", "Los contratos deben tener consentimiento libre y capacidad legal.")

    # Buscar términos
    resultados1 = sistema.buscar_conocimiento("fotosíntesis")
    resultados2 = sistema.buscar_conocimiento("software")
    resultados3 = sistema.buscar_conocimiento("corazón")
    resultados4 = sistema.buscar_conocimiento("contratos")

    print("Resultados búsqueda 'fotosíntesis':", resultados1)
    print("Resultados búsqueda 'software':", resultados2)
    print("Resultados búsqueda 'corazón':", resultados3)
    print("Resultados búsqueda 'contratos':", resultados4)

if __name__ == "__main__":
    test_sistema_conocimiento()
