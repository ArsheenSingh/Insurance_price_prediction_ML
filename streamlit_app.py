import streamlit as st
import pandas as pd
from schema.user_input import user_input
from model.predict import predict_output

# --- Page Configuration ---
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    h1 { font-family: 'Georgia', serif; text-align: center; }
    h2 { font-family: 'Georgia', serif; }
    .stButton>button {
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        width: 100%;
    }
    .result-box {
        background-color: #e0f2fe;
        border-left: 6px solid #2563eb;
        color: #0c4a6e;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }
    .result-box h3 { margin: 0; font-size: 24px; font-weight: bold; }
    .result-box p { margin: 5px 0 0 0; font-size: 18px; }
    .footer { text-align: center; margin-top: 2rem; font-size: 0.9rem; color: #888; }
</style>
""", unsafe_allow_html=True)


# --- App Layout ---
st.title("🛡️ Insurance Premium Predictor")
st.markdown("<p style='text-align: center; color: grey;'>Enter your details below to get an estimated insurance premium category.</p>", unsafe_allow_html=True)

# --- Sidebar for User Inputs ---
with st.sidebar:
    st.header("👤 User Details")
    age = st.slider("Age", 18, 120, 30)
    col1, col2 = st.columns(2)
    with col1: weight = st.number_input("Weight (kg)", 1.0, 150.0, 70.0, 0.1)
    with col2: height = st.number_input("Height (m)", 0.1, 2.5, 1.75, 0.01)
    income_lpa = st.number_input("Annual Income (LPA)", 0.1, 100.0, 10.0, 0.1)
    smoker = st.radio("Are you a smoker?", ("Yes", "No"), index=1)
    # The city list is now correctly sourced from your user_input schema logic
    city = st.selectbox("City", ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Jaipur', 'Chandigarh', 'Indore', 'Lucknow', 'Patna', 'Ranchi', 'Visakhapatnam', 'Coimbatore', 'Bhopal', 'Nagpur', 'Vadodara', 'Surat', 'Rajkot', 'Jodhpur', 'Raipur', 'Amritsar', 'Varanasi', 'Agra', 'Dehradun', 'Mysore', 'Jabalpur', 'Guwahati', 'Thiruvananthapuram', 'Ludhiana', 'Nashik', 'Allahabad', 'Udaipur', 'Aurangabad', 'Hubli', 'Belgaum', 'Salem', 'Vijayawada', 'Tiruchirappalli', 'Bhavnagar', 'Gwalior', 'Dhanbad', 'Bareilly', 'Aligarh', 'Gaya', 'Kozhikode', 'Warangal', 'Kolhapur', 'Bilaspur', 'Jalandhar', 'Noida', 'Guntur', 'Asansol', 'Siliguri', 'Other'])
    occupation = st.selectbox("Occupation", ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])
    predict_button = st.button("Predict Premium Category")

# --- Main Area for Output ---
if predict_button:
    try:
        # 1. Create an instance of your Pydantic model with data from the UI
        user_data = user_input(
            age=age,
            weight=weight,
            height=height,
            income_lpa=income_lpa,
            smoker=(smoker == "Yes"),
            city=city,
            occupation=occupation
        )

        # 2. Use the computed properties from the Pydantic model to create the input dictionary
        input_data_for_model = {
            'bmi': user_data.bmi,
            'age_group': user_data.age_group.lower(), # Ensure lowercase for model compatibility
            'lifestyle_risk': user_data.lifestyle_risk,
            'city_tier': user_data.city_tier.replace(" ", "_").lower(), # e.g., "Tier 1" -> "tier_1"
            'income_lpa': user_data.income_lpa,
            'occupation': user_data.occupation
        }

        # 3. Call the prediction function with the correctly formatted data
        prediction_result = predict_output(input_data_for_model)
        
        # Display the result
        st.markdown(f"""
        <div class="result-box">
            <p>Estimated Premium Category</p>
            <h3>{prediction_result['predicted_category']}</h3>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("Your Profile at a Glance")
        bmi_category = "Underweight" if user_data.bmi < 18.5 else "Normal" if user_data.bmi < 25 else "Overweight" if user_data.bmi < 30 else "Obese"
        st.metric(label="Your BMI", value=f"{user_data.bmi:.2f}", delta=bmi_category)

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

st.markdown("---")
st.info("Disclaimer: This is a predictive model and the results are an estimation, not a guaranteed quote.")
st.markdown("<div class='footer'>Made by Arsheen Singh</div>", unsafe_allow_html=True)
