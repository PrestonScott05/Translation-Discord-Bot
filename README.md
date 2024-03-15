# Discord Translation Bot

This Discord bot enables real-time translation of messages within Discord channels, supporting a wide range of languages through the Google Translate API. Designed to foster more inclusive and accessible communication across language barriers, the bot listens for translation requests in chat and responds with translated text.

## Features

- **Message Translation**: Translates messages from one language to another in real-time.
- **Support for Multiple Languages**: Utilizes the Google Translate API to support a wide range of languages.
- **User-specific Translation**: Can translate messages from a specific user upon request.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- A Discord account and a Discord bot token
- `pip` for installing Python packages


## Configuration

1. Create a `.env` file in the root directory of the project.
2. Add your Discord bot token to the `.env` file:


### Commands

- `!translate <language_code> <user_id>`: Translates the most recent message from the specified user ID into the given language code.

## Contributing

We welcome contributions to the Discord Translation Bot! If you have suggestions or improvements, feel free to fork the repository and create a pull request. For major changes, please open an issue first to discuss what you would like to change.

Please ensure to update tests as appropriate.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- This project uses the [googletrans](https://pypi.org/project/googletrans/) library for translation services.
- Thanks to the [discord.py](https://discordpy.readthedocs.io/) library for providing an excellent API wrapper.
