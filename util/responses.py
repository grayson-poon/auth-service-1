import json

from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from requests.exceptions import HTTPError


def http_response(body: dict[str, any], code: int) -> JSONResponse:
    return JSONResponse(content=body, status_code=code)


def raise_exception(exception: Exception | HTTPError, code: int) -> None:
    if type(exception) is HTTPError:
        py_dict: dict[str, any] = json.loads(exception.strerror)

        code: int = code if py_dict.get("error").get("code") is None else py_dict.get("error").get("code")
        body: dict[str, any] = { **py_dict, "error_type": str(type(exception)) }
        raise HTTPException(detail=body, status_code=code)

    body: dict[str, str] = { "error": str(exception), "error_type": str(type(exception)) }
    raise HTTPException(detail=body, status_code=code)
