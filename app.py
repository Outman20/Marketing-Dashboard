import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Daten 
data = {
    "Kampagne": ["Google Ads", "Instagram", "TikTok", "Facebook", "Email"],
    "Kosten": [500, 300, 200, 400, 100],
    "Klicks": [1000, 900, 1200, 1100, 500],
    "Käufe": [50, 45, 60, 55, 30]
}

df = pd.DataFrame(data)

# KPIs berechnen
df["CPC"] = df["Kosten"] / df["Klicks"]
df["CPA"] = df["Kosten"] / df["Käufe"]
df["Conversion Rate"] = df["Käufe"] / df["Klicks"]

# Titel
st.title(" Marketing Dashboard")

kampagne = st.selectbox("Wähle eine Kampagne", df["Kampagne"])

df_filtered = df[df["Kampagne"] == kampagne]
st.write("Ausgewählte Kampagne:", df_filtered)
st.subheader("KPIs Übersicht")

col1, col2, col3 = st.columns(3)

col1.metric("Durchschnitt CPC", round(df["CPC"].mean(), 2))
col2.metric("Beste Kampagne", df.loc[df["Käufe"].idxmax(), "Kampagne"])
col3.metric("Beste Conversion", round(df["Conversion Rate"].max(), 2))
# Tabelle
st.subheader("Rohdaten")
st.dataframe(df)

# KPIs
st.subheader("KPIs")
st.write("Durchschnitt CPC:", df["CPC"].mean())
st.write("Beste Kampagne (Käufe):", df.loc[df["Käufe"].idxmax(), "Kampagne"])
st.write("Beste Kampagne (Conversion Rate):", df.loc[df["Conversion Rate"].idxmax(), "Kampagne"])

# Grafik 1: Käufe
st.subheader("Käufe pro Kampagnme")
fig1, ax1 = plt.subplots()
ax1.bar(df_filtered["Kampagne"], df_filtered["Käufe"])
st.pyplot(fig1)

#Grafik 2 : Conversion Rate
st.subheader("Conversion Rate pro Kampagne")
fig2, ax2 = plt.subplots()
ax2.bar(df_filtered["Kampagne"], df_filtered["Conversion Rate"])
st.pyplot(fig2)