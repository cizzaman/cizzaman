# Portrait artwork

The portrait was created with the built-in image-generation tool from a photo supplied by Christian Landsnes. The original photo is not included in this repository.

## Generation prompt

Use case: identity-preserve / lighting cleanup. Edit the provided portrait photograph for a personal GitHub profile. This is the actual person; preserve his exact face, bone structure, eyes, nose, mouth, smile, teeth, hairstyle, hairline, head proportions and pose. Keep the original natural expression and recognizable likeness. Make a clean, tasteful photographic restoration: remove the muddy sepia cast and coarse print grain, use natural neutral black-and-white tones, gentle studio-quality tonal contrast, crisp but realistic details. Replace the distracting background with a uniform very dark charcoal #10151d. Keep head and shoulders and shirt, with the whole hairstyle visible, centered. Avoid a harsh cutout; gently blend the shoulders into the dark backdrop at the lower edge. Aim for an authentic attractive black-and-white portrait, faithful to the original source, not a different person, not an artificial glamour makeover. No ASCII art, no text, no symbols, no halftone, no pixelation, no harsh shadow across the eyes, no added accessories, no waxy smoothing. The photograph is to be placed on the left of an elegant dark terminal-style GitHub profile card.

## Updating the profile

Edit `profile.json`, then run `python3 scripts/render.py` from the repository root. The renderer uses only Python's standard library. It creates self-contained desktop and mobile SVGs with no remote image or statistics services.
