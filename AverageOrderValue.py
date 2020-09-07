import pandas as pd
import numpy as np

filename = '2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv'

def WeightedAverage(values, weights):
    if len(values) != len(weights):
        print('size mismatch')
        return
    else:
        numerator = sum([v*w for v, w in zip(values, weights)])
        denominator = sum(weights)
        return numerator / denominator

def AverageShoePrice(amounts, counts):
    prices = [a/c for a, c in zip(amounts, counts)]
    return WeightedAverage(prices, counts)

if __name__ == '__main__':
    df = pd.read_csv(filename)
    print(df.describe())
    print("This mean does not take into account total items in the purchase")

    amt = df['order_amount']
    cnt = df['total_items']
    print("Calculating weighted average...")
    print("Average Shoe Price: $%s" % round(AverageShoePrice(amt, cnt), 2))




