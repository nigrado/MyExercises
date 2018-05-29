def Kurvendiskussion_einer_Parabel(a,b,c):
    D=b**2-4*a*c
    p=(b)/a
    q=(c)/a
    if D> 0:
        print("Die Diskriminante ist:",D)
        n=(-(p/2))+((((p/2)**2)-q)**0.5)
        N=(-(p/2))-((((p/2)**2)-q)**0.5)
        print("Die Nullstellen sind: ")
        print(n,N)
        x=-b/(2*a)
        print("Der Extrempunkt liegt bei x= ",x)
        Art_des_Punktes=2*a
        if Art_des_Punktes>=0:
            print("Es ist ein Tiefpunkt")
        else:
            print("Es ist ein Hochpunkt")
    elif D==0:
        print("Die Diskriminante ist:",D)
        N=(-(p/2))+((((p/2)**2)-q)**0.5)
        n=(-(p/2))-((((p/2)**2)-q)**0.5)
        print("Die Nullstellen sind: ")
        print(N,n)
        x=-b/(2*a)
        print("Der Extrempunkt liegt bei x= ",x)
        Art_des_Punktes=2*a
        if Art_des_Punktes>=0:
            print("Es ist ein Tiefpunkt")
        else:
            print("Es ist ein Hochpunkt")
    else:
        print("Es gibt keine reele Nullstellen")
        x=-b/(2*a)
        print("Der Extrempunkt liegt bei x= ",x)
        Art_des_Punktes=2*a
        if Art_des_Punktes>=0:
            print("Es ist ein Tiefpunkt")
        else:
            print("Es ist ein Hochpunkt")