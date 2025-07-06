import streamlit as st
import pickle

# Load the saved model using pickle
with open('final_model.pickle', 'rb') as f:
    model_loaded = pickle.load(f)

# Define the layout of your app
st.write("# Estimate your salary")

# Add input widgets for user input
jobt = st.radio(
     "Select the Job Title:",
     ('Data Analyst', 'Product Manager', 'Software Engineer'))

if jobt == 'Data Analyst':
    jobt = 0
elif jobt == 'Product Manager':
    jobt = 1
else:
    jobt = 2

loc = st.radio(
     "Select the Location:",
     ('Banglore', 'Mumbai', 'New Delhi'))

if loc == 'Banglore':
    loc = 0
elif loc == 'Mumbai':
    loc = 1
else:
    loc = 2

ctype = st.radio(
     "Select the Company Type:",
     ('Private', 'Public'))

if ctype == 'Private':
    ctype = 0
else:
    ctype = 1

rating = st.text_input("Enter the company rating:")

mean_rating = 3.9253456221198153
std_rating = 0.32371762457856657

mean_salary = 574787.0357142857
std_salary = 271989.2886259066

if len(rating)!=0:
    rating = float(rating)
    rating = (rating - mean_rating)/std_rating

# st.write("Rating as a float:", rating)


# Define the model prediction function
def predict(jobt,loc,rating,ctype):
    # Your prediction code goes here
    return model_loaded.predict([[jobt,loc,rating,ctype]])

# Add a button to trigger the prediction
if st.button("Predict"):
    result = predict(jobt,loc,rating,ctype)
    st.write("Estimated salary per Annum (in INR):", int(result*std_salary+mean_salary))
