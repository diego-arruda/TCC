import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import datetime
import locale
import os

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

def format_files(active, dt_start, dt_end, interval):
    
    if active == 'IBOVESPA':
        df = web.get_data_yahoo('^BVSP', start=dt_start, end=dt_end,interval=interval).reset_index()
    else:
        df = web.get_data_yahoo(f'{active}.SA', start=dt_start, end=dt_end,interval=interval).reset_index()
    
    df.rename(columns={'Date': 'data',
                       'High': 'maxima', 
                       'Low': 'minima', 
                       'Open': 'abertura', 
                       'Adj Close': 'fechamento_adj', 
                       'Volume': 'volume'}, inplace=True)
    df['variacao'] = (df['fechamento_adj']-df['abertura'])/df['abertura']
    df = df[['data', 'maxima', 'minima', 'abertura', 'fechamento_adj', 'variacao']]
    
    start_month = datetime.datetime.strptime(dt_start, "%Y-%m-%d").strftime("%b").upper()
    start_year = datetime.datetime.strptime(dt_start, "%Y-%m-%d").strftime("%y")

    end_month = datetime.datetime.strptime(dt_end, "%Y-%m-%d").strftime("%b").upper()
    end_year = datetime.datetime.strptime(dt_end, "%Y-%m-%d").strftime("%y")

    file_name = f"{active.lower()}_{start_month}{start_year}_{end_month}{end_year}"
    print(file_name)

    outdir = f"./data/{start_month}{start_year}_{end_month}{end_year}"
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    fullname = os.path.join(outdir, f"{file_name}.csv")    

    df.to_csv(fullname,index=False)

    return fullname

def load_data2(ativo, start_date, end_date):
    interval = 'm'
    fullname = format_files(ativo,start_date,end_date,interval)
    return fullname


# def load_data(benchmark, ativos, start_date, end_date):
#     interval = 'm'
#     # format_files(benchmark,start_date,end_date,interval)
#     # for ativo in ativos:
#     #     format_files(ativo,start_date,end_date,interval)
#     #     print(ativo)
#     try: 
#         format_files(benchmark,start_date,end_date,interval)
#         for ativo in ativos:
#             format_files(ativo,start_date,end_date,interval)

#     except Exception as e:
#         print(e)
#         return 1

#     return 0


