import enum


class StatusTaskEnum(enum.Enum):
    BACKLOG = 1
    SPRINT_CANDIDATE = 2
    SPIRIT_BACKLOG = 3
    ON_GOING = 4
    REVIEW = 5
    QA = 6
    DOCUMENTATION = 7
    APPROVAL_BY_CUSTOMER = 8
    DONE = 9
