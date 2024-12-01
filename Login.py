import streamlit as st
import pyotp

# Simulated user database
users = {"Abdullah_Example@gmail.com": {"password": "SWE314_Abood", "otp_secret": pyotp.random_base32()},
         "Baseel_Example@gmail.com": {"password": "SWE314_Abood", "otp_secret": pyotp.random_base32()},
         "Meshal_Example@gmail.com": {"password": "SWE314_Meshal", "otp_secret": pyotp.random_base32()}, 

         }
st.title("Login System with OTP")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = users.get(email)
    if user and user["password"] == password:
        otp = pyotp.TOTP(user["otp_secret"]).now()
        st.success(f"OTP sent: {otp}")
    else:
        st.error("Invalid credentials")

otp = st.text_input("Enter OTP")
if st.button("Verify OTP"):
    user = users.get(email)
    if user and pyotp.TOTP(user["otp_secret"]).verify(otp):
        st.success("Login successful!")
    else:
        st.error("Invalid OTP")


