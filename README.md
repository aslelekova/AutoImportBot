# AutoImportBot

This Telegram bot helps users evaluate the cost-effectiveness of importing cars from Korea to Russia. Choose the perfect car and compare costs effortlessly with AutoImportBot. It streamlines the process by parsing listings from [Encar.com](http://www.encar.com/index.do) (Korea) and [Auto.ru](https://auto.ru) (Russia), allowing you to easily find the most suitable vehicle and compare costs with a user-friendly interface.

## Features

- Parses car listings from [Encar.com](http://www.encar.com/index.do) (Korea) and [Auto.ru](https://auto.ru) (Russia) to evaluate cost-effectiveness of importing cars to Russia.
- Calculates import duties, taxes, and fees for each car listing.
- Provides detailed car information: engine power, displacement, mileage, year, fuel type, and price in KRW.
- Displays clickable links to original listings and total import costs.
- Matches Korean car listings with three most similar Russian cars using vector similarity and Euclidean distance.

## Installation

### Prerequisites

- Python 3.7+
- Telegram Bot API token
- Docker

### Clone the Repository

```bash
git clone https://github.com/aslelekova/telegram-car-import-cost-bot.git
```

### Build Docker Image

Build the Docker image using the provided Dockerfile:

```bash
docker build -t autoimportbot:latest .
```

### Run Docker Container

Run a Docker container from the built image:

```bash
docker run -d autoimportbot:latest
```

This command starts the AutoImportBot container in detached mode (`-d`), executing the bot inside the Docker container.

### Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### Configuration

Update the `config.py` file in the root directory of the project with your Telegram Bot API token:

```python
TOKEN = 'your_telegram_bot_token_here'
```

Replace `'your_telegram_bot_token_here'` with your actual Telegram Bot API token.

### Run the Bot

To start the bot, run:

```bash
python main.py
```

## Usage

1. Start a chat with your Telegram bot.
2. Set your search parameters by selecting the brand, model, year, fuel type, and mileage.
3. The bot will provide a list of five cars from Encar.com that match your criteria, along with their details and the three most similar cars from Auto.ru.
4. Click on the "Show More" button to load more cars, five at a time.

## Contact

Lelekova Anastasia - [@aslelekova](https://t.me/aslelekova)
