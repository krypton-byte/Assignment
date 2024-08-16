from datetime import date
from typing import Annotated, List, Optional
from fastapi import FastAPI, Form, Request
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from app.api.responses import CreateTaskResponse, DeleteStatus, TaskResponse, UpdateStatus, UpdateWebhookStatus

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


app = FastAPI()


@app.get("/")
async def home():
    return "Hello World"

@app.get('/task/{task_id}', response_model=TaskResponse)
async def get_task(task_id: int):
    task = await TasksActivity.filter(task_id=task_id).first()
    if task:
        return TaskResponse(
            success=True,
            message='Task Fetched Successfully',
            data=task.to_model()
        )
    return TaskResponse(
        success=False,
        message='Task Not Found'
    )

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
        return CreateTaskResponse(success=True, message="Record added successfully", data=task_activity.to_model())
    except Exception:
        return CreateTaskResponse(success=False, message="Failed to add record")


@app.get("/task-activity", response_model=List[TasksActivityModel])
async def read_task_activity(
    from_end: Optional[bool] = False,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
):
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
    return UpdateStatus(success=bool(updated), message='Task Updated Succesfully' if updated else 'Task Not Found')


@app.delete("/task-activity")
async def delete_task_activity(task_id: Annotated[int, Form()]):
    deleted = TasksActivity.filter(task_id=task_id).delete()
    if deleted:
        await History.create(
            task_id=task_id,
            action=HistoryActionType.DELETE,
            description=f"Task {task_id} was deleted by user",
        )
    return DeleteStatus(success=bool(deleted), message='Task deleted succesfully' if deleted else 'Task Not Found')


@app.get("/histories", response_model=List[HistoryModel])
async def histories(
    from_end: Optional[bool] = False,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
):
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
    try:
        payload = await request.json()
        task_id = payload.pop("task_id")
        if isinstance(task_id, int):
            task_activity_keys = set(TasksActivity._meta.fields_map) - {"id"}
            intersection = set(payload) & task_activity_keys
            update_data = {key: payload[key] for key in intersection}
            status = await TasksActivity.filter(task_id=task_id).update(**update_data)
            if status:
                await History.create(
                    task_id=task_id,
                    action=HistoryActionType.UPDATE,
                    description=f"Task {task_id} was updated: {', '.join(intersection)} were modified.",
                )
            return UpdateWebhookStatus(success=bool(status), message='task updated successfully' if status else 'Task Not Found')
        return UpdateWebhookStatus(success=False, message='Task Not Found')
    except Exception:
        return UpdateWebhookStatus(success=False, message='Task Not Found')


async def Initialize():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["app.models.db_task"]},
        routers=[],
    )
    await Tortoise.generate_schemas()


register_tortoise(
    app, db_url="sqlite://db.sqlite3", modules={"models": ["app.models.db_task"]}
)
