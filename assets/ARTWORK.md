# Portrait artwork

The portrait was created with the built-in image-generation tool from a photo supplied by Christian Landsnes. The original photo is not included in this repository.

## Generation prompt

Use case: style-transfer. Asset type: portrait asset for a GitHub profile terminal UI. Input image 1 is the portrait reference and identity source. Create an ASCII-art portrait of this exact person, preserving his recognizable face, smile, hairstyle, and front-facing pose. Only head and shoulders, centered, with empty margin around the head. Depict the entire person exclusively using dense small monospaced ASCII characters such as @ % # * + : . / |, like a high-resolution terminal ASCII portrait, not a smooth photograph and not pixel blocks. The characters should be pale silver and muted cool blue on a perfectly uniform solid background color #10151d. Image should be portrait orientation about 3:4. High contrast around eyes and hair, softer facial shading, clearly recognizable smile. No labels, captions, names, terminal frame, window controls or decorative elements. Keep the face large, hair fully visible and shoulders near the bottom. This will be the left-side illustration of a carefully typeset terminal UI.

## Updating the profile

Edit `profile.json`, then run `python3 scripts/render.py` from the repository root. The renderer uses only Python's standard library. It creates self-contained desktop and mobile SVGs with no remote image or statistics services.
