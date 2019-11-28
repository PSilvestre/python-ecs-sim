import functools
from concurrent.futures.thread import ThreadPoolExecutor

from PhysicsUtils import square_collide, combine_vectors


class PhysicsSystem:
    def __init__(self, positions_components, physics_components, boundary_x, boundary_y):
        self.positions_components = positions_components
        self.physics_components = physics_components
        self.bound_x = boundary_x
        self.bound_y = boundary_y
        self.num_threads = 1
        self.thread_pool = ThreadPoolExecutor(max_workers=self.num_threads)

    def step(self, delta_millis):
        delta_sec = delta_millis / 1000
        length = len(self.positions_components)
        perThread = int(length / self.num_threads)
        for i in range(self.num_threads):
            if i != self.num_threads -1:
                self.thread_pool.submit(self.update_range(delta_sec, i*perThread, i+1*perThread))
            else:
                self.thread_pool.submit(self.update_range(delta_sec, i*perThread, length))

    def update_range(self, delta_sec, start, end):
        for i in range(start, end):
            self.update_index(delta_sec, i)

    def update_index(self, delta_sec, i):
        pos = self.positions_components[i]
        phy = self.physics_components[i]
        phy.ax = 0
        phy.ay = 0
        # gravity
        phy.forces.append((phy.mass * 0.01, 0, 1))

        # collide particles
        for j in range(len(self.positions_components)):
            pos_other = self.positions_components[j]
            colliding, d1x, d1y, d2x, d2y = square_collide(pos, pos_other)
            if colliding:
                if pos.ownerId != pos_other.ownerId:
                    self.bounce(delta_sec, phy)

        # Collide with walls
        if pos.x < 0 or pos.x + pos.w > self.bound_x or pos.y < 0 or pos.y + pos.h >= self.bound_y:
            self.bounce(delta_sec, phy)
            #if pos.y + pos.h > self.bound_y:
                #phy.forces.append((phy.mass * 9, 0, -1))
               # pos.y = self.bound_y - pos.h


        #drag
        vel_mag = (abs(phy.vx) + abs(phy.vy)) / delta_sec
        mag_adj = phy.mass * vel_mag
        if mag_adj != 0:
            x_comp = (-phy.vx / delta_sec) /  vel_mag
            y_comp = (-phy.vy / delta_sec) / vel_mag
            phy.forces.append((0.001 * (1+mag_adj) * (1+mag_adj), x_comp, y_comp))


        # reduce and apply forces
        mag, xc, yc = functools.reduce(combine_vectors,phy.forces)
        phy.forces = []
        print((mag, xc, yc))

        # recalc vel and pos
        phy.ax = mag * xc
        phy.ay = mag * yc

        phy.vx += phy.ax * delta_sec
        phy.vy += phy.ay * delta_sec

        #Friction
        phy.vx = 0.95 * phy.vx
        phy.vy = 0.95 * phy.vy

        pos.x += phy.vx * delta_sec
        pos.y += phy.vy * delta_sec

    def bounce(self, delta_sec, phy):

        deacceleration_mag = (abs(phy.vx) + abs(phy.vy)) / delta_sec
        mag = phy.mass * deacceleration_mag
        if deacceleration_mag != 0:
            x_comp = (-phy.vx / delta_sec) / deacceleration_mag
            y_comp = (-phy.vy / delta_sec) / deacceleration_mag
            phy.forces.append((mag, x_comp, y_comp))
        phy.vx *= -0.7
        phy.vy *= -0.7




