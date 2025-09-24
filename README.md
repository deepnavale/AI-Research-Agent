# AI Research Agent

AI Research Agent is a tool that helps users generate structured research reports. It searches the web, extracts content from webpages and PDFs, and creates reports with summaries, key points, and source links. All reports are stored in a local SQLite database for future access.

## Features

* Searches the web using Tavily API
* Extracts text from webpages and PDFs
* Generates structured reports using Ollama's LLaMA model
* Reports include summary, key points, and sources
* Saves reports in a local SQLite database
* Provides a Streamlit interface for easy use

## Project Structure

```
AI-Research-Agent/
│── agent.py          # Core logic for search, extraction, and report generation
│── app.py            # Streamlit frontend
│── db.py             # Database functions (init, save, fetch reports)
│── requirements.txt  # Dependencies
│── .env              # Environment variables (API keys)
│── research_reports.db (created automatically)
```

## Setup Instructions

1. Clone the repository:

```bash
git clone <repo-url>
cd AI-Research-Agent
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add environment variables in a `.env` file:

```env
TAVILY_API_KEY=your_api_key_here
```

Make sure Ollama is installed and running locally with the `llama3.1` model.

5. Run the Streamlit app:

```bash
streamlit run app.py
```

## Example Usage

Enter a query in the app input box. The agent will search online, extract content, and generate a structured report.

### Example 1

**Query:**

```
How to learn Generative AI
```

**Generated Report:**

```
Summary of Findings
The report provides an overview of resources available to learn Generative AI from Coursera, DeepLearning.AI, and Google Cloud. It shows that there are introductory to advanced courses and highlights the importance of GenAI skills for career growth.

Key Points or Takeaways
- Coursera offers courses such as "Generative AI: Introduction and Applications".
- DeepLearning.AI provides "Generative AI for Everyone".
- Google Cloud offers training programs and certifications.
- GenAI skills are in high demand and valuable for professional success.

Source URLs
https://www.coursera.org/courses?query=generative%20ai
https://www.deeplearning.ai/courses/generative-ai-for-everyone/
https://ai.google/learn-ai-skills
```

### Example 2

**Query:**

```
Impact of Mediterranean diet on heart health
```

**Generated Report:**

```
Summary of Findings
The report shows that the Mediterranean diet is strongly linked to improved heart health. It emphasizes the role of fruits, vegetables, whole grains, fish, and olive oil in reducing cardiovascular risk.

Key Points or Takeaways
- Studies indicate lower risk of heart disease with a Mediterranean diet.
- High intake of olive oil and nuts contributes to improved cholesterol levels.
- Diet reduces inflammation and supports healthy blood pressure.
- Considered one of the most heart-friendly dietary patterns worldwide.

Source URLs
https://www.health.harvard.edu/blog/mediterranean-diet-2019021516012
https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/fats/mediterranean-diet
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6566796/
```

## Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit
requests
beautifulsoup4
PyPDF2
sqlite3
python-dotenv
tavily-python
```


