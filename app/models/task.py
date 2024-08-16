from dataclasses import field
from pydantic import BaseModel, Field
from datetime import date, datetime
from .enum import (
    ActivityName,
    GroupCategory,
    GroupName,
    StageName,
    SubCategoryName,
    Status,
)


class TasksActivityModel(BaseModel):
    task_id: int = Field()
    task_name: str = Field()
    task_description: str = Field()
    activity_type_id: int = Field()
    activity_type_name: ActivityName = Field()
    activity_group_sub_category_id: int = Field()
    activity_group_sub_category_name: SubCategoryName = Field()
    activity_group_id: int = Field()
    activity_group_name: GroupName = Field()
    stage_id: int = Field()
    stage_name: StageName = Field()
    core_group_category_id: int = Field()
    core_group_category: GroupCategory = Field()
    core_group_id: int = Field()
    core_group_name: str = Field()
    due_date: date = Field()
    action_type: str = Field()
    related_to: str = Field()
    related_to_picture_id: int = Field()
    related_to_email: str = Field()
    related_to_company: str = Field()
    assign_to: str = Field()
    assign_to_picture_id: int = Field()
    assign_to_email: str = Field()
    assignt_to_company: str = Field()
    notes: str = Field()
    status: Status = Field()
    attachment_id: int = Field()
    attachments: str = Field()
    link_response_id: int = Field()
    link_object_id: int = Field()
    created_by: str = Field()
    created_on: datetime = Field()
