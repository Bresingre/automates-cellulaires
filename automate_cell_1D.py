import time


ligne_cell = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for g in range(10):
    ligne_remplace = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print (ligne_cell)
    time.sleep(2)  #cmb de temps entre générations
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

