import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('model.pkl', 'rb'))

st.title('Car Price Predictor')

km_driven = st.number_input('Enter Km driven')

selected_fuel_type = st.selectbox('Select fuel type', ['Diesel', 'Petrol'])

selected_seller_type = st.selectbox(
    'Select seller type', ['Individual', 'Dealer'])

selected_transmission = st.selectbox(
    'Select transmission', ['Manual', 'Automatic'])

selected_owner = st.selectbox('Select owner', [
                              'First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'])

mileage = st.number_input('Enter mileage km/l')

engine = st.number_input('Enter engine cc')

max_power = st.number_input('Max Power in bhp')

seats = st.number_input('Number of seats')

purchase_year = st.number_input('Purchase Year')

brands = ['Maruti', 'Hyundai', 'Mahindra', 'Tata', 'Honda', 'Ford', 'Toyota',
          'Chevrolet', 'Renault', 'Volkswagen', 'Nissan', 'Skoda', 'Datsun']
selected_brand = st.selectbox('Select brand', brands)

if st.button('Predict Price'):
    input_query = np.array([[km_driven, selected_fuel_type, selected_seller_type, selected_transmission,
                           selected_owner, mileage, engine, max_power, seats, 2020-purchase_year, selected_brand]])
    price = pipe.predict(input_query)[0]
    st.header(f"Your Extimated Price: {int(price)}")