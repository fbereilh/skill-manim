---
name: manim-best-practices
description: Best practices for Manim - programmatic math/explainer animation in Python (3Blue1Brown style). Use when creating or editing Manim scenes, rendering videos, or building animated explainers.
metadata:
  tags: manim, video, python, animation, math, 3blue1brown
---

## When to use

Use this skill whenever dealing with Manim code to obtain domain-specific knowledge. Manim (ManimCommunity / `manim`) renders Python `Scene` classes to MP4. It is the engine behind 3Blue1Brown videos — best for math, diagrams, plots, and step-by-step explainers.

This skill targets **ManimCommunity (`manim`)**, not the older `manimgl` / `3b1b/manim`. Their APIs differ; do not mix.

## Requirements

This skill assumes the `manim` CLI (ManimCommunity) is on `PATH`. Check with `manim --version`. The install method does not matter. Run the plain `manim …` commands in this skill as written. If the project keeps manim inside an environment (a venv, `devbox run --`, `pixi run`, `docker run …`), apply that same wrapper to each `manim` call.

You also need an `ffmpeg` binary on `PATH` for encoding; most install methods include it. LaTeX is optional. You need it only for `Tex` / `MathTex` (typeset equations), since plain `Text()` uses Pango. See [rules/math.md](rules/math.md).

No `manim` yet? Any route works: a conda/pixi env (`pixi add manim`), a Nix/devbox env, the `manimcommunity/manim` Docker image, or pip into a venv. With pip, some platforms also need the system `cairo` dev lib plus `pkg-config`, so a method that bundles cairo/pango/ffmpeg saves you the compile step.

## New project setup

A scene is one `.py` file; no scaffolding needed. Create `scene.py`, define a `Scene` subclass, and render it by class name (see *Rendering*).

## Scene anatomy

A scene is a class subclassing `Scene`; all animation goes in `construct()`. The file can hold many scenes — you render one by name.

```python
from manim import *


class HelloWorld(Scene):
    def construct(self):
        title = Text("Hello World", font_size=72)
        self.play(Write(title))          # animate it on
        self.wait(0.5)                   # hold
        self.play(FadeOut(title))
```

Mental model vs frame-based tools (Remotion): you do NOT compute per-frame values from a clock. You declare **mobjects** (the things on screen) and drive them through **animations** with `self.play(...)`. Time is the sum of each `play`/`wait`'s `run_time`. Order in `construct()` IS the timeline.

- `self.add(m)` / `self.remove(m)` — put a mobject on screen instantly (no animation).
- `self.play(Anim, run_time=secs, rate_func=...)` — animate. Multiple anims in one `play` run simultaneously.
- `self.wait(secs)` — hold the current frame.
- `mobject.animate.<change>` — turn any property change into an animation: `self.play(sq.animate.shift(RIGHT).set_color(BLUE))`.

## Mobjects & layout

Build visuals from `Circle`, `Square`, `Rectangle`, `Ellipse`, `Arc`, `Line`, `Dot`, `Polygon`, `Text`, `VGroup`, etc. See [rules/mobjects.md](rules/mobjects.md) for the catalog, styling (`fill_opacity`, `stroke_width`, color), and positioning (`.move_to`, `.next_to`, `.shift`, `.to_edge`, `.arrange`, directional constants `UP/DOWN/LEFT/RIGHT/ORIGIN`).

Group related parts with `VGroup(a, b, c)` and animate/position them together. Coordinates are scene units: origin at center, default frame is ~14.2 units wide × 8 tall.

## Animating

`self.play()` takes one or more animations. Two styles:

```python
# 1. Named animation classes
self.play(Create(circle), FadeIn(label), run_time=1)
# 2. The .animate syntax — animate the result of any method call
self.play(circle.animate.scale(2).set_fill(RED, 0.5))
```

Common animations: `Create`, `Write`, `FadeIn`/`FadeOut` (accept `shift=`), `Transform(a, b)` / `ReplacementTransform`, `GrowFromCenter`, `Indicate`, `Flash`, `MoveAlongPath`. See [rules/animations.md](rules/animations.md).

Sequencing helpers: `LaggedStart(*anims, lag_ratio=)`, `Succession(*anims)`, `AnimationGroup(*anims)`. See [rules/timing.md](rules/timing.md).

## Timing & easing

Control feel with `run_time` (seconds) and `rate_func`. Defaults to `smooth` (ease in/out). Others: `linear`, `rush_into`, `rush_from`, `there_and_back`, `ease_out_bounce`, `wiggle`. See [rules/timing.md](rules/timing.md).

There is no `spring()`. For bouncy/overshoot feel use `rate_func=rate_functions.ease_out_back` or `ease_out_bounce`.

## Rendering

Render one scene by class name. Quality flag picks resolution/fps:

```bash
manim -ql scene.py SceneName     # 480p15  — fast iteration (use this while building)
manim -qm scene.py SceneName     # 720p30
manim -qh scene.py SceneName     # 1080p60 — final
```

Output lands in `media/videos/<file>/<res>/SceneName.mp4`. Useful flags:

- `-p` preview (auto-open the file when done)
- `-s` render only the **last frame** as a PNG — fast sanity check of layout/colors
- `--format gif` output a GIF instead of mp4
- `-a` render every scene in the file
- `-o name` override output filename

See [rules/render.md](rules/render.md) for transparency, GIFs, sections, and resolution overrides.

## Preview / iteration loop

Manim has no live studio. Iterate with: render `-ql` (or `-s` for a still) → look at the file → adjust. For a quick layout check without rendering the full timeline, `-s` is much faster than `-ql`.

## Math & LaTeX

For typeset equations use `MathTex(r"...")` / `Tex(r"...")` — requires a LaTeX install. For plain styled text use `Text` / `MarkupText` (no LaTeX). See [rules/math.md](rules/math.md).

## Graphs, axes & functions

Plotting functions, axes, number lines, and coordinate planes is Manim's core strength (the 3Blue1Brown look). See [rules/graphs.md](rules/graphs.md) for `Axes`, `plot`, `NumberPlane`, `get_graph_label`, and animating along a curve.

## Text & fonts

`Text` (Pango, supports system fonts, weights, `t2c` color maps) vs `MarkupText` (Pango markup) vs `MathTex` (LaTeX). See [rules/text.md](rules/text.md).

## Camera & 3D

Move/zoom the camera with `MovingCameraScene`; build 3D with `ThreeDScene`, `ThreeDAxes`, `Surface`. See [rules/camera.md](rules/camera.md).

## Updaters (frame-by-frame logic)

When you genuinely need per-frame behavior (a label tracking a moving dot, a value counter), use `add_updater` and `ValueTracker` / `always_redraw`. See [rules/updaters.md](rules/updaters.md).
