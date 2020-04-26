import statistics
print("Calculadora de medias. Versión Alpha")
print("Creado por Óscar Gómez Valero")
print("Para ver las asignaturas pulse 1")
print("Para seleccionar una asignatura pulse 2")
print("Para saber cómo escribir la asignatura elegida pulse 3")
print("AVISO IMPORTANTE: Escribe EXACTAMENTE como se indica en el apartado 3 o lo entenderá como un error")
asignaturas = int(input())
if asignaturas == 1:
    print("Estas son las asignaturas disponibles")
    print("Lengua, Matemáticas,Geografía e Historia, Música")
    print("Educación Física, Física y Química, Inglés, Tecnología")
    print("Economía y Francés")
if asignaturas == 2:
    print("Escriba la asignatura que desee:")
    elec = input()
    if elec == "Lengua":
        veces = int(input("¿Cúantos exámenes has hecho?: "))
        examen = []
        for x in range(veces):
            nota = float(input("Pon una nota: "))
            examen.append(nota)
        media = statistics.median(examen)
        print("Tu media es:" + str(media))
        nota2 = float(input("¿Cuál crees que es tu nota en comportamiento? : "))
        evaluacion = ((media * 70) + (nota2 * 30))/100
        print("Tu nota esta evaluación es de: " + str(evaluacion))
    if elec == "Mates":
        veces = int(input("¿Cúantos exámenes has hecho?: "))
        examen = []
        for x in range(veces):
            nota = float(input("Pon una nota: "))
            examen.append(nota)
        media = statistics.median(examen)
        print("Tu media es:" + str(media))
        nota2 = float(input("¿Cuál crees que es tu nota en comportamiento? : "))
        evaluacion = ((media * 70) + (nota2 * 30))/100
        print("Tu nota esta evaluación es de: " + str(evaluacion))
    if elec == "GyH":
        veces = int(input("¿Cúantos exámenes has hecho?: "))
        examen = []
        for x in range(veces):
            nota = float(input("Pon una nota: "))
            examen.append(nota)
        media = statistics.median(examen)
        print("Tu media es:" + str(media))
        nota2 = float(input("¿Cuál crees que es tu nota en comportamiento? : "))
        evaluacion = ((media * 70) + (nota2 * 30))/100
        print("Tu nota esta evaluación es de: " + str(evaluacion))
    if elec == "Música":
        veces = int(input("¿Cúantos exámenes has hecho?: "))
        examen = []
        for x in range(veces):
            nota = float(input("Pon una nota: "))
            examen.append(nota)
        media = statistics.median(examen)
        print("Tu media es:" + str(media))
        nota2 = float(input("¿Cuál crees que es tu nota en comportamiento? : "))
        evaluacion = ((media * 70) + (nota2 * 30))/100
        print("Tu nota esta evaluación es de: " + str(evaluacion))
    if elec == "E.F":
        veces = int(input("¿Cúantos exámenes has hecho?: "))
        examen = []
        for x in range(veces):
            nota = float(input("Pon una nota: "))
            examen.append(nota)
        media = statistics.median(examen)
        print("Tu media es:" + str(media))
        nota2 = float(input("¿Cuál crees que es tu nota en comportamiento? : "))
        evaluacion = ((media * 70) + (nota2 * 30))/100
        print("Tu nota esta evaluación es de: " + str(evaluacion))
    if elec == "FyQ":
        veces = int(input("¿Cúantos exámenes has hecho?: "))
        examen = []
        for x in range(veces):
            nota = float(input("Pon una nota: "))
            examen.append(nota)
        media = statistics.median(examen)
        print("Tu media es:" + str(media))
        nota2 = float(input("¿Cuál crees que es tu nota en comportamiento? : "))
        evaluacion = ((media * 70) + (nota2 * 30))/100
        print("Tu nota esta evaluación es de: " + str(evaluacion))
    if elec == "Inglés":
        veces = int(input("¿Cúantos exámenes has hecho?: "))
        examen = []
        for x in range(veces):
            nota = float(input("Pon una nota: "))
            examen.append(nota)
        media = statistics.median(examen)
        print("Tu media es:" + str(media))
        nota2 = float(input("¿Cuál crees que es tu nota en comportamiento? : "))
        evaluacion = ((media * 70) + (nota2 * 30))/100
        print("Tu nota esta evaluación es de: " + str(evaluacion))
    if elec == "Tecno":
        veces = int(input("¿Cúantos exámenes has hecho?: "))
        examen = []
        for x in range(veces):
            nota = float(input("Pon una nota: "))
            examen.append(nota)
        media = statistics.median(examen)
        print("Tu media es:" + str(media))
        nota2 = float(input("¿Cuál crees que es tu nota en comportamiento? : "))
        evaluacion = ((media * 70) + (nota2 * 30))/100
        print("Tu nota esta evaluación es de: " + str(evaluacion))
    if elec == "Economía":
        veces = int(input("¿Cúantos exámenes has hecho?: "))
        examen = []
        for x in range(veces):
            nota = float(input("Pon una nota: "))
            examen.append(nota)
        media = statistics.median(examen)
        print("Tu media es:" + str(media))
        nota2 = float(input("¿Cuál crees que es tu nota en comportamiento? : "))
        evaluacion = ((media * 70) + (nota2 * 30))/100
        print("Tu nota esta evaluación es de: " + str(evaluacion))
    if elec == "Francés":
        veces = int(input("¿Cúantos exámenes has hecho?: "))
        examen = []
        for x in range(veces):
            nota = float(input("Pon una nota: "))
            examen.append(nota)
        media = statistics.median(examen)
        print("Tu media es:" + str(media))
        nota2 = float(input("¿Cuál crees que es tu nota en comportamiento? : "))
        evaluacion = ((media * 70) + (nota2 * 30))/100
        print("Tu nota esta evaluación es de: " + str(evaluacion))
if asignaturas == 3:
    print("AVISO IMPORTANTE: Escribe EXACTAMENTE como se indica o lo entenderá como un error")
    print("Lengua : Lengua")
    print("Matemáticas : Mates")
    print("Geografía e historia : GyH")
    print("Música : Música")
    print("Educación física : E.F")
    print("Física y química : FyQ")
    print("Inglés : Inglés")
    print("Tecnología : Tecno")
    print("Economía : Economía")
    print("Francés : Francés")
