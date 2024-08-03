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
def txtpronto():    
    '''
    RETORNA STRING 'txtpronto'
    '''
    return 'txtpronto'
def cospe(a):
    '''
    EXATAMENTE IGUAL A INPUT()
    '''
    return input('')
def deixainteiro(a):
    '''
    DEIXA UM NUMERO INTEIRO
    '''
    return int((input(a)))
def tralha(a):
    '''
    retorna uma tralha ou seja não exibe nada
    '''
    return #
funcoes = [txtpronto,cospe,deixainteiro,tralha]
dicionario = {
    'NUMEROS' :numeros,
    'misto':misto,
    'palavras':palavras,
    'espacos':espacos,
    'REPETIDOS':'ULTIMO',
    'REPETIDOS':'PRIMEIRO',
    'variaveis':variaveis,
    'funcoes duvidosas':funcoes,
    'lista vazio E exclusiva':vazio,
}
# aqui começa o dicionario de uso E que nào tem o dict com key e value exclusivo
manipulacao = {
    'NUMEROS' :numeros,
    'misto':misto,
    'palavras':palavras,
    'espacos':espacos,
    'REPETIDOS':'REPETIDOS02',
    'REPETIDOS':'REPETIDOS01',
    'variaveis':variaveis,
    'funcoes duvidosas':funcoes,
    'DICIONARIO': dicionario,
}