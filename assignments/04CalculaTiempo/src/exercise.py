def main():
    #escribe tu código abajo de esta línea
    
    edad = int(input("Dame tu edad: "))


    año = int(input("Dame el año actual: "))

    nacimiento = año-edad
    años_100 = nacimiento +100

    print("Cumplirás 100 años en el año: "+str(años_100))


if __name__ == '__main__':
    main()
