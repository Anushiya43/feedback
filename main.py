from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
import json

app = FastAPI()

class user_data(BaseModel):
    star : int
    detail : str



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
        data.append(
            {
                    "star":u.star,
                    "details":u.detail
            }
        )
        with open("feedbackdata.json",'w') as file:
            json.dump(data,file,indent=4)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

