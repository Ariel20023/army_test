from fastapi import UploadFile, File
import pandas as pd
from io import StringIO

@router.post("/items/upload_csv")
async def upload_items_csv(file: UploadFile = File(...)):

    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Please upload a CSV file")

    content = await file.read()
    decoded = content.decode("utf-8")

    df = pd.read_csv(StringIO(decoded))

    required_cols = {"id", "name", "price"}
    if not required_cols.issubset(df.columns):
        raise HTTPException(
            status_code=400,
            detail=f"CSV must contain columns: {required_cols}"
        )

    added_items = 0
    for _, row in df.iterrows():
        item_id = int(row["id"])

        items_db[item_id] = {
            "id": item_id,
            "name": row["name"],
            "price": float(row["price"])
        }
        added_items += 1

    return {
        "message": f"{added_items} items added successfully",
        "total_items_in_db": len(items_db)
    }