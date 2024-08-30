# Import dependencies
from work_life_balance import config as config

# Import Library
import joblib
from pydantic import BaseModel, Field, field_validator, ValidationError, validator
import json
import pandas as pd

# Validate input
class Predict(BaseModel):
    FRUITS_VEGGIES : int = Field(ge=0, le=5, repr=False)
    AVERAGE_STRESS : str = Field(repr=False)
    PLACES_VISITED : int = Field(ge=0, le=10, repr=False)
    CORE_CIRCLE : int = Field(ge=0, le=10, repr=False)
    SUPPORTING_OTHERS : int = Field(ge=0, le=10, repr=False)
    SOCIAL_NETWORK : int = Field(ge=0, le=10, repr=False)
    ACHIEVEMENT : int = Field(ge=0, le=10, repr=False)
    DONATION : int = Field(ge=0, le=5, repr=False)
    BMI_RANGE : int = Field(ge=1, le=2, repr=False)
    TODO_COMPLETED : int = Field(ge=0, le=10, repr=False)
    AVERAGE_DAILY_STEPS : int = Field(ge=0, le=10, repr=False)
    SLEEP_HOURS : int = Field(ge=0, le=10, repr=False)
    LOST_VACATION : int = Field(ge=0, le=10, repr=False)
    AVERAGE_SHOUTING : int = Field(ge=0, le=10, repr=False)
    SUFFICIENT_INCOME : int = Field(ge=1, le=2, repr=False)
    PERSONAL_AWARDS : int = Field(ge=0, le=10, repr=False)
    TIME_FOR_PASSION : int = Field(ge=0, le=10, repr=False)
    WEEKLY_MEDITATION : int = Field(ge=0, le=10, repr=False)
    AGE : str = Field(repr=False)
    GENDER : str = Field(repr=False)

    @field_validator('BMI_RANGE','SUFFICIENT_INCOME', mode='before')
    @classmethod
    def choice_validator(cls, bmi_range: str) -> int:
        ref_dict = {'yes': 1, 'no': 2}
        return ref_dict[bmi_range]



def score(data):
    """Takes dictionary as input and provide model prediction"""
    try:
        predict_data = Predict(**data)
        data_json = predict_data.model_dump()
        data = pd.DataFrame([data_json])
    except ValidationError:
        raise Exception('Data is invalid')

    model = joblib.load(config.MODEL_PATH / 'model-v1.joblib')
    
    score = model.predict(data)
    target_transform = joblib.load(config.TRANSFORMER_PATH / 'target_scalar.joblib')
    return target_transform.inverse_transform([score])[0]
