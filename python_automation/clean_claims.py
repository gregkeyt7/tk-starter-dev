#!/usr/bin/env python3

"""
clean_claims.py

Usage:
    python clean_claims.py input.csv output.csv

Cleans and normalizes:
- Dates -> YYYY-MM-DD
- Amounts -> float (no $ or commas)
- Names -> Title Case
- Trims extra whitespace
"""
import sys, re
from datetime import datetime
import pandas as pd
from dateutil import parser

def normalize_date(val):
    try:
        return parser.parse(str(val)).date().isoformat()
    except Exception:
        return None

def normalize_amount(val):
    if val is None:
        return 0.0
    s = str(val).strip()
    s = re.sub(r'[^0-9.\-]', '', s)
    try:
        return float(s) if s else 0.0
    except Exception:
        return 0.0

def titlecase(val):
    return str(val).strip().title() if val is not None else ""

def main():
    if len(sys.argv) < 3:
        print("Usage: python clean_claims.py input.csv output.csv")
        sys.exit(1)
    inp, outp = sys.argv[1], sys.argv[2]
    df = pd.read_csv(inp)
    # Standardize columns if they exist
    if 'loss_date' in df.columns:
        df['loss_date'] = df['loss_date'].apply(normalize_date)
    if 'amount' in df.columns:
        df['amount'] = df['amount'].apply(normalize_amount)
    if 'insured_name' in df.columns:
        df['insured_name'] = df['insured_name'].apply(titlecase)
    # Trim strings
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()
    df.to_csv(outp, index=False)
    print(f"Saved cleaned file -> {outp}")

if __name__ == "__main__":
    main()
