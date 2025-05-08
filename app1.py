import streamlit as st
import pandas as pd

# Define the data
data = {
    "Paint Name": [
        "ECOS Exterior Paint", "Clare Exterior Paint", "Montage Signature Eco-Friendly Exterior Paint",
        "ECOS Interior Wall Paint", "Clare Interior Paint", "Benjamin Moore Natura",
        "Sherwin-Williams Harmony", "Behr Premium Plus Ultra Pure"
    ],
    "Type": ["Acrylic Latex"] * 8,
    "Application": ["Exterior", "Exterior", "Exterior", "Interior", "Interior", "Interior", "Interior", "Interior"],
    "Key Features": [
        "Zero-VOC, non-toxic, UV/mildew resistance, odor-free",
        "Zero-VOC, Greenguard Gold, fade/mildew resistance, self-priming",
        "Low-VOC, mold/mildew-resistant, eco-friendly, recycled materials",
        "Zero-VOC, non-toxic, odor-free, mildew-resistant, washable",
        "Zero-VOC, Greenguard Gold, washable, stain-resistant, self-priming",
        "Zero-VOC, asthma/allergy-friendly, mildew-resistant, washable",
        "Zero-VOC, antimicrobial, odor-eliminating, washable",
        "Low-VOC, paint/primer in one, mildew-resistant, washable"
    ],
    "Best Uses": [
        "Wood, masonry, eco-conscious projects",
        "Modern homes, wood, eco-friendly projects",
        "Wood, masonry, eco-conscious projects",
        "Walls, ceilings, sensitive environments",
        "Walls, trim, modern interiors",
        "Walls, ceilings, high-traffic areas",
        "Walls, ceilings, bedrooms, nurseries",
        "Walls, ceilings, budget-conscious eco projects"
    ],
    "Coverage (sq. ft./gallon)": ["350–400", "350–400", "300–400", "400–450", "350–400", "350–400", "350–400", "350–400"],
    "Price Range": ["$$$ (~$50–$70)", "$$$ (~$50–$70)", "$$ (~$30–$50)", "$$$ (~$50–$70)", "$$$ (~$50–$70)", "$$$$ (~$70+)", "$$$ (~$50–$70)", "$$ (~$30–$50)"],
    "Sheảnh: Flat, Eggshell, Semi-Gloss"] * 6 + ["Flat, Eggshell, Satin, Semi-Gloss"],
    "VOC Content": ["0 g/L"] * 6 + ["<50 g/L"] * 2,
    "Certifications": [
        "Declare Label, allergy-friendly", "Greenguard Gold, LEED-compliant", "Green Wise",
        "Declare Label, allergy-friendly", "Greenguard Gold, LEED-compliant", "Asthma & Allergy Friendly, Greenguard Gold",
        "Greenguard Gold", "Greenguard Gold"
    ],
    "Warranty": ["Not specified"] * 3 + ["Not specified", "Not specified", "Limited lifetime", "Limited lifetime", "Lifetime limited"]
}

df = pd.DataFrame(data)

# Streamlit app
st.title("Eco-Friendly Paint Comparison")
st.write("Compare eco-friendly interior and exterior paints based on various criteria.")

# Filters
st.sidebar.header("Filters")
application = st.sidebar.multiselect("Application", options=["Interior", "Exterior"], default=["Interior", "Exterior"])
price_range = st.sidebar.multiselect("Price Range", options=["$$ (~$30–$50)", "$$$ (~$50–$70)", "$$$$ (~$70+)"], default=["$$ (~$30–$50)", "$$$ (~$50–$70)", "$$$$ (~$70+)"])
voc_content = st.sidebar.multiselect("VOC Content", options=["0 g/L", "<50 g/L"], default=["0 g/L", "<50 g/L"])
sheen = st.sidebar.multiselect("Sheen Options", options=["Flat", "Eggshell", "Satin", "Semi-Gloss"], default=["Flat", "Eggshell", "Satin", "Semi-Gloss"])

# Apply filters
filtered_df = df[
    (df["Application"].isin(application)) &
    (df["Price Range"].isin(price_range)) &
    (df["VOC Content"].isin(voc_content))
]

# Custom sheen filter
for s in sheen:
    filtered_df = filtered_df[filtered_df["Sheen Options"].str.contains(s)]

# Display table
st.dataframe(filtered_df)

# Download button
csv = filtered_df.to_csv(index=False)
st.download_button("Download CSV", csv, "eco_friendly_paints.csv", "text/csv")
