def cliente (informacion : dict): 
    
    # Atraccion X-Treme, mayor de 18 años, primer ingreso
    if informacion['edad'] > 18:
        apto = True
        atraccion = 'X-Treme'
        if  informacion["primer_ingreso"] == True:
            operacion =  20000 - (20000 * 0.05)  
            impresion = {'nombre':informacion['nombre'], 'edad':informacion['edad'], 'atraccion':atraccion, 'apto':apto, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':operacion} 
            return impresion
        else:
            operacion= 20000
            impresion = {'nombre':informacion['nombre'], 'edad':informacion['edad'], 'atraccion':atraccion, 'apto':apto, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':operacion} 
            return impresion

    # Carros chocones, entre 15 y 18 años, primer ingreso
    if informacion['primer_ingreso'] == True:
        if informacion['edad'] >= 15 and informacion['edad'] <= 18:
            operacion = 5000 - (5000 * 0.07)
            apto = True
            impresion = {'nombre':informacion['nombre'], 'edad':informacion['edad'], 'atraccion':atraccion, 'apto':apto, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':operacion}    
            return impresion
        else:
            operacion = 5000
            impresion = {'nombre':informacion['nombre'], 'edad':informacion['edad'], 'atraccion':atraccion, 'apto':apto, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':operacion}    
            return impresion
        
    # Sillas voladoras, entre 7 y 15 años, primer ingreso
    if informacion['primer_ingreso'] == True:
        if informacion['edad'] >= 7 and informacion['edad'] <= 15:
            operacion = 10000 - (10000 * 0.05)
            apto = True
            atraccion = "Sillas Voladoras"
            impresion = {'nombre':informacion['nombre'], 'edad':informacion['edad'], 'atraccion':atraccion, 'apto':True, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':operacion}
            return impresion
        else:
            operacion = 10000
            impresion = {'nombre':informacion['nombre'], 'edad':informacion['edad'], 'atraccion':atraccion, 'apto':True, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':operacion}
            return impresion 
                
    if informacion['edad'] <7: 
        apto = False
        atraccion = 'N/A'
        total_boleta = 'N/A'
        impresion = {'nombre':informacion['nombre'], 'edad':informacion['edad'], 'atraccion':atraccion, 'total_boleta':total_boleta['total_boleta']}
        
inf = {}
inf['id_cliente']=int(1),
inf['nombre']= 'Johana Fernandez', 
inf['edad']= int (20), 
inf['primer_ingreso']=bool (1)

print(cliente(inf))