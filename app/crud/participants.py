from __future__ import annotations

from app.crud.base import CRUDBase
from app.models.participant import Participant
from app.schemas.participant import ParticipantCreate
from app.schemas.participant import ParticipantUpdate


class CRUDParticipant(CRUDBase[Participant, ParticipantCreate, ParticipantUpdate]):
    pass


participant = CRUDParticipant(Participant)
