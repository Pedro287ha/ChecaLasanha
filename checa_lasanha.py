import re
import requests
from bs4 import BeautifulSoup

## Constantes de configuracao
HEADERS = {
    "Host": "www.olx.com.br",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image",
    "Connection": "keep-alive",
}

def gerar_conteudo_pagina_anuncios(link) -> dict:
    LIMITE_PAGINA = 120
    TAMANHO_PAGINA_SEM_ANUNCIO = 202900 # valor pode variar com atualizacoes
    
    # Validando tamanho de paginas a ser vereficado
    for numero_pagina in range(1,LIMITE_PAGINA):
        link_com_numero_pagina = f"{link}?o={numero_pagina}"
        
        # Iniciando request com servidor
        r = requests.get(link_com_numero_pagina, headers=HEADERS)
        
        conteudo_pagina = r.text
        tamanho_conteudo_pagina = len(r.text)
        
        ## Fechando conexao
        r.close()


        ## Se fim de paginas de anuncios termine

        PAGINA_NAO_CONTEM_ANUNCIOS = tamanho_conteudo_pagina <= TAMANHO_PAGINA_SEM_ANUNCIO

        if PAGINA_NAO_CONTEM_ANUNCIOS: # Geralmente tamanho pagina anuncios retorna baixos
            print("FIM")
            print(link_com_numero_pagina, numero_pagina - 1)
            break
        else:
            print("valido ", link_com_numero_pagina)
            #gerar_dados_do_anuncio()

    #return anuncios

def main() -> None:
    with open("link_anuncios.txt", "r") as f: 
        for link in f:
            gerar_conteudo_pagina_anuncios(link)






if __name__ == "__main__":
    main()
