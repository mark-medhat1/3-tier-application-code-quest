# 🛠️ Three-Tier Kubernetes App with DevSecOps

This repository contains a **three-tier application** (Frontend, Backend, Postgres DB) deployed on **Kubernetes** with complete **DevSecOps practices** including CI/CD, security, and monitoring.

---

## 🔑 Features
- **Application**  
  - Backend API with simple task management:  
    - `POST /addTask`  
    - `DELETE /deleteTask`  
    - `GET /listTasks`  
  - Postgres DB (deployed with Helm).  
  - NGINX frontend (basic).  
  - Local testing supported with `docker-compose.yml`.

- **Kubernetes**  
  - Helm chart for app + Postgres.  
  - Horizontal Pod Autoscaler (HPA) for backend.  
  - Pod Security Admission (non-root).  
  - NetworkPolicies to restrict DB access.

- **Testing**  
  - Locust load test script to validate HPA scaling.  

- **CI/CD**  
  - GitHub Actions pipelines:  
    - **App pipeline** → Build, scan, and deploy.  
    - **Infra pipeline** → Validate and apply infrastructure with Terraform.  
  - Security scanning with **Trivy**.  

- **Security**  
  - Secrets management (Kubernetes secrets).  
  - RBAC & NetworkPolicies.  
  - Image scanning.  
  - Non-root container execution.  

- **Monitoring**  
  - Prometheus & Grafana dashboards.  
  - Alerts: High CPU, pod crash loops, DB unavailable.  
  - Optional OpenTelemetry + Jaeger for tracing.  

---

## 🧰 Tech Stack
- **Cloud**: Minikube (local) / AWS EKS (optional)  
- **IaC**: Terraform, Helm  
- **CI/CD**: GitHub Actions  
- **Monitoring**: Prometheus, Grafana, OpenTelemetry, Jaeger  
- **Security**: Trivy, RBAC, NetworkPolicies  

---

## 📂 Repo Structure

├── backend/ # Backend source code

├── frontend/ # Frontend (served by NGINX)

├── helm/ # Helm chart for app + DB

├── locust/ # Locust load test script

├── manifests/ # Raw K8s manifests (reference)

├── docker-compose.yml # Local testing setup

└── .github/workflows/ # CI/CD pipelines
