def CDT (usuario:str,capital:float,tiempo:int):
    intereses = (capital * 0.03 * tiempo) / 12
    perdida = (capital * 0.02)
    if tiempo > 2: 
        valor_total = (intereses + capital)
    else:
        valor_total = (capital - perdida)
    tiempo2 = str(tiempo)
    capital2 = str(capital)
    valor_total2 = str(valor_total)
    return ("Para el usuario " + usuario + " La cantidad de dinero a recibir, según el monto inicial " + capital2 + " para un tiempo de " + tiempo2 + " meses es: " + valor_total2)

print (CDT("AB1012",1000000,3))
print (CDT("ER3366",650000, 2))