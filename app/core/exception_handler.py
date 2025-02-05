from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette import status

from app.schemas.responses.error_schema_response import ErrorResponse, ErrorsResponse


async def http_exception_handler(request: Request, exc: HTTPException):
    message = exc.detail
    return JSONResponse(
        status_code=exc.status_code, 
        content=ErrorResponse(message=message).model_dump()
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    messages = []
    for error in exc.errors():
        head_removed = str(error["msg"]).split(", ")[1]
        messages.append(head_removed)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ErrorsResponse(messages=messages).model_dump()
    )

async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500, 
        content=ErrorResponse(message="Có lỗi xảy ra").model_dump()
    )