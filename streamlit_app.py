import firebase_admin
from firebase_admin import credentials, db, auth
import streamlit as st


# Initialize Firebase Admin SDK only if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('/workspaces/gdp-dashboard/cloud-project-e22b5-firebase-adminsdk-d4sdc-9fcb9ef892.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://cloud-project-e22b5-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

# Access the database
ref = db.reference('appointments')


# Firebase Authentication
web_api_key = "AIzaSyAFnX93fKXWLyH1sZ4loXu1-we28PrJcs0"
email = "moonnazole@gmail.com"
password = "12345678"

try:
    # Check if the user exists or create a new user
    user = auth.get_user_by_email(email)
    st.write(f"Authenticated as {user.email}")
except auth.UserNotFoundError:
    user = auth.create_user(
        email=email,
        email_verified=False,
        password=password,
        display_name="Moon Nazole",
    )
    st.write(f"New user created: {user.email}")

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
    try:
        ref.push(data)
        st.success("Appointment booked successfully!")
        st.write("### Appointment Receipt")
        st.write(f"*Name:* {name}")
        st.write(f"*Birthdate:* {birthdate}")
        st.write(f"*Phone Number:* {phone}")
        st.write(f"*IC:* {ic}")
        st.write(f"*Clinic:* {clinic}")
        st.write(f"*Date:* {date}")
        st.write(f"*Time:* {time}")
    except Exception as e:
        st.error(f"Failed to save appointment: {e}")
