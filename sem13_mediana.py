# -*- coding: utf-8 -*-
"""Sem13_Mediana

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_cNYv0dgczuCprcFhhklRZy1E3KjQltT
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Estadistica").getOrCreate()

spark

data = [("Jess",20),
        ("José",40),
        ("Crisvalencia",17),
        ("Pablito",25),
        ("Alisson",19),
        ("Sasha",18),
        ("Ana",15),
        ("Samantha",21)]
columns = ["Nombre", "Edad"]
variable = spark.createDataFrame(data,columns)

var_mediana = variable.approxQuantile("Edad",[0.5], 0.0)

print("La mediana es:" ,var_mediana)