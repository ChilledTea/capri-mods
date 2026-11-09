# Hologram Speech Glass

![Hologram Speech Glass banner](preview.png)

A Windows code mod for [Capri Desktop](https://github.com/lachydotmcg/capri-desktop) that makes Capri's speech bubble translucent in Hologram mode.

The mod shows a click-through copy of the speech bubble at 63% opacity while Hologram mode is active. The standard bubble returns when you exit Hologram mode or turn Speech Glass off.

## Installation

1. Download [hologram-speech-glass.capri-code](hologram-speech-glass.capri-code).
2. Open **Mainframe → CAPRI → Mods and approve it.
3. Open **Mainframe → Settings → Capri** and use the **Speech Glass** switch in the **Hologram** section. The mod remembers your choice.

## Submit without git
No git needed: fill in the [Submit a mod](https://github.com/lachydotmcg/capri-mods/issues/new?template=submit-mod.yml) form and drag your mod file in, zipped first. A pull request gets opened for you, with your GitHub username as the author, and it's read like any other mod before it goes up. To change something, edit your issue.

## Stay safe
- Only install mods from here, or from people you trust.
- Only get Capri itself from [capriai.app](https://capriai.app) or [its GitHub](https://github.com/lachydotmcg/capri-desktop/releases).

### v0.1.10

- Removed continuous idle checks. The timer stops when the speech bubble is hidden or Speech Glass is disabled.
- With a visible bubble, check every 50 ms while the effect is active and every 500 ms outside Hologram mode.
- Reuse the translucent image buffer across frames of the same size. Reuse the rendered image when the bubble only moves and release rendering resources when the effect ends.
- Update the Mainframe layout when settings rows change. Speech Glass appears below Music Light when both mods are enabled and leaves the Music Light row in place.

### v0.1.4

- Initial release with a click-through, translucent speech bubble in Hologram mode and a Speech Glass toggle in Mainframe.
- 10ms (fixed in new Version)

## Compatibility

Version 0.1.10 uses internal Capri interfaces for speech rendering and settings. Future Capri updates may require a mod update. Speech Glass can run alongside Capri Bezel LED v0.6.1.

## Credits

- Made by: Dominik20074
- AI assisted with the code and preview artwork.
