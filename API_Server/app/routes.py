from fastapi import APIRouter, HTTPException
from .models import Item
from .database import items_db
from fastapi import UploadFile
import csv
import io

router = APIRouter()

@router.post("/upload-csv")
def upload_csv(file: UploadFile):

    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}


    content = file.file.read().decode("utf-8")

    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)

    for line in rows:
        print(line)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "total_rows": len(rows),
        "columns": header,
        "data": rows[0:5],
        "message": f"Successfully processed CSV with {len(rows)} rows"
    }


#
# @router.post("/upload-csv")
# def soldier_by_distance(file: UploadFile):
#     if file.content_type != "text/csv":
#          return {"error": "File must be a CSV"}
#
#
#
#     content = file.file.read().decode("utf-8")
#
#     reader = csv.reader(io.StringIO(content))
#     header = next(reader)
#     rows = list(reader)
#
#     for line in rows:
#         if
#             print(line)
#
#



# @router.get("/items")
# def get_items():
#     return list(items_db.values())
#
# @router.get("/items/{item_id}")
# def get_item(item_id: int):
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return items_db[item_id]
#
# @router.post("/items")
# def create_item(item: Item):
#     if item.id in items_db:
#         raise HTTPException(status_code=400, detail="ID already exists")
#     items_db[item.id] = item
#     return {"message": "Item created", "item": item}
#
# @router.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     items_db[item_id] = item
#     return {"message": "Item updated", "item": item}
#
# @router.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     del items_db[item_id]
#     return {"message": "Item deleted"}
