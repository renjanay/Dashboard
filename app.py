import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from flask import Flask, render_template

app = Flask(__name__)

def read_data_from_excel(file_path):
    # Read data from the CSV file using pandas
    data = pd.read_csv(file_path)
    return data

@app.route('/')
def index():
    # Path to your Excel file
    excel_file_path = 'https://github.com/renjanay/Dashboard/blob/main/Data.xlsx'
    
    # Read data from Excel
    data = read_data_from_excel(excel_file_path)

    # Visualize the data (you can customize this based on your requirements)
    fig = px.scatter(data, x='bulan', y='pend_total', title='Data Visualization')

    # Convert the Plotly figure to JSON for JavaScript rendering
    plot_json = fig.to_json()

    return render_template('index.html', plot_json=plot_json)

if __name__ == '__main__':
    app.run(debug=True)