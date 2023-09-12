from pydantic import BaseModel


class RequestJsonLogSchema(BaseModel):
    """
    Scheme of the request-response part of the log in JSON format
    """

    request_uri: str
    request_referer: str
    request_protocol: str
    request_method: str
    request_path: str
    request_host: str
    request_size: int
    request_content_type: str
    request_headers: str
    request_body: str
    request_direction: str
    remote_ip: str
    remote_port: str
    response_status_code: int
    response_size: int
    response_headers: str
    response_body: str
    duration: int
