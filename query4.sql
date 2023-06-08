--Inscritos por sexo a física en la Universidad Nacional de Colombia, bogotá desde el año 2014 al 2021

SELECT Año,
       SUM(CASE WHEN Sexo = 'MASCULINO' THEN Inscritos ELSE 0 END) AS 'Hombres',
       SUM(CASE WHEN Sexo = 'FEMENINO' THEN Inscritos ELSE 0 END) AS 'Mujeres'
FROM filtered_data
WHERE [Institución de Educación Superior (IES)] = 'UNIVERSIDAD NACIONAL DE COLOMBIA'
  AND [Municipio de oferta del programa] = 'BOGOTA D.C.'
  AND [Programa Académico] = 'FISICA'
  AND Año BETWEEN 2014 AND 2021
GROUP BY Año;


