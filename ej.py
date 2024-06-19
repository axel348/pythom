while True:
    try:
        num = int(input("ingrese un numero: "))
        if num <= 0:
            print("debe ingresar un numero positivo")
        else:
            fac = 1

            cont = 0


            while cont<num:
                cont*cont+1
                fac = fac*cont
            print(fac)
            break
    except ValueError:
        print("ingrese solo numero ")