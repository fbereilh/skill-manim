# manim-best-practices

A [Claude Code](https://claude.com/claude-code) **agent skill** that teaches Claude how to write and render [Manim](https://www.manim.community/) animations — programmatic, 3Blue1Brown-style math/explainer videos in Python.

It gives the model domain knowledge for ManimCommunity: scene anatomy, mobjects & layout, animations, easing/timing, rendering, LaTeX math, plots/axes, updaters, camera & 3D — plus a reproducible **devbox (Nix)** setup that sidesteps Manim's painful native dependencies (`pycairo`, `pango`, `ffmpeg`, optional LaTeX).

## What's inside

```
SKILL.md            # entry point — setup, scene anatomy, render loop, links to rules
rules/              # focused, load-on-demand reference
  animations.md       play()/.animate, transforms, LaggedStart
  mobjects.md         shapes, styling, positioning, VGroup
  timing.md           run_time, rate_func easing, sequencing
  render.md           quality flags, stills, gif/transparent, devbox usage
  text.md             Text vs MarkupText vs MathTex, fonts
  math.md             MathTex/Tex + LaTeX install notes
  graphs.md           Axes, plot, NumberPlane (the 3b1b core)
  updaters.md         ValueTracker / always_redraw (per-frame logic)
  camera.md           MovingCamera, ThreeDScene
examples/           # runnable scenes
  dog_eating.py       shape-built character animation
  kl_divergence.py    full 3b1b-style explainer (title → formula → properties)
devbox.json         # Nix env: prebuilt manim + ffmpeg, no brew/pip compile
```

## Install (as a Claude Code skill)

Clone into your skills directory so Claude picks it up. The folder name should match the skill's `name` (`manim-best-practices`):

```bash
# user-level (all projects)
git clone https://github.com/<you>/manim-skill ~/.claude/skills/manim-best-practices

# or project-level
git clone https://github.com/<you>/manim-skill .claude/skills/manim-best-practices
```

Claude reads `SKILL.md` and pulls in the relevant `rules/*.md` on demand. Ask Claude to "make a Manim video of …" and it applies the skill.

## Running the examples

The native deps (cairo, pango, ffmpeg, LaTeX) are the usual Manim pain point. The committed `devbox.json` pins a Nix environment with a **prebuilt** manim — no compiling `pycairo` from source, no Homebrew:

```bash
# install devbox once: https://www.jetify.com/devbox
devbox install
devbox run -- manim -qh examples/kl_divergence.py KLDivergence
devbox run -- manim -ql examples/dog_eating.py DogEating
```

Output lands in `media/videos/<file>/<res>/SceneName.mp4`.

Prefer not to use devbox? See `SKILL.md` → *New project setup* for conda/pixi, uv + system cairo, and Docker alternatives.

## License

MIT — see [LICENSE](LICENSE).
