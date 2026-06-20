# Camera & 3D

## Moving / zooming the camera (2D)

Subclass `MovingCameraScene` to pan and zoom `self.camera.frame`:

```python
class Zoomed(MovingCameraScene):
    def construct(self):
        dot = Dot(RIGHT * 3)
        self.add(dot)
        self.play(self.camera.frame.animate.scale(0.4).move_to(dot))  # zoom in on dot
        self.play(self.camera.frame.animate.scale(2.5).move_to(ORIGIN))  # zoom back out
```

- `self.camera.frame` is a mobject — animate `.scale()` (zoom; <1 in, >1 out), `.move_to()` (pan), `.rotate()`.
- `self.camera.frame.save_state()` then `Restore(self.camera.frame)` to return to a saved view.
- Make the camera follow a moving mobject with an updater: `self.camera.frame.add_updater(lambda f: f.move_to(dot))`.

## Background color

```python
self.camera.background_color = "#1a1a2e"   # set per scene, in construct()
```

Or globally via `config.background_color`.

## 3D

Subclass `ThreeDScene`:

```python
class Surf(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: axes.c2p(u, v, u**2 - v**2),
            u_range=[-2, 2], v_range=[-2, 2],
            resolution=(30, 30),
        )
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes), Create(surface))
        self.begin_ambient_camera_rotation(rate=0.2)   # slow auto-spin
        self.wait(4)
        self.stop_ambient_camera_rotation()
```

- `set_camera_orientation(phi=, theta=, zoom=)` — `phi` tilts from top-down, `theta` rotates around vertical.
- `move_camera(phi=, theta=, run_time=)` animates the viewpoint.
- `begin_ambient_camera_rotation(rate=)` / `stop_ambient_camera_rotation()` for a turntable spin.
- 3D mobjects: `Sphere`, `Cube`, `Prism`, `Cone`, `Cylinder`, `ThreeDAxes`, `Surface`, `ParametricFunction`.
- Keep 2D labels facing the viewer with `self.add_fixed_in_frame_mobjects(label)`.

3D renders are slower — iterate at `-ql`.
