from django.conf import settings

HARD_DELETE = 0
SOFT_DELETE = 1
SOFT_DELETE_CASCADE = 2
HARD_DELETE_NOCASCADE = 3
NO_DELETE = 4

DELETED_INVISIBLE = 10
DELETED_VISIBLE_BY_FIELD = DELETED_VISIBLE_BY_PK = 11
DELETED_ONLY_VISIBLE = 12
DELETED_VISIBLE = 13
FIELD_NAME = getattr(settings, 'SAFE_DELETE_FIELD_NAME', 'deleted')
DELETED_BY_CASCADE_FIELD_NAME = getattr(settings, 'SAFE_DELETE_CASCADED_FIELD_NAME', 'deleted_by_cascade')