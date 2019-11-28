from Component.PhysicsComponent import PhysicsComponent
from Component.PositionComponent import PositionComponent
from Entity.Entity import Entity


class WaterDropletEntity(Entity):
	def __init__(self, x, y, wh):
		super().__init__()
		self.position_component = PositionComponent(self.id, x, y, wh, wh)
		self.physics_component = PhysicsComponent(self.id, 1)
		self.components.append(self.position_component)
		self.components.append(self.physics_component)

