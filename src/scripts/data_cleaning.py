import numpy as np
import pandas as pd

# Cleaning Cybersecurity risk dataset
df_riskdata = pd.read_csv('data/raw/cybersecurity_risk.csv')

#TODO: Perform data cleaning steps

df_riskdata.to_csv('data/processed/cybersecurity_risk_clean.csv', index=False)

# Cleaning Phishing dataset
df_riskdata = pd.read_csv('data/raw/cybersecurity_phishing.csv')

#TODO: Perform data cleaning steps

df_riskdata.to_csv('data/processed/ccybersecurity_phishing_clean.csv', index=False)
