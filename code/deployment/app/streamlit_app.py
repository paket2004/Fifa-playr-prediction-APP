import streamlit as st
import requests

# Streamlit app title
st.title("FIFA Player Rating Predictor")

# Create input fields for all attributes in the PredictionRequest model
age = st.number_input("Age", min_value=15, max_value=50, value=31)
weight_kgs = st.number_input("Weight (in kg)", min_value=50.0, max_value=120.0, value=72.1)
potential = st.slider("Potential", min_value=1, max_value=100, value=94)
value_euro = st.number_input("Value (in €)", value=110500000.0)
wage_euro = st.number_input("Wage (in €)", value=565000.0)
international_reputation = st.slider("International Reputation", min_value=1, max_value=5, value=5)
weak_foot = st.slider("Weak Foot", min_value=1, max_value=5, value=4)
skill_moves = st.slider("Skill Moves", min_value=1, max_value=5, value=4)
release_clause_euro = st.number_input("Release Clause (in €)", value=226500000.0)
national_rating = st.slider("National Rating", min_value=1, max_value=100, value=82)
crossing = st.slider("Crossing", min_value=1, max_value=100, value=86)
finishing = st.slider("Finishing", min_value=1, max_value=100, value=95)
heading_accuracy = st.slider("Heading Accuracy", min_value=1, max_value=100, value=70)
short_passing = st.slider("Short Passing", min_value=1, max_value=100, value=92)
volleys = st.slider("Volleys", min_value=1, max_value=100, value=86)
dribbling = st.slider("Dribbling", min_value=1, max_value=100, value=97)
curve = st.slider("Curve", min_value=1, max_value=100, value=93)
freekick_accuracy = st.slider("Freekick Accuracy", min_value=1, max_value=100, value=94)
long_passing = st.slider("Long Passing", min_value=1, max_value=100, value=89)
ball_control = st.slider("Ball Control", min_value=1, max_value=100, value=96)
acceleration = st.slider("Acceleration", min_value=1, max_value=100, value=91)
sprint_speed = st.slider("Sprint Speed", min_value=1, max_value=100, value=86)
agility = st.slider("Agility", min_value=1, max_value=100, value=93)
reactions = st.slider("Reactions", min_value=1, max_value=100, value=95)
balance = st.slider("Balance", min_value=1, max_value=100, value=95)
shot_power = st.slider("Shot Power", min_value=1, max_value=100, value=85)
jumping = st.slider("Jumping", min_value=1, max_value=100, value=68)
stamina = st.slider("Stamina", min_value=1, max_value=100, value=72)
strength = st.slider("Strength", min_value=1, max_value=100, value=66)
long_shots = st.slider("Long Shots", min_value=1, max_value=100, value=94)
aggression = st.slider("Aggression", min_value=1, max_value=100, value=48)
interceptions = st.slider("Interceptions", min_value=1, max_value=100, value=22)
positioning = st.slider("Positioning", min_value=1, max_value=100, value=94)
vision = st.slider("Vision", min_value=1, max_value=100, value=94)
penalties = st.slider("Penalties", min_value=1, max_value=100, value=75)
composure = st.slider("Composure", min_value=1, max_value=100, value=96)
marking = st.slider("Marking", min_value=1, max_value=100, value=33)
standing_tackle = st.slider("Standing Tackle", min_value=1, max_value=100, value=28)
sliding_tackle = st.slider("Sliding Tackle", min_value=1, max_value=100, value=26)

# Prediction button
if st.button("Predict"):
    # Prepare the payload for the API request
    input_data = {
        "age": age,
        "weight_kgs": weight_kgs,
        "potential": potential,
        "value_euro": value_euro,
        "wage_euro": wage_euro,
        "international_reputation_from_1_to_5": international_reputation,
        "weak_foot_from_1_to_5": weak_foot,
        "skill_moves_from_1_to_5": skill_moves,
        "release_clause_euro": release_clause_euro,
        "national_rating": national_rating,
        "crossing": crossing,
        "finishing": finishing,
        "heading_accuracy": heading_accuracy,
        "short_passing": short_passing,
        "volleys": volleys,
        "dribbling": dribbling,
        "curve": curve,
        "freekick_accuracy": freekick_accuracy,
        "long_passing": long_passing,
        "ball_control": ball_control,
        "acceleration": acceleration,
        "sprint_speed": sprint_speed,
        "agility": agility,
        "reactions": reactions,
        "balance": balance,
        "shot_power": shot_power,
        "jumping": jumping,
        "stamina": stamina,
        "strength": strength,
        "long_shots": long_shots,
        "aggression": aggression,
        "interceptions": interceptions,
        "positioning": positioning,
        "vision": vision,
        "penalties": penalties,
        "composure": composure,
        "marking": marking,
        "standing_tackle": standing_tackle,
        "sliding_tackle": sliding_tackle,
    }

    # Send the request to FastAPI to get the prediction
    response = requests.post("http://fastapi:80/predict", json=input_data)
    if response.status_code == 200:
        # Parse and display the prediction result
        result = response.json()
        # st.success(f"Predicted Rating: {result['prediction'][0]}")
        st.success(f"Predicted Rating: {result}")
    else:
        st.error(f"Error: {response.status_code}")
