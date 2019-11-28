from Component.Component import Component


class PositionComponent(Component):
	def __init__(self, ownerId):
		super().__init__(ownerId)
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0
	def __init__(self,ownerId, x, y, w, h):
		super().__init__(ownerId)
		self.x = x
		self.y = y
		self.w = w
		self.h = h