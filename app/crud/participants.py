from crud.base import CRUDBase
from models.participant import Participant
from schemas.participant import ParticipantCreate, ParticipantUpdate


class CRUDParticipant(CRUDBase[Participant, ParticipantCreate, ParticipantUpdate]):
    pass


participant = CRUDParticipant(Participant)
