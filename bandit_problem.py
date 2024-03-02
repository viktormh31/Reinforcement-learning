import numpy as np 

zbir = 0
broj_ponavljanja = 1
broj_akcija = 3 # broj mogućih akcija
epsilon = 0.2 # faktor istraživanja
broj_izbora = np.zeros(broj_akcija)


def akcija():
    global broj_uradjenih_akcija
    global q_trenutna_procena
    global broj_izbora
    
    izbor = 0
    choice = 0
    if np.random.rand() < epsilon:
        
        """
        deo koda za biranje akcije koja nije greedy
        radimo random.choice bira random broj iz datog arraya
        mi pravimo array od y za svaki y koji je različit indexu najveće trenutne 
        procenjene vrednosti q.
        
        """
        
        izbor = np.random.choice([y for y in range(broj_akcija) if y != np.argmax(q_trenutna_procena)])
         
    else:

        izbor = np.argmax(q_trenutna_procena)
            
    broj_izbora[izbor]+=1 # koliko puta je koja akcija izabrana
    reward = q_stvarno[izbor] + (np.random.rand() * 2 - 1)# računanje nagrade sa devijacijom od +-1 oko stvarne vrednosti
        
    broj_uradjenih_akcija += 1#brojimo koliko puta je odrađena akcija
    q_trenutna_procena[izbor] = q_trenutna_procena[izbor] + 1/broj_uradjenih_akcija*(reward - q_trenutna_procena[izbor])
   


def proba():
    global broj_uradjenih_akcija
    global zbir
    global q_stvarno
    global q_trenutna_procena
    
    for i in range(broj_ponavljanja):
       
        q_stvarno = np.random.rand(broj_akcija)*2-1 # generisanje stvarnih vrednosti
        print("Stvarna vrednost -             ",q_stvarno)
        q_trenutna_procena = np.zeros(broj_akcija) # generisanje arraya pocetnih procena vrednosti
        
        broj_uradjenih_akcija = 0 # broj izbršenih dodela akcija
        acuracy_avg = 100 # prosečna preciznost procene vrednosti
        acuracy = np.zeros(broj_akcija) # generisanje početnih preciznosti
        it = 0
        
        while(acuracy_avg > 5):
            akcija()
            if it%100 == 0:
                for x in range(broj_akcija):
                    acuracy[x] = abs((q_trenutna_procena[x] - q_stvarno[x])/q_stvarno[x]) * 100
                
                acuracy_avg = acuracy.sum()/broj_akcija
                
            
            if broj_uradjenih_akcija > 2000000:
                break;
            it+=1
        it = 0
        zbir += broj_uradjenih_akcija
        print("Trenutna pronadjena vrednost - ",q_trenutna_procena)
        print("Broj izbora -                  ",broj_izbora/20000)
        print("Average accuracy - ",acuracy_avg)
        print("preciznost je - ",acuracy)
        print("broj iteracija je - ",broj_uradjenih_akcija-1)
        
        print("Prosečna nagrada - ")
            
    print("prosecan broj iteracija je - ",(zbir-1)/100)      


proba()




