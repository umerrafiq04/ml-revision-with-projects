import streamlit as st
import pandas as pd
import joblib

# Load everything
model = joblib.load(r"C:\Users\malik\Desktop\ML_Revise\11_decision_tree\model.pkl")
encoder = joblib.load(r"C:\Users\malik\Desktop\ML_Revise\11_decision_tree\encoder.pkl")
feature_order = joblib.load(r"C:\Users\malik\Desktop\ML_Revise\11_decision_tree\features.pkl")
cat_cols = joblib.load(r"C:\Users\malik\Desktop\ML_Revise\11_decision_tree\cat_cols.pkl")

st.title("🚨 Cybersecurity Intrusion Detection System")

st.write("Enter network flow details or use sample data")

# -------------------------------
# SAMPLE BUTTONS
# -------------------------------

if st.button("🔴 Load Attack Sample"):
    sample = {
        'dur': 0.000009, 'proto': 'ddp', 'service': '-', 'state': 'INT',
        'spkts': 2, 'dpkts': 0, 'sbytes': 200, 'dbytes': 0,
        'rate': 111111.109375, 'sload': 88888888.0, 'dload': 0.0,
        'sloss': 0, 'dloss': 0, 'sinpkt': 0.009, 'dinpkt': 0.0,
        'sjit': 0.0, 'djit': 0.0, 'swin': 0, 'stcpb': 0, 'dtcpb': 0,
        'dwin': 0, 'tcprtt': 0.0, 'synack': 0.0, 'ackdat': 0.0,
        'smean': 100, 'dmean': 0, 'trans_depth': 0,
        'response_body_len': 0, 'ct_src_dport_ltm': 1,
        'ct_dst_sport_ltm': 1, 'is_ftp_login': 0,
        'ct_ftp_cmd': 0, 'ct_flw_http_mthd': 0,
        'is_sm_ips_ports': 0
    }
    st.session_state["sample"] = sample

if st.button("🟢 Load Normal Sample"):
    sample = {
        'dur': 0.121478, 'proto': 'tcp', 'service': '-', 'state': 'FIN',
        'spkts': 6, 'dpkts': 4, 'sbytes': 258, 'dbytes': 172,
        'rate': 74.087486, 'sload': 14158.942383, 'dload': 8495.365234,
        'sloss': 0, 'dloss': 0, 'sinpkt': 24.295601, 'dinpkt': 8.375000,
        'sjit': 30.177547, 'djit': 11.830604, 'swin': 255,
        'stcpb': 621772692, 'dtcpb': 2202533631, 'dwin': 255,
        'tcprtt': 0.0, 'synack': 0.0, 'ackdat': 0.0,
        'smean': 43, 'dmean': 43, 'trans_depth': 0,
        'response_body_len': 0, 'ct_src_dport_ltm': 1,
        'ct_dst_sport_ltm': 1, 'is_ftp_login': 0,
        'ct_ftp_cmd': 0, 'ct_flw_http_mthd': 0,
        'is_sm_ips_ports': 0
    }
    st.session_state["sample"] = sample

# -------------------------------
# INPUT FORM
# -------------------------------

sample = st.session_state.get("sample", {})

input_data = {}

for col in feature_order:
    if col in cat_cols:
        input_data[col] = st.text_input(col, value=str(sample.get(col, "")))
    else:
        input_data[col] = st.number_input(col, value=float(sample.get(col, 0)))

# -------------------------------
# PREDICTION
# -------------------------------

if st.button("🚀 Predict"):
    df = pd.DataFrame([input_data])
    
    # Encode categorical
    df[cat_cols] = encoder.transform(df[cat_cols])
    
    # Order columns
    df = df[feature_order]
    
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0]
    
    if pred == 1:
        st.error("🚨 Attack Detected!")
    else:
        st.success("✅ Normal Traffic")
    
    st.write("### Prediction Probabilities:")
    st.write({
        "Normal": float(prob[0]),
        "Attack": float(prob[1])
    })