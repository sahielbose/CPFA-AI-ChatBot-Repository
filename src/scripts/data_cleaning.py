import numpy as np
import pandas as pd

# Cleaning Cybersecurity risk dataset
df_riskdata = pd.read_csv('data/raw/cybersecurity_risk.csv')

#TODO: Perform data cleaning steps
print(df_riskdata.info())

#delete notes column as it contains all nulls
del df_riskdata['notes']

df_riskdata.to_csv('data/processed/cybersecurity_risk_clean.csv', index=False)

# Cleaning Phishing dataset
df_phishdata = pd.read_csv('data/raw/cybersecurity_phishing.csv')

#TODO: Perform data cleaning steps

df_phishdata.to_csv('data/processed/ccybersecurity_phishing_clean.csv', index=False)
