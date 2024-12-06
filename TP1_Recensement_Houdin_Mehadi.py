import csv
from pylab import *

liste_2008_vl = []
liste_2008_pop = []
liste_2016_vl = []
liste_2016_pop = []
liste_2021_vl = []
liste_2021_pop = []
liste_2023_vl = []
liste_2023_pop = []
sum_pop_2008 = 0
sum_pop_2016 = 0
sum_pop_2021 = 0
sum_pop_2023 = 0
année = ['année_2008','année_2016','année_2021','année_2023']
population = []
pop_auxerre_2008 = 0
pop_auxerre_2016 = 0
pop_auxerre_2021 = 0
pop_auxerre_2023 = 0
liste_pop_auxerre = []
pourcentage_ville_aux_2023 = 0


with open("donnees_2008.csv",newline = "") as csvfile:			#on récupère les données qui nous intéresses pour l'année 2008
	data1 = csv.reader(csvfile,delimiter = ';')
	for val1 in data1:
		temp = val1[0].strip()
		val_tab = temp.split(",")
		if val_tab[2] == "89":
			liste_2008_vl.append(val_tab[6])
			liste_2008_pop.append(val_tab[9])
			

with open("donnees_2016.csv",newline = "") as csvfile:			#on récupère les données qui nous intéresses pour l'année 2016
	data2 = csv.reader(csvfile,delimiter = ';')
	for val2 in data2:
		temp = val2[0].strip()
		val_tab = temp.split(",")
		if val_tab[2] == "89":
			liste_2016_vl.append(val_tab[6])
			liste_2016_pop.append(val_tab[9])		

with open("donnees_2021.csv",newline = "") as csvfile:			#on récupère les données qui nous intéresses pour l'année 2021
	data3 = csv.reader(csvfile,delimiter = ';')
	for val3 in data3:
		if val3[1] == "89":
			liste_2021_vl.append(val3[2])
			liste_2021_pop.append(val3[5])

with open("donnees_2023.csv",newline = "") as csvfile:			#on récupère les données qui nous intéresses pour l'année 2008
	data4 = csv.reader(csvfile,delimiter = ';')
	for val4 in data4:
		if val4[2] == "89":
			liste_2023_vl.append(val4[7])
			liste_2023_pop.append(val4[10])


for i in range(len(liste_2008_pop)):						#On parcours la les des populations et villes de l'Yonne, on fait la somme des habitants et on récupères le nombres
	if liste_2008_vl[i] == "Auxerre":						# d'habitant de la ville d'Auxerre. Et on fait cela pour 2008, 2016, 2021 et 2023
		pop_auxerre_2008 += int(liste_2008_pop[i])
	sum_pop_2008 += int(liste_2008_pop[i])	
population.append(sum_pop_2008)
liste_pop_auxerre.append(pop_auxerre_2008)

for i in range(len(liste_2016_pop)):
	if liste_2016_vl[i] == "Auxerre":
		pop_auxerre_2016 += int(liste_2016_pop[i])
	sum_pop_2016 += int(liste_2016_pop[i])
population.append(sum_pop_2016)
liste_pop_auxerre.append(pop_auxerre_2016)

for i in range(len(liste_2021_pop)):
	if liste_2021_vl[i] == "89024":
		pop_auxerre_2021 += int(liste_2021_pop[i])
	sum_pop_2021 += int(liste_2021_pop[i])
population.append(sum_pop_2021)
liste_pop_auxerre.append(pop_auxerre_2021)

for i in range(len(liste_2023_pop)):
	if liste_2023_vl[i] == "Auxerre":
		pop_auxerre_2023 += int(liste_2023_pop[i])
	sum_pop_2023 += int(liste_2023_pop[i])
population.append(sum_pop_2023)
liste_pop_auxerre.append(pop_auxerre_2023)

pourcentage_ville_aux_2023 = (pop_auxerre_2023 / population[3])*100

plt.plot(année,population,marker='o')
plt.xlabel(année)
plt.ylabel(population)														#On affiche la courbe de la population du département de l'Yonne entre 2008 et 2023 avec mathplotlib
plt.title("Population du département de l'Yonne entre 2008-2023")

for i in range(len(population)):
			plt.text(année[i],population[i],str(population[i]), ha='left', va='top', bbox=dict(facecolor="white"))

plt.show()

plt.plot(année,liste_pop_auxerre,marker='o')
plt.xlabel(année)
plt.ylabel(liste_pop_auxerre)												#On affiche la courbe de la population de la ville d'Auxerre entre 2008 et 2023 avec mathplotlib
plt.title("Population de la ville d'Auxerre entre 2008-2023")

for i in range(len(population)):
			plt.text(année[i],liste_pop_auxerre[i],str(liste_pop_auxerre[i]), ha='left', va='top', bbox=dict(facecolor="white"))
			
popularity = {"Auxerre": pourcentage_ville_aux_2023,}
popularity["Le reste de l'Yonne"] = 100 - pourcentage_ville_aux_2023
explode = [0.15 if lang == "Auxerre" else 0 for lang in popularity]
			
plt.show()

plt.title("Population d'Auxerre en pourcentage par rapport à celle de l'Yonne")
plt.pie(popularity.values(),           
        labels=popularity.keys(),      										#On affiche un diagramme circulaire de la population de la ville d'Auxerre en 2023 par rapport a celle
        explode=explode,           											# de l'Yonne avec mathplotlib
        autopct='%.2f %%',             
        shadow=True,                   
        startangle=90,                 
        counterclock=False)            

plt.show()


		

