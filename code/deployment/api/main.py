from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
import os
# os.environ["PROJECTDIR"] = r"C:\Users\79133\PMLDL_A1"
# path = os.getenv("PROJECTDIR")
# print(path)
# PROJECTDIR = os.getenv('PROJECTDIR', '/code')  # Default to '/code' if not set

# Load the model using the PROJECTDIR
# model_path = os.path.join(PROJECTDIR, 'models/FIFA_rating_prediction.pkl')
with open("FIFA_rating_prediction.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# class storing necessary input data to predict player's rating
class PredictionRequest(BaseModel):
    age: int
    weight_kgs: float
    potential: int
    value_euro: float
    wage_euro: float
    international_reputation_from_1_to_5: int
    weak_foot_from_1_to_5: int
    skill_moves_from_1_to_5: int
    release_clause_euro: float
    national_rating: float
    crossing: int
    finishing: int
    heading_accuracy: int
    short_passing: int
    volleys: int
    dribbling: int
    curve: int
    freekick_accuracy: int
    long_passing: int
    ball_control: int
    acceleration: int
    sprint_speed: int
    agility: int
    reactions: int
    balance: int
    shot_power: int
    jumping: int
    stamina: int
    strength: int
    long_shots: int
    aggression: int
    interceptions: int
    positioning: int
    vision: int
    penalties: int
    composure: int
    marking: int
    standing_tackle: int
    sliding_tackle: int


@app.post("/predict")
async def predict(request: PredictionRequest):
    # features = np.array(request.features).reshape(1, -1)
    features = np.array([[
        request.age,
        request.weight_kgs,
        request.potential,
        request.value_euro,
        request.wage_euro,
        request.international_reputation_from_1_to_5,
        request.weak_foot_from_1_to_5,
        request.skill_moves_from_1_to_5,
        request.release_clause_euro,
        request.national_rating,
        request.crossing,
        request.finishing,
        request.heading_accuracy,
        request.short_passing,
        request.volleys,
        request.dribbling,
        request.curve,
        request.freekick_accuracy,
        request.long_passing,
        request.ball_control,
        request.acceleration,
        request.sprint_speed,
        request.agility,
        request.reactions,
        request.balance,
        request.shot_power,
        request.jumping,
        request.stamina,
        request.strength,
        request.long_shots,
        request.aggression,
        request.interceptions,
        request.positioning,
        request.vision,
        request.penalties,
        request.composure,
        request.marking,
        request.standing_tackle,
        request.sliding_tackle,
    ]])
    try:
        prediction = model.predict(features)

        return{"Predicted rating of the player:" : prediction[0]}
        # return {"zhopa"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# example of predicting messi rating
@app.post("/prediction-example")
async def predict_example(
        request: PredictionRequest = PredictionRequest (
            age=31,
            weight_kgs=72.1,
            potential=94,
            value_euro=110500000.0,
            wage_euro=565000.0,
            international_reputation_from_1_to_5=5,
            weak_foot_from_1_to_5=4,
            skill_moves_from_1_to_5=4,
            release_clause_euro=226500000.0,
            national_rating=82.000000,
            crossing=86,
            finishing=95,
            heading_accuracy=70,
            short_passing=92,
            volleys=86,
            dribbling=97,
            curve=93,
            freekick_accuracy=94,
            long_passing=89,
            ball_control=96,
            acceleration=91,
            sprint_speed=86,
            agility=93,
            reactions=95,
            balance=95,
            shot_power=85,
            jumping=68,
            stamina=72,
            strength=66,
            long_shots=94,
            aggression=48,
            interceptions=22,
            positioning=94,
            vision=94,
            penalties=75,
            composure=96,
            marking=33,
            standing_tackle=28,
            sliding_tackle=26,
                )):
    # features = np.array(request)
    # print(features)
    # return {"Predicted rating of the player:": model.predict(features)}
    # Extract the features from the request as a list
    features = np.array([[
        request.age,
        request.weight_kgs,
        request.potential,
        request.value_euro,
        request.wage_euro,
        request.international_reputation_from_1_to_5,
        request.weak_foot_from_1_to_5,
        request.skill_moves_from_1_to_5,
        request.release_clause_euro,
        request.national_rating,
        request.crossing,
        request.finishing,
        request.heading_accuracy,
        request.short_passing,
        request.volleys,
        request.dribbling,
        request.curve,
        request.freekick_accuracy,
        request.long_passing,
        request.ball_control,
        request.acceleration,
        request.sprint_speed,
        request.agility,
        request.reactions,
        request.balance,
        request.shot_power,
        request.jumping,
        request.stamina,
        request.strength,
        request.long_shots,
        request.aggression,
        request.interceptions,
        request.positioning,
        request.vision,
        request.penalties,
        request.composure,
        request.marking,
        request.standing_tackle,
        request.sliding_tackle,
    ]])

    # Ensure the shape of the array is (1, num_features) as expected by your model
    prediction = model.predict(features)

    # Assuming the prediction is a float, you can round or convert it to an integer if needed
    predicted_rating = int(round(prediction[0]))

    return {"Predicted rating of the player": predicted_rating}

@app.get("/")
def read_root():
    return {"message": "Welcome to the model API!"}