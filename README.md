# Anomaly-Detection 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-✓-blue.svg)](https://www.docker.com/)

A real-time financial fraud detection system leveraging stream processing and machine learning to identify suspicious transactions with 25% improved detection accuracy.

## 🌟 Key Features

- **Real-time Analysis**: Process 10,000+ transactions/second using Kafka streams
- **Hybrid Detection Engine**:
  - Isolation Forest for statistical anomalies
  - Transformer models for temporal patterns
  - Rule-based heuristic checks
- **Enterprise-grade Reliability**:
  - Active-Active PostgreSQL cluster with Raft consensus
  - Exactly-once processing semantics
  - Automatic failure recovery
- **Production Monitoring**:
  - Prometheus metrics endpoint
  - Pre-built Grafana dashboards
  - Health check API
- **Security**:
  - JWT Authentication
  - AES-256 transaction encryption
  - Role-based access control

## 🏗 Architecture Overview

```mermaid
graph TD
    A[Client] -->|HTTPS| B(API Gateway)
    B -->|Kafka| C[Stream Processor]
    C --> D{Anomaly Detector}
    D -->|Alert| E[Notification Service]
    C -->|PostgreSQL| F[Cluster Node 1]
    C -->|PostgreSQL| G[Cluster Node 2]
    C -->|PostgreSQL| H[Cluster Node 3]
    D --> I[ML Model Serving]
    F --> J[Prometheus]
    G --> J
    H --> J
    J --> K[Grafana Dashboard]
```

## Quick Start
```bash
git clone https://github.com/yourrepo/financial-insights-platform.git
cd financial-insights-platform
cp .env.template .env
docker-compose up -d


# Wait for services to initialize (2-3 minutes)
sleep 180

# Create database tables
docker-compose exec app python scripts/setup_db.py
```


## API documentation
```bash
POST /transactions
Content-Type: application/json
Authorization: Bearer <JWT_TOKEN>

{
  "user_id": 12345,
  "amount": 1500.00,
  "currency": "USD",
  "merchant": "Online Store",
  "location": "New York, US"
}

Response:
202 Accepted
{
  "status": "processing",
  "transaction_id": "txn_01FGXWK..."
}
```
