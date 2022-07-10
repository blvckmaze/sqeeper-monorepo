from django.db.models import Manager
from users.services import UserData
from datetime import datetime
from . import models


class NoteManager(Manager):
    def create_note(
        self,
        title: str,
        content: str = None,
        priority: int = None,
        reminder: str = None,
        owner: UserData = None,
        is_active: bool = True,
        updated_at: datetime = None,
    ) -> "models.Note":
        assert len(title.strip()) >= 2, "Title is too short or empty"

        note = models.Note(
            owner=owner,
            title=title,
            content=content,
            priority=priority,
            reminder=reminder,
            is_active=is_active,
            updated_at=updated_at,
        )

        note.save()

        return note
