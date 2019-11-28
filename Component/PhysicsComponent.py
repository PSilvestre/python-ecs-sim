from Component.Component import Component


class PhysicsComponent(Component):
	def __init__(self, ownerId):
		super().__init__(ownerId)
		self.forces = []
		self.mass = 0
		self.vx = 0
		self.vy = 0
		self.ax = 0
		self.ay = 0

	def __init__(self,ownerId,  mass):
		super().__init__(ownerId)
		self.forces = []
		self.mass = mass
		self.vx = 0
		self.vy = 0
		self.ax = 0
		self.ay = 0
