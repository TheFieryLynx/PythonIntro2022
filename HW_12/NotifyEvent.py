#!/usr/bin/env python3

class NotifyEvent(asyncio.Event):
	def set(self, _name=None):
		self.name = _name
		