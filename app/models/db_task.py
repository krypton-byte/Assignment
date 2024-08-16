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


class TasksActivity(Model):
    class Meta:  # type: ignore
        table = "TasksActivity"

    task_id = fields.IntField(primary_key=True, source_field="TaskID")
    task_name = fields.TextField(source_field="task_name")
    task_description = fields.TextField(source_field="TaskDescription")
    activity_type_id = fields.IntField(source_field="ActivityTypeID")
    activity_type_name = fields.CharEnumField(
        ActivityName, source_field="ActivityTypeName"
    )
    activity_group_sub_category_id = fields.IntField(
        source_field="ActivityGroupSubCategoryId"
    )
    activity_group_sub_category_name = fields.CharEnumField(
        SubCategoryName, source_field="ActivityGroupSubCategoryName"
    )
    activity_group_id = fields.IntField(source_field="ActivityGroupID")
    activity_group_name = fields.CharEnumField(
        GroupName, source_field="ActivityGroupName"
    )
    stage_id = fields.IntField(source_field="StageID")
    stage_name = fields.CharEnumField(StageName, source_field="StageName")
    core_group_category_id = fields.IntField(source_field="CoreGroupCategoryID")
    core_group_category = fields.CharEnumField(
        GroupCategory, source_field="CoreGroupCategory"
    )
    core_group_id = fields.IntField(source_field="CoreGroupID")
    core_group_name = fields.TextField(source_field="CoreGroupName")
    due_date = fields.DateField(source_field="DueDate")
    action_type = fields.CharField(max_length=255, source_field="ActionType")
    related_to = fields.CharField(max_length=255, source_field="RelatedTo")
    related_to_picture_id = fields.IntField(source_field="RelatedToPictureID")
    related_to_email = fields.CharField(max_length=255, source_field="RelatedToEmail")
    related_to_company = fields.CharField(
        max_length=255, source_field="RelatedToCompany"
    )
    assign_to = fields.CharField(max_length=255, source_field="AssignTo")
    assign_to_picture_id = fields.IntField(source_field="AssignToPictureID")
    assign_to_email = fields.CharField(max_length=255, source_field="AssignToEmail")
    assign_to_company = fields.CharField(max_length=255, source_field="AssignToCompany")
    notes = fields.TextField(source_field="Notes")
    status = fields.CharEnumField(Status, source_field="Status")
    attachment_id = fields.IntField(source_field="AttachmentID")
    attachments = fields.CharField(max_length=255, source_field="Attachments")
    link_object_id = fields.IntField(source_field="LinkObjectID")
    link_response_id = fields.IntField(source_field="LinkResponseID")
    created_by = fields.CharField(max_length=255, source_field="CreatedBy")
    created_on = fields.DatetimeField(auto_now=True, source_field="CreatedOn")

    def to_model(self) -> TasksActivityModel:
        """Converts TasksActivity instance to TasksActivityModel.

        :return: Converted TasksActivityModel instance
        :rtype: TasksActivityModel
        """    
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
    class Meta:  # type: ignore
        table = "History"

    id = fields.IntField(primary_key=True)
    task_id = fields.IntField()
    action = fields.CharEnumField(HistoryActionType)
    description = fields.TextField()
    time = fields.DatetimeField(auto_now=True)
    def to_model(self) -> HistoryModel:
        """Converts History instance to HistoryModel.

        :return: Converted HistoryModel instance
        :rtype: HistoryModel
        """
        return HistoryModel(
            id=self.id,
            task_id=self.task_id,
            action=self.action,
            time=self.time,
            description=self.description,
        )


async def InitializeDB():
    """Initialize Tortoise ORM.

    This function initializes Tortoise ORM with SQLite database connection
    and generates schemas based on specified models.

    :return: None
    """
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["app.models.db_task"]},
        routers=[],
    )
    await Tortoise.generate_schemas()


def Initialize():
    run_async(InitializeDB())
