#Clean up loans data for R plotting

import pandas as pd 
import numpy as np 

data = pd.read_csv('D:\R\Loans\DATA\loansData.csv')

#Breaking down the 'Fico.Range' column into max and min. Also averaging the data to make it easier to work with
fico = data['FICO.Range']

def returnMin(x):
	x=x.split('-')
	return int(x[0])
def returnMax(x):
	x=x.split('-')
	return int(x[1])

ficoMin = fico.map(lambda x: returnMin(x))
ficoMax = fico.map(lambda x: returnMax(x))
ficoAvg = (ficoMin+ficoMax)/2

#droping the percentage so it's easier to work with in r
def dropPercentage(x):
	x = float(x[0:-1])
	return x

data['Interest.Rate']= data['Interest.Rate'].map(lambda x: dropPercentage(x))
data['Debt.To.Income.Ratio']= data['Debt.To.Income.Ratio'].map(lambda x: dropPercentage(x))
data['Fico.Min']=ficoMin
data['Fico.Max']=ficoMax
data['Fico.Avg']=ficoAvg

data.to_csv('D:\\R\\Loans\\DATA\\cleanLoansData.csv')