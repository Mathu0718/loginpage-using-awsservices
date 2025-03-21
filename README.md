# AWS-Based Smart Attendance System

## 📌 Project Overview
The **AWS-Based Smart Attendance System** allows users to **log in and log out** using their email addresses. Each action is recorded in an AWS **DynamoDB** table, ensuring accurate attendance tracking. The system leverages **AWS Lambda** and **API Gateway** to handle user authentication requests.

---

## 🎯 Features
✅ User login/logout tracking with timestamps  
✅ Data storage in **AWS DynamoDB**  
✅ Serverless architecture using **AWS Lambda**  
✅ Secure API access via **AWS API Gateway**  
✅ CORS-enabled for frontend integration  

---

## 🏗️ Project Structure
```
├── frontend/           # Frontend files (HTML, CSS, JavaScript)
│   ├── index.html     # Login UI
│   ├── style.css      # Styling for UI
│   ├── script.js      # API requests to Lambda
│
├── backend/           # Backend AWS Lambda function
│   ├── lambda_function.py  # Python script for handling login/logout
│
└── README.md          # Project documentation
```

---

## 🚀 AWS Services Used
- **AWS Lambda** → Processes login/logout requests
- **Amazon DynamoDB** → Stores user attendance records
- **Amazon API Gateway** → Exposes Lambda as a REST API
- **AWS IAM** → Manages permissions and security

---

## 📌 How It Works
1️⃣ **User enters email and logs in**  
2️⃣ **AWS Lambda** receives the request and updates **DynamoDB** with status "logged_in"  
3️⃣ **User logs out** → Lambda updates the **same record** in DynamoDB to "logged_out"  
4️⃣ **Frontend fetches and displays messages** based on API responses  

---

## ⚙️ Deployment Guide
### **Step 1: Set Up DynamoDB Table**
1. Go to **AWS Console → DynamoDB**
2. Create a table named **AttendanceRecords**
3. Set **Primary Key** as `email` (String)

### **Step 2: Deploy AWS Lambda Function**
1. Open **AWS Lambda**
2. Create a new function **(Python 3.x runtime)**
3. Upload `lambda_function.py`
4. Attach a **DynamoDB Full Access** IAM Role
5. Deploy & copy the function ARN

### **Step 3: Create API Gateway**
1. Navigate to **API Gateway**
2. Create a new **HTTP API**
3. Connect it to the **Lambda function**
4. Enable **CORS**
5. Deploy and copy the **API endpoint URL**

### **Step 4: Configure Frontend**
1. Update `script.js` with your **API Gateway URL**
2. Open `index.html` in a browser
3. Enter email → Click Login/Logout

---

## 🖥️ Usage
### **Login Request**
```json
{
  "action": "login",
  "email": "user@example.com"
}
```

### **Logout Request**
```json
{
  "action": "logout",
  "email": "user@example.com"
}
```

---

## 📌 Future Enhancements
🔹 **User authentication via AWS Cognito**  
🔹 **Detailed attendance dashboard**  
🔹 **Face recognition-based login (AWS Rekognition)**  

---

## 🛠️ Troubleshooting
**500 Internal Server Error?**  
🔹 Ensure **DynamoDB Table** exists with the correct name  
🔹 Check **Lambda permissions** (DynamoDB access)  
🔹 Verify **API Gateway URL** in `script.js`  

---

## 📜 License
This project is **open-source**. Feel free to modify and improve it! 🚀