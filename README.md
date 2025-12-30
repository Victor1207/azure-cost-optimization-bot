# Azure Cost Optimization Bot (Serverless)

A serverless Azure Function that automatically queries real Azure subscription
cost data using **Azure Cost Management API** and **Managed Identity**.

## Architecture
- Azure Functions (Python)
- Azure Managed Identity (no secrets)
- Azure Cost Management API
- Timer Trigger (every 5 minutes)
- GitHub CI/CD ready

## Key Features
- 🔐 Zero secrets (Managed Identity only)
- 📊 Real-time cost data from Azure
- 🔄 Automated execution via Timer Trigger
- 🧠 Cloud-native security design
- ⚙️ Production-ready logging

## Why this matters
This project demonstrates:
- Professional Azure RBAC usage
- Secure cloud authentication patterns
- Serverless automation
- Cost governance fundamentals

## Technologies
- Python 3.10
- Azure Functions
- Azure SDK for Python
- GitHub Actions (CI/CD ready)

## Author
Olasehinde Victor
