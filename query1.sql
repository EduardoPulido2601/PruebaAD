--Número de inscritos en la Universidad Nacional de Colombia, bogotá desde el año 2014 al 2021

SELECT Año, SUM(Inscritos) AS 'Total Inscritos'
FROM filtered_data
WHERE [Institución de Educación Superior (IES)] = 'UNIVERSIDAD NACIONAL DE COLOMBIA'
  AND [Municipio de oferta del programa] = 'BOGOTA D.C.'
  AND Año BETWEEN 2014 AND 2021
GROUP BY Año;


