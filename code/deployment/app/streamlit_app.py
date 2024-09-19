import streamlit as st
import requests

# Streamlit app title
st.title("FIFA Player Rating Predictor")

# Create input fields for all attributes in the PredictionRequest model
age = st.number_input("Age", min_value=1, max_value=120, value=25)
weight_kgs = st.number_input("Weight (in kg)", min_value=10.0, max_value=200.0, value=75.0)
potential = st.slider("Potential", min_value=1, max_value=100, value=75)
value_euro = st.number_input("Value (in €)", value=100000.0)
wage_euro = st.number_input("Wage (in €)", value=5000.0)
international_reputation = st.slider("International Reputation", min_value=1, max_value=5, value=3)
weak_foot = st.slider("Weak Foot", min_value=1, max_value=5, value=3)
skill_moves = st.slider("Skill Moves", min_value=1, max_value=5, value=3)
release_clause_euro = st.number_input("Release Clause (in €)", value=10000000.0)
national_rating = st.number_input("National Rating", min_value=1, max_value=100, value=50)
crossing = st.slider("Crossing", min_value=1, max_value=100, value=50)
finishing = st.slider("Finishing", min_value=1, max_value=100, value=50)
heading_accuracy = st.slider("Heading Accuracy", min_value=1, max_value=100, value=50)
short_passing = st.slider("Short Passing", min_value=1, max_value=100, value=50)
volleys = st.slider("Volleys", min_value=1, max_value=100, value=50)
dribbling = st.slider("Dribbling", min_value=1, max_value=100, value=50)
curve = st.slider("Curve", min_value=1, max_value=100, value=50)
freekick_accuracy = st.slider("Freekick Accuracy", min_value=1, max_value=100, value=50)
long_passing = st.slider("Long Passing", min_value=1, max_value=100, value=50)
ball_control = st.slider("Ball Control", min_value=1, max_value=100, value=50)
acceleration = st.slider("Acceleration", min_value=1, max_value=100, value=50)
sprint_speed = st.slider("Sprint Speed", min_value=1, max_value=100, value=50)
agility = st.slider("Agility", min_value=1, max_value=100, value=50)
reactions = st.slider("Reactions", min_value=1, max_value=100, value=50)
balance = st.slider("Balance", min_value=1, max_value=100, value=50)
shot_power = st.slider("Shot Power", min_value=1, max_value=100, value=50)
jumping = st.slider("Jumping", min_value=1, max_value=100, value=50)
stamina = st.slider("Stamina", min_value=1, max_value=100, value=50)
strength = st.slider("Strength", min_value=1, max_value=100, value=50)
long_shots = st.slider("Long Shots", min_value=1, max_value=100, value=50)
aggression = st.slider("Aggression", min_value=1, max_value=100, value=50)
interceptions = st.slider("Interceptions", min_value=1, max_value=100, value=50)
positioning = st.slider("Positioning", min_value=1, max_value=100, value=50)
vision = st.slider("Vision", min_value=1, max_value=100, value=50)
penalties = st.slider("Penalties", min_value=1, max_value=100, value=50)
composure = st.slider("Composure", min_value=1, max_value=100, value=50)
marking = st.slider("Marking", min_value=1, max_value=100, value=50)
standing_tackle = st.slider("Standing Tackle", min_value=1, max_value=100, value=50)
sliding_tackle = st.slider("Sliding Tackle", min_value=1, max_value=100, value=50)
birth_year = st.number_input("Birth Year", min_value=1950, max_value=2022, value=1990)

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
        "birth_year": birth_year,
    }

    # Send the request to FastAPI to get the prediction
    # response = requests.post("http://localhost:8000/predict", json=input_data)
    # response = requests.post("http://host.docker.internal:8000/predict", json=input_data)
    response = requests.post("http://fastapi:80/predict", json=input_data)
    if response.status_code == 200:
        # Parse and display the prediction result
        result = response.json()
        # st.success(f"Predicted Rating: {result['prediction'][0]}")
        st.success(f"Predicted Rating: {result}")
    else:
        st.error(f"Error: {response.status_code}")
