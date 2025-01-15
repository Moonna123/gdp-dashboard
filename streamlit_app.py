import firebase_admin
from firebase_admin import credentials, db
import streamlit as st
import json

# Initialize Firebase only if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('/workspaces/cloud-health-form/firebase_credentials.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://<your-firebase-project-id>.firebaseio.com'
    })

# Firebase Realtime Database initialization
ref = db.reference('appointments')

# Create the Streamlit form
st.title("Health Appointment Booking")

with st.form("appointment_form"):
    name = st.text_input("Name")
    birthdate = st.date_input("Birthdate")
    phone = st.text_input("Phone Number")
    ic = st.text_input("IC")
    clinic = st.selectbox("Clinic", ["Clinic A", "Clinic B", "Clinic C"])
    date = st.date_input("Appointment Date")
    time = st.time_input("Appointment Time")
    
    submitted = st.form_submit_button("Submit")

if submitted:
    # Data to send to Firebase Realtime Database
    data = {
        "name": name,
        "birthdate": str(birthdate),
        "phone": phone,
        "ic": ic,
        "clinic": clinic,
        "date": str(date),
        "time": str(time)
    }
    
    # Store the data in Firebase Realtime Database
    ref.push(data)

    st.success("Appointment booked successfully!")
    st.write("### Appointment Receipt")
    st.write(f"**Name:** {name}")
    st.write(f"**Birthdate:** {birthdate}")
    st.write(f"**Phone Number:** {phone}")
    st.write(f"**IC:** {ic}")
    st.write(f"**Clinic:** {clinic}")
    st.write(f"**Date:** {date}")
    st.write(f"**Time:** {time}")
