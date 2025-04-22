import time
import matplotlib.pyplot as plt

ligne_cell = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#tableau pour l'affichage
affich_plt = []

for g in range(50):
    ligne_remplace = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print (ligne_cell)
    time.sleep(0.1)  #cmb de temps entre générations

    affich_plt.append(ligne_cell.copy())
    
    for i in range(1,len(ligne_cell)-1): #pas touche aux bords

        if ligne_cell[i-1] == 0 and ligne_cell[i] == 0 and ligne_cell[i+1] == 0:
            ligne_remplace[i] = 0

        if ligne_cell[i-1] == 0 and ligne_cell[i] == 0 and ligne_cell[i+1] == 1:
            ligne_remplace[i] = 1

        if ligne_cell[i-1] == 0 and ligne_cell[i] == 1 and ligne_cell[i+1] == 0:
            ligne_remplace[i] = 1

        if ligne_cell[i-1] == 0 and ligne_cell[i] == 1 and ligne_cell[i+1] == 1:
            ligne_remplace[i] = 0

        if ligne_cell[i-1] == 1 and ligne_cell[i] == 0 and ligne_cell[i+1] == 0:
            ligne_remplace[i] = 1

        if ligne_cell[i-1] == 1 and ligne_cell[i] == 0 and ligne_cell[i+1] == 1:
            ligne_remplace[i] = 1

        if ligne_cell[i-1] == 1 and ligne_cell[i] == 1 and ligne_cell[i+1] == 0:
            ligne_remplace[i] = 0

        if ligne_cell[i-1] == 1 and ligne_cell[i] == 1 and ligne_cell[i+1] == 1:
            ligne_remplace[i] = 0

    ligne_cell = ligne_remplace

plt.imshow(affich_plt, cmap="plasma", interpolation="nearest")
plt.title("Automate Cellulaire 1D suivant une rêgle 30")
plt.axis("off")
plt.show()
