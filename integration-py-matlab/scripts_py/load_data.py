import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import datetime
import locale
import os

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')


def format_files(active, dt_start, dt_end, interval):
    start_month = datetime.datetime.strptime(dt_start, "%Y-%m-%d").strftime("%b").upper()
    start_year = datetime.datetime.strptime(dt_start, "%Y-%m-%d").strftime("%y")

    end_month = datetime.datetime.strptime(dt_end, "%Y-%m-%d").strftime("%b").upper()
    end_year = datetime.datetime.strptime(dt_end, "%Y-%m-%d").strftime("%y")

    # file_name = f"{active.lower()}_{start_month}{start_year}_{end_month}{end_year}"
    file_name = f"{active.lower()}_{dt_start}_{dt_end}"
    # print(file_name)

    # outdir = f"./data/{start_month}{start_year}_{end_month}{end_year}"
    outdir = f"./data/{dt_start}_{dt_end}"
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    fullname = os.path.join(outdir, f"{file_name}.csv")

    file_exists = os.path.exists(fullname)

    if not file_exists:
        if active == 'IBOVESPA':
            df = web.get_data_yahoo('^BVSP', start=dt_start, end=dt_end, interval=interval).reset_index()
        else:
            df = web.get_data_yahoo(f'{active}.SA', start=dt_start, end=dt_end, interval=interval).reset_index()

        df.rename(columns={'Date': 'data',
                           'High': 'maxima',
                           'Low': 'minima',
                           'Open': 'abertura',
                           'Close': 'fechamento',
                           'Volume': 'volume'}, inplace=True)
        df['variacao'] = (df['fechamento'] - df['abertura']) / df['abertura']
        df = df[['data', 'maxima', 'minima', 'abertura', 'fechamento', 'variacao']]

        df.to_csv(fullname, index=False)

    else:
        df = pd.read_csv(fullname)

    return df


def load_data(ativo, start_date, end_date, interval):
    df = pd.DataFrame()
    try:
        df = format_files(ativo, start_date, end_date, interval)
    except KeyError:
        print(f'Erro no ativo {ativo}')
        pass

    return df
