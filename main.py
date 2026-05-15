import pandas as pd
import matplotlib.pyplot as plt

# Marketing Kampagnen Daten
data = {
    "Kampagne": ["Google Ads", "Instagram", "TikTok", "Facebook", "Email"],
    "Kosten": [500, 300, 200, 400, 100],
    "Klicks": [1000, 900, 1200, 1100, 500],
    "Käufe": [50, 45, 60, 55, 30]
}

df = pd.DataFrame(data)

print(df)

# Cost per Click
df["CPC"] = df["Kosten"] / df["Klicks"]
 
# Cost per Acquisition

df["CPA"] = df["Kosten"] / df["Käufe"]

# Conversion Rate
df["Conversion Rate"] = df["Käufe"] / df["Klicks"]

print("\nDurchschnitt CPC:", df["CPC"].mean())
print("Beste Kampagne (mehr Käufe):", df.loc[df["Käufe"].idxmax(), "Kampagne"])

# Umsatz pro Klick berechnen
df["Umsatz pro Klick"] = df["Käufe"] / df["Klicks"]

print("\nBeste Kampagne nach Käufen:", df.loc[df["Käufe"].idxmax(), "Kampagne"])
print("Beste Kampagne nach Effizienz:", df.loc[df["Conversion Rate"].idxmax(), "Kampagne"])

kampagne = st.selectbox("Wähle eine Kampagne", df["Kampagne"])
plt.figure(figsize=(10,5))

plt.bar(df["Kampagne"], df["Käufe"])

plt.title("Käufe pro Kampagne")
plt.xlabel("Kampagne")
plt.ylabel("Käufe")
plt.show()

kampagne = st.selectbox("Wähle eine Kampagne", df["Kampagne"])
plt.figure(figsize=(10,5))
plt.bar(df["Kampagne"], df["Conversion Rate"])
plt.title("Conversion Rate pro Kampagne")
plt.xlabel("Kampagne")
plt.ylabel("Conversion Rate")
plt.show()