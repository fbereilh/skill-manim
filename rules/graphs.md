# Graphs, axes & functions

Manim's signature strength: animated plots, axes, and coordinate planes (the 3Blue1Brown look). No LaTeX needed for axes themselves (labels via `Text` are LaTeX-free; `MathTex` labels need LaTeX).

## Axes + plotting a function

```python
ax = Axes(
    x_range=[-3, 3, 1],          # [min, max, step]
    y_range=[-1, 9, 2],
    axis_config={"include_tip": True},
)
labels = ax.get_axis_labels(x_label="x", y_label="y")

curve = ax.plot(lambda x: x**2, color=YELLOW)             # graph the function
area = ax.get_area(curve, x_range=[0, 2], color=BLUE, opacity=0.4)

self.play(Create(ax), Write(labels))
self.play(Create(curve))
self.play(FadeIn(area))
```

- `ax.plot(fn, x_range=[a,b], color=)` → a curve mobject in the axes' coordinate system.
- `ax.coords_to_point(x, y)` (alias `ax.c2p`) maps data coords → scene point; `ax.p2c` reverses. Use `c2p` to place dots/labels at data positions.
- `ax.get_graph_label(curve, label="f(x)", x_val=2)` attaches a label to a curve.
- `ax.get_area(curve, x_range=)`, `ax.get_riemann_rectangles(curve, x_range=, dx=)` for integrals.

## Moving a dot along a curve

```python
t = ValueTracker(-3)
dot = always_redraw(lambda: Dot(ax.c2p(t.get_value(), t.get_value()**2), color=RED))
self.add(dot)
self.play(t.animate.set_value(3), run_time=3)   # dot rides the parabola
```

(See updaters.md for `ValueTracker` / `always_redraw`.)

## NumberPlane / grid

```python
plane = NumberPlane(x_range=[-6, 6, 1], y_range=[-4, 4, 1])
self.play(Create(plane))
self.play(plane.animate.apply_matrix([[2, 1], [0, 1]]))   # linear-algebra transform viz
```

`NumberLine(x_range=[0, 10, 1])` for a single axis; `add_numbers()` to label ticks.

## Common pieces

- `Vector([2, 1])` / `Arrow` for vectors; `Matrix([[1,0],[0,1]])` for matrices (LaTeX).
- `Dot(ax.c2p(x, y))` to mark a point; `ax.get_vertical_line(point)` / `get_horizontal_line` for guides.
- Animate a function morph: `self.play(Transform(curve, ax.plot(lambda x: x**3, color=GREEN)))`.

## Tip

Build the scene in data space via `c2p` so everything stays aligned when you change `x_range`/`y_range`. Don't hard-code scene coordinates for points that belong on the graph.
