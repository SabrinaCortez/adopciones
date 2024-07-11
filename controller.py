from db import conexionMySQL

# para probar
def probar_Conexion():
    return conexionMySQL()

# combos parametricas
def obtener_TipoAnimales():
    # conexion
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = "SELECT cidTipoAnimal, cDescripcion FROM tipoanimal ORDER BY cDescripcion"
        cursor.execute(query)
    # procesar los resultados -> fetch
        result = cursor.fetchall()
    # cerrar la conexion
        conexion.commit()
        conexion.close()
        return result

def obtener_TipoEstado():
    # conexion
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = "SELECT cidTipoEstado, cDescripcion FROM tipoestado ORDER BY cDescripcion"
        cursor.execute(query)
    # procesar los resultados -> fetch
        result = cursor.fetchall()
    # cerrar la conexion
        conexion.commit()
        conexion.close()
        return result

# resto sql 
def obtener_AnimalesEnTransito(cidTipoAnimal):
    # conexion
    conexion = conexionMySQL()
    # consulta db
    # print ("Hago una consulta  ")
    with conexion.cursor() as cursor:
        # ojo que en la autoinsercion el valor de transitorio debe ser 2
        query = """ SELECT A.cNombre, TA.cDescripcion, A.cRaza, A.cEdad, 
                           A.cCondicionEspecial ,  CASE WHEN A.cSexo ='M' THEN 'macho' ELSE 'Hembra' END as Sexo, 
                           cImagen
                      FROM animales A 
                      INNER JOIN tipoanimal TA
                            ON TA.cidTipoAnimal = A.cidTipoAnimal
                      INNER JOIN estados ES 
                            ON ES.idAnimales = A.idAnimales
                    WHERE ES.cidTipoEstado = 'TR'
                    AND   (ES.cDNI is null or ES.cDNI='')
                    AND A.cidTIpoAnimal = %s
                """
        cursor.execute(query,(cidTipoAnimal))
    # procesar los resultados -> fetch
        result = cursor.fetchall()
        # si queres verlo en el debug
        # for row in result:
        #    print(row)
    # cerrar la conexion
        conexion.commit()
        conexion.close()
        return result

def obtener_AnimalesPublicados(cidTipoAnimal):
    # conexion
    conexion = conexionMySQL()
    # consulta db
    with conexion.cursor() as cursor:
        query = """ SELECT A.cNombre, TA.cDescripcion, A.cRaza, A.cEdad, 
                           A.cCondicionEspecial ,  CASE WHEN A.cSexo ='M' THEN 'macho' ELSE 'Hembra' END as Sexo, 
                           cImagen
                      FROM animales A 
                        INNER JOIN tipoanimal TA
                            ON TA.cidTipoAnimal = A.cidTipoAnimal
                        INNER JOIN estados ES 
                            ON ES.idAnimales = A.idAnimales
                    WHERE ES.cidTipoEstado = 'PU'
                    AND   (ES.cDNI is null or ES.cDNI='')
                 AND A.cidTIpoAnimal = %s
                """
        cursor.execute(query,(cidTipoAnimal))
    # procesar los resultados -> fetch
        result = cursor.fetchall()
    # cerrar la conexion
        conexion.commit()
        conexion.close()
        return result
       
def obtener_AnimalesPublicadosNombres():
    # conexion
    conexion = conexionMySQL()
    # consulta db
    with conexion.cursor() as cursor:
        query = """ SELECT A.idAnimales, A.cNombre
                      FROM animales A 
                        INNER JOIN tipoanimal TA
                            ON TA.cidTipoAnimal = A.cidTipoAnimal
                        INNER JOIN estados ES 
                            ON ES.idAnimales = A.idAnimales
                    WHERE ES.cidTipoEstado = 'PU'
                    AND   (ES.cDNI is null or ES.cDNI='')
                """
        cursor.execute(query)
    # procesar los resultados -> fetch
        result = cursor.fetchall()
    # cerrar la conexion
        conexion.commit()
        conexion.close()
        return result
    
def adoptante_nuevo(cDNI,cNombreyApellido,cCorreo,cLinkInstagram,cTelefono,dFechaNacimiento,cCasaDepartamento):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = "INSERT INTO adoptante (cDNI,cNombreyApellido,cCorreo,cLinkInstagram,cTelefono,dFechaNacimiento,cCasaDepartamento) VALUES (%s, %s, %s,%s, %s, %s,%s)"
        cursor.execute(query, (cDNI,cNombreyApellido,cCorreo,cLinkInstagram,cTelefono,dFechaNacimiento,cCasaDepartamento))
        result = cursor
        conexion.commit()
        conexion.close()
        return result
    

def estado_Actualizar (idAnimales , cDNI, tipoestado):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE estados SET cDNI = %s, cidTipoEstado = %s WHERE idAnimales = %s and dHasta is null ",(cDNI,tipoestado,idAnimales))
        result = cursor
    conexion.commit()
    conexion.close()
    return result