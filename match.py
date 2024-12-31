#Seria como la version de swtich case pero para python

serie = 'N-10'

match serie:
    case 'N-01':
        print("Samsung")
    case 'N-02':
        print("Motorola")
    case 'N-03':
        print("Nokia")
    case _:
        print("No existe el producto")

cliente = {'nombre': 'Priscila',
           'edad': 23,
           'ocupacion': 'Estudiante'}

pelicula = {'titulo': 'Matrix',
            'ficha_tecnica':{'protagonista': 'Keanu Reeves',
                             'director':'Matha Higareda'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad':edad,
              'ocupacion': ocupacion}:
            print("ES un cliente")
            print(nombre, edad, ocupacion)

        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista':protagonista,
                                'director': director}}:
            print("ES una pelicula")
            print(titulo, protagonista, director)

        case _:
            print("NO se que es esto")

