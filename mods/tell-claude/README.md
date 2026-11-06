TELL CLAUDE, a mod for Capri (by Potato)
=========================================
One file: tell-claude.capri-code. Say "tell Claude to ..." and Claude Code does the job, then Capri tells you the answer.

  "Tell Claude to check what's using my GPU"
  "Capri, ask Claude why my game is lagging"
  "Tell Claude to open Valorant"
  "Tell Claude to put some music on"
  "Claude, what did you find?"      (repeats the last answer)

You don't have to say "Capri" first, even with "Listening for Capri" on: while the mod is on, "tell Claude", "ask Claude",
"Hey Claude" and how her ears mishear them (Telcloud, Tel Cloud, asked Cloud...) wake her too.

WHAT YOU NEED
- Capri 0.8.3 or newer, on Windows (code mods are Windows only).
- A Claude plan that includes Claude Code (Pro, Max, Team or Enterprise), or an Anthropic API account. A free Claude
  account can't use Claude Code. Each job uses your plan's usage.
- Claude Code installed and signed in once: install it from claude.com/claude-code, open a terminal, run  claude,
  type  /login  and follow the browser. If Claude Code asks for Git for Windows, install that too (git-scm.com).
- Capri set to English: the wake words are English ("tell Claude").
Nothing else: no relay, no Python, and it doesn't use her brain (it works even if her brain is out of free requests).
If something's missing she says what, in plain words.

INSTALL
Capri's Mainframe > Mods > Import mod > pick  tell-claude.capri-code.
Capri warns that it runs code: that's normal for code mods. Read it first if you like (it's plain C#).

WHAT CLAUDE CAN AND CAN'T DO HERE
- Can: read files on your PC, search and read the web, check your graphics card (nvidia-smi) and running programs
  (tasklist), open apps by their Start menu name, and press media keys (play/pause, next, previous, volume, mute).
- Can't: run any other commands, change, move or delete files, or install anything. It runs one job at a time,
  15 minutes at most, hidden in the background, without your personal Claude Code settings, hooks or MCP servers.
- Only lines you say or type to Capri start a job. Text on your screen or in Discord can't.
- Files Claude reads go to Anthropic as part of the job, like any Claude Code session.

SETTINGS (in Capri's folder: %LOCALAPPDATA%\Capri\mods\tell-claude-data)
- notes.md     facts about your PC for Claude (your audio setup, games, what not to touch)
- settings.txt model = (empty, sonnet or opus), apps = on/off, media = on/off
- answers.md   every answer Claude gave
Her log (%LOCALAPPDATA%\Capri\errors.txt) has a "mod tell-claude" line for each app or key it used, and any problems.

TURN IT OFF
Mainframe > Mods > Tell Claude > On/Off, or Remove. Off also takes its wake words away again.
