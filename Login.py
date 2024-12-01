import streamlit as st
import pyotp #used to generate random OTP 
import time

# Simulated user database
users = {
    "Test_User@gmail.com": {"password": "Test1234", "otp_secret": pyotp.random_base32()},
    "Abdullah_Example@gmail.com": {"password": "SWE314_Abood", "otp_secret": pyotp.random_base32()},
    "Baseel_Example@gmail.com": {"password": "SWE314_Baseel", "otp_secret": pyotp.random_base32()},
    "Meshal_Example@gmail.com": {"password": "SWE314_Meshal", "otp_secret": pyotp.random_base32()},
}

# Initialize session state for navigation and storing current user
if "page" not in st.session_state:
    st.session_state.page = "login"  # Default to login page
if "current_user" not in st.session_state:
    st.session_state.current_user = None  # No user logged in by default
if "otp_secret" not in st.session_state:
    st.session_state.otp_secret = None  # To store OTP secret in session state


#========================================>Login Page<======================================
def login_page():
    # st.title("MFA Authentication - Login")
    st.markdown("<h1 style='text-align: center; color:light grey;'>MFA Authentication - Login</h1>", unsafe_allow_html=True)

    # Display test credentials
    st.markdown("<h3 style='color: #4B4B4B;'>Test Login Credentials</h6>", unsafe_allow_html=True)
    # st.write("Email: **Test_User@gmail.com**")
    st.markdown("<p style='color: #555555;'>Email: Test_User@gmail.com</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: #555555;'>Password: Test1234</p>", unsafe_allow_html=True)
  
    st.divider()

    # Input fields
    email = st.text_input("Email").strip()
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = users.get(email)
        if user and user["password"] == password:
            otp = pyotp.TOTP(user["otp_secret"]).now()  # Generate OTP
            st.session_state.current_user = email  # Save the logged-in user
            st.session_state.otp_secret = user["otp_secret"]  # Store OTP secret in session state

            st.success("OTP sent")  
            st.toast(f"OTP: {otp}")
            time.sleep(4)
            st.session_state.page = "otp"  # Go to OTP page
            st.rerun()  # rerun to display OTP page
        else:
            st.error("Invalid credentials")


#========================================>OTP Page<======================================
def otp_page():
    st.markdown("<h1 style='text-align: center; color: light grey;'>MFA Authentication - OTP Verification</h1>", unsafe_allow_html=True)
    st.divider()
    # Ensure the user is logged in
    if not st.session_state.current_user:
        st.warning("Please log in first!")
        st.session_state.page = "login"
        st.rerun()

    # OTP verification
    otp = st.text_input("Enter OTP")
    if st.button("Verify OTP"):
        user = users.get(st.session_state.current_user)  # Get current user
        if user and pyotp.TOTP(st.session_state.otp_secret).verify(otp, valid_window=1):  # Verify OTP
            st.success("Login successful!")
            time.sleep(2.5)
            st.session_state.page = "main"  # Reset page to login
            st.session_state.current_user = None  # Clear user session
            st.session_state.otp_secret = None  # Clear OTP secret
            st.rerun()  # Trigger rerun to reset the app state
        else:
            st.error("Invalid OTP")

    # Option to go back
    if st.button("Go Back"):
        st.session_state.page = "login"
        st.rerun()
#========================================>Main Page<======================================
def main_page():

    st.markdown("<h1 style='text-align: center; color: light grey;'>Customer Banking System</h1>", unsafe_allow_html=True)
    st.divider()

    st.subheader("Account Summary") # Simple Account Summary
    st.write("**Account Balance:** $12,345.67")
    st.write("**Savings Balance:** $8,210.45")

    # Simple Quick Actions
    st.subheader("Quick Actions")
    col1, col2, col3 = st.columns(3) #split the features into 3 columns
    with col1:
        if st.button("Transfer Funds",use_container_width=True):
            st.toast("Transfer Fund feature coming soon!")
    with col2:
        if st.button("Pay Bills",use_container_width=True):
            st.toast("Bill payment feature coming soon!")
    with col3:
        if st.button("View Statements",use_container_width=True):
            st.toast("View Statement view feeature coming soon!")


    
    st.divider()
    if st.button("Log Out",use_container_width=True): # Logout Button
        st.session_state.page = "login"
        st.rerun()
        


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Navigation between pages~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "otp":
    otp_page()
elif st.session_state.page == "main":
    main_page()