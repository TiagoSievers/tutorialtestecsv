from fastapi import FastAPI, File, UploadFile
import pandas

app = FastAPI()

@app.get("/")
def home():
    return "Hell world, minha API está no ar"

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    df = pandas.read_csv(file.file)
    data_list = df.to_dict(orient="records")

    result = {"data": data_list}

    return result
