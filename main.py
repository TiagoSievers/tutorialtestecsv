from fastapi import FastAPI, File, UploadFile
import pandas

app = FastAPI()

@app.post("/")
async def create_upload_file(file: UploadFile = File(...)):
    df = pandas.read_csv(file.file)
    data_list = df.to_dict(orient="records")

    result = {"data": data_list}

    return result
