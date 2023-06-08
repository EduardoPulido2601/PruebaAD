import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go


xlresult1 = '/home/okabe/Proyectos/prueba/query1.xlsx'
xlresult2 = '/home/okabe/Proyectos/prueba/query2.xlsx'
xlresult3 = '/home/okabe/Proyectos/prueba/query3.xlsx'
xlresult4 = '/home/okabe/Proyectos/prueba/query4.xlsx'
xlresult5 = '/home/okabe/Proyectos/prueba/query5.xlsx'

xlfile = '/home/okabe/Proyectos/prueba/filtered_data.xlsx'
data = pd.read_excel(xlfile)  
conn = sqlite3.connect('datos.db') 
tabla = 'filtered_data'
data.to_sql(tabla, conn, if_exists='replace', index=False)

#Datos para la primera gráfica
with open('query1.sql', 'r') as file:
    query1 = file.read()

result1 = pd.read_sql_query(query1, conn)

#Gráfica
fig1 = px.bar(result1, x='Año', y='Total Inscritos')

# Configurar título centrado y ajustado
fig1.update_layout(
    title={
        'text': 'Inscritos en la Universidad Nacional de Colombia, Bogotá (2014-2021)',
        'xanchor': 'center',
        'yanchor': 'top',
        'x': 0.5,
        'y': 0.95
    }
)

# Guardar la gráfica como un archivo PNG
fig1.write_image('/home/okabe/Proyectos/prueba/query1.png')

#Guarda los resultados en un excel
result1.to_excel(xlresult1, index=False) 


#Datos para la segunda gráfica
with open('query2.sql', 'r') as file:
    query2 = file.read()

result2 = pd.read_sql_query(query2, conn)

# Gráfica
fig2 = px.bar(result2, x='Año', y=['Hombres', 'Mujeres'], color_discrete_sequence=['blue', 'orange'])

# Configurar título centrado y ajustado
fig2.update_layout(
    title={
        'text': 'Inscritos por sexo en la Universidad Nacional de Colombia, Bogotá (2014-2021)',
        'xanchor': 'center',
        'yanchor': 'top',
        'x': 0.5,
        'y': 0.95
    },
    xaxis_title='Año',
    yaxis_title='Inscritos',
    barmode='group'  
)

# Guardar la gráfica como un archivo PNG
fig2.write_image('/home/okabe/Proyectos/prueba/query2.png')

#Guarda los resultados en un excel
result2.to_excel(xlresult2, index=False) 

#Datos para la tercera gráfica
with open('query3.sql', 'r') as file:
    query3 = file.read()

result3 = pd.read_sql_query(query3, conn)

# Obtener los totales de hombres y mujeres
total_hombres = int(result3['Total Hombres'].iloc[0])
total_mujeres = int(result3['Total Mujeres'].iloc[0])

# Gráfica
fig3 = go.Figure(data=[go.Pie(labels=['Total Hombres', 'Total Mujeres'], values=[total_hombres, total_mujeres])])

# Título de la gráfica
fig3.update_layout(
    title='Distribución de inscritos: Hombres vs Mujeres',
    title_x=0.5  # Centrar el título
)

# Guardar la gráfica como un archivo PNG
fig3.write_image('/home/okabe/Proyectos/prueba/query3.png')

#Guarda los resultados en un excel
result3.to_excel(xlresult3, index=False) 


#Datos para la cuarta gráfica
with open('query4.sql', 'r') as file:
    query4 = file.read()

result4 = pd.read_sql_query(query4, conn)

# Gráfica
fig4 = px.bar(result4, x='Año', y=['Hombres', 'Mujeres'], color_discrete_sequence=['blue', 'orange'])

# Configurar título centrado y ajustado
fig4.update_layout(
    title={
        'text': 'Inscritos a física en la UNAL entre el 2014 y el 2021',
        'xanchor': 'center',
        'yanchor': 'top',
        'x': 0.5,
        'y': 0.95
    },
    xaxis_title='Año',
    yaxis_title='Inscritos',
    barmode='group'  
)

# Guardar la gráfica como un archivo PNG
fig4.write_image('/home/okabe/Proyectos/prueba/query4.png')

#Guarda los resultados en un excel
result4.to_excel(xlresult4, index=False) 


#Datos para la quinta gráfica
with open('query5.sql', 'r') as file:
    query5 = file.read()

result5 = pd.read_sql_query(query5, conn)

# Obtener los totales de hombres y mujeres
total_hombres = int(result5['Total Hombres'].iloc[0])
total_mujeres = int(result5['Total Mujeres'].iloc[0])

# Gráfica
fig5 = go.Figure(data=[go.Pie(labels=['Total Hombres', 'Total Mujeres'], values=[total_hombres, total_mujeres])])

# Título de la gráfica
fig5.update_layout(
    title='Distribución de inscritos en la carrera de física: Hombres vs Mujeres',
    title_x=0.5  # Centrar el título
)

# Guardar la gráfica como un archivo PNG
fig5.write_image('/home/okabe/Proyectos/prueba/query5.png')

#Guarda los resultados en un excel
result5.to_excel(xlresult5, index=False) 






conn.close()






