from __future__ import annotations

from crud.base import CRUDBase
from models.participant import Participant
from schemas.participant import ParticipantCreate
from schemas.participant import ParticipantUpdate


class CRUDParticipant(CRUDBase[Participant, ParticipantCreate, ParticipantUpdate]):
    pass


participant = CRUDParticipant(Participant)
