# Animations

Everything visible is a **Mobject**; everything that moves is an **Animation** passed to `self.play()`. Animations in one `play()` run concurrently; separate `play()` calls run in sequence.

## Two ways to animate

```python
# Named animation class — wraps a mobject
self.play(Create(square))

# .animate — animate the change made by any chained method
self.play(square.animate.shift(RIGHT * 2).rotate(PI / 4))
```

Use `.animate` for property/transform changes (move, scale, color). Use named classes for entrance/exit and special effects. `.animate` interpolates start→end state; it does NOT replay the method's path (e.g. `.animate.rotate(2*PI)` looks like no motion — use `Rotate(m, 2*PI)` instead).

## Entrances / exits

- `Create(m)` / `Uncreate(m)` — draw/undraw strokes
- `Write(m)` / `Unwrite(m)` — handwriting effect (great for `Text`/`MathTex`)
- `FadeIn(m, shift=UP, scale=0.8)` / `FadeOut(m, shift=DOWN)` — opacity (+ optional motion)
- `GrowFromCenter(m)`, `GrowFromEdge(m, DOWN)`, `SpinInFromNothing(m)`
- `DrawBorderThenFill(m)`

## Transforms (morph one thing into another)

```python
self.play(Transform(a, b))             # a morphs into b's shape; `a` stays the on-screen object
self.play(ReplacementTransform(a, b))  # a replaced by b; use b afterwards
self.play(TransformMatchingTex(eq1, eq2))   # match & move common LaTeX sub-parts
self.play(TransformMatchingShapes(t1, t2))  # match by shape (e.g. Text → Text)
```

Rule of thumb: `ReplacementTransform(a, b)` when you keep referring to `b` after; `Transform(a, b)` when you keep referring to `a`.

## Emphasis / indication

`Indicate(m)`, `Flash(point)`, `Circumscribe(m)`, `Wiggle(m)`, `FocusOn(point)`, `ApplyWave(m)`, `Indicate(m, color=YELLOW)`.

## Motion

- `m.animate.move_to(point)` / `.shift(vec)` / `.to_edge(UP)`
- `Rotate(m, angle=PI, about_point=ORIGIN)`
- `MoveAlongPath(m, path)` — path is any VMobject (e.g. an `Arc`, `ParametricFunction`)

## Running several together / staggered

```python
self.play(FadeIn(a), FadeIn(b), Create(c))          # simultaneous
self.play(AnimationGroup(a1, a2))                    # group as one
self.play(LaggedStart(a1, a2, a3, lag_ratio=0.3))   # staggered start
self.play(Succession(a1, a2, a3))                    # strictly one after another
```

`lag_ratio`: 0 = all together, 1 = fully sequential, 0.1–0.5 = overlapping cascade.

## Common mistakes

- CSS-style thinking does not apply. You cannot "set a transition" on a mobject; you animate explicitly via `play`.
- `self.play()` with no animation errors — pass at least one, or use `self.wait()` / `self.add()`.
- `.animate.rotate(2*PI)` / full-loop transforms interpolate endpoints → no visible motion. Use the `Rotate` class.
- Changing a mobject with a plain method (`m.shift(...)`) outside `play`/`add` updates state silently with no animation and no redraw until the next render step.
