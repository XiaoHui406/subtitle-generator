from manager.asr.interface.asr_model_manager import ASRModelManager
from manager.asr.whisper_model_manager import WhisperModelManager
from manager.asr.asr_model_adapter import ASRModelAdapter


asr_model_adapter: ASRModelAdapter = ASRModelAdapter()
asr_model_manager: ASRModelManager = asr_model_adapter.get_asr_model_manager(
    model_name='FunASR SenseVoice Small'
)
