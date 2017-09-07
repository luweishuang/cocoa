from cocoa.sessions.session import Session as BaseSession
from core.event import Event

class Session(BaseSession):
    def offer(self, offer):
        """Send an offer event.

        Args:
            offer ({'price': float, 'sides', str})

        Returns:
            OfferEvent

        """
        return Event.OfferEvent(self.agent, offer, time=self.timestamp())

    def accept(self, data):
        return Event.AcceptEvent(self.agent, time=self.timestamp(), data=data)

    def mark_deal_agreed(self, data):
        return Event.AcceptEvent(self.agent, time=self.timestamp(), data=data)

    def reject(self):
        return Event.RejectEvent(self.agent, time=self.timestamp())

    def quit(self):
        return Event.QuitEvent(self.agent, time=self.timestamp())
