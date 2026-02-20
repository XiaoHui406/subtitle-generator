from fastapi import APIRouter
from manager.output_format.output_format_manager import OutputFormatManager
from model.output_format import OutputFormatRequest, OutputFormatResponse
from typing import List

output_format_router = APIRouter(
    prefix='/output_format',
    tags=['格式化导出']
)

output_format_manager = OutputFormatManager()


@output_format_router.post('/format')
def format(
    output_formatted_request: OutputFormatRequest
) -> List[OutputFormatResponse]:
    formatted_responses: List[OutputFormatResponse] = output_format_manager.format(
        output_format_request=output_formatted_request
    )
    return formatted_responses
