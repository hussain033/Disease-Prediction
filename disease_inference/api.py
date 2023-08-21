from fastapi import FastAPI, Query
import uvicorn
from predict import prediction, preprocess
from typing import List
from mangum import Mangum


app = FastAPI()
handler = Mangum(app)

@app.get('/predict')
async def diseaseApi(dataFrame: List[str] = Query(None)):
    processed = preprocess(dataFrame)
    predict = prediction(processed)
    return predict

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000,debug=True)
