import streamlit as st
from streamlit.logger import get_logger
import requests

LOGGER = get_logger(__name__)

def send_email_for_analysis(email_body):
    response = requests.post(
        'https://ruchai-ansjhewkia-el.a.run.app/predict',  # Replace with your API endpoint
        json={"email_body": email_body}
    )
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error from API: " + response.text)
        return None

def run():
    st.set_page_config(
        page_title="Email Analysis Tool",
        page_icon="📧",
    )

    st.title("Email Analysis Tool")

    st.sidebar.info("Enter the body of an email and get its analysis.")

    email_body = st.text_area("Enter the body of the email:", height=300)

    if st.button('Analyze Email'):
        if email_body:
            result = send_email_for_analysis(email_body)
            if result:
                st.subheader("Summary:")
                st.write(result.get("summary"))

                predicted_class = result.get("predicted_class")
                if predicted_class == 0:
                    st.markdown("<h2 style='color: red;'>Urgent</h2>", unsafe_allow_html=True)
                elif predicted_class == 1:
                    st.markdown("<h2 style='color: orange;'>Moderate</h2>", unsafe_allow_html=True)
                elif predicted_class == 2:
                    st.markdown("<h2 style='color: green;'>Low</h2>", unsafe_allow_html=True)
        else:
            st.warning("Please enter the email body to analyze.")

    st.markdown(
        """
        **Streamlit App for Email Analysis**  
        This tool analyzes the content of emails and classifies them based on urgency.
        """
    )

if __name__ == "__main__":
    run()
