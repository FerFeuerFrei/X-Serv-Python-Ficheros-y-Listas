
fich = open("/etc/passwd","r")
# LISTA DE LINEAS
lineas = fich.readlines()

#lineas[:1] # ['pepepepepepe'] LISTA
#lineas[0] # 'pepepepepepepe' STRING

## FORMA 1
#
## [:2] - PRIMERA Y SEGUNDA LINEA
## for linea in lineas[:2]:
#for linea in lineas:
#    print(linea)
#    pos_fin = linea.find(":")
#    # LOGIN
#    login = linea [:pos_fin]
#    # -1: es el /n
#    # SHELL    
#    # pos_com - COMIENZO
#    pos_com = linea.rfind(":")
#    # + 1 SIGUIENTE POSICIÓN A LOS :
#    shell = linea[pos_com + 1:-1]
#    print(login, shell)
#
#
## FORMA 2
#
#for linea in lineas:
#        elementos = linea.split()
##        print(elementos)
#        login = elementos[0]
#        shell = elementos[-1]
#        print(login, shell)
#        shell_bueno = shell[:-1]
#        print(login, shell_bueno)


# FORMA 3

for linea in lineas:
        login = linea.split(':')[0]
        shell = linea.split(':')[-1][:-1]
        print(login, shell)