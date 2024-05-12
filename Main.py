from Modulos.Menus import Menu_Inicial, MenuAdmin, MenuUser
from Modulos.DatosYValidaciones import*
from datetime import datetime
JSON_UBICACION = "Datos/UsuariosServiciosProductos.json"

Datos = Cargar_datos(JSON_UBICACION)

print("""
                .-+*#########*+-.                
            .+#####*=::....:-+#####*.            
          *#####-...............:+####*          
       .#####*-:-------------------=#####.       
      *#####=========================+#####.     
    -######+++++++++++++++++++++++++++*#####=    
   +######*****************************######+   
  =###########################################+  
 :################################+  #####*.###- 
 #################################*  ###+  .#### 
=#####=:..-*##*.-##################=-##. .######=
####-  -+=.  *+ .##=...-##+=+--##-..:*#+*########
###+  ######*#+ .#  =#-  #.  -+-  ==  .#*.  .:###
###+  ########+ .#*      #. +##  ####  +#+===+###
####-  =*+:  *+ .*  *#-  #. +##: .+*: .##########
=#####-.  :+##* -#=. .: .#:.*###*:  .=##########=
 ############################################### 
 -####################******###################- 
  +################************###############+  
   +#############***+++++++++****############+   
    =###########***+++=====++++***##########=    
     .##########**+++========++***#########.     
       .########**+++========++***#######:       
          *######***+++====+++**#######.         
            .*######**********#####*:            
                .-+**#######**+-.                """)
print("")
print("*"*50)
print("")
print("BIENVENIDO".center(50))
print("")

while True:
  Rol = Menu_Inicial(Datos)
  if Rol == "Admin":
    MenuAdmin(Datos)
    break
  elif Rol == "User":
    MenuUser(Datos)
    break
  elif Rol == 0:
    print("Vuelve a Intentarlo")
  else:
    print("Vuelve a Intentarlo")
    
Guardar_datos(Datos, JSON_UBICACION)