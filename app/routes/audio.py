from fastapi import APIRouter, UploadFile, File, Depends
from ..services.audio_transcription import AudioTranscriptionService
import os

router = APIRouter()
transcription_service = AudioTranscriptionService()



@router.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Sube un archivo de audio y devuelve la transcripción usando Whisper.
    """

    file_path = f"temp/{file.filename}"


    # Guardar archivo temporalmente
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Transcribir audio con Whisper
    transcription = transcription_service.transcribe_audio(file_path)

    # (Opcional) Eliminar archivo después de procesarlo
    os.remove(file_path)

    return {"transcription": transcription}
