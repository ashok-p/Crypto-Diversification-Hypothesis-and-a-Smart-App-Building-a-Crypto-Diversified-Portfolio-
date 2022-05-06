import pandas  as pd
import questionary
import fire
import fourfactor as ff
import cryptoanalysis as ca
import xactcryptos as tc

tickers = ['BTC-USD','ETH-USD','BNB-USD','XRP-USD','SOL-USD','LUNA-USD','ADA-USD','AVAX-USD','DOT-USD','DOGE-USD','EXIT']

#try:
resp=questionary.select("SELECT ONE CRYPTO", choices=tickers).ask()
print (f'Your selection is {resp}')

if resp=='EXIT':
    print('Thank you for visiting!!')
ff.ffanalyse(resp)
ca.analyse(tickers)
tc.xact(resp)

#except Exception:
#  print(f'Exception happened: ...')