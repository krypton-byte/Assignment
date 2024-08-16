from datetime import date, datetime
from typing import Annotated, List, Optional
from fastapi import FastAPI, Form
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from app.api.responses import DeleteStatus, UpdateStatus

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


@app.route("/")
async def home():
    return "Hello World"


@app.post("/tasks-activity", response_model=TasksActivityModel)
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
    )
    return task_activity.to_model()


@app.get("/task-activity", response_model=List[TasksActivityModel])
async def read_task_activity(task_id: Optional[int] = None):
    if task_id is None:
        tasks = await TasksActivity.all()
    else:
        tasks = await TasksActivity.filter(task_id=task_id).all()

    return [task.to_model() for task in tasks]


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
            action=HistoryActionType.UPDATE
        )
    return UpdateStatus(success=bool(updated))


@app.delete("/task-activity")
async def delete_task_activity(task_id: Annotated[int, Form()]):
    deleted = TasksActivity.filter(task_id=task_id).delete()
    if deleted:
        await History.create(
            task_id=task_id,
            action=HistoryActionType.DELETE
        )
    return DeleteStatus(success=bool(deleted))


@app.get("/histories", response_model=List[HistoryModel])
async def histories(
    from_end: Optional[bool] = False,
    limit: Optional[int] = None,
):
    awaitable = History.all()
    if from_end:
        awaitable=awaitable.order_by('-id')
    if not (limit is None):
        awaitable=awaitable.limit(limit)
    return [
        history.to_model() for history in await awaitable
    ]



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
