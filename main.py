from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class DataItem(BaseModel):
    data_id: int
    data_contents: str

all_data = [
    {"data_id": 1, "data_contents": "IMPORTANT"},
    {"data_id": 2, "data_contents": "zdfa"},
    {"data_id": 3, "data_contents": "asfdas"},
    {"data_id": 4, "data_contents": "w23"},
]

@app.get("/")
def page():
    return {'Go through': 'Pathways'}

@app.get("/alldata")
def gather_data():
    return all_data

@app.post("/datacreation")
def create_data(item: DataItem):
    return item

@app.delete("/removedata")
def remove_data(delete_id: int):
    for item in all_data:
        if item["data_id"] == delete_id: #Basically item['data_id] is doing this item = the ID and data_id is the whole dict of it self
            all_data.remove(item)
            return {"message": "Deleted successfully"}

    return {"message": "Can't delete: ID not found"}
@app.put("/adjustdata")
def adjust(adjusted: DataItem, adjusted_id: int):
    for item in all_data:
        if item["data_id"] == adjusted_id:
            item.update(adjusted)
            return {
                "message": "Successfully adjusted",
                "updated_item": item
            }

    return {"message": "Cannot adjust: ID not found"}