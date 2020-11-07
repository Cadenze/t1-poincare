from manim import *
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)

        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class ThreeDFunctionPlot(ThreeDScene):
    def construct(self):
        resolution_fa = 22
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_plane(u, v):
            x = u
            y = v
            z = 0
            return np.array([x, y, z])

        plane = ParametricSurface(
            param_plane,
            resolution=(resolution_fa, resolution_fa),
            v_min=-2,
            v_max=+2,
            u_min=-2,
            u_max=+2,
        )
        plane.scale_about_point(2, ORIGIN)

        def param_gauss(u, v):
            x = u
            y = v
            d = np.sqrt(x * x + y * y)
            sigma, mu = 0.4, 0.0
            z = np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])

        gauss_plane = ParametricSurface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_min=-2,
            v_max=+2,
            u_min=-2,
            u_max=+2,
        )

        gauss_plane.scale_about_point(2, ORIGIN)
        gauss_plane.set_style(fill_opacity=1)
        gauss_plane.set_style(stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(GREEN, BLUE, opacity=0.1)

        axes = ThreeDAxes()

        self.add(axes)
        self.play(Write(plane))
        self.play(Transform(plane, gauss_plane))
        self.wait()