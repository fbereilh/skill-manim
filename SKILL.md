---
name: manim-best-practices
description: Best practices for Manim - programmatic math/explainer animation in Python (3Blue1Brown style). Use when creating or editing Manim scenes, rendering videos, or building animated explainers.
metadata:
  tags: manim, video, python, animation, math, 3blue1brown
---

## When to use

Use this skill whenever dealing with Manim code to obtain domain-specific knowledge. Manim (ManimCommunity / `manim`) renders Python `Scene` classes to MP4. It is the engine behind 3Blue1Brown videos — best for math, diagrams, plots, and step-by-step explainers.

This skill targets **ManimCommunity (`manim`)**, not the older `manimgl` / `3b1b/manim`. Their APIs differ; do not mix.

## New project setup

Manim needs Python plus native pieces — the **cairo**/**pango** C libraries (for `pycairo`/`manimpango`) and an **ffmpeg** binary. The painful part is `pycairo`: it has no macOS-arm wheel, so a pip install compiles it from source and needs the cairo headers + `cairo.pc`. The clean, reproducible fix is **devbox** (Nix), which ships a prebuilt `manim` with all native deps bundled — no brew, no pip compile, no system pollution.

Create `devbox.json`:

```json
{
  "packages": ["manim@latest", "ffmpeg@latest"],
  "shell": { "init_hook": ["echo 'manim env ready'"] }
}
```

Then:

```bash
devbox install                                   # pulls prebuilt manim + deps from the nix cache
devbox run -- manim -ql scene.py SceneName       # render inside the env
# or: devbox shell   (drop into the env, then run manim directly)
```

This avoids the `pycairo`-from-source trap entirely — Nix's manim is already linked against its own cairo/pango.

**Other install routes** (if not using devbox):
- **conda/pixi**: `pixi add manim` — conda-forge ships manim binary with cairo/pango/ffmpeg bundled.
- **uv + system cairo**: `uv pip install manim imageio-ffmpeg`, but first install the cairo C lib (mac: `brew install cairo pkg-config`; Linux: `apt install libcairo2-dev pkg-config`). ffmpeg via the `imageio-ffmpeg` pip pkg — symlink it onto PATH: `ln -sf "$(.venv/bin/python -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())')" .venv/bin/ffmpeg`.
- **Docker**: `manimcommunity/manim` image, zero host deps.

**LaTeX is optional** — only for `Tex` / `MathTex` (typeset equations); plain `Text()` uses Pango, no LaTeX. With devbox, add `"texlive.combined.scheme-medium"` (or `"texliveMedium"`) to `packages`. Otherwise mac: `brew install --cask mactex-no-gui` / `basictex`. See [rules/math.md](rules/math.md).

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
