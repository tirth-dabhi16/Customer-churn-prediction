import pandas as pd
import joblib
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from pathlib import Path

app = FastAPI(
    title="E-commerce Customer Churn Prediction API",
    description="API to predict customer churn using XGBoost",
    version="1.0.0"
)

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR/"customer_churn_model.pkl"

model = joblib.load(MODEL_PATH)

class CustomerData(BaseModel):
    Age: float | None = None
    Gender : str
    Country: str
    City: str

    Membership_Years: float
    Login_Frequency: float
    Session_Duration_Avg: float | None = None
    Pages_Per_Session: float | None = None
    Cart_Abandonment_Rate: float

    Wishlist_Items: float | None = None
    Total_Purchases: float
    Average_Order_Value: float

    Days_Since_Last_Purchase: float | None = None
    Discount_Usage_Rate: float | None = None
    Returns_Rate: float | None = None
    Email_Open_Rate: float | None = None

    Customer_Service_Calls: float
    Product_Reviews_Written: float | None = None
    Social_Media_Engagement_Score: float | None = None
    Mobile_App_Usage: float | None = None

    Payment_Method_Diversity: float | None = None
    Lifetime_Value: float
    Credit_Balance: float | None = None

    Signup_Quarter: str

@app.get("/")
def home():
    return {
        "message" : "Customer Churn Prediction API"
    }

@app.post("/predict")
def predict_churn(data : CustomerData):
    try:
        customer_dict = data.model_dump()
        input_df = pd.DataFrame([customer_dict])
        prediction = int(model.predict(input_df)[0])
        probability = float(model.predict_proba(input_df)[0][1])

        result = "Churned" if prediction == 1 else "Not Churned"

        return {
            "prediction" : prediction,
            "result" : result,
            "churn_probability" : f"{probability * 100:.2f}%",
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

