import enum


class State(enum.Enum):
    none = "none"   # Для фильтра тайтлов, у которых нет заданного пользователем статуса
    planned = "planned"
    in_progress = "in_progress"
    abandoned = "abandoned"
    completed = "completed"
