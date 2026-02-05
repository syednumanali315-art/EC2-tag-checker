 # EC2 Tag Compliance Checker 🚀

## 📌 Project Overview
This project automatically checks AWS EC2 instances for required tags using AWS Lambda.
If any EC2 instance is missing mandatory tags, an email alert is sent using Amazon SNS.

This helps improve cost tracking, governance, and resource management.

---

## 🛠️ AWS Services Used
- Amazon EC2
- AWS Lambda
- Amazon SNS
- Amazon EventBridge (CloudWatch Events)
- IAM

---

## 🏷️ Mandatory Tags Checked
- Name
- Environment
- Owner

---

## ⚙️ Architecture
EventBridge triggers the Lambda function on a schedule.  
Lambda scans EC2 instances for missing tags.  
SNS sends an email alert if any instance is non-compliant.
