from fileinput import filename
import pandas as pd
import sys
import unicodedata
import os


# funcao que remove acentos
def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


try:
    # Leitura do nome do arquivo dos argumentos
    filepath = str(sys.argv[1])

except:
    print("Erro ao carregar nome do arquivo")

else:

    try:
        # Leitura mes de inicio dos argumentos
        periodInitial = str(sys.argv[2]).upper()
        # Leitura mes de final dos argumentos
        periodFinal = str(sys.argv[3]).upper()

    except:

        print("Erro ao carregar o periodo desejado")

    else:
        # Leitura do arquivo
        df = pd.read_csv(filepath)
        # Trocando virgula por ponto para ficar no formato do matlab e retirando os simbolos de porcentagem
        df = df.replace(',', '.', regex=True).replace('%', '', regex=True)
        # Renomeando as colunas
        df.columns = ['DATA', 'ULTIMO', 'ABERTURA', 'MAXIMA', 'MINIMA', 'VOLUME', 'VARIACAO']
        # Passando as porcentagem para valores de 0 a 1
        df['VARIACAO'] = df['VARIACAO'].astype(float) / 100
        # Padronização da coluna DATA
        df['DATA'] = df['DATA'].str.upper()
        # Index da linha que contem a data de inicio especificada
        indexInitial = df.index[df['DATA'] == periodInitial].tolist()[0]
        # Index da linha que contem a data de fim especificada
        indexFinal = df.index[df['DATA'] == periodFinal].tolist()[0]
        # Filtro para obtenção dos dados no periodo especificado
        df_filtered = df.filter(items=range(indexFinal, indexInitial + 1), axis=0)

        splitedFilepath = filepath.split('/')
        # Separando o nome do arquivo do resto do path
        filename = splitedFilepath[len(splitedFilepath) - 1]
        # Montagem do nome do arquivo
        filename_treated = strip_accents(filename.lower().replace(' ', '_').replace('.csv', ''))

        # Criando a pasta que serao salvos os dados tratados
        outdir = './dados_historicos_tratados'
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        outname = filename_treated + '_tratado_' + periodInitial.replace(' ', '') + '-' + periodFinal.replace(' ',
                                                                                                              '') + '.csv'

        # Salvando o dataframe no formato csv
        df_filtered.to_csv(os.path.join(outdir, outname), index=False)

        print("Script executado com sucesso")
