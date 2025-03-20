# 🔍 Research Paper Finder  

## 📖 Overview  
**Research Paper Finder** is a **Flask-based web application** that allows users to search for **research papers** from **PubMed** and download results as a **CSV file**.  
It provides a simple, user-friendly **interface with a Light/Dark Mode Toggle** for an improved reading experience.  

---

## 🚀 Features  
✅ **Real-time Research Paper Search** using PubMed API  
✅ **Fetch Research Papers** with Title, Date, Authors & Affiliations  
✅ **Clickable PubMed Links** to read full research papers  
✅ **Download Search Results as CSV** for offline use  
✅ **Dark/Light Mode Toggle** for better UI experience  
✅ **Mobile Responsive Design** 📱  

---

## 🛠️ Tech Stack  
| Component     | Technology Used |
|--------------|----------------|
| **Backend**  | Flask (Python)  |
| **Frontend** | HTML, CSS, JavaScript |
| **Data Handling** | PubMed API, Pandas |
| **Deployment** | Flask Local Server / Cloud |

---

📂 Research-Paper-Finder  
│-- 📄 app.py              # Flask backend code  
│-- 📄 requirements.txt    # Dependencies for the project  
│-- 📂 templates  
│   │-- 📄 index.html      # Frontend UI  
│-- 📂 static (optional)   # Store CSS/JS files if needed  
│-- 📄 README.md           # Project documentation  

---


---

## ⚙️ Installation & Setup  

### 1️⃣ Install Dependencies  
Ensure **Python 3** is installed, then run:  
```bash
pip install flask pandas requests
```
---

### 2️⃣ Run the Application
```bash
python app.py
```

🔗 The server will start at:
```bash 
http://127.0.0.1:5000/
```

---

### 🔬 How It Works  
1️⃣ **Enter a search keyword** in the input field  
2️⃣ **Click the "Search" button** to fetch research papers  
3️⃣ **The app retrieves** Title, Publication Date, Authors, and Affiliations  
4️⃣ **Click on PubMed ID** to read the full research paper  
5️⃣ **Click on "Download CSV"** to save the search results  

---


### 🌐 API Used
The app fetches research paper data from PubMed API:
```bash
🔗 https://api.ncbi.nlm.nih.gov/lit/ctxp/v1/pubmed/
```
This API returns metadata including Title, Authors, Date, and Affiliations.

---

### 💡 Future Enhancements  
🚀 **Implement user authentication** to save searches  
🚀 **Add advanced filters** (Author, Journal, Year)  
🚀 **Deploy on Heroku/Vercel** for public access  
🚀 **Improve UI** with better animations & styling  

---

### 🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit a Pull Request. 💡

---

### 📄 License
This project is open-source and available under the MIT License.

---







