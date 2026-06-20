# Timing & easing

Total runtime = sum of every `self.play(...)` `run_time` plus every `self.wait(...)`. There is no global frame clock you sample; you compose durations.

## run_time

```python
self.play(Create(c), run_time=2)   # take 2 seconds
self.wait(0.5)                      # hold half a second
self.wait()                        # default 1 second
```

## rate_func (easing)

Controls how progress maps 0→1 over `run_time`. Default is `smooth` (ease in & out).

```python
from manim import rate_functions as rf

self.play(m.animate.shift(RIGHT*4), rate_func=linear)            # constant speed
self.play(m.animate.shift(UP), rate_func=rf.ease_out_bounce)     # bounce settle
self.play(m.animate.scale(1.5), rate_func=rf.ease_out_back)      # slight overshoot (spring-like)
self.play(Indicate(m), rate_func=there_and_back)                 # go and return
```

Useful funcs: `linear`, `smooth`, `rush_into`, `rush_from`, `slow_into`, `there_and_back`, `there_and_back_with_pause`, `ease_in_sine`, `ease_out_sine`, `ease_in_out_quad`, `ease_out_back`, `ease_out_bounce`, `wiggle`.

There is **no `spring()`** (unlike Remotion). For overshoot/bouncy feel use `ease_out_back` (subtle) or `ease_out_bounce` (pronounced).

## Concurrency & sequencing

```python
# concurrent: one play, many anims
self.play(FadeIn(a), Create(b), run_time=1)

# staggered cascade
self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.2))

# strict sequence inside a single play (shares one run_time)
self.play(Succession(Create(a), Create(b), Create(c)))

# group several as one unit (e.g. to give them a shared rate_func)
self.play(AnimationGroup(a1, a2, lag_ratio=0))
```

`lag_ratio` (for `LaggedStart`/`AnimationGroup`): `0` simultaneous, `1` fully sequential, fractional = overlap. `LaggedStartMap(FadeIn, group)` applies one animation across a group's children with a built-in lag.

## Pacing tips

- Entrances 0.5–1s, emphasis 0.5s, big transforms 1.5–2s. Add small `wait()`s so viewers can read.
- Per-animation `run_time` beats one giant `play`; it keeps the timeline readable and editable.
