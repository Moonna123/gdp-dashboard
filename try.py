import firebase_admin
from firebase_admin import credentials, db, auth
import streamlit as st

# Firebase service account credentials
firebase_credentials = {
    "type": "service_account",
    "project_id": "cloud-project-e22b5",
    "private_key_id": "1a474193e3ab2f3aa5054a8d7b661c8ab4876547",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCx0VSVra/fo4tG\n2jGT2Y4NUtxuJLEv2YiT+QhPd1iV28gh+fB27AtpfkI73wRqeYrndGB83g2wBRxz\nocPM+ERojGJVvS0utEbQFYjqcmlRAu93paJ/NMQ//i4y8wgihftZgmnvwMJoQZjN\ntJeMx3hKjbv+VIHF5BGGH0cDaeE1SuG1xNVZ7kDHI3QAA7afVkNjQaOjFd7VCd+e\n1OZi8Y6o7F/6EHnhKA3ruJkc7wbxJrT2dpEWbdDYA7rYJJEP1Tq7Ln3UQhOvKw8D\nfeQZ/2ajggJ+paR18Y+gggcGN52W4TcGRVhbxeADsvkwcTE3/zqCb/k8ZfIM32TB\nqmwRPzKnAgMBAAECggEACPWJE3mK0PPGgq1frhlaBOXV4V7L5qNJNFtpxcc3mWVX\ncg7LxNIjyQ7pe2bDLDIvg3Xjnqb5fZLkWhcebGdd2v6nvbYoXqAKqVVMbrORBtnl\nAtw/kbUw5iCCZ2LDWCnz/hCKEeBeay5S6ppcwGUUdH0rqabMWxIgp+dPhqaBCFRF\n17QXZSTB6ctzY4fqSpCNVEL5XKu246iJAT7opJ5D+cIGTngOiDWWyuyKZO7nJoK/\nByUIiAMORZ6at5YEm8/h6OzRhkQ7tmkA9zmQgAup4m43ZCllgryEHMQQ8vloZYDZ\n5xG74liA2gOE4bUrHaFFNfXUA1LJL7ek+jIip7YMoQKBgQDzP8CUazRvaxPQ/Y9G\nVr5qwkn05ICZumUUwzu4zid4xIu2OPk6xwVt/2rJwwEf2UHpzKcCeBVgprG4//xK\noxA68pAq5rMZiNqYOcWKBTk8HOeMJUPMSWclW3roSj3iX8HRCOy7r0Yo4FdO9pqT\n6LJufFvz8e1EfETfbz8VGtWhrwKBgQC7I4f3pk1ZxHbQNdU1UxJZktVxreiR5/wJ\n1AHZu1QKaoCZlwrDp9k0baxyquyALjri5UVFWa/eYt7trBBhkrh2B6ufwJxQT9Bv\nU9XViYUMIJFT5aXwqauIGKriBq+B7a8HGb/2IscapRzMFqLqnx/rj2DuaH2ZrbCj\n4XN95NYUiQKBgQC4/6yEdIA9mM9Ka/1yfnh1k2xR3xNbV2KXBuC97bQhakHjhbMv\nG7wqa04ZQsDxKvexS99cxl1j04No8u87CIdIfcBdkHV4Hxg5G/77uHtOF6GWeaT1\nkoHq7IcucYBdUXyDcWkyWNxgLDbarDzl7tz9oIECp+VO58AtulrcvzroqwKBgHd7\nOQ2KFWrSABXxuP4B2v5rvHGHWq0Fk6rmvIO6ke7QjukBQbMoEIrj1y2jKbqxSZGi\nVnbvy1TOhYzzxcW2eqWJQi+ON38jZm4d9bIPym2ywXbycd9VRRpwvXHwWNA44/5B\nl4lcLQk7EEbR0RTBogyxD29IMaET/2qywB1KJNEZAoGBAKTft+OcBeEUUFGk1XKQ\nU2e98/3mR6LEVjz7w+i9pgglk7D4+OaSvbcNuNhwz8o0TtKRo2Kwv6O5T264o8wj\nifrmLioG/SmG6iFvNwo89LtmJ8KG1B8zKAnm/Lf1Of+5jTR4E27J0Qb00P4smwzD\ngqh0o8y0X9wwv10lQRyboNPu\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-d4sdc@cloud-project-e22b5.iam.gserviceaccount.com",
    "client_id": "110215200426610128996",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-d4sdc%40cloud-project-e22b5.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Initialize Firebase Admin SDK only if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_credentials)
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
