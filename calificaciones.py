import pandas as pd
import numpy as np

# Generar nombres y apellidos aleatorios
nombres = ["Juan", "María", "Carlos", "Laura", "Pedro", "Ana", "Luis", "Elena", "Miguel", "Sofía"]
apellidos = ["García", "Martínez", "Rodríguez", "Fernández", "López", "González", "Pérez", "Sánchez", "Díaz", "Torres"]

# Generar datos aleatorios para cada campo
np.random.seed(0)  # Para reproducibilidad
datos = {
    'Nombre': np.random.choice(nombres, 100),
    'Apellido': np.random.choice(apellidos, 100),
    'Edad': np.random.randint(18, 60, 100),
    'Asignatura': np.random.choice(['Matemáticas', 'Ciencias', 'Historia', 'Lengua'], 100),
    'Nota': np.random.uniform(5, 10, 100)  # Notas entre 5 y 10
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Mostrar las primeras filas del DataFrame
print(df.head())

# 1. calcular la edad promedio de los estudiantes
edad_promedio = df['Edad'].mean()
print("La edad promedio de los estudiantes es:", edad_promedio)

#2. encontrar el estudiante mas joven y el mas viejo
indice_estudiante_mas_joven = df['Edad'].idxmin()
estudiante_mas_joven = df.loc[indice_estudiante_mas_joven]

indice_estudiante_mas_viejo = df['Edad'].idxmax()
estudiante_mas_viejo = df.loc[indice_estudiante_mas_viejo]

print("Estudiante más joven:")
print(estudiante_mas_joven)

print("\nEstudiante más viejo:")
print(estudiante_mas_viejo)

#3. encontrar a los estudiantes con las 10 notas mas altas
top_10_notas = df.sort_values(by='Nota', ascending=False).head(10)

print("Los estudiantes con las 10 notas más altas son:")
print(top_10_notas)

#4. Contar el numero de estudiantes por materia
estudiantes_por_materia = df['Asignatura'].value_counts()

print("Número de estudiantes por materia:")
print(estudiantes_por_materia)

#5. encontrar la materia con la nota mas baja y la materia con la nota mas alta
nota_promedio_por_materia = df.groupby('Asignatura')['Nota'].mean()

materia_nota_mas_baja = nota_promedio_por_materia.idxmin()
nota_mas_baja = nota_promedio_por_materia.min()

materia_nota_mas_alta = nota_promedio_por_materia.idxmax()
nota_mas_alta = nota_promedio_por_materia.max()

print("Materia con la nota más baja:", materia_nota_mas_baja, "con una nota promedio de", nota_mas_baja)
print("Materia con la nota más alta:", materia_nota_mas_alta, "con una nota promedio de", nota_mas_alta)

#6. calcular el promedio de notas de los estudiantes
# Calcular el promedio de notas de los estudiantes
promedio_notas = df['Nota'].mean()

print("El promedio de notas de los estudiantes es:", promedio_notas)

#7. Contar cuantos estudiantes ganan y cuantos estudiantes pierden (nota menor a 6 es perder)
estudiantes_ganan = df[df['Nota'] >= 6].shape[0]

estudiantes_pierden = df[df['Nota'] < 6].shape[0]

print("Número de estudiantes que ganan:", estudiantes_ganan)
print("Número de estudiantes que pierden:", estudiantes_pierden)

#8. Encontrar la nota mas alta en matematicas y quien la tiene
notas_matematicas = df[df['Asignatura'] == 'Matemáticas']

nota_mas_alta_matematicas = notas_matematicas['Nota'].max()

estudiante_nota_mas_alta_matematicas = notas_matematicas[notas_matematicas['Nota'] == nota_mas_alta_matematicas]

print("La nota más alta en Matemáticas es:", nota_mas_alta_matematicas)
print("El estudiante con la nota más alta en Matemáticas es:")
print(estudiante_nota_mas_alta_matematicas)

#9. encontrar la nota mas baja en historia y quien la tiene
notas_historia = df[df['Asignatura'] == 'Historia']

nota_mas_baja_historia = notas_historia['Nota'].min()

estudiante_nota_mas_baja_historia = notas_historia[notas_historia['Nota'] == nota_mas_baja_historia]

print("La nota más baja en Historia es:", nota_mas_baja_historia)
print("El estudiante con la nota más baja en Historia es:")
print(estudiante_nota_mas_baja_historia)

#10. contar cuantos estudiantes se encuentran en el rango de 30 a 40 años
estudiantes_rango_edad = df[(df['Edad'] >= 30) & (df['Edad'] <= 40)]

num_estudiantes_rango_edad = estudiantes_rango_edad.shape[0]

print("El número de estudiantes en el rango de 30 a 40 años es:", num_estudiantes_rango_edad)