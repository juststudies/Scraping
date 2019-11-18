import urllib.request
import codecs
import json
import zlib

url = 'https://catalogo.conecta.gov.br/Metadados-Estatisticos/v2/pesquisas'
file = codecs.open('pesc', 'w', 'utf-8')
resp = urllib.request.urlopen(url)
decompressed = zlib.decompress(resp.read(), 16+zlib.MAX_WBITS)
updateJSON = json.loads(decompressed)

for x in updateJSON:

    file.write('Nome: ' + x['nome'] + '\n')
    file.write('Categoria: ' + x['categoria'] + '\n')

    file.write('\n')
    file.write('\n')
