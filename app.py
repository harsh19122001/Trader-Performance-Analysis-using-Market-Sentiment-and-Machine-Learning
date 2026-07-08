import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Trader Performance Prediction",
    page_icon="📈",
    layout="wide"
)

# ---------------- LOAD MODEL ---------------- #
with open("random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("encoders.pkl", "rb") as file:
    encoders = pickle.load(file)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.main{
background:#0E1117;
}

.title{
font-size:40px;
font-weight:bold;
text-align:center;
color:#00E5FF;
}

.sub{
font-size:18px;
text-align:center;
color:white;
margin-bottom:30px;
}

.stButton>button{
background:#00E5FF;
color:black;
font-size:18px;
font-weight:bold;
width:100%;
height:50px;
border-radius:10px;
}

.result{
padding:15px;
border-radius:12px;
font-size:28px;
font-weight:bold;
text-align:center;
}

</style>
""",unsafe_allow_html=True)

st.markdown("<div class='title'>📈 Trader Performance Prediction</div>",unsafe_allow_html=True)

st.markdown("<div class='sub'>Predict whether a trade will be PROFIT or LOSS using Machine Learning</div>",unsafe_allow_html=True)

st.sidebar.header("About")

st.sidebar.write("""
### Tech Stack

- Python
- Streamlit
- Random Forest
- Scikit-Learn
- Pandas
- NumPy

Model Accuracy : **98.7%**
""")

# ---------------- INPUT ---------------- #

left,right=st.columns(2)

with left:

    sentiment=st.selectbox(

        "Market Sentiment",

        encoders['classification'].classes_

    )

    coin=st.selectbox(

        "Coin",

        encoders['Coin'].classes_

    )

    side=st.selectbox(

        "Side",

        encoders['Side'].classes_

    )

    direction=st.selectbox(

        "Direction",

        encoders['Direction'].classes_

    )

with right:

    execution_price=st.number_input(

        "Execution Price",

        min_value=0.0,

        value=100000.0

    )

    size_tokens=st.number_input(

        "Size Tokens",

        min_value=0.0,

        value=1.0

    )

    size_usd=st.number_input(

        "Size USD",

        min_value=0.0,

        value=1000.0

    )

    fee=st.number_input(

        "Fee",

        min_value=0.0,

        value=1.0

    )

hour=st.slider(

    "Trading Hour",

    0,

    23,

    12

)

month=st.slider(

    "Month",

    1,

    12,

    6

)
# ---------------- PREDICTION ---------------- #

if st.button("Predict Trade Outcome"):

    try:

        sentiment_encoded = encoders["classification"].transform([sentiment])[0]
        coin_encoded = encoders["Coin"].transform([coin])[0]
        side_encoded = encoders["Side"].transform([side])[0]
        direction_encoded = encoders["Direction"].transform([direction])[0]

        input_data = pd.DataFrame({

            "classification":[sentiment_encoded],
            "Coin":[coin_encoded],
            "Execution Price":[execution_price],
            "Size Tokens":[size_tokens],
            "Size USD":[size_usd],
            "Side":[side_encoded],
            "Direction":[direction_encoded],
            "Fee":[fee],
            "Hour":[hour],
            "Month":[month]

        })

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0]

        confidence = np.max(probability) * 100

        st.markdown("---")

        st.subheader("Prediction Result")

        if prediction == 1:

            st.success("🟢 PROFIT TRADE")

        else:

            st.error("🔴 LOSS TRADE")

        st.metric(

            label="Prediction Confidence",

            value=f"{confidence:.2f}%"

        )

        st.progress(float(confidence/100))

        st.subheader("Prediction Probability")

        prob_df = pd.DataFrame({

            "Outcome":["Loss","Profit"],

            "Probability":[

                probability[0]*100,

                probability[1]*100

            ]

        })

        st.bar_chart(

            prob_df,

            x="Outcome",

            y="Probability"

        )

        st.subheader("Input Summary")

        st.dataframe(input_data)

    except Exception as e:

        st.error(f"Prediction Error : {e}")
        
        st.markdown("---")

st.info("""
### Model Information

- Model : Random Forest Classifier
- Test Accuracy : 98.75%
- Features Used :
    • Market Sentiment
    • Coin
    • Execution Price
    • Size Tokens
    • Size USD
    • Side
    • Direction
    • Fee
    • Trading Hour
    • Month
""")

st.markdown("---")

st.caption("Developed by Harsh Jaiswal | Trader Performance Analysis using Market Sentiment & Machine Learning")