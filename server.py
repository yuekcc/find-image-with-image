from fastapi import FastAPI, File, UploadFile
import hashlib
import json

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "hello, world"}


@app.post('/upload_file')
async def upload_file(file: UploadFile):
    file_content = await file.read()

    file_hash = hashlib.sha1(file_content)
    file_hashed = file_hash.hexdigest()
    out_path = f'store/file/{file_hashed}'
    meta_out_path = f'store/file/{file_hashed}.meta'
    with open(out_path, "wb") as f:
        file_size = f.write(file_content)

    metadata = {"file_size": file_size, "filename": file.filename, "id": file_hashed}
    with open(meta_out_path, "w") as f:
        f.write(json.dumps(metadata))

    return metadata
