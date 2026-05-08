from turtle import Terminator


print("Seja bem vinvdo ao programa de pintura de parede")

print ("Lembre-se de colocar as medias em metros das paredes")

tinta=float(input("Insira quantos litros de tinta você tem ?"))

altura=float(input("Insira a altura da sua Parede? "))

largura=float(input("Insira a largura da sua poarede ?"))

preenche= 5
litros= 3

qt=(preenche / litros)

qtpreenche=(altura * largura)

usuario=(qt * tinta)

necessario = (qtpreenche - usuario)



if usuario >= qtpreenche:
 print (f" Com {tinta} litros Você consegue pintar a parede de {qtpreenche} M2")
else:
 print (f"Você tem {tinta} litros, precisará de {necessario:.2f} litros de tinta para terminar ")

