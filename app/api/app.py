from datetime import date
import os
from typing import Annotated, List, Optional
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise

from app.api.body import TasksActivityBody
from app.api.responses import (
    CreateTaskResponse,
    DeleteStatus,
    TaskResponse,
    UpdateStatus,
    UpdateWebhookStatus,
)

from ..models.task import HistoryModel, TasksActivityModel
from ..models.enum import (
    HistoryActionType,
    ActivityName,
    GroupCategory,
    GroupName,
    StageName,
    Status,
    SubCategoryName,
)
from ..models.db_task import History, TasksActivity
from ..const import HOST, PORT
import httpx

app = FastAPI()


@app.route("/")
async def home(_: Request):
    """Redirects the root URL to the API documentation."""
    return RedirectResponse("/docs")


@app.get("/task/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    """Fetches a task by its ID and returns the task details."""
    task = await TasksActivity.filter(task_id=task_id).first()
    if task:
        return TaskResponse(
            success=True, message="Task Fetched Successfully", data=task.to_model()
        )
    return TaskResponse(success=False, message="Task Not Found")


@app.post("/tasks-activity", response_model=CreateTaskResponse)
async def create_task_activity(
    task_name: Annotated[str, Form()],
    task_description: Annotated[str, Form()],
    activity_type_id: Annotated[int, Form()],
    activity_type_name: Annotated[ActivityName, Form()],
    activity_group_sub_category_id: Annotated[int, Form()],
    activity_group_sub_category_name: Annotated[SubCategoryName, Form()],
    activity_group_id: Annotated[int, Form()],
    activity_group_name: Annotated[GroupName, Form()],
    stage_id: Annotated[int, Form()],
    stage_name: Annotated[StageName, Form()],
    core_group_category_id: Annotated[int, Form()],
    core_group_category: Annotated[GroupCategory, Form()],
    core_group_id: Annotated[int, Form()],
    core_group_name: Annotated[str, Form()],
    due_date: Annotated[date, Form()],
    action_type: Annotated[str, Form()],
    related_to: Annotated[str, Form()],
    related_to_picture_id: Annotated[int, Form()],
    related_to_email: Annotated[str, Form()],
    related_to_company: Annotated[str, Form()],
    assign_to: Annotated[str, Form()],
    assign_to_picture_id: Annotated[int, Form()],
    assign_to_email: Annotated[str, Form()],
    assign_to_company: Annotated[str, Form()],
    notes: Annotated[str, Form()],
    status: Annotated[Status, Form()],
    attachment_id: Annotated[int, Form()],
    attachments: Annotated[int, Form()],
    link_response_id: Annotated[int, Form()],
    link_object_id: Annotated[int, Form()],
    created_by: Annotated[str, Form()],
):
    """Creates a new task activity and records it in the database."""
    try:
        task_activity = await TasksActivity.create(
            task_name=task_name,
            task_description=task_description,
            activity_type_id=activity_type_id,
            activity_type_name=activity_type_name,
            activity_group_sub_category_id=activity_group_sub_category_id,
            activity_group_sub_category_name=activity_group_sub_category_name,
            activity_group_id=activity_group_id,
            activity_group_name=activity_group_name,
            stage_id=stage_id,
            stage_name=stage_name,
            core_group_category_id=core_group_category_id,
            core_group_category=core_group_category,
            core_group_id=core_group_id,
            core_group_name=core_group_name,
            due_date=due_date,
            action_type=action_type,
            related_to=related_to,
            related_to_picture_id=related_to_picture_id,
            related_to_email=related_to_email,
            related_to_company=related_to_company,
            assign_to=assign_to,
            assign_to_email=assign_to_email,
            assign_to_picture_id=assign_to_picture_id,
            assign_to_company=assign_to_company,
            notes=notes,
            status=status,
            attachment_id=attachment_id,
            attachments=attachments,
            link_response_id=link_response_id,
            link_object_id=link_object_id,
            created_by=created_by,
        )
        await History.create(
            task_id=task_activity.task_id,
            action=HistoryActionType.CREATE,
            description=f"Task {task_activity.task_id} was created by user",
        )
        return CreateTaskResponse(
            success=True,
            message="Record added successfully",
            data=task_activity.to_model(),
        )
    except Exception as e:
        return CreateTaskResponse(
            success=False, message=" ".join(i.__str__() for i in e.args)
        )


@app.get("/task-activity", response_model=List[TasksActivityModel])
async def read_task_activity(
    from_end: Optional[bool] = False,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
):
    """Fetches a list of task activities from the database."""
    awaitable = TasksActivity.all()
    if from_end:
        awaitable = awaitable.order_by("-id")
    if isinstance(offset, int):
        awaitable = awaitable.offset(offset)
    if not (limit is None):
        awaitable = awaitable.limit(limit)
    return [history.to_model() for history in await awaitable]


@app.put("/task-activity")
async def update_task_activity(
    task_id: Annotated[int, Form()],
    task_name: Annotated[str, Form()],
    task_description: Annotated[str, Form()],
    activity_type_id: Annotated[int, Form()],
    activity_type_name: Annotated[ActivityName, Form()],
    activity_group_sub_category_id: Annotated[int, Form()],
    activity_group_sub_category_name: Annotated[SubCategoryName, Form()],
    activity_group_id: Annotated[int, Form()],
    activity_group_name: Annotated[GroupName, Form()],
    stage_id: Annotated[int, Form()],
    stage_name: Annotated[StageName, Form()],
    core_group_category_id: Annotated[int, Form()],
    core_group_category: Annotated[GroupCategory, Form()],
    core_group_id: Annotated[int, Form()],
    core_group_name: Annotated[str, Form()],
    due_date: Annotated[date, Form()],
    action_type: Annotated[str, Form()],
    related_to: Annotated[str, Form()],
    related_to_picture_id: Annotated[int, Form()],
    related_to_email: Annotated[str, Form()],
    related_to_company: Annotated[str, Form()],
    assign_to: Annotated[str, Form()],
    assign_to_picture_id: Annotated[int, Form()],
    assign_to_email: Annotated[str, Form()],
    assign_to_company: Annotated[str, Form()],
    notes: Annotated[str, Form()],
    status: Annotated[Status, Form()],
    attachment_id: Annotated[int, Form()],
    attachments: Annotated[int, Form()],
    link_response_id: Annotated[int, Form()],
    link_object_id: Annotated[int, Form()],
    created_by: Annotated[str, Form()],
):
    """Updates an existing task activity in the database."""
    updated = await TasksActivity.filter(task_id=task_id).update(
        task_name=task_name,
        task_description=task_description,
        activity_type_id=activity_type_id,
        activity_type_name=activity_type_name,
        activity_group_sub_category_id=activity_group_sub_category_id,
        activity_group_sub_category_name=activity_group_sub_category_name,
        activity_group_id=activity_group_id,
        activity_group_name=activity_group_name,
        stage_id=stage_id,
        stage_name=stage_name,
        core_group_category_id=core_group_category_id,
        core_group_category=core_group_category,
        core_group_id=core_group_id,
        core_group_name=core_group_name,
        due_date=due_date,
        action_type=action_type,
        related_to=related_to,
        related_to_picture_id=related_to_picture_id,
        related_to_email=related_to_email,
        related_to_company=related_to_company,
        assign_to=assign_to,
        assign_to_email=assign_to_email,
        assign_to_picture_id=assign_to_picture_id,
        assign_to_company=assign_to_company,
        notes=notes,
        status=status,
        attachment_id=attachment_id,
        attachments=attachments,
        link_response_id=link_response_id,
        link_object_id=link_object_id,
        created_by=created_by,
    )
    if updated:
        await History.create(
            task_id=task_id,
            action=HistoryActionType.UPDATE,
            description=f"Task {task_id} was updated",
        )
    return UpdateStatus(
        success=bool(updated),
        message="Task Updated Succesfully" if updated else "Task Not Found",
    )


@app.delete("/task-activity")
async def delete_task_activity(task_id: Annotated[int, Form()]):
    """Deletes a task activity from the database."""
    deleted = await TasksActivity.filter(task_id=task_id).delete()
    if deleted:
        await History.create(
            task_id=task_id,
            action=HistoryActionType.DELETE,
            description=f"Task {task_id} was deleted by user",
        )
    return DeleteStatus(
        success=bool(deleted),
        message="Task deleted succesfully" if deleted else "Task Not Found",
    )


@app.get("/histories", response_model=List[HistoryModel])
async def histories(
    from_end: Optional[bool] = False,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
):
    """Fetches a list of history records from the database."""
    awaitable = History.all()
    if from_end:
        awaitable = awaitable.order_by("-id")
    if isinstance(offset, int):
        awaitable = awaitable.offset(offset)
    if not (limit is None):
        awaitable = awaitable.limit(limit)
    return [history.to_model() for history in await awaitable]


@app.post("/webhook", response_model=UpdateWebhookStatus)
async def update_task_activity_webhook(request: Request):
    """Handle incoming webhook data to update a task activity.

    This function processes a JSON payload received via a POST request.
    The payload is expected to contain fields related to a `TaskActivity`.
    If the payload includes fields that do not correspond to `TaskActivity`, 
    they will be ignored. The function ensures data type validation, 
    and returns an error if the data types are incorrect.
    """    
    try:
        payload = await request.json()
        task_id = payload.get("task_id")
        if isinstance(task_id, int):
            task_activity_keys = set(TasksActivityBody.model_fields.keys())
            intersection = set(payload) & task_activity_keys
            key_with_default_value = task_activity_keys - intersection
            update_data = TasksActivityBody.model_validate(
                {key: payload[key] for key in intersection}
                | {i: None for i in key_with_default_value}
            )
            payload_kwargs = update_data.model_dump(exclude={"task_id"}, exclude_none=True)
            status = await TasksActivity.filter(task_id=task_id).update(
                **payload_kwargs
            )
            if status:
                await History.create(
                    task_id=task_id,
                    action=HistoryActionType.UPDATE,
                    description=f"Task {task_id} was updated: {', '.join(payload_kwargs)} were modified.",
                )
            return UpdateWebhookStatus(
                success=bool(status),
                message="task updated successfully" if status else "Task Not Found",
            )
        return UpdateWebhookStatus(success=False, message="Task Not Found")
    except Exception as e:
        return UpdateWebhookStatus(
            success=False,
            message=f"{e.__class__}:" + f" ".join(i.__str__() for i in e.args),
        )


@app.post("/webhook-playground", response_model=UpdateWebhookStatus)
async def webhook_playground(body: TasksActivityBody):
    """Simulate sending a webhook request to update task activity.

    This function accepts a `TasksActivityBody` object, converts it to JSON format, 
    and sends it as a POST request to an external webhook endpoint. The response 
    from the external endpoint is then returned as an instance of `UpdateWebhookStatus`.
    """    
    async with httpx.AsyncClient() as client:
        json_payload = body.model_dump(exclude_none=True, mode="json")
        response = await client.post(f"http://{HOST}:{PORT}/webhook", json=json_payload)
        return UpdateWebhookStatus(**response.json())


register_tortoise(
    app, db_url="sqlite://db.sqlite3", modules={"models": ["app.models.db_task"]}
)
