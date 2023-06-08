--Inscritos totales por sexo en la Universidad Nacional de Colombia, bogotá desde el año 2014 al 2021

SELECT SUM(CASE WHEN Sexo = 'MASCULINO' THEN Inscritos ELSE 0 END) AS 'Total Hombres',
       SUM(CASE WHEN Sexo = 'FEMENINO' THEN Inscritos ELSE 0 END) AS 'Total Mujeres'
FROM filtered_data
WHERE [Institución de Educación Superior (IES)] = 'UNIVERSIDAD NACIONAL DE COLOMBIA'
  AND [Municipio de oferta del programa] = 'BOGOTA D.C.'
