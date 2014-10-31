from random import random

N_EXPERIMENTOS = 1000000

PROB_cara_D = 2/3
PROB_cara_H = 1/2

PROB_D = 1/2

evento = ["cara", "cara"]

# quantas vezes a moeda desonesta foi escolhida
cont_D = 0

# quantas vezes o evento desejado ocorreu
cont_evento = 0

# quantas vezes a moeda desonesta foi escolhida *e* o evento desejado ocorreu
cont_D_e_evento = 0

for experimento in range(N_EXPERIMENTOS):
    # escolho aleatoriamente a moeda que sera utilizada
    if random() < PROB_D:
        moeda = "D"
        prob_cara = PROB_cara_D
        cont_D += 1
    else:
        moeda = "H"
        prob_cara = PROB_cara_H

    resultados = []
    for lancamento in range(len(evento)):
        if random() < prob_cara:
            resultados += ["cara"]
        else:
            resultados += ["coroa"]

    if resultados == evento:
        cont_evento += 1
        if moeda == "D":
            cont_D_e_evento += 1
            
evento_str = "-".join(evento)
print("Total de experimentos = %d" % N_EXPERIMENTOS)
print("Total de escolhas da moeda desonesta = %d" % cont_D)
print("Total de ocorrencias do evento %s = %d (%.10f%%)" %
      (evento_str, cont_evento, 100*cont_evento/N_EXPERIMENTOS))
print("Total de ocorrencias do evento com a moeda D = %d" %
      cont_D_e_evento)
print("Prob{D|evento} = %.10f" % (cont_D_e_evento/cont_evento))

      


    

    
    
