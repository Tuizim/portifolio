import pandas
import requests
from bs4 import BeautifulSoup

def criando_tabela_excel():
##LISTANDO VARIAVEIS
quantidade_busca= int(input('Digite a quantidade de elementos que deseja buscar: ')) 
list_names=[]
list_numbers=[]
rank=[]
ano=[]

##EXTRAINDO DADOS
headers= {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.86"}
url='https://www.imdb.com/chart/top?ref_=nv_mv_250'
site= requests.get(url, headers=headers)    #entrando no site
soup= BeautifulSoup(site.content, 'html.parser')   #pegando conteudo do site como html

## EXTRAINDO DADOS E ADICIONANDO AS LISTAS
for i in range(0,quantidade_busca):
    ## EXTRAINDO ELEMENTOS HTML
    film_list=soup.find_all('tbody', class_='lister-list')
    film=film_list[0]
    ##EXTRAINDO NOME DE FILMES
    film_name_list= film.find_all('td',class_='titleColumn')
    film_name=film_name_lista[i].get_text().strip()
    ##EXTRAINDO NOTA DOS FILMES
    nota_list=film.find_all('td', class_='ratingColumn imdbRating')
    nota_conversao=nota_list[i].get_text()
    ##EXTRAINDO ANO DOS FILMES
    years_list=film.find_all('span', class_='secondaryInfo')
    years_conversao=years_list[i].get_text()
        
    ##FORMATAÇÃO DOS DADOS
    nota=nota_conversao.replace('\n','')
    years=years_conversao[1:5]
    contagem_letras= len(film_name)
    film=film_name[9:(contagem_letras-7)] #aqui uso a contagem para remover caracteres indesejados
    ##ADICIONANDO ITENS A SUAS DEVIDAS LISTAS
    lista_names.append(filme)
    lista_numbers.append(nota)
    ano.append(int(years))
    rank.append(i+1)
    ##MONTANDO A TABELA
    tabela={'Rank':rank,'Nome do Filme' : list_names,'Ano': ano, 'Nota' : list_numbers}
    dados= pandas.DataFrame(data=tabela)
#imprimindo a tabela
print(dados)
#criando arquivo excel
try:
    dados.to_excel('RankImdb.xls', index=False)
except:
    print('ERRO: Já existe um arquivo com este nome no diretório')
