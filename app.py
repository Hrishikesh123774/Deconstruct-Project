import pandas as pd
import google.generativeai as genai
import streamlit as st
import time

# --- 1. SETUP GEMINI API ---
GEMINI_API_KEY = "YOUR_API_KEY_HERE" 
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. STREAMLIT DASHBOARD CONFIG ---
st.set_page_config(page_title="Market Intelligence Pipeline", layout="wide")
st.title("🚀 GenAI Market Intelligence Dashboard")
st.write("Automated analysis of unstructured competitor data.")

# --- 3. DATA INGESTION & CLEANING (PANDAS) ---
@st.cache_data 
def load_and_clean_data():
    df = pd.read_csv("data.csv")
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df

df = load_and_clean_data()

st.subheader("Raw Data Feed (Cleaned)")
st.dataframe(df)

# --- 4. THE AI PROCESSING PIPELINE ---
def analyze_text_with_llm(text_data):
    prompt = f"""
    You are a strategic business analyst working in the Founder's Office. 
    Review the following raw customer feedback regarding a competitor's product.
    
    Extract the following insights:
    1. Overall Sentiment (Positive/Negative/Mixed)
    2. Top 2 Strengths of the product
    3. Top 2 Weaknesses or Operational Bottlenecks
    4. One strategic recommendation on how we can capitalize on their weaknesses.
    
    Format the output clearly with bullet points.
    
    Raw Data:
    {text_data}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error connecting to AI: {e}"

# --- 5. DASHBOARD INTERACTION ---
st.markdown("---")
st.subheader("🧠 Run AI Analysis")

if st.button("Generate Executive Insights"):
    with st.spinner("AI is analyzing the data..."):
        combined_text = " | ".join(df['Review_Text'].tolist())
        insights = analyze_text_with_llm(combined_text)
        
        st.success("Analysis Complete!")
        st.markdown("### Executive Summary")
        st.info(insights)
