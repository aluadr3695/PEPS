def times_table(n):
    ancho = len (str( n * n ))
    for y in range (1, n+1):            
        for x in range (1, n+1):
            print (x * y, end=' ' * ancho - (len(str(x * y))))
        print(' ')