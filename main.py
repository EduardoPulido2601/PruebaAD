import pandas as pd
import sqlite3

for i in range(8):

    xlfile = '/home/okabe/Proyectos/prueba/datos/'+ str(2014 + i) + '.xlsx'
    xlresult = '/home/okabe/Proyectos/prueba/filtered_data.xlsx'

    data = pd.read_excel(xlfile)  
    conn = sqlite3.connect('datos.db')
    tabla = 'tabla_' + str(2014 + i)
    data.to_sql(tabla, conn, if_exists='replace', index=False)

    query = """SELECT DISTINCT
                    UPPER(`Institución de Educación Superior (IES)`) AS `Institución de Educación Superior (IES)`,
                    UPPER(`Programa Académico`) AS `Programa Académico`,
                    UPPER(`Nivel Académico`) AS `Nivel Académico`,
                    UPPER(`Nivel de Formación`) AS `Nivel de Formación`,
                    UPPER(`Área de Conocimiento`) AS `Área de Conocimiento`,
                    UPPER(`Núcleo Básico del Conocimiento (NBC)`) AS `Núcleo Básico del Conocimiento (NBC)`,
                    UPPER(`Municipio de oferta del programa`) AS `Municipio de oferta del programa`,
                    UPPER(Género) AS Género,
                    Año,
                    Semestre,
                    Inscritos
                FROM tabla_2014
                WHERE
                    `Institución de Educación Superior (IES)` IS NOT NULL
                    AND `Programa Académico` IS NOT NULL
                    AND `Nivel Académico` IS NOT NULL
                    AND `Nivel de Formación` IS NOT NULL
                    AND `Área de Conocimiento` IS NOT NULL
                    AND `Núcleo Básico del Conocimiento (NBC)` IS NOT NULL
                    AND `Municipio de oferta del programa` IS NOT NULL
                    AND Género IS NOT NULL
                    AND Año IS NOT NULL
                    AND Semestre IS NOT NULL
                    AND Inscritos IS NOT NULL;
            """

    result = pd.read_sql_query(query, conn)


    result.to_excel(xlresult, index=False)


