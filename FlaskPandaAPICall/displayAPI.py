from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def display_csv():
    # Read the CSV file
    df = pd.read_csv('nba.csv')

    # Convert the DataFrame to HTML table
    table_html = df.to_html()

    # Render the HTML template with the table
    return render_template('display.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
