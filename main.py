#Como criar 10000 mil arquivos .txt 

numero_do_arquivo = 0

for n in range(10000):
    numero_do_arquivo += 1

    conteudo_do_arquivo = f"""
Arquivo_{numero_do_arquivo}
"""
    with open(f"Arquivos//arquivo_{numero_do_arquivo}.txt", 
    "w") as arquivo:

        for conteudo in conteudo_do_arquivo:
            arquivo.write(str(conteudo))