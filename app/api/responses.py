from pydantic import BaseModel


class Status(BaseModel):
    success: bool


class UpdateStatus(Status):
    pass


class DeleteStatus(Status):
    pass
