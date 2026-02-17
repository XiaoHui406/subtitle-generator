from model.interface.asr_model_manager import ASRModelManager
from model.whisper_model_manager import WhisperModelManager

asr_model_manager: ASRModelManager = WhisperModelManager('small')
