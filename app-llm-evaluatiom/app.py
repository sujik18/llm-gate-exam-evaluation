import streamlit as st
import subprocess

st.set_page_config(page_title="LLM Evaluation", layout="wide")

st.title("🚀 LLM Evaluation Runner (MLCFlow)")

st.markdown("Run the `process.py` script directly in this Space using the MLCFlow framework.")

if st.button("Run process.py"):
    st.info("Running evaluation... please wait ⏳")
    try:
        result = subprocess.run(["python3", "process.py"], capture_output=True, text=True)
        st.success("Process completed!")
        st.subheader("Output Log")
        st.code(result.stdout)
        if result.stderr:
            st.subheader("Errors / Warnings")
            st.code(result.stderr)
    except Exception as e:
        st.error(f"Failed to run process.py: {e}")
