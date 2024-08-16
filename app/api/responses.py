from typing import Optional
from pydantic import BaseModel

from app.models.task import TasksActivityModel


class Status(BaseModel):
    success: bool
    message: str


class UpdateStatus(Status):
    pass


class DeleteStatus(Status):
    pass


class UpdateWebhookStatus(Status):
    pass


class CreateTaskResponse(BaseModel):
    success: bool
    message: str
    data: Optional[TasksActivityModel] = None


class TaskResponse(CreateTaskResponse):
    pass