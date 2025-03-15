# 🍳 AI Recipe Recommendation

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📖 Overview

A Python application that suggests creative recipes based on ingredients you have available, powered by OpenAI's API. Get detailed cooking instructions and meal ideas instantly!

## ✨ Features

- **Ingredient-Based Suggestions** 🥕 - Receive personalized recipe recommendations
- **Step-by-Step Instructions** 👩🍳 - Detailed cooking directions with preparation times
- **Async Processing** ⚡ - Fast response times with asynchronous API calls
- **Environment Configuration** 🔒 - Secure API key management using `.env` files

## 🛠 Requirements

- Python 3.12+
- [OpenAI API Key](https://platform.openai.com/api-keys)
- Python packages:
  ```text
  openai
  python-dotenv

  🚀 Installation
Clone the repository

bash
Copy
git clone https://github.com/yourusername/AIRecipeRec.git
cd AIRecipeRec
Install dependencies

bash
Copy
pip install -r requirements.txt
Configure environment variables

Create .env file:

bash
Copy
touch .env
Add your API key:

env
Copy
OPENAI_API_KEY=your_api_key_here
🧑💻 Usage
Start the application

bash
Copy
python agent.py
Enter ingredients when prompted:

text
Copy
Enter ingredients (comma-separated): chicken, rice, broccoli
Receive recipe with:

Recipe name

Preparation time

Cooking instructions

Serving suggestions

Example output:

text
Copy
🍴 Creamy Chicken & Broccoli Rice Bowl
⏱ Prep time: 10 mins | Cook time: 25 mins

1. Cook rice according to package instructions
2. Sauté chicken with olive oil...
...
🤝 Contributing
We welcome contributions! Here's how:

🍴 Fork the repository

🌿 Create your feature branch: git checkout -b feature/amazing-feature

💾 Commit changes: git commit -m 'Add amazing feature'

🚀 Push to branch: git push origin feature/amazing-feature

📦 Submit a pull request

📜 License
Distributed under the MIT License. See LICENSE for more information.
