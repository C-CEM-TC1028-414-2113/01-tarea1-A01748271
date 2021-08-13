def main():
    #escribe tu código abajo de esta línea
    
    nacimiento = int(input("Dame el año de nacimiento: "))
    actual = int(input("Dame el año actual: "))

    edad = (actual-nacimiento)
    lustros =float(edad)/5

    print("Los lustros que has vivido son: "+str(lustros))


if __name__ == '__main__':
    main()
