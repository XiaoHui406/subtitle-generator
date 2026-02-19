from typing import List, Dict
from model.asr_model_config import ASRModelConfig, ASRModelJsonConfig
from manager.asr.interface.asr_model_manager import ASRModelManager
from manager.asr.whisper_model_manager import WhisperModelManager
from manager.asr.funasr_model_manager import FunasrModelManager
import json


class ASRModelAdapter:
    def __init__(self) -> None:
        self.asr_model_config_map: Dict[str, ASRModelConfig] = {}
        with open('config/asr_model.json', 'r', encoding='utf8') as config_file:
            data: ASRModelJsonConfig = ASRModelJsonConfig(
                **json.loads(config_file.read())
            )
        for model in data.models:
            self.asr_model_config_map[model.name] = model

    def get_asr_model_manager(
        self,
        model_name: str,
        device: str | None = None
    ) -> ASRModelManager:
        asr_model_config: ASRModelConfig = self.asr_model_config_map[model_name]
        model_size: str = asr_model_config.size
        match asr_model_config.type:
            case 'whisper':
                return WhisperModelManager(model_size=model_size, device=device)
            case 'funasr':
                return FunasrModelManager(model_size=model_size, device=device)
            case _:
                raise ValueError(f'model {model_name} is not supported')
