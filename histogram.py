# Copyright (c) 2023 Víctor Bárcena Mena
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import matplotlib.pyplot as plt
import csv

# Crear listas para almacenar las latencias
latencias_nrt = []
latencias_nrt_hackbench = []
latencias_nrt_bonnie = []

# Leer el archivo CSV y almacenar las latencias en la lista
with open('capturas/cyclictestURJC_nrt_1.csv', 'r') as archivo_csv:
    csv_reader = csv.reader(archivo_csv)
    next(csv_reader)  # Saltar la primera fila si contiene encabezados
    for row in csv_reader:
        # if row[0] == "1":
        latencia = int(row[2]) /1000 # Convertir la latencia a entero
        latencias_nrt.append(latencia)
            #print(row[0])

with open('capturas/cyclictestURJC_nrt_2.csv', 'r') as archivo_csv:
    csv_reader = csv.reader(archivo_csv)
    next(csv_reader)  # Saltar la primera fila si contiene encabezados
    for row in csv_reader:
        # if row[0] == "1":
        latencia = int(row[2]) / 1000 # Convertir la latencia a entero
        latencias_nrt_hackbench.append(latencia)
            #print(row[0])

with open('capturas/cyclictestURJC_nrt_3.csv', 'r') as archivo_csv:
    csv_reader = csv.reader(archivo_csv)
    next(csv_reader)  # Saltar la primera fila si contiene encabezados
    for row in csv_reader:
        # if row[0] == "1":
        latencia = int(row[2]) / 1000 # Convertir la latencia a entero
        latencias_nrt_bonnie.append(latencia)
            #print(row[0])

# Crear un histograma
plt.hist(latencias_nrt, bins=100, range=[0, 40], color='red', alpha=0.5, label='Non real time - idle ')
plt.hist(latencias_nrt_hackbench, bins=100, range=[0, 40], color='blue', alpha=0.5, label='Non real time - hackbench')
plt.hist(latencias_nrt_bonnie, bins=100, range=[0, 40], color='green', alpha=0.5, label='Non real time - bonnie')
plt.xlabel('Latencia (microsegundos)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Latencias')
plt.legend()
plt.grid(True)

# Mostrar el histograma
plt.show()


latencias_rt = []
latencias_rt_hackbench = []
latencias_rt_bonnie = []

# Leer el archivo CSV y almacenar las latencias en la lista
with open('capturas/cyclictestURJC_rt_1.csv', 'r') as archivo_csv:
    csv_reader = csv.reader(archivo_csv)
    next(csv_reader)  # Saltar la primera fila si contiene encabezados
    for row in csv_reader:
        # if row[0] == "1":
        latencia = int(row[2]) /1000 # Convertir la latencia a entero
        latencias_rt.append(latencia)
            #print(row[0])

with open('capturas/cyclictestURJC_rt_2.csv', 'r') as archivo_csv:
    csv_reader = csv.reader(archivo_csv)
    next(csv_reader)  # Saltar la primera fila si contiene encabezados
    for row in csv_reader:
        # if row[0] == "1":
        latencia = int(row[2]) / 1000 # Convertir la latencia a entero
        latencias_rt_hackbench.append(latencia)
            #print(row[0])

with open('capturas/cyclictestURJC_rt_3.csv', 'r') as archivo_csv:
    csv_reader = csv.reader(archivo_csv)
    next(csv_reader)  # Saltar la primera fila si contiene encabezados
    for row in csv_reader:
        # if row[0] == "1":
        latencia = int(row[2]) / 1000 # Convertir la latencia a entero
        latencias_rt_bonnie.append(latencia)
            #print(row[0])

plt.hist(latencias_rt, bins=100, range=[0, 40], color='red', alpha=0.5, label='Real time - idle')
plt.hist(latencias_rt_hackbench, bins=100, range=[0, 40], color='blue', alpha=0.5, label='Real time - hackbench')
plt.hist(latencias_rt_bonnie, bins=100, range=[0, 40], color='green', alpha=0.5, label='Real time - bonnie')
plt.xlabel('Latencia (microsegundos)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Latencias')
plt.legend()

plt.grid(True)

# Mostrar el histograma
plt.show()
