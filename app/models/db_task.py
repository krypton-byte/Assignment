from pydantic import ClickHouseDsn
from tortoise import Model, Tortoise, fields, run_async
from .enum import (
    ActivityName,
    GroupCategory,
    GroupName,
    HistoryActionType,
    StageName,
    SubCategoryName,
    Status,
)
from .task import HistoryModel, TasksActivityModel
# from tortoise.fields.data import CharEnumType


class TasksActivity(Model):
    task_id = fields.IntField(primary_key=True)
    task_name = fields.TextField()
    task_description = fields.TextField()
    activity_type_id = fields.IntField()
    activity_type_name = fields.CharEnumField(ActivityName)
    activity_group_sub_category_id = fields.IntField()
    activity_group_sub_category_name = fields.CharEnumField(SubCategoryName)
    activity_group_id = fields.IntField()
    activity_group_name = fields.CharEnumField(GroupName)
    stage_id = fields.IntField()
    stage_name = fields.CharEnumField(StageName)
    core_group_category_id = fields.IntField()
    core_group_category = fields.CharEnumField(GroupCategory)
    core_group_id = fields.IntField()
    core_group_name = fields.TextField()
    due_date = fields.DateField()
    action_type = fields.CharField(max_length=255)
    related_to = fields.CharField(max_length=255)
    related_to_picture_id = fields.IntField()
    related_to_email = fields.CharField(max_length=255)
    related_to_company = fields.CharField(max_length=255)
    assign_to = fields.CharField(max_length=255)
    assign_to_picture_id = fields.IntField()
    assign_to_email = fields.CharField(max_length=255)
    assign_to_company = fields.CharField(max_length=255)
    notes = fields.TextField()
    status = fields.CharEnumField(Status)
    attachment_id = fields.IntField()
    attachments = fields.CharField(max_length=255)
    link_object_id = fields.IntField()
    link_response_id = fields.IntField()
    created_by = fields.CharField(max_length=255)
    created_on = fields.DatetimeField(auto_now=True)

    def to_model(self):
        return TasksActivityModel(
            task_id=self.task_id,
            task_name=self.task_name,
            task_description=self.task_description,
            activity_type_id=self.activity_type_id,
            activity_type_name=self.activity_type_name,
            activity_group_sub_category_id=self.activity_group_sub_category_id,
            activity_group_sub_category_name=self.activity_group_sub_category_name,
            activity_group_id=self.activity_group_id,
            activity_group_name=self.activity_group_name,
            stage_id=self.stage_id,
            stage_name=self.stage_name,
            core_group_category_id=self.core_group_category_id,
            core_group_category=self.core_group_category,
            core_group_id=self.core_group_id,
            core_group_name=self.core_group_name,
            due_date=self.due_date,
            action_type=self.action_type,
            related_to=self.related_to,
            related_to_picture_id=self.related_to_picture_id,
            related_to_email=self.related_to_email,
            related_to_company=self.related_to_company,
            assign_to=self.assign_to,
            assign_to_picture_id=self.assign_to_picture_id,
            assign_to_email=self.assign_to_email,
            assignt_to_company=self.assign_to_company,
            notes=self.notes,
            status=self.status,
            attachment_id=self.attachment_id,
            attachments=self.attachments,
            link_response_id=self.link_response_id,
            link_object_id=self.link_object_id,
            created_by=self.created_by,
            created_on=self.created_on,
        )


class History(Model):
    id = fields.IntField(primary_key=True)
    task_id = fields.IntField()
    action = fields.CharEnumField(HistoryActionType)
    time = fields.DatetimeField(auto_now=True)
    def to_model(self):
        return HistoryModel(
            id=self.id,
            task_id=self.task_id,
            action=self.action,
            time=self.time
        )

async def InitializeDB():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["app.models.db_task"]},
        routers=[],
    )
    await Tortoise.generate_schemas()


def Initialize():
    run_async(InitializeDB())
