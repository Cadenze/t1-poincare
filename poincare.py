from manim import *

class Homeomorphic(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u: np.array([
                1.5 * np.cos(u),
                1.5 * np.sin(u),
                1.5 * u
            ]), u_min=0, u_max=PI
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes)
        self.play(Write(cylinder))