### **Multi-Factor Authentication (MFA) System**

This project showcases a **Multi-Factor Authentication (MFA)** system implemented with **Streamlit** and **PyOTP**. It provides a user-friendly interface for secure login and simulates a basic customer banking system with features like account summaries, quick actions, and logout functionality. The system is designed to demonstrate how MFA enhances security by combining password authentication with one-time password (OTP) verification.

---

### **Features**
1. **Login**:
   - Users enter their email and password to authenticate.
   - Credentials are encrypted using **DES encryption** for demonstration purposes.
   - Includes input validation to ensure email and password formats meet security standards.

2. **OTP Verification**:
   - After a successful login, an OTP is generated and displayed.
   - OTP adds an additional security layer, ensuring that only authorized users gain access.
   - Verifies OTP with a validity window for flexibility.

3. **Banking Features**:
   - Placeholder options for:
     - Viewing account balances and summaries.
     - Transferring funds.
     - Paying bills.
     - Viewing account statements.

4. **Logout**:
   - Users can log out securely and return to the login page.

5. **Test Credentials**:
   - Ready-to-use test credentials are provided to explore the system:
     - **Email**: `Test_User@gmail.com`
     - **Password**: `Test1234`

---

### **How It Works**
1. **Login Page**:
   - Navigate to the login page.
   - Enter a valid email and password.
   - The application validates inputs and checks encrypted credentials against the database.

2. **OTP Page**:
   - After login, an OTP is generated for the authenticated user.
   - Enter the OTP in the verification input field to complete the login process.

3. **Main Page**:
   - Upon successful OTP verification, access the main page to view:
     - Account balances.
     - Placeholder actions for transferring funds, paying bills, and viewing statements.

4. **Logout**:
   - Securely log out and return to the login page for another session.

---

### **Run the Application**
To run the app locally, follow these steps:
1. Clone the repository containing the code.
2. Install required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the application by running:
   ```bash
   streamlit run simple_login.py
   ```
4. Open the application in your browser using the URL provided by Streamlit.

---
