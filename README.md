# AI Research Agent

This project is a take-home assignment to build an AI agent that automates the research process. It takes a user query, finds relevant online sources, extracts their content, generates a structured summary report using an LLM, and saves the results in a local database for future reference.

## Architecture

The agent is built with a simple, modular architecture:

* **`app.py`**: The web interface, built with **Streamlit**. It handles user input and displays current and past reports.
* **`agent.py`**: The core logic, orchestrated by **LangChain**. It uses the Tavily API for web searches, `trafilatura` and `pypdf` for content extraction, and a local **Ollama Llama 3** model for report generation.
* **`db.py`**: A simple database handler for the **SQLite** database, which stores all generated reports.



## How to Run the Project

Follow these steps to get the application running locally:

1.  **Clone the Repository**
    ```bash
    git clone <your-repo-url>
    cd research_agent
    ```

2.  **Install Dependencies**
    Make sure you have Python 3.8+ installed.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up Environment Variables**
    Create a `.env` file in the root directory and add your Tavily API key:
    ```
    TAVILY_API_KEY="your_tavily_api_key_here"
    ```

4.  **Run Ollama**
    Ensure the Ollama desktop application is running and you have downloaded the Llama 3 model:
    ```bash
    ollama run llama3
    ```

5.  **Start the Application**
    Run the Streamlit app from your terminal:
    ```bash
    streamlit run app.py
    ```
    The application will open in your web browser.

## Example Results

**Query:**
`Latest research on AI in education`

**Sample Report:**

> ### Summary of Findings
>
> Recent research on AI in education focuses on its potential to create personalized learning paths, automate administrative tasks for teachers, and provide intelligent tutoring systems. Key applications include adaptive learning platforms that adjust difficulty based on student performance and AI tools that offer instant feedback on assignments. However, challenges related to data privacy, algorithmic bias, and the need for proper teacher training remain significant concerns.
>
> ### Key Points
>
> * **Personalized Learning:** AI algorithms can analyze student data to customize educational content and pacing.
> * **Administrative Automation:** AI can handle tasks like grading, scheduling, and student monitoring, freeing up teacher time.
> * **Intelligent Tutoring:** AI-powered systems offer one-on-one support and practice for students at any time.
> * **Ethical Concerns:** The use of AI raises important issues regarding student data privacy and the potential for bias in AI models.
>
> ### Sources
>
> * https://example-source-1.com/ai-in-education
> * https://example-source-2.org/research-paper
> * https://example-source-3.edu/future-of-learning

## Use of AI Help

AI assistance (ChatGPT-4/Gemini) was used for:
* Generating boilerplate code for the Streamlit interface and SQLite functions.
* Refining the LLM prompt for optimal report structure.
* Debugging minor integration issues between libraries.

The core agent logic, tool integration, and error handling were designed and implemented manually.
