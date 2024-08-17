from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field

from ..models.enum import (
    ActivityName,
    GroupCategory,
    GroupName,
    StageName,
    Status,
    SubCategoryName,
)


class TasksActivityBody(BaseModel):
    task_id: int = Field()
    task_name: Optional[str] = Field(default=None)
    task_description: Optional[str] = Field(default=None)
    activity_type_id: Optional[int] = Field(default=None)
    activity_type_name: Optional[ActivityName] = Field(default=None)
    activity_group_sub_category_id: Optional[int] = Field(default=None)
    activity_group_sub_category_name: Optional[SubCategoryName] = Field(default=None)
    activity_group_id: Optional[int] = Field(default=None)
    activity_group_name: Optional[GroupName] = Field(default=None)
    stage_id: Optional[int] = Field(default=None)
    stage_name: Optional[StageName] = Field(default=None)
    core_group_category_id: Optional[int] = Field(default=None)
    core_group_category: Optional[GroupCategory] = Field(default=None)
    core_group_id: Optional[int] = Field(default=None)
    core_group_name: Optional[str] = Field(default=None)
    due_date: Optional[date] = Field(default=None)
    action_type: Optional[str] = Field(default=None)
    related_to: Optional[str] = Field(default=None)
    related_to_picture_id: Optional[int] = Field(default=None)
    related_to_email: Optional[str] = Field(default=None)
    related_to_company: Optional[str] = Field(default=None)
    assign_to: Optional[str] = Field(default=None)
    assign_to_picture_id: Optional[int] = Field(default=None)
    assign_to_email: Optional[str] = Field(default=None)
    assign_to_company: Optional[str] = Field(default=None)
    notes: Optional[str] = Field(default=None)
    status: Optional[Status] = Field(default=None)
    attachment_id: Optional[int] = Field(default=None)
    attachments: Optional[str] = Field(default=None)
    link_response_id: Optional[int] = Field(default=None)
    link_object_id: Optional[int] = Field(default=None)
    created_by: Optional[str] = Field(default=None)
    created_on: Optional[datetime] = Field(default=None)
