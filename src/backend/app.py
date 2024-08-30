from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os
from textbsr.textbsr import bsr

app = FastAPI()

@app.post("/restore-text/")
async def restore_text(
    input_file: UploadFile = File(...),
    bg_file: UploadFile = File(None),
    output_path: str = None,
    aligned: bool = False,
    save_text: bool = False,
    device: str = None
):
    input_path = f"./temp/{input_file.filename}"
    os.makedirs(os.path.dirname(input_path), exist_ok=True)
    
    with open(input_path, "wb") as f:
        f.write(await input_file.read())
    
    bg_path = None
    if bg_file:
        bg_path = f"./temp/{bg_file.filename}"
        with open(bg_path, "wb") as f:
            f.write(await bg_file.read())
    
    if output_path is None:
        output_path = f"./temp/output_{input_file.filename}"
    
    bsr(input_path=input_path, bg_path=bg_path, output_path=output_path, aligned=aligned, save_text=save_text, device=device)
    
    return FileResponse(output_path, media_type='image/png', filename=os.path.basename(output_path))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)