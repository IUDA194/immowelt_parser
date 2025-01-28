# Immowelt Parser

This project is a parser for the [Immowelt](https://www.immowelt.de/) website. It scrapes the latest real estate listings and sends them to a Telegram chat. Initially, the parser fetches the last 30 listings and then monitors the website in real-time, sending updates as new listings are added.

## Features
- Fetches the 30 most recent listings upon startup.
- Monitors the website in real-time for new listings.
- Sends updates directly to a specified Telegram chat.

## Getting Started

### Prerequisites
- Docker and Docker Compose installed.
- A Telegram bot token and chat ID (explained below).

### Environment Variables
Create a `.env` file in the root of the project and populate it with the following variables:

```env
BOT_TOKEN=8101223749:AAGhbJ9rtTZH3Khab8_xkuk3vj1vd1lx2cw
CHAT_ID=-4658888134
URL=https://www.immowelt.de/classified-search?distributionTypes=Rent&estateTypes=Apartment&locations=AD08DE7633&numberOfRoomsMax=7&numberOfRoomsMin=2&priceMax=750&priceMin=10&projectTypes=Stock&spaceMax=100&spaceMin=50
```

#### Explanation of Variables:
- `BOT_TOKEN`: Telegram bot token obtained from [BotFather](https://core.telegram.org/bots#botfather).
- `CHAT_ID`: The ID of the Telegram chat where updates will be sent. This can be a group, channel, or individual chat.
- `URL`: The Immowelt URL to be scraped. Adjust the query parameters based on your preferences (e.g., price range, location, etc.).

### Docker Setup
A `docker-compose.yml` file is included for easy setup and deployment.

#### Adding a Volume
To ensure persistence for logs or other data, define a volume in your `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  immowelt-parser:
    build: .
    environment:
      - BOT_TOKEN=${BOT_TOKEN}
      - CHAT_ID=${CHAT_ID}
      - URL=${URL}
    volumes:
      - ./data:/app/data
```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/IUDA194/immowelt_parser.git
   cd immowelt_parser
   ```

2. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```

### Usage
Once the container is running:
- The parser will fetch the latest 30 listings and send them to the specified Telegram chat.
- It will continuously monitor the website and send new listings as they are published.

## Customization
- **URL Parameters:** Update the `URL` in your `.env` file to customize the listings you want to parse (e.g., change price range, location, or property type).
- **Polling Interval:** Adjust the polling interval in the source code if needed (e.g., how frequently the parser checks for new listings).

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for any improvements or bugs.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- Built using Python and Telegram Bot API.


