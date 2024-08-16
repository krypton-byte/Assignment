from enum import Enum


class ActivityName(Enum):
    TASKS = "tasks"
    EMAIL = "email"
    CHATS = "chats"
    NOTES = "notes"
    MEETINGS = "meetings"
    CALLS = "calls"
    LOGS = "logs"


class SubCategoryName(Enum):
    CUSTOMER_CONTACT = "customer contact"
    PARTNER_CONTACT = "partner contact"
    EMPLOYEE_CONTACT = "emplopyee contact"
    


class GroupName(Enum):
    CONTACT = "contact"
    ENGAGEMENT = "engagement"
    PRODUCTS = "products"
    PARTNERS = "partners"
    QUOTES = "quotes"
    NOTES = "notes"
    STAGE_HISTORY = "stage history"
    APPROVAL_HISTORY = "approval history"
    FILES = "files"


class StageName(Enum):
    NEW = "new"
    PROPOSAL_CREATION = "proposal creation"
    PRESENTATION = "presentation"
    NEGOTIATION = "negotiation"
    CLOSED = "closed"
    MARK_AS_COMPLETED = "mark as completed"


class GroupCategory(Enum):
    CONTACTS = "contacts"
    LEADS = "leads"
    OPPORTUNITY = "opportunity"
    CUSTOMERS = "customers"


class Status(Enum):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"
    WAITING_ON = "waiting on"
    DIFFERED = "differed"


class HistoryActionType(Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
