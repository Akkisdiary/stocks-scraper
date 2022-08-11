from typing import Any, Dict, Tuple


def response(data: Dict[str, Any], status_code: int) -> Tuple[Dict, int]:
    data.update({
        "status_code": status_code
    })
    return data, status_code
