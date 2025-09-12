__version__ = '0.1.0'

from .decorators import handle_events
from .models import DomainEvent, DomainEventHandler

__all__ = (
    'DomainEvent',
    'DomainEventHandler',
    'handle_events',
)
