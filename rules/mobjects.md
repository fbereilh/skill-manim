# Mobjects & layout

A **Mobject** is anything on screen. **VMobject** = vectorized (stroke + fill) — most shapes. Build complex visuals by composing simple ones in a `VGroup`.

## Shape catalog

```python
Circle(radius=1, color=BLUE)
Square(side_length=2)
Rectangle(width=4, height=2)
Ellipse(width=3, height=1.5)
Triangle()
RegularPolygon(n=6)
Polygon(*points)          # explicit vertices, each a 3-vector
Line(start, end)
Arrow(start, end, buff=0)
DoubleArrow(start, end)
Dot(point=ORIGIN, radius=0.08)
Arc(radius=1, start_angle=0, angle=PI/2)
Annulus(inner_radius=1, outer_radius=2)
Vector([2, 1, 0])         # arrow from origin
```

## Styling

```python
sq = Square()
sq.set_fill(BLUE, opacity=0.7)
sq.set_stroke(WHITE, width=4)
sq.set_color(RED)                       # both stroke & fill
Square(color=GREEN, fill_opacity=1, stroke_width=2)   # in constructor
```

Colors: built-in constants `RED, GREEN, BLUE, YELLOW, WHITE, BLACK, ORANGE, PURPLE, PINK, TEAL, GRAY, GOLD, MAROON`, lightness variants `BLUE_A..BLUE_E` (A light → E dark). Hex strings work too: `Square(color="#c8862f")`. `fill_opacity` defaults to 0 — shapes are hollow outlines unless you set it.

## Positioning

Coordinate system: origin at center, +x right, +y up, units are scene units (frame ≈ 14.2 wide × 8 tall). Direction constants are unit vectors: `UP, DOWN, LEFT, RIGHT, UL, UR, DL, DR, ORIGIN`. Multiply to scale: `RIGHT * 3`.

```python
m.move_to(RIGHT * 2 + UP)          # absolute
m.shift(LEFT * 0.5)                # relative
m.next_to(other, RIGHT, buff=0.3)  # place beside another mobject
m.to_edge(UP, buff=0.5)            # against a frame edge
m.to_corner(UR)                    # to a corner
m.align_to(other, LEFT)            # align one edge
m.move_to(other.get_center())      # match a point; also get_top/bottom/left/right/corner
```

Negative `buff` in `next_to` overlaps mobjects (useful for joining body parts).

## Groups

```python
group = VGroup(head, body, tail)        # treat as one
group.arrange(RIGHT, buff=0.2)          # lay children out in a row (or DOWN for a column)
group.arrange_in_grid(rows=2, cols=3)
group.move_to(ORIGIN)                   # moves all together
group.scale(1.5)
group[0]                                # index into children
group.add(extra)                        # append
```

`VGroup` is the workhorse for building characters/diagrams from primitives, then animating or positioning the whole assembly at once. (`Group` — non-V — is needed when mixing in `ImageMobject`, which isn't vectorized.)

## Images

```python
from manim import ImageMobject
logo = ImageMobject("assets/logo.png").scale(0.5).to_corner(UL)
self.add(logo)   # ImageMobject is NOT a VMobject — no Create/Write; use FadeIn / add
```

Manim has no native video import — it composites still mobjects and renders frames.
