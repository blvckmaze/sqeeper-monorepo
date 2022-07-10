from .models import Note
from users.models import User
from datetime import datetime
from dataclasses import dataclass
from users.services import UserData
from rest_framework import exceptions
from django.shortcuts import get_object_or_404


@dataclass
class NoteData:
    title: str
    id: int = None
    created: datetime = None
    description: str = None
    priority: int = None
    reminder: datetime = None
    owner: UserData = (None,)
    is_active: bool = True
    updated_at: datetime = None

    @classmethod
    def from_instance(cls, note: "Note") -> "NoteData":
        return cls(
            id=note.id,
            owner=note.owner,
            title=note.title,
            created=note.created.strftime("%d %b %H:%M:%S"),
            description=note.description,
            priority=note.priority,
            reminder=note.reminder.strftime("%d %b %H:%M:%S")
            if note.reminder
            else note.reminder,
            is_active=note.is_active,
            updated_at=note.updated_at.strftime("%d %b %H:%M:%S")
            if note.updated_at
            else note.updated_at,
        )


def create_note(user: "User", note: "NoteData") -> NoteData:
    instance = Note(
        owner=user,
        title=note.title,
        created=note.created,
        description=note.description,
        priority=note.priority,
        reminder=note.reminder,
        is_active=note.is_active,
    )

    instance.save()

    return NoteData.from_instance(instance)


def update_note(user: "User", note_id: int, note_data: "NoteData") -> NoteData:
    user_note = get_object_or_404(Note, pk=note_id)

    if user.id != user_note.owner.id:
        raise exceptions.PermissionDenied("You're not the owner of a note")

    assert note_data.title is not None, "Title cannot be empty"

    user_note.title = note_data.title
    user_note.description = note_data.description
    user_note.priority = note_data.priority if note_data.priority else 1
    user_note.reminder = note_data.reminder
    user_note.updated_at = datetime.now()

    return user_note.save()


def delete_note(user: "User", note_id: int) -> NoteData:
    user_note = get_object_or_404(Note, pk=note_id)

    if user.id != user_note.owner.id:
        raise exceptions.PermissionDenied("You're not the owner of a note")

    return user_note.delete()


def get_user_note(note_id: int) -> NoteData:
    user_note = get_object_or_404(Note, pk=note_id)

    return NoteData.from_instance(user_note)
