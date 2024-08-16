from datetime import date
from typing import Annotated, List, Optional
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
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


@app.route("/")
async def home(_: Request):
    """Redirects the root URL to the API documentation.

    :param _: The incoming HTTP request object.
    :type _: Request
    :return: A redirect response to the API documentation.
    :rtype: RedirectResponse
    """
    return RedirectResponse(
        "/docs"
    )

@app.get('/task/{task_id}', response_model=TaskResponse)
async def get_task(task_id: int):
    """Fetches a task by its ID and returns the task details.

    :param task_id: The ID of the task to be fetched.
    :type task_id: int
    :return: A response containing the task details if found, or an error message if not found.
    :rtype: TaskResponse
    """    
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
    """Creates a new task activity and records it in the database.

    :param task_name: The name of the task.
    :type task_name: Annotated[str, Form]
    :param task_description: A description of the task.
    :type task_description: Annotated[str, Form]
    :param activity_type_id: The ID of the activity type.
    :type activity_type_id: Annotated[int, Form]
    :param activity_type_name: The name of the activity type.
    :type activity_type_name: Annotated[ActivityName, Form]
    :param activity_group_sub_category_id: The ID of the activity group sub-category.
    :type activity_group_sub_category_id: Annotated[int, Form]
    :param activity_group_sub_category_name: The name of the activity group sub-category.
    :type activity_group_sub_category_name: Annotated[SubCategoryName, Form]
    :param activity_group_id: The ID of the activity group.
    :type activity_group_id: Annotated[int, Form]
    :param activity_group_name: The name of the activity group.
    :type activity_group_name: Annotated[GroupName, Form]
    :param stage_id: The ID of the stage.
    :type stage_id: Annotated[int, Form]
    :param stage_name: The name of the stage.
    :type stage_name: Annotated[StageName, Form]
    :param core_group_category_id: The ID of the core group category.
    :type core_group_category_id: Annotated[int, Form]
    :param core_group_category: The name of the core group category.
    :type core_group_category: Annotated[GroupCategory, Form]
    :param core_group_id: The ID of the core group.
    :type core_group_id: Annotated[int, Form]
    :param core_group_name: The name of the core group.
    :type core_group_name: Annotated[str, Form]
    :param due_date: The due date of the task.
    :type due_date: Annotated[date, Form]
    :param action_type: The action type related to the task.
    :type action_type: Annotated[str, Form]
    :param related_to: The entity to which the task is related.
    :type related_to: Annotated[str, Form]
    :param related_to_picture_id: The picture ID related to the task.
    :type related_to_picture_id: Annotated[int, Form]
    :param related_to_email: The email related to the task.
    :type related_to_email: Annotated[str, Form]
    :param related_to_company: The company related to the task.
    :type related_to_company: Annotated[str, Form]
    :param assign_to: The user to whom the task is assigned.
    :type assign_to: Annotated[str, Form]
    :param assign_to_picture_id: The picture ID of the assigned user.
    :type assign_to_picture_id: Annotated[int, Form]
    :param assign_to_email: The email of the assigned user.
    :type assign_to_email: Annotated[str, Form]
    :param assign_to_company: The company of the assigned user.
    :type assign_to_company: Annotated[str, Form]
    :param notes: Additional notes for the task.
    :type notes: Annotated[str, Form]
    :param status: The status of the task.
    :type status: Annotated[Status, Form]
    :param attachment_id: The ID of the attachment.
    :type attachment_id: Annotated[int, Form]
    :param attachments: The attachments related to the task.
    :type attachments: Annotated[int, Form]
    :param link_response_id: The response ID related to the task.
    :type link_response_id: Annotated[int, Form]
    :param link_object_id: The object ID related to the task.
    :type link_object_id: Annotated[int, Form]
    :param created_by: The user who created the task.
    :type created_by: Annotated[str, Form]
    :return: A response indicating whether the task creation was successful or not.
    :rtype: CreateTaskResponse
    """
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
    """Fetches a list of task activities from the database.

    :param from_end: If True, returns the task activities in reverse order (newest first). Defaults to False.
    :type from_end: Optional[bool], optional
    :param limit: Limits the number of task activities returned. If None, returns all. Defaults to None.
    :type limit: Optional[int], optional
    :param offset: Skips the first 'offset' number of task activities. Useful for pagination. Defaults to None.
    :type offset: Optional[int], optional
    :return: A list of task activities.
    :rtype: List[TasksActivityModel]
    """
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
    """Updates an existing task activity in the database.

    :param task_id: The ID of the task activity to update.
    :type task_id: Annotated[int, Form]
    :param task_name: The updated name of the task activity.
    :type task_name: Annotated[str, Form]
    :param task_description: The updated description of the task activity.
    :type task_description: Annotated[str, Form]
    :param activity_type_id: The updated ID of the activity type associated with the task activity.
    :type activity_type_id: Annotated[int, Form]
    :param activity_type_name: The updated name of the activity type associated with the task activity.
    :type activity_type_name: Annotated[ActivityName, Form]
    :param activity_group_sub_category_id: The updated ID of the sub-category of the activity group.
    :type activity_group_sub_category_id: Annotated[int, Form]
    :param activity_group_sub_category_name: The updated name of the sub-category of the activity group.
    :type activity_group_sub_category_name: Annotated[SubCategoryName, Form]
    :param activity_group_id: The updated ID of the activity group associated with the task activity.
    :type activity_group_id: Annotated[int, Form]
    :param activity_group_name: The updated name of the activity group associated with the task activity.
    :type activity_group_name: Annotated[GroupName, Form]
    :param stage_id: The updated ID of the stage associated with the task activity.
    :type stage_id: Annotated[int, Form]
    :param stage_name: The updated name of the stage associated with the task activity.
    :type stage_name: Annotated[StageName, Form]
    :param core_group_category_id: The updated ID of the core group category associated with the task activity.
    :type core_group_category_id: Annotated[int, Form]
    :param core_group_category: The updated category of the core group associated with the task activity.
    :type core_group_category: Annotated[GroupCategory, Form]
    :param core_group_id: The updated ID of the core group associated with the task activity.
    :type core_group_id: Annotated[int, Form]
    :param core_group_name: The updated name of the core group associated with the task activity.
    :type core_group_name: Annotated[str, Form]
    :param due_date: The updated due date of the task activity.
    :type due_date: Annotated[date, Form]
    :param action_type: The updated action type associated with the task activity.
    :type action_type: Annotated[str, Form]
    :param related_to: The updated related information associated with the task activity.
    :type related_to: Annotated[str, Form]
    :param related_to_picture_id: The updated ID of the related picture associated with the task activity.
    :type related_to_picture_id: Annotated[int, Form]
    :param related_to_email: The updated email address related to the task activity.
    :type related_to_email: Annotated[str, Form]
    :param related_to_company: The updated company related to the task activity.
    :type related_to_company: Annotated[str, Form]
    :param assign_to: The updated assignee of the task activity.
    :type assign_to: Annotated[str, Form]
    :param assign_to_picture_id: The updated ID of the assignee's picture associated with the task activity.
    :type assign_to_picture_id: Annotated[int, Form]
    :param assign_to_email: The updated email address of the assignee associated with the task activity.
    :type assign_to_email: Annotated[str, Form]
    :param assign_to_company: The updated company of the assignee associated with the task activity.
    :type assign_to_company: Annotated[str, Form]
    :param notes: The updated notes related to the task activity.
    :type notes: Annotated[str, Form]
    :param status: The updated status of the task activity.
    :type status: Annotated[Status, Form]
    :param attachment_id: The updated ID of the attachment associated with the task activity.
    :type attachment_id: Annotated[int, Form]
    :param attachments: The updated number of attachments associated with the task activity.
    :type attachments: Annotated[int, Form]
    :param link_response_id: The updated ID of the linked response associated with the task activity.
    :type link_response_id: Annotated[int, Form]
    :param link_object_id: The updated ID of the linked object associated with the task activity.
    :type link_object_id: Annotated[int, Form]
    :param created_by: The updated creator of the task activity.
    :type created_by: Annotated[str, Form]
    :return: Status of the update operation.
    :rtype: UpdateStatus
    """
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
    """Deletes a task activity from the database.

    :param task_id: The ID of the task activity to delete.
    :type task_id: Annotated[int, Form]
    :return: Status of the delete operation.
    :rtype: DeleteStatus
    """
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
    """Fetches a list of history records from the database.

    :param from_end: If True, fetch records in descending order based on ID. Defaults to False.
    :type from_end: Optional[bool], optional
    :param limit: Maximum number of records to fetch. Defaults to None (fetch all).
    :type limit: Optional[int], optional
    :param offset: Number of records to skip before fetching. Defaults to None (no skipping).
    :type offset: Optional[int], optional
    :return: List of history records, serialized as HistoryModel.
    :rtype: List[HistoryModel]
    """
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
    """Endpoint to handle webhook updates for task activities.

    This endpoint expects a JSON payload containing at least a 'task_id' field,
    and other fields representing updated data for the task activity.

    :param request: The incoming HTTP request object containing JSON payload.
    :type request: Request
    :return: Response indicating the success or failure of the update operation.
    :rtype: UpdateWebhookStatus
    """
    try:
        payload = await request.json()
        task_id = payload.pop("task_id")
        if isinstance(task_id, int):
            task_activity_keys = set(TasksActivity._meta.fields_map) - {"task_id"}
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




register_tortoise(
    app, db_url="sqlite://db.sqlite3", modules={"models": ["app.models.db_task"]}
)
