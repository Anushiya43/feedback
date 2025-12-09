from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
import json
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class user_data(BaseModel):
    rating : int
    comment : str
    timestamp : str
    



@app.get("/data")
def get_data():
    try:
        with open("feedbackdata.json", "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/add")
def add_data(u :user_data):
    try:
        with open("feedbackdata.json", "r") as file:
            data = json.load(file)
        print(data)
        print("...........................")
        print(len(data))
        d=datetime.utcnow()
        data.append(
            {
                "id":int(len(data)+1),
                "rating": u.rating,
                "comment": u.comment,
                "timestamp":u.timestamp
            }
        )
        with open("feedbackdata.json",'w') as file:
            json.dump(data,file,indent=4)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

