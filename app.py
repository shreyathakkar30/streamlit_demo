import streamlit as st

# Title
st.title("📦 Delivery Time Prediction App")

# User Inputs
product_category = st.selectbox("Select Product Category", ["Electronics", "Clothing", "Home Appliances"])
customer_location = st.selectbox("Select Customer Location", ["Urban", "Suburban", "Rural"])
shipping_method = st.selectbox("Select Shipping Method", ["Standard", "Express", "Same-day"])

# Prediction Logic (Simple if-else, can be replaced with ML model)
if st.button("Predict Delivery Time"):
    if shipping_method == "Same-day":
        delivery_time = "1 day"
    elif shipping_method == "Express":
        delivery_time = "2-3 days"
    else:
        if customer_location == "Urban":
            delivery_time = "4-5 days"
        elif customer_location == "Suburban":
            delivery_time = "5-7 days"
        else:
            delivery_time = "7-10 days"

    st.success(f"📦 Expected Delivery Time: **{delivery_time}**")

# Footer with Developer Info
st.markdown("---")
st.markdown("👩‍💻 **Developed by [Shreya Thakkar](https://github.com/shreya-thakkar)** 💙")
