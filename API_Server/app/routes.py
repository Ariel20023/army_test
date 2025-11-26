from fastapi import APIRouter, HTTPException
from fastapi import UploadFile
import csv
import io
from classes import soldier


router = APIRouter()

@router.post("/assignWithCsv")
def assignWithCsv(file: UploadFile):

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


@router.post("/get_name_by_km-csv")
def select_by_km(file: UploadFile):
    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}

    content = file.file.read().decode("utf-8")

    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)
    distant_soldiers = []
    sleeping_places = 160
    n = len(rows)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if int(rows[j][5]) < int(rows[j + 1][5]):
                rows[j], rows[j + 1] = rows[j + 1], rows[j]
    for place in range(sleeping_places):
        distant_soldiers.append(rows[place])
    return distant_soldiers



















