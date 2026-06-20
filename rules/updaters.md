# Updaters & ValueTracker (per-frame logic)

When a mobject must react every frame to something else (a label following a dot, a counter, a line staying attached), use **updaters**. This is the closest Manim gets to Remotion's per-frame `useCurrentFrame`, but it is opt-in and local.

## add_updater

```python
dot = Dot()
label = Text("")
label.add_updater(lambda m: m.become(
    Text(f"x = {dot.get_x():.2f}").next_to(dot, UP)
))
self.add(dot, label)
self.play(dot.animate.shift(RIGHT * 4))   # label re-renders each frame, tracking the dot
label.clear_updaters()                    # stop when done
```

`m.add_updater(fn)` calls `fn(m)` every frame; `fn(m, dt)` if it takes a second arg (dt = seconds since last frame). `clear_updaters()` / `remove_updater(fn)` to stop.

## ValueTracker — animate a number

A `ValueTracker` holds a float you can animate; read it in updaters to drive anything.

```python
t = ValueTracker(0)
counter = always_redraw(lambda: Text(f"{t.get_value():.0f}").to_edge(UP))
self.add(counter)
self.play(t.animate.set_value(100), run_time=2)   # counts 0 → 100
```

`t.get_value()` reads; `t.animate.set_value(x)` animates it; `t.set_value(x)` sets instantly.

## always_redraw

`always_redraw(fn)` = shorthand for a mobject rebuilt from scratch every frame:

```python
ax = Axes()
k = ValueTracker(1)
graph = always_redraw(lambda: ax.plot(lambda x: k.get_value() * x**2, color=YELLOW))
self.add(ax, graph)
self.play(k.animate.set_value(3))   # parabola steepens live
```

Use `always_redraw` when the mobject's whole shape depends on a changing value (graphs, areas, lines between moving points). Use `add_updater` when you nudge an existing mobject in place.

## Gotchas

- A mobject with an active updater keeps updating during later `play`/`wait`. Call `clear_updaters()` (or `self.wait()` with `frozen_frame=False`) to control this.
- `become(new_mobject)` replaces a mobject's content in place — handy inside updaters to "redraw" text/shapes.
- Don't over-use: for simple choreographed motion, plain `self.play(m.animate...)` is clearer and cheaper than updaters.
