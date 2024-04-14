import streamlit as st
import google.generativeai as genai

# Configure Gemini with API key
genai.configure(api_key="AIzaSyBy0nEMHwDwImc0ySdDRIZfVVGkuzzgX9E")

def generate_business_names(input_text):
    # Prompt for Gemini model
    prompt =  f"""
        You are a creative consultant specializing in branding and marketing. 
        Your task is to generate unique and catchy business names based on the provided business details:"{input_text}".
        Aim to capture the essence and appeal of the business in the generated names. 
        Please ensure that the names are suitable for branding and easily memorable by potential customers.
        """

    # Use Gemini to generate business names
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit App
st.set_page_config(page_title="Business Name Generator 🕴" )

st.header("Business Name Generator")

# User input for business details
business_details = st.text_input("Enter details about your business:")

generate_names = st.button("Generate Business Names")

if generate_names:
    if business_details:
        try:
            st.info("Generating business names...")
            business_names = generate_business_names(business_details)
            st.subheader("Creative Business Names:")
            st.write(business_names)
        except Exception as e:
            st.error("An error occurred while generating business names. Please try again later.")
    else:
        st.warning("Please enter details about your business.")
