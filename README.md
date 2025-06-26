# Grafana Monitoring Lab with Exporters

This repository contains a setup for monitoring various services using **Grafana**, **Prometheus**, and several **exporters** (PostgreSQL, Apache, Bind9, etc.). The lab is designed to visualize metrics for different services in a Dockerized environment.

## Technologies

- **Docker** for containerization
- **Grafana** for visualization
- **Prometheus** for monitoring and scraping metrics
- **PostgreSQL** exporter for PostgreSQL monitoring
- **Apache** exporter for Apache monitoring
- **Bind9** exporter for DNS monitoring

## Components

1. **Grafana** - The visualization tool for displaying metrics.
2. **Prometheus** - The monitoring system and time-series database.
3. **PostgreSQL** - A relational database that serves as a metric source.
4. **Apache** - A web server that will be monitored.
5. **Bind9** - A DNS server with exporter for metrics collection.

## Setup

### Prerequisites

- Install **Docker** and **Docker Compose** on your machine.
- Ensure your machine has internet access for downloading Docker images.

### How to Use

1. Clone this repository:
    ```bash
    git clone https://github.com/AYOUB334/grafana-lab.git
    cd grafana-lab
    ```

2. **Start the containers** with Docker Compose:
    ```bash
    docker compose -f postgres.yml up -d
    docker compose -f apache_exporter.yml up -d
    docker compose -f bind9.yml up -d
    ```

3. **Access Grafana**:
   - Open your browser and go to `http://localhost:3000` (default credentials: `admin`/`admin`).
   - Configure the data source in Grafana to point to Prometheus (`http://localhost:9090`).

4. **View Dashboards**:
   - Dashboards for PostgreSQL, Apache, and Bind9 metrics are available in Grafana. You can import predefined dashboards or create custom ones using Prometheus queries.

## Exporters Configuration

1. **PostgreSQL Exporter**: Monitors PostgreSQL database metrics.
2. **Apache Exporter**: Exports metrics from the Apache server.
3. **Bind9 Exporter**: Collects DNS metrics from the Bind9 server.

## Volumes and Persistence

- Docker volumes are used to persist Grafana data and PostgreSQL data:
    - `grafana-data` - persists Grafana data.
    - `pgdata` - persists PostgreSQL data.

## Troubleshooting

- **Grafana Dashboard Not Loading**: Ensure that Prometheus is properly scraping the metrics by visiting `http://localhost:9090` and checking the targets page.
- **Port Conflicts**: If a port is already in use (e.g., port 9090 or 3000), change the ports in the respective Docker Compose files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to make modifications or extend this project as per your needs!

