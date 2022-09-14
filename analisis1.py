import pandas as pd
#LO IMPORTÉ Y LE DI UN ALIAS, UN NOMBRE PARA LLAMAR AL PANDA

#CARGAR LOS DATOS
#SE RECOMIENDA TENER LA BD EN EL PROYECTO
dataFrame=pd.read_csv('./empleados.csv')
#CADA UNA DE LAS FILAS ES UNA LISTA(REGISTRO)
#print(dataFrame)

#CARGAR TODOS LOS DATOS - LLAMO AL MÉTODO PROPIO DE PANDAS to_string()
#print(dataFrame.to_string())

#CARGAR LOS PRIMEROS N REGISTROS DE UN BANCO DE DATOS, SI NO PONGO NADA EN LOS PARÉNTESIS DEL head() me arroja los primeros 5
#print(dataFrame.head(20))

#CARGAR LOS ÚLTIMOS N REGISTROS DE UN BANCO DE DATOS, SI NO PONGO NADA EN LOS PARÉNTESIS DEL head() me arroja los primeros 5
#print(dataFrame.tail())

#OBTENER INFORMACIÓN DE LOS DATOS CARGADOS
#print(dataFrame.info())
#print(dataFrame.describe())

#ACCEDER A DATOS O REGISTROS ESPECÍFICOS (ES COMO ACCEDER A UN REGISTRO ESPECÍFICO, UNA POSICIÓN)
# print(dataFrame['nombres'].head())
# print(dataFrame['salario'].tail(20))

#ACCEDER A REGISTROS POR SU ÍNDICE
#print(dataFrame.iloc[20:30]) #Aquí me mostraría del 20 al 30
#print(dataFrame.loc[[10,20,30,40]]) #Para acceder a una serie de registros específicos
#print(dataFrame.loc[[1,5,10],['nombres']])#acceder a los nombres y los registros específicos

#Estoy creando una tabla para mostrar el filtro
'''
tabla=(dataFrame.loc[[1,5,10],['nombres']])
html=tabla.to_html()
text_file=open("index.html","w") #"w" es para darle permisos de lectura (write)
text_file.write(html)
text_file.close()
'''

#FILTROS CON CODICIONES LÓGICAS
#print(dataFrame[dataFrame["salario"]>5500000].head(10)) #dentro del primer [] busco la propiedad que deseo acceder y luego el filtro que deseo

print(dataFrame[(dataFrame["salario"]>5500000)&(dataFrame["cargo"]=="analista2")])
