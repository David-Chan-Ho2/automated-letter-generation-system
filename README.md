# Automated letter generation system

Automate creating letters for clients using Python.

---

## 📖 Description
This program was developed for a non-profit organization that sends letters and other documentation to government agencies on behalf of their clients.

Previously, the process involved manually typing the client’s name and identification number from an Excel file. Since the documents were nearly identical, the process was a perfect candidate for automation.

The program automates the workflow by:
1. Pulling client information from a database  
2. Generating a new letter using a template  
3. Replacing the client’s name and ID in the letter  
4. Merging all the files into a single document for printing  

---

## 🛠️ Libraries Used
- **Pandas** – Work with CSV files (used to pull data from Excel and seed the database)  
- **sqlite3** – Manage the local database storing client information  
- **datetime** – Handle date and time formatting in documents  
- **docx** – Create and edit Word documents  
- **docxtpl** – Simplify document templating by merging data into predefined Word templates  
