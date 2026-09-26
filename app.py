from dash import Dash, dcc, html, Input, Output
import joblib
import pandas as pd

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
feature_columns = joblib.load('feature_columns.pkl')

app = Dash(__name__)
server = app.server  # needed for deployment

app.layout = html.Div([
    html.H1("Customer Churn Predictor"),

    html.Label("Contract Type"),
    dcc.Dropdown(
        id='contract',
        options=[{'label': c, 'value': c} for c in ['Month-to-month', 'One year', 'Two year']],
        value='Month-to-month'
    ),

    html.Label("Tenure (months)"),
    dcc.Slider(id='tenure', min=0, max=72, step=1, value=12,
               marks={0:'0', 24:'24', 48:'48', 72:'72'}),

    html.Label("Monthly Charges ($)"),
    dcc.Slider(id='monthly_charges', min=18, max=120, step=1, value=70,
               marks={18:'$18', 60:'$60', 120:'$120'}),

    html.Label("Internet Service"),
    dcc.Dropdown(
        id='internet_service',
        options=[{'label': i, 'value': i} for i in ['DSL', 'Fiber optic', 'No']],
        value='Fiber optic'
    ),

    html.Br(),
    html.Div(id='prediction-output', style={'fontSize': 24, 'marginTop': 20})
])

@app.callback(
    Output('prediction-output', 'children'),
    Input('contract', 'value'),
    Input('tenure', 'value'),
    Input('monthly_charges', 'value'),
    Input('internet_service', 'value')
)
def predict_churn(contract, tenure, monthly_charges, internet_service):
    row = {col: 0 for col in feature_columns}
    row['tenure'] = tenure
    row['MonthlyCharges'] = monthly_charges
    row['TotalCharges'] = tenure * monthly_charges
    row['avg_monthly_spend'] = monthly_charges
    row['num_services'] = 2

    if contract == 'One year':
        row['Contract_One year'] = 1
    elif contract == 'Two year':
        row['Contract_Two year'] = 1

    if internet_service == 'Fiber optic':
        row['InternetService_Fiber optic'] = 1
    elif internet_service == 'No':
        row['InternetService_No'] = 1

    input_df = pd.DataFrame([row])[feature_columns]
    numeric_cols = ['tenure','MonthlyCharges','TotalCharges','avg_monthly_spend','num_services']
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

    prob = model.predict_proba(input_df)[0][1]
    return f"Predicted churn probability: {prob*100:.1f}%"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port)
