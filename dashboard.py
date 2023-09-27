from flask import Flask
from flask import render_template, url_for, redirect, flash, get_flashed_messages
import pandas as pd
import json

saleapp = Flask(__name__)

"---------------------------------"


@saleapp.route('/')
def index():
    # Read CSV file from local
    df = pd.read_csv('data/saledata.csv')

    header = df.columns.values.tolist()
    data = df.to_dict(orient='records')
    return render_template('index.html', context={'header': header, 'data': data})


@saleapp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    df = pd.read_csv('data/saledata.csv')

    customer_wise = df.groupby('Customer')['Amount'].sum()
    customer_wise_sale_label = customer_wise.reset_index()['Customer'].tolist()
    customer_wise_sale = customer_wise.reset_index()['Amount'].tolist()

    date_wise = df.groupby('Date')['Amount'].sum()
    date_wise_sale_label = date_wise.reset_index()['Date'].tolist()
    date_wise_sale = date_wise.reset_index()['Amount'].tolist()

    customer_wise_weight = df.groupby('Customer')['Weight'].sum()
    customer_wise_weight_label = customer_wise_weight.reset_index()[
        'Customer'].tolist()
    customer_wise_weight = customer_wise_weight.reset_index()[
        'Weight'].tolist()

    context = {'customer_wise_sale': json.dumps(customer_wise_sale),
               'customer_wise_sale_label': json.dumps(customer_wise_sale_label),
               'date_wise_sale': json.dumps(date_wise_sale),
               'date_wise_sale_label': json.dumps(date_wise_sale_label),
               'customer_wise_weight': json.dumps(date_wise_sale),
               'customer_wise_weight_label': json.dumps(date_wise_sale_label),
               }
    print(context, "context")

    return render_template('dashboard.html', context=context)
