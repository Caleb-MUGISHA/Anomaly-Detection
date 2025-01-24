# Anomaly-Detection

Real-time fraud detection system with Kafka streaming and ML-powered anomaly detection.

## Features
- Real-time transaction processing (10k+ TPS)
- Hybrid anomaly detection (Isolation Forest + Temporal Patterns)
- Active-Active PostgreSQL cluster with Raft consensus
- REST API with JWT authentication
- Prometheus/Grafana monitoring

## Quick Start
```bash
git clone https://github.com/yourrepo/financial-insights-platform.git
cd financial-insights-platform
cp .env.template .env
docker-compose up -d
