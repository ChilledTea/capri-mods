# Capri Bezel LED

![Capri Bezel LED preview](preview.png)

Music Light adds a diffuse, moving RGB glow around your primary display. It pulses to music, with an extra brightness boost on detected bass hits. The overlay fades inward and lets mouse clicks pass through.

## Installation

1. Download [capri-bezel-led.capri-code](capri-bezel-led.capri-code).
2. Open **Mainframe → CAPRI → Mods → Import mod** and select the file.
3. Approve the code mod when prompted.
4. Use **Mainframe → Settings → Capri → Music Light** to enable or disable the effect.

## Changelog

### v7.0.1

Fixes Mainframe GUI glitches.
This is the Final Build and done.
Future Fixed for Capri will be provided in case the Mod needs patches for newer Capri versions in the Future.

### v0.6.1

- The render and bass workers prefer E-cores on supported Intel hybrid CPUs. Windows can still schedule them on other cores.
- On AMD and systems without detected Intel E-cores, Windows continues to choose where the workers run.
- Added bass-reactive flashes using Windows playback audio. Bass detection runs in the background while Capri detects music.
- Kept the diffuse RGB renderer and existing fullscreen and taskbar behavior.

### Changes since v0.5.2

- Moved RGB pixel rendering off Capri's UI thread and reused pixel buffers. The renderer now calculates corner and color values per column, and the mod checks less often when idle.
- Registered the Music Light row with the Mainframe settings layout so it scrolls with the other controls.
- The glow follows the desktop work area and extends to the monitor edges in fullscreen. Cached strips resize together when switching modes to keep the bottom corners joined.

### v0.5.2

- Initial public release.

## Compatibility

Windows code mod for [Capri Desktop](https://github.com/lachydotmcg/capri-desktop). The mod uses internal Capri interfaces for music detection, audio capture, and Mainframe controls. Future Capri releases may require an update.

## Credits

- Made by: Dominik20074
- AI assisted with the code and preview artwork.

