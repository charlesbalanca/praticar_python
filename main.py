# %%
# aqui tem os values das keys e um dict com key e value exclusivo
from random import randint as aliasimportinteiroaleatorio
numeros = [[0],[1,3,5,7,8,0,8,6,4]]
misto   = [8,'e',4,'o','u',0,2,'a','i',6,1010,'000']
palavras = [['pitagóricos'],'HERÁCLITO','parmênides','Platão',['ArIstÓtElEs','alexandre magno'],'sÓcRaTeS',['AGOSTINHO','De','hipona'],['Zenão de Eleia']]
espacos = ['    a','e    ','    i    ','    ']
n01,n02,n3,n04=1,2,3.0,4.0
a,b,c,n01MAISn02,n3VEZESn04,n04PORn02,n04MENOSn02='a','b','c',n01+n02,n3*n04,n04/n02,n04-n02
variaveis = [n01,n02,n3,n04,aliasimportinteiroaleatorio,a,b,c,n01MAISn02,n3VEZESn04,n04PORn02,n04MENOSn02]
vazio = [[],[],[]]
def imprime(a):
    return input()
def cospe(a,b=0):
    return print('...')
def somatoria(a,b=0):
    return int(a)+int(b)
somatoria(10,10)
funcoes = [imprime,cospe,somatoria]
dicionario = {
    'numeros' :numeros,
    'misto':misto,
    'palavras':palavras,
    'espacos':espacos,
    'REPETIDOS':'ULTIMO',
    'REPETIDOS':'PRIMEIRO',
    'variaveis':variaveis,
    'lista vazio E exclusiva':vazio,
    'funcoes duvidoas':funcoes,
}
# aqui começa o dicionario de uso E que nào tem o dict com key e value exclusivo
manipulacao = {
    'REPETIDOS':'ULTIMO',
    'REPETIDOS':'PRIMEIRO',
    'numeros' :numeros,
    'misto':misto,
    'palavras':palavras,
    'espacos':espacos,
    'variaveis':variaveis,
    'lista vazio E exclusiva':vazio,
    'funcoes duvidoas':funcoes,
    'DICIONARIO': dicionario,
}