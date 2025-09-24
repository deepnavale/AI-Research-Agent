import streamlit as st
from agent import run_agent
from db import init_db, save_report, get_all_reports


init_db()


st.set_page_config(
    page_title="AI Research Agent ",
    page_icon="",
    layout="wide"
)

st.title("AI Research Agent ")
st.markdown("Enter a query to find sources, summarize them, and create a structured report.")


if 'current_report' not in st.session_state:
    st.session_state.current_report = ""

with st.form("research_form"):
    query = st.text_input("Enter your research query:", placeholder="e.g., Impact of Mediterranean diet on heart health")
    submit_button = st.form_submit_button("Generate Report")

if submit_button and query:
    with st.spinner("Finding sources and generating report... Please wait."):
        try:
            report = run_agent(query)
            st.session_state.current_report = report
            save_report(query, report)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.session_state.current_report = ""

if st.session_state.current_report:
    st.subheader("Generated Report")
    st.markdown(st.session_state.current_report)


st.sidebar.title(" Report History")
all_reports = get_all_reports()

if not all_reports:
    st.sidebar.info("No reports have been generated yet.")
else:
    for report_data in all_reports:
        report_id, saved_query, saved_report, timestamp = report_data
        with st.sidebar.expander(f"**{saved_query}** - {timestamp[:10]}"):
            st.markdown(saved_report)