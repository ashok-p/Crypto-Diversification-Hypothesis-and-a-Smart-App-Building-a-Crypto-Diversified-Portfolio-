import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import yfinance as yf
import hvplot.pandas
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
#%matplotlib inline
import panel as pn
import questionary

def get_data(ticker, start, end, source='Yahoo', pct_change=True):
    if source=="" or source=='Yahoo' or source == 'y' or source == 'Y':
       if pct_change==False:
         return pdr.get_data_yahoo(ticker, start, end)
       else:
        return pdr.get_data_yahoo(ticker, start, end).pct_change().dropna()
    else:
        print(f"The data source {source} is not yet implemented")
        return None
def prep_data(dataframe1, dataframe2, options):
    print("Yet to implement")
def analyze_and_plot(title, daily_ret, xcol, ycol, plot_type, mkt='SPY'):
    
    #PLOT TYPE - Historical or Dailiy Returns
    if plot_type=='H' or plot_type=='h' or plot_type == 'D' or plot_type == 'd':
        x= daily_ret[ycol].hvplot(
            title = title,
            ylabel = ycol,  # lambda y:  if ycol!=None: y=ycol,
            xlabel = xcol, # lambda x: if xcol!=None: x=xcol,
           # height = 600,
            width = 400
            )
        return x
        #hvplot.show(x)
    elif plot_type=='C' or plot_type=='c' or plot_type == 'Cumulative':
        cumulative_returns = (1 + daily_ret).cumprod() -1
        x= cumulative_returns[ycol].hvplot(
            title = title,
            ylabel = ycol,  # lambda y:  if ycol!=None: y=ycol,
            xlabel = xcol, # lambda x: if xcol!=None: x=xcol,
           # height = 600,
            width = 400
        )
        return x
       # hvplot.show(x)
  #Example -get_beta(df['Close']['BTC-USD'], df['Close']['ETH-USD'])
def get_beta(df1, df2):
    return df1.cov(df2) / df2.var()
          # df - daily return data frame for the security..we pass the Close column or Adj Close as param, 
# e.g. get_sharpe(dailyret['Adj Close'])

def get_sharpe(df):
    year_trading_days = 252
    average_annual_return = df.mean()* year_trading_days
    std_dev = df.std()
    annualized_std = std_dev * np.sqrt(year_trading_days)
    sharpe_ratio = average_annual_return / annualized_std
    return sharpe_ratio

def do_montecarlo(df):
    print('will do soon')


def xact(ticker):
    print(f'Hey Rich guy!!!  WANNA BUY SOME  {ticker}  CRYptos.. U have some guts!!\n ')
    
    x =f'''To assist you in your decision, provided below are:
    - Beta 
    - Sharpe Ratios
    - projection w MonteCarlo plot\n'''
    print(x)

    start = dt.datetime(2017, 1, 1)
    end = dt.datetime(2022, 5, 2)
    df1= get_data(ticker, start, end)

    etf_name=['S&P 500',
    'iShares U.S. Technology',
    'Invesco China Technology',
    'Invesco S&P 500 Equal Weight Technology',
    'iShares Evolved U.S. Technology',
    'iShares Russell 2000',
    'Vanguard Total Bond Market',
    'Ark Innovation',
    'Invesco S&P500 Pure Value']

    etfs=['SPY', 'IYW', 'CQQQ', 'RYT', 'IETC', 'IWM', 'BND','ARKK','RPV']
    x=get_sharpe(df1['Close'])
    print (f"\nSHARPE Ratio for {ticker} is ...{x}\n")
    
    print('The Betas against various Technology Funds are...\n')
    j=0
    for i in etfs:

        df2=get_data(i, start, end)
        b=get_beta(df1['Close'],df2['Close'])
        print (f'{etf_name[j]}\t{b:.2f}')
        j+=1

    resp=questionary.text("When you are done digesting Betas and Sharpe, press enter..").ask()

    cp=analyze_and_plot('Cumulative Returns', df1, xcol='Date', ycol='Close', plot_type='c')
    hvplot.show(cp)
