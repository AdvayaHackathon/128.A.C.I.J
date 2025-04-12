import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Personalized Treatment Plan Generator",
    page_icon="🏥",
    layout="centered"
)

# Custom CSS with improved colors and contrast for visibility
st.markdown("""
<style>
    .stApp {
        background-color: #f0f8ff;
    }
    
    /* Ensure all text elements have sufficient contrast */
    .stTextInput label, .stNumberInput label, .stSelectbox label, .stSlider label, .stTextArea label {
        color: #3b82f6  !important;
        font-weight: 500 !important;
    }
    
    /* Fix for form input text visibility */
    .stTextInput input, .stNumberInput input, .stSelectbox select, .stTextArea textarea {
        color: #3b82f6  !important;
        background-color: white !important;
    }
    
    /* Override any other text colors to ensure visibility */
    p, span, li, label, div {
        color: #3b82f6  !important;
    }
    
    /* Fix for dropdown menus */
    .stSelectbox div[role="listbox"] div {
        color: #3b82f6  !important;
        background-color: white !important;
    }
    
    .stSelectbox div[data-baseweb="select"] div {
        color: #3b82f6  !important;
    }
    
    /* Maintain special styling for headers and important elements */
    .main-header {
        font-size: 2.5rem;
        color: #1e3a8a !important;
        text-align: center;
        margin-bottom: 1.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        padding: 1rem;
        background: linear-gradient(135deg, #c7e9fb 0%, #e3f4fc 100%);
        border-radius: 10px;
    }
    
    .sub-header {
        font-size: 1.8rem;
        color: #2563eb !important;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #93c5fd;
        padding-bottom: 0.5rem;
    }
    
    /* Fix recommendation text visibility */
    .recommendation {
        background-color: #f0f9ff;
        padding: 1.2rem;
        border-radius: 8px;
        border-left: 5px solid #3b82f6;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    .recommendation strong {
        color: #3b82f6  !important;
        font-weight: bold;
    }
    
    .recommendation span {
        color: #3b82f6  !important;
    }
    
    /* Fix BMI indicators */
    .bmi-normal {
        color: #15803d !important;
        font-weight: bold;
        padding: 3px 8px;
        background-color: #dcfce7;
        border-radius: 4px;
    }
    
    .bmi-warning {
        color: #b45309 !important;
        font-weight: bold;
        padding: 3px 8px;
        background-color: #fef3c7;
        border-radius: 4px;
    }
    
    .bmi-danger {
        color: #b91c1c !important;
        font-weight: bold;
        padding: 3px 8px;
        background-color: #fee2e2;
        border-radius: 4px;
    }
    
    .stButton>button {
        background-color: #3b82f6;
        color: white !important;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    
    .stButton>button:hover {
        background-color: #2563eb;
    }
    
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        border-radius: 6px;
        border: 1px solid #bfdbfe;
    }
    
    .section-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
    }
    
    h3 {
        color: #1e40af !important;
    }
    
    .disclaimer {
        background-color: #ffe4e6;
        border-left: 5px solid #f43f5e;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1.5rem;
        color: #3b82f6  !important;
    }
    
    /* Override Streamlit text color */
    .css-nahz7x, .css-15tx938, .css-1jp2gje {
        color: #3b82f6  !important;
    }
    
    .st-bk {
        color: #3b82f6  !important;
    }
    
    .st-ae {
        color: #3b82f6  !important;
    }
    
    /* Ensure all text is visible */
    div[data-testid="stForm"] {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        color: #3b82f6  !important;
    }
    
    /* Fix for text in recommendation cards */
    .recommendation * {
        color: #3b82f6  !important;
    }
    
    /* Fix for multiselect option text */
    [data-baseweb="select-option"] {
        color: #3b82f6  !important;
    }
    
    /* Making sure all text elements have proper contrast */
    div, p, span, li, h1, h2, h3, h4, h5, h6 {
        color: #3b82f6  !important;
    }
    
    /* Special styling elements can override the above */
    .main-header, .sub-header, h3 {
        color: #1e40af !important;
    }
    
    /* High contrast for all recommendation text */
    .recommendation-text {
        color: #3b82f6  !important;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Main title with decorative elements
st.markdown("<h1 class='main-header'>🏥 Personalized Treatment Plan Generator 🏥</h1>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; margin-bottom: 2rem; color: #3b82f6  !important; background-color: white; padding: 1rem; border-radius: 8px;'>
    Complete the form below to receive your customized health recommendations and treatment plan based on your unique profile.
</div>
""", unsafe_allow_html=True)

# Create a form with improved styling
with st.form("treatment_plan_form"):
    # Personal Information Section
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>👤 Personal Information</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=1, max_value=120, step=1, value=30)
    
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Prefer not to say"])
        occupation = st.text_input("Occupation")
    
    col3, col4 = st.columns(2)
    with col3:
        height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, step=0.1, value=170.0)
    with col4:
        weight = st.number_input("Weight (kg)", min_value=1.0, max_value=500.0, step=0.1, value=70.0)
    
    allergies = st.text_area("Do you have any known allergies? If yes, please specify.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Medical History Section
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>📋 Medical History</h2>", unsafe_allow_html=True)
    
    medical_conditions = st.text_area("Do you have any current medical conditions? (e.g., diabetes, hypertension, heart disease, etc.)")
    
    col5, col6 = st.columns(2)
    with col5:
        sleep_hours = st.slider("Hours of sleep on average per night", 1, 12, 7)
    with col6:
        exercise_frequency = st.selectbox("How often do you exercise?", ["Regularly", "Occasionally", "Never"])
    
    surgeries = st.text_area("Have you had any major surgeries or hospitalizations in the past?")
    medications = st.text_area("Are you currently taking any medications? If yes, please provide details (medication names and the conditions they treat).")
    family_history = st.text_area("Do you have a family history of any chronic diseases? (e.g., cancer, heart disease, diabetes)")
    
    col7, col8 = st.columns(2)
    with col7:
        junk_food = st.selectbox("What are your eating habits when it comes to junk food?", ["High", "Moderate", "Low"])
    with col8:
        if gender == "Female":
            menstrual_cycle = st.selectbox("How would you describe your menstrual cycle?", ["Regular", "Irregular", "Not applicable"])
        else:
            menstrual_cycle = "Not applicable"
    
    recent_illnesses = st.text_area("Have you had any recent illnesses or injuries?")
    mental_health = st.text_area("Have you been diagnosed with any mental health conditions? (e.g., anxiety, depression, etc.)")
    st.markdown("</div>", unsafe_allow_html=True)

    # Submit button with improved styling
    col_submit1, col_submit2, col_submit3 = st.columns([1, 2, 1])
    with col_submit2:
        submitted = st.form_submit_button("Generate My Treatment Plan")

# Process form and generate recommendations when submitted
if submitted:
    st.markdown("<div class='section-card' style='background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>✅ Your Personalized Treatment Plan</h2>", unsafe_allow_html=True)
    
    # Display personal greeting
    st.markdown(f"<h3 style='color: #1e40af !important; text-align: center;'>Hello {full_name}! 👋</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='text-align: center; margin-bottom: 1.5rem; color: #3b82f6  !important;'>
        Thank you for providing your health information. Here's your personalized treatment plan based on your responses.
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate BMI with colorful indicators
    if height > 0 and weight > 0:
        bmi = weight / ((height/100) ** 2)
        st.markdown("<h3 style='color: #1e40af !important;'>🔢 BMI Calculation</h3>", unsafe_allow_html=True)
        
        # BMI category and styling
        if bmi < 18.5:
            bmi_category = "Underweight"
            bmi_class = "bmi-warning"
            bmi_icon = "⚠️"
        elif 18.5 <= bmi < 25:
            bmi_category = "Normal weight"
            bmi_class = "bmi-normal"
            bmi_icon = "✅"
        elif 25 <= bmi < 30:
            bmi_category = "Overweight"
            bmi_class = "bmi-warning"
            bmi_icon = "⚠️"
        else:
            bmi_category = "Obese"
            bmi_class = "bmi-danger"
            bmi_icon = "⚠️"
        
        st.markdown(f"""
        <div style='background-color: white; padding: 1rem; border-radius: 8px; text-align: center; margin-bottom: 1.5rem;'>
            Your BMI is: <span class='{bmi_class}'>{bmi:.1f}</span> {bmi_icon}<br>
            <span style='font-size: 1.1rem; color: #3b82f6  !important;'>Category: {bmi_category}</span>
        </div>
        """, unsafe_allow_html=True)
        
        # BMI-based recommendations
        if bmi < 18.5:
            st.markdown("<div class='recommendation'><strong style='color: #3b82f6  !important;'>💡 Weight Recommendation:</strong> <span class='recommendation-text'>Consider increasing your caloric intake with nutrient-dense foods. Focus on proteins, healthy fats, and complex carbohydrates.</span></div>", unsafe_allow_html=True)
        elif 25 <= bmi < 30:
            st.markdown("<div class='recommendation'><strong style='color: #3b82f6  !important;'>💡 Weight Recommendation:</strong> <span class='recommendation-text'>Consider a moderate caloric deficit through balanced diet and regular exercise to achieve a healthier weight.</span></div>", unsafe_allow_html=True)
        elif bmi >= 30:
            st.markdown("<div class='recommendation'><strong style='color: #3b82f6  !important;'>💡 Weight Recommendation:</strong> <span class='recommendation-text'>It's advisable to consult with a healthcare provider for a comprehensive weight management plan.</span></div>", unsafe_allow_html=True)
    
    # Lifestyle Recommendations
    st.markdown("<h3 style='color: #1e40af !important;'>🌿 Lifestyle Recommendations</h3>", unsafe_allow_html=True)
    
    # Sleep recommendations
    if sleep_hours < 6:
        st.markdown("<div class='recommendation'><strong style='color: #3b82f6  !important;'>😴 Sleep:</strong> <span class='recommendation-text'>Your sleep duration appears to be below the recommended range. Aim for 7-9 hours of quality sleep per night. Consider establishing a regular sleep schedule and creating a restful environment.</span></div>", unsafe_allow_html=True)
    elif sleep_hours > 9:
        st.markdown("<div class='recommendation'><strong style='color: #3b82f6  !important;'>😴 Sleep:</strong> <span class='recommendation-text'>You're getting more sleep than average. While extra sleep isn't necessarily harmful, excessive sleep can sometimes indicate underlying health issues. Monitor how you feel during the day.</span></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='recommendation'><strong style='color: #3b82f6  !important;'>😴 Sleep:</strong> <span class='recommendation-text'>Your sleep duration falls within the recommended range. Continue maintaining this healthy sleep pattern.</span></div>", unsafe_allow_html=True)
    
    # Exercise recommendations
    if exercise_frequency == "Never":
        st.markdown("<div class='recommendation'><strong style='color: #3b82f6  !important;'>🏃‍♂️ Exercise:</strong> <span class='recommendation-text'>Regular physical activity is important for overall health. Consider starting with light activities like walking for 15-30 minutes daily and gradually increase intensity.</span></div>", unsafe_allow_html=True)
    elif exercise_frequency == "Occasionally":
        st.markdown("<div class='recommendation'><strong style='color: #3b82f6  !important;'>🏃‍♂️ Exercise:</strong> <span class='recommendation-text'>Try to establish a more consistent exercise routine. Aim for at least 150 minutes of moderate activity or 75 minutes of vigorous activity per week.</span></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='recommendation'><strong style='color: #3b82f6  !important;'>🏃‍♂️ Exercise:</strong> <span class='recommendation-text'>Great job maintaining regular exercise! Continue with your routine and consider incorporating variety in workouts for overall fitness.</span></div>", unsafe_allow_html=True)
    
    # Stress management based on occupation
    st.markdown(f"<div class='recommendation'><strong style='color: #3b82f6  !important;'>🧘 Stress Management:</strong> <span class='recommendation-text'>Based on your occupation as {occupation}, consider incorporating stress management techniques such as mindfulness, deep breathing exercises, or short breaks during work hours.</span></div>", unsafe_allow_html=True)
    
    # Preventive Measures
    st.markdown("<h3 style='color: #1e40af !important;'>🛡️ Preventive Measures</h3>", unsafe_allow_html=True)
    
    # Age-based recommendations
    if age > 40:
        st.markdown("<div class='recommendation'><span class='recommendation-text'>Consider regular health check-ups including blood pressure monitoring, cholesterol screening, and other age-appropriate screenings.</span></div>", unsafe_allow_html=True)
    
    # Medical condition-based recommendations
    if medical_conditions and medical_conditions.lower().find("diabetes") != -1:
        st.markdown("<div class='recommendation'><span class='recommendation-text'>For diabetes management, regular blood glucose monitoring is essential. Consider consulting with a dietitian for meal planning.</span></div>", unsafe_allow_html=True)
    
    if medical_conditions and (medical_conditions.lower().find("hypertension") != -1 or medical_conditions.lower().find("high blood pressure") != -1):
        st.markdown("<div class='recommendation'><span class='recommendation-text'>For hypertension management, consider the DASH diet approach and regular blood pressure monitoring.</span></div>", unsafe_allow_html=True)
    
    if family_history and (family_history.lower().find("heart") != -1 or family_history.lower().find("cardiac") != -1):
        st.markdown("<div class='recommendation'><span class='recommendation-text'>Given your family history of heart-related conditions, consider cardiovascular screenings and heart-healthy lifestyle choices.</span></div>", unsafe_allow_html=True)
    
    if mental_health:
        st.markdown("<div class='recommendation'><span class='recommendation-text'>For mental health support, consider regular check-ins with mental health professionals and explore techniques like meditation or cognitive behavioral therapy approaches.</span></div>", unsafe_allow_html=True)
    
    # Food Recommendations
    st.markdown("<h3 style='color: #1e40af !important;'>🍎 Food Recommendations</h3>", unsafe_allow_html=True)
    
    # Junk food habits
    if junk_food == "High":
        st.markdown("<div class='recommendation'><span class='recommendation-text'>Consider gradually reducing processed food intake. Try incorporating more whole foods like fruits, vegetables, and lean proteins into your diet.</span></div>", unsafe_allow_html=True)
    elif junk_food == "Moderate":
        st.markdown("<div class='recommendation'><span class='recommendation-text'>You're making good progress with moderating junk food. Try to further limit processed foods and increase whole food consumption.</span></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='recommendation'><span class='recommendation-text'>Great job maintaining a low junk food intake! Continue focusing on whole, nutrient-dense foods.</span></div>", unsafe_allow_html=True)
    
    # General nutrition advice
    st.markdown("<div class='recommendation'><span class='recommendation-text'>Aim for a balanced diet that includes a variety of vegetables, fruits, lean proteins, and whole grains. Stay hydrated by drinking adequate water throughout the day.</span></div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Disclaimer
    st.markdown("<div class='disclaimer'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #b91c1c !important;'>⚠️ Disclaimer</h3>", unsafe_allow_html=True)
    st.markdown("<span style='color: #3b82f6  !important;'>This treatment plan is generated based on the information you provided and is meant for general guidance only. It should not replace professional medical advice. Please consult with healthcare professionals for personalized medical recommendations.</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Option to download the plan as PDF (simplified representation)
    st.markdown("---")
    current_date = datetime.now().strftime("%Y-%m-%d")
    pdf_data = f"Personalized Treatment Plan for {full_name}\nGenerated on: {current_date}\n\n"
    
    # Enhanced download button
    col_dl1, col_dl2, col_dl3 = st.columns([1, 2, 1])
    with col_dl2:
        st.download_button(
            label="📥 Download Treatment Plan",
            data=pdf_data,
            file_name=f"treatment_plan_{full_name.replace(' ', '_')}.txt",
            mime="text/plain",
            key="download-btn"
        )

# Add improved footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 1rem; color: #3b82f6  !important; font-size: 0.9rem; background-color: white; border-radius: 8px;'>
    © 2025 Personalized Treatment Plan Generator<br>
    This application is for educational purposes only.<br>
    Created with ❤️ for better health outcomes.
</div>
""", unsafe_allow_html=True)