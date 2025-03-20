## **📄 PDF Utility Tool**
### **🔹 Overview**
This web-based PDF tool allows you to **merge, compress, and secure PDF files** . It’s completely **free** and runs on your web browser—no installation required.

### **💡 Features**
✔ **Merge PDFs** – Combine multiple PDFs into one.  
✔ **Compress PDFs** – Reduce the file size of scanned PDFs.  
✔ **Encrypt PDFs (User Password)** – Add a password to protect your PDF.   
✔ **No Need for Adobe Acrobat** – Works entirely online.  

### **🌟 Who Is This For?**
- **Individuals & Businesses** who need a **free** and **easy** way to edit PDFs.  
- **Students & Professionals** managing reports, research papers, or scanned documents.  
- **Anyone without access to Adobe Acrobat** but needing to modify PDFs.  

---

## **🚀 How to Use the App**
1️⃣ **Go to the [App URL](https://pdfmate.streamlit.app/)** (or run it locally).  
2️⃣ **Choose a tool from the sidebar**:
   - Merge PDFs
   - Compress PDFs
   - Encrypt PDFs  
3️⃣ **Upload your PDF(s)** and adjust settings.  
4️⃣ **Download your processed file** instantly! 🎉  

---

## **🛠️ Running Locally**
### **🔹 Install Requirements**
1. Install Python (if not installed): [Download Python](https://www.python.org/downloads/)  
2. Install dependencies:
   ```bash
   pip install streamlit pypdf pdf2image img2pdf pillow
   ```
3. If using **Linux or Streamlit Cloud**, install:
   ```bash
   sudo apt-get update
   sudo apt-get install -y libgl1-mesa-glx poppler-utils
   ```

### **🔹 Run the App**
```bash
streamlit run app.py
```
Then, open the link in your browser.

---

## **🔐 Security & Privacy**
✔ **No files are stored** – All processing is done in memory.  
✔ **Secure encryption** – Password-protected files are encrypted using `pypdf`.  
✔ **Open-source** – You can review and modify the code!  

---

## **📌 Additional Notes**
- The app supports **all major PDF formats**.
- If your **scanned PDFs appear rotated**, try rotating them before merging.
- **Large files may take time** to process, especially in the compression tool.

---

## **📝 License**
This project is open-source under the **MIT License**.

---

### **📬 Need Help?**
If you experience any issues or have feature suggestions, feel free to reach out! 🚀

---
