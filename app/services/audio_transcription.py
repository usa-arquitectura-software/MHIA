import whisper
import os
from fastapi import HTTPException

class AudioTranscriptionService:
    def __init__(self, model_size="base"):
        """
        Inicializa Whisper con el modelo especificado.
        Modelos disponibles: "tiny", "base", "small", "medium", "large".
        """
        self.model = whisper.load_model(model_size)

    def transcribe_audio(self, file_path: str) -> str:
        """
        Transcribe un archivo de audio a texto usando Whisper.
        """
        if not os.path.exists(file_path):
            raise HTTPException(status_code=400, detail="Archivo no encontrado")

        result = self.model.transcribe(file_path)
        return result["text"]

# Ejemplo de uso
if __name__ == "__main__":
    service = AudioTranscriptionService()
    transcript = service.transcribe_audio("/home/burbanox/MHIA/audio_prueba.ogg")
    print("Transcripción:", transcript)
