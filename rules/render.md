# Rendering

```bash
manim [flags] file.py SceneName
```

Renders the named scene class. Output: `media/videos/<file>/<resolution>/SceneName.mp4`.

## Quality flags

| Flag | Resolution / fps | Use |
|------|------------------|-----|
| `-ql` | 480p15 | fast iteration while building |
| `-qm` | 720p30 | review |
| `-qh` | 1080p60 | final |
| `-qk` | 4K60 | export |

## Common flags

- `-p` — preview: open the output when done
- `-s` — render only the **last frame** to PNG (fast layout/color check, skips the timeline)
- `--format gif` — output GIF instead of mp4 (`--format webm`, `mov` also valid; `mov` + transparency below)
- `-a` — render every scene in the file
- `-o NAME` — set output filename
- `-n K` — start from animation index K (skip ahead while iterating)
- `-r W,H` — custom resolution, e.g. `-r 1080,1920` for vertical/portrait
- `--fps 30` — override fps
- `--disable_caching` — force re-render (Manim caches partial movies; usually leave on)

## Iteration loop (no live studio)

Manim has no preview studio. Fastest loops:
1. `manim -s file.py SceneName` → inspect the last-frame PNG for layout/colors.
2. `manim -ql file.py SceneName` → watch motion at low res.
3. Bump to `-qh` only for the final render.

If you only changed the end, `-s` checks it instantly. Use `-n <index>` to jump to a later animation without replaying earlier ones.

## Transparency

```bash
manim -qh --format mov --transparent file.py SceneName   # alpha channel (ProRes 4444)
manim -qh --format webm --transparent file.py SceneName  # alpha (smaller)
```

Use a transparent render to overlay the animation on other footage.

## Portrait / social

```bash
manim -qh -r 1080,1920 file.py SceneName   # 9:16 vertical
```

Set `config.frame_width`/`frame_height` in-scene if you need the coordinate frame to match the aspect.

## Environment wrappers

If the project's manim lives inside an environment (a venv, `devbox run --`, `pixi run`, `docker run …`), apply that same wrapper to the `manim` command — the flags above are identical either way. Avoid `bash -lc` wrappers: a login shell can change the working directory so manim can't find the scene file.

## ffmpeg

Manim shells out to the `ffmpeg` binary on PATH to encode. `FileNotFoundError: ffmpeg` means it isn't on PATH — install it or activate the environment that provides it (most manim installs bundle it).
