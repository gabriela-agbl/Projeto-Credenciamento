import random
import string
import time


def gerar_chave():
   return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


try:
   while True:
       chave=gerar_chave()
       with open("chave.txt", "w") as arquivo:
           arquivo.write(chave)
       print(f"[GERADOR] Nova chave gerada: {chave} (válida por 10s)")
       time.sleep(10)


except KeyboardInterrupt:
   print("\nGerador encerrado")