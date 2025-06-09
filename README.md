# Quantum Discord Bot

This repository contains **엄채희 중학교 3학년 Quantum Brain Bot**, an advanced Discord bot built with `discord.py`.

## Requirements

- Python 3.8+
- `discord.py` (`pip install discord.py`)

## Setup

1. Create a Discord application and bot and copy the token.
2. Set the token as an environment variable:

```bash
export DISCORD_TOKEN="<your token>"
```
3. Install requirements and run the bot:

```bash
python quantum_brain_bot.py
```

The command prefix is `채희야`. Invoke commands by typing it followed by the
command name, for example `채희야 quantum`.

## Departments

The bot is organized into two departments implemented as cogs:

- **Agent Department** – user commands such as `채희야 quantum`, `채희야 echo`, `채희야 predict`, `채희야 brainwave`, and `채희야 about`.
- **Admin Department** – administration commands (server administrators only), including `채희야 create_role` and `채희야 shutdown` to control the bot.

## Example Commands

- `채희야 quantum` – get a quantum thought.
- `채희야 echo <message>` – echo back a message.
- `채희야 predict` – receive a pseudo quantum prediction.
- `채희야 brainwave` – view a random quantum brainwave pattern.
- `채희야 about` – information about the bot.
- `채희야 create_role <name>` – admin command to create a server role.
- `채희야 shutdown` – admin command to gracefully shut down the bot.
