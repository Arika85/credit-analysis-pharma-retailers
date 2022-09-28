import pickle
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

from visualization import *


st.markdown("<h1 style='text-align: center; color: blue;'>Credit Score Analysis</h1><br>",
            unsafe_allow_html=True)


main_options = option_menu(menu_title=None,
                           options=['VISUALIZATION', 'PREDICTION'],
                           default_index=0,
                           orientation="horizontal",
                           icons=['map', 'steam'])

if main_options == 'VISUALIZATION':
    vis_1()

# if main_options == 'What is RFM?':
#     st.write(''' #### The RFM (*Recency, Frequency, Monetary*) model helps you generate segments based on customer behavior analysis that you can apply to your entire customer base.

# You have to assign a score for each variable:

# - “R” stands for Recency and refers to how recently a customer has bought;
# - “F” stands for Frequency and refers to how frequently a customer has ordered;
# - “M” stands for Monetary and refers to how much a customer has spent buying from your business.
# After you calculate the RFM score for each customer, you’ll be able to group your customers into
# different segments that reflect their purchase behavior. You’ll easily spot loyal customers from
# deal hunters and everything in between.

# #### How to calculate the RFM score?
# First, you have to analyze the historical purchase data, looking for the minimum and the maximum
# value for each of the three RFM variables or RFM metrics.

# - Their most recent purchase date.
# - Number of purchases within a set time period (i.e. one year).
# - Total sales from that customer (you could also use average sales or average margin).

# Second, you have to choose the suitable scale according to the size of your customer base:

# - 1 – 3 scale for less than 30k customers;
# - 1 – 4 scale for 30k – 200k customers;
# - 1 – 5 scale for more than 200k customers.
# The minimum and maximum values for recency, frequency, and monetary will help you define the
# intervals for each point in your scale.

# ''')


if main_options == 'PREDICTION':
    # loading gnb model
    rfr_model = pickle.load(open('./rfr_model', 'rb'))

    # header
    st.write('### Give the RFM (*Recency, Frequency, Monetary*) values here')

    # defining function

    def user_input_features():
        recency = st.number_input('Enter the Recency of a customer:')
        frequency = st.number_input('Enter the Frequency of a customer:')
        monetary = st.number_input('Enter the Monetary of a customer:')

        data = {'Recency': recency,
                'Frequency': frequency,
                'Monetary': monetary,
                }
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_features()

    # prediction button
    if st.button('Predict'):
        # Apply model to make predictions
        prediction = rfr_model.predict(df)

        # # prediction
        st.subheader('Prediction')
        if prediction == 1:
            st.success('Your Customer is of level Gold (High)')
        elif prediction == 2:
            st.success('Your Customer is of level Silver (Medium)')
        elif prediction == 3:
            st.success('Your Customer is of level Platinum (Medium)')
        else:
            st.success('Your Customer is of level Bronze (Low)')
