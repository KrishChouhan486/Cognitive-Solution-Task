# 🔍 Research Paper Finder

## 📖 Overview
This is a **Flask-based web application** that allows users to **search for research papers** from **PubMed** and download the results in **CSV format**.  
It has an intuitive UI with a **light/dark mode toggle** for better readability.

## 🚀 Features
- ✅ **Search for Research Papers** using keywords  
- ✅ **Fetch Real-Time Data** from PubMed API  
- ✅ **Display Paper Details** (Title, Date, Authors, Affiliations)  
- ✅ **Clickable PubMed Links** to read full papers  
- ✅ **Download Data as CSV** for offline use  
- ✅ **Dark/Light Mode Toggle** for better UI experience  

---

## 🛠️ Tech Stack
| Component    | Technology Used |
|-------------|----------------|
| **Backend**  | Flask (Python) |
| **Frontend** | HTML, CSS, JavaScript |
| **Data Handling** | PubMed API, Pandas |
| **Deployment** | Flask Local Server / Cloud |

---

## 📂 Folder Structure
📁 Research-Paper-Finder │-- 📄 app.py # Flask backend code │-- 📄 requirements.txt # Dependencies for the project │-- 📁 templates │ │-- 📄 index.html # Frontend UI │-- 📁 static (optional) # Store CSS/JS files if needed │-- 📄 README.md # Project documentation

yaml
Copy
Edit

---


---

## ⚙️ Installation & Setup
### 1️⃣ Install Dependencies  
Make sure you have **Python 3** installed, then run:
```bash
pip install flask pandas requests

---

2️⃣ Run the Application
bash
Copy
Edit
python app.py
It will start the server at http://127.0.0.1:5000/

---

📌 How It Works
1️⃣ Enter a search keyword in the input field
2️⃣ Click the Search button
3️⃣ The app fetches PubMed research papers based on the keyword
4️⃣ It displays Paper Title, Publication Date, Authors, and Company Affiliations
5️⃣ Click on PubMed ID to view the full research paper
6️⃣ Click on Download CSV to export the results

---

🛠️ API Used
The app fetches data from PubMed API: 1️⃣ https://api.ncbi.nlm.nih.gov/lit/ctxp/v1/pubmed/
2️⃣ This API returns research paper metadata including Title, Authors, Date, and Affiliations.

💡 Future Enhancements
🔹 Implement user authentication for saving searches
🔹 Add advanced filters like author, journal, and publication year
🔹 Deploy on Heroku/Vercel for public access
🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit Pull Requests.

📄 License
This project is open-source and available under the MIT License.

shell
Copy
Edit

### ✅ **Now, just copy-paste this into your `README.md` in VS Code!** 🚀#   C o g n i t i v e - S o l u t i o n - T a s k  
 