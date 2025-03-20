from flask import Flask, render_template, request, send_file
import requests
import pandas as pd
import io

app = Flask(__name__)

# PubMed API URLs
PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_papers(query):
    """Fetch research papers from PubMed API"""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10
    }
    headers = {"User-Agent": "Mozilla/5.0"}  

    response = requests.get(PUBMED_SEARCH_URL, params=params, headers=headers).json()
    paper_ids = response.get("esearchresult", {}).get("idlist", [])

    if not paper_ids:
        return []

    # Fetch detailed paper data
    summary_params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    summary_response = requests.get(PUBMED_SUMMARY_URL, params=summary_params, headers=headers).json()

    papers = []
    for paper_id in paper_ids:
        paper_data = summary_response.get("result", {}).get(paper_id, {})
        title = paper_data.get("title", "No Title")
        pub_date = paper_data.get("pubdate", "Unknown")
        source = paper_data.get("source", "Unknown")

        # Extract authors
        authors = paper_data.get("authors", [])
        author_names = [author["name"] for author in authors] if authors else ["Unknown"]
        
        # Extract non-academic authors (assuming they are not university-affiliated)
        non_academic_authors = [author for author in author_names if "University" not in author]

        # Extract company affiliation (if available)
        company_affiliation = paper_data.get("source", "Unknown")

        papers.append({
            "Pubmed ID": paper_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors) if non_academic_authors else "Unknown",
            "Company Affiliation(s)": company_affiliation
        })

    return papers

@app.route("/", methods=["GET", "POST"])
def index():
    papers = []
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            papers = fetch_papers(query)
    return render_template("index.html", papers=papers)

@app.route("/download")
def download_csv():
    """Download research papers as a CSV file"""
    query = request.args.get("query")
    if not query:
        return "No query provided", 400

    papers = fetch_papers(query)
    if not papers:
        return "No data available for download", 404

    df = pd.DataFrame(papers)
    csv_file = io.StringIO()
    df.to_csv(csv_file, index=False)
    csv_file.seek(0)

    return send_file(
        io.BytesIO(csv_file.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="research_papers.csv"
    )

if __name__ == "__main__":
    app.run(debug=True)
