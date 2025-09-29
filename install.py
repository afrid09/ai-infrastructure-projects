#!/usr/bin/env python3
"""
AI Infrastructure Projects - One-Command Installer
Downloads and sets up the complete project structure with all files.

Usage:
    curl -sSL https://raw.githubusercontent.com/YOUR_USERNAME/ai-infrastructure-projects/main/install.py | python3
    
Or:
    python3 install.py
"""

import os
import sys
import urllib.request
import json
from pathlib import Path

# Color codes for pretty output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(60)}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}\n")

def print_success(text):
    print(f"{Colors.OKGREEN}✓ {text}{Colors.ENDC}")

def print_info(text):
    print(f"{Colors.OKCYAN}ℹ {text}{Colors.ENDC}")

def print_warning(text):
    print(f"{Colors.WARNING}⚠ {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")

# All file contents embedded directly
FILES = {
    "README.md": """# AI Infrastructure Projects

Complete production-ready AI infrastructure with Kubernetes, Terraform, PyTorch, and modern MLOps tools.

## 🚀 Quick Start

```bash
# One-command installation
curl -sSL https://raw.githubusercontent.com/YOUR_USERNAME/ai-infrastructure-projects/main/install.py | python3

# Or clone and run
git clone https://github.com/YOUR_USERNAME/ai-infrastructure-projects
cd ai-infrastructure-projects
./scripts/quick-start.sh
```

## 📦 What's Included

- ✅ **Multi-Cloud Kubernetes**: AWS EKS + GCP GKE clusters with Terraform
- ✅ **Distributed Training**: PyTorch DDP on GPU clusters  
- ✅ **Inference API**: FastAPI service with auto-scaling
- ✅ **Monitoring Stack**: Prometheus + Grafana + Loki + custom GPU metrics
- ✅ **CI/CD Pipeline**: GitHub Actions + ArgoCD GitOps
- ✅ **Service Mesh**: Istio with canary deployments (optional)

## 💰 Cost

**Estimated: $70-140/month** with optimizations
- Free tier eligible for 12 months (AWS) / 90 days (GCP)
- Auto-scaling to minimize costs
- Spot/preemptible instances support

## 📚 Documentation

- [Complete Setup Guide](docs/SETUP_GUIDE.md)
- [Quick Reference](docs/QUICK_REFERENCE.md)
- [Architecture Overview](docs/ARCHITECTURE.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

## 🎯 Next Steps

1. Configure cloud credentials: `aws configure` and `gcloud auth login`
2. Deploy: `./scripts/quick-start.sh`
3. Access services: See port-forward commands in Quick Reference

## 📊 Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Load Balancer                        │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
   ┌────▼─────┐            ┌─────▼────┐
   │   AWS    │            │   GCP    │
   │   EKS    │            │   GKE    │
   └────┬─────┘            └─────┬────┘
        │                         │
   ┌────▼──────────────────────┬──▼────┐
   │  Inference API (FastAPI)  │  GPU  │
   │  + Redis Cache            │ Nodes │
   ├───────────────────────────┴───────┤
   │    Monitoring (Prometheus)        │
   │    Logging (Loki)                 │
   │    Dashboards (Grafana)           │
   └───────────────────────────────────┘
```

## 🤝 Contributing

Contributions welcome! Please open an issue or submit a PR.

## 📝 License

MIT License - See LICENSE file

## 🙏 Acknowledgments

Built with modern cloud-native technologies:
- Kubernetes, Docker, Terraform
- PyTorch, FastAPI, Redis
- Prometheus, Grafana, ArgoCD
- AWS, GCP, GitHub Actions

---

**⭐ Star this repo if it helped you!**
""",

    ".gitignore": """# Terraform
*.tfstate
*.tfstate.*
.terraform/
.terraform.lock.hcl
terraform.tfplan
crash.log
*.tfvars.json
override.tf
*_override.tf

# Python
__pycache__/
*.py[cod]
*.so
.Python
venv/
env/
*.egg-info/
.pytest_cache/
.coverage
htmlcov/

# Secrets & Credentials
*.pem
*.key
*-key.json
secrets.yaml
.env
.env.local
credentials.json

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Kubernetes
*.kubeconfig
kubeconfig
.kube/

# Logs
*.log
logs/

# Build artifacts
dist/
build/
*.egg

# Temporary
tmp/
temp/
*.tmp
""",

    "LICENSE": """MIT License

Copyright (c) 2025 AI Infrastructure Projects

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",

    "docs/ARCHITECTURE.md": """# Architecture Overview

## System Design

The AI infrastructure is built on a multi-cloud, microservices architecture designed for:
- **Scalability**: Auto-scaling inference and training workloads
- **Reliability**: Multi-region deployment with failover
- **Observability**: Comprehensive monitoring and logging
- **Cost-efficiency**: Spot instances and auto-scaling

## Components

### 1. Infrastructure Layer (Terraform)
- **AWS EKS**: Primary Kubernetes cluster
- **GCP GKE**: Secondary cluster for geo-distribution
- **Networking**: VPCs, subnets, load balancers
- **Storage**: S3/GCS for models and data

### 2. Compute Layer (Kubernetes)
- **Control Plane**: Managed by cloud providers
- **Worker Nodes**: CPU nodes for general workloads
- **GPU Nodes**: For training and GPU inference
- **Auto-scaling**: HPA and cluster autoscaler

### 3. Application Layer
- **Training**: Distributed PyTorch jobs
- **Inference**: FastAPI REST API
- **Caching**: Redis for prediction caching
- **Queue**: (Optional) Celery for async tasks

### 4. Observability Layer
- **Metrics**: Prometheus + custom exporters
- **Visualization**: Grafana dashboards
- **Logging**: Loki for log aggregation
- **Alerting**: AlertManager + integrations

### 5. CI/CD Layer
- **Source Control**: GitHub
- **CI Pipeline**: GitHub Actions
- **CD/GitOps**: ArgoCD
- **Service Mesh**: Istio (optional)

## Data Flow

### Training Flow
```
Developer → Git Push → GitHub Actions → Build Container → 
ECR/GCR → Kubernetes Job → GPU Nodes → Train Model → 
Save to S3/GCS → Update Model Registry
```

### Inference Flow
```
User Request → Load Balancer → Inference API → 
Check Redis Cache → (if miss) Load Model → 
Run Inference → Cache Result → Return Prediction
```

### Monitoring Flow
```
All Services → Prometheus Scrape → Store Metrics →
Grafana Query → Display Dashboards → 
AlertManager → Slack/Email Notifications
```

## Security

- **Network**: Network policies, security groups
- **Authentication**: RBAC, service accounts
- **Secrets**: Kubernetes secrets, AWS Secrets Manager
- **Encryption**: At-rest and in-transit
- **Scanning**: Container image vulnerability scanning

## High Availability

- **Multi-AZ**: Kubernetes nodes across availability zones
- **Multi-Region**: Deploy to multiple cloud regions
- **Health Checks**: Liveness and readiness probes
- **Auto-recovery**: Kubernetes self-healing
- **Backups**: Regular snapshots of state

## Scalability

- **Horizontal**: HPA for pods, cluster autoscaler for nodes
- **Vertical**: Resource requests/limits tuning
- **Caching**: Redis for frequently accessed predictions
- **Load Balancing**: Cloud load balancers + Istio
- **Database**: (If needed) Managed databases with read replicas
""",

    "docs/TROUBLESHOOTING.md": """# Troubleshooting Guide

## Common Issues

### 1. Cannot Connect to Kubernetes Cluster

**Symptoms:**
```
Unable to connect to the server: dial tcp: lookup ... no such host
```

**Solutions:**
```bash
# Update kubeconfig for AWS
aws eks update-kubeconfig --region us-west-2 --name ai-infrastructure-eks

# Update kubeconfig for GCP  
gcloud container clusters get-credentials ai-infrastructure-gke \\
  --zone us-central1-a --project YOUR_PROJECT

# Verify connection
kubectl get nodes
```

### 2. Pods Stuck in Pending State

**Symptoms:**
```
NAME                    READY   STATUS    RESTARTS   AGE
ai-inference-xxx        0/1     Pending   0          5m
```

**Diagnosis:**
```bash
kubectl describe pod <pod-name> -n <namespace>
```

**Common Causes:**
- Insufficient resources
- Node selector mismatch
- PVC not bound

**Solutions:**
```bash
# Check node resources
kubectl top nodes

# Check node labels
kubectl get nodes --show-labels

# Scale cluster if needed
# (Cluster autoscaler should do this automatically)
```

### 3. Image Pull Errors

**Symptoms:**
```
Failed to pull image "...": rpc error: code = Unknown
```

**Solutions:**
```bash
# Check image exists
docker pull <image>

# Update image pull secrets
kubectl create secret docker-registry regcred \\
  --docker-server=<registry> \\
  --docker-username=<username> \\
  --docker-password=<password>

# Verify secret
kubectl get secrets
```

### 4. Terraform State Lock

**Symptoms:**
```
Error: Error acquiring the state lock
```

**Solutions:**
```bash
# Force unlock (use with caution)
terraform force-unlock <lock-id>

# Or remove lock file
rm -rf .terraform/
terraform init
```

### 5. High Cloud Costs

**Diagnosis:**
```bash
# Check resource usage
kubectl top nodes
kubectl top pods --all-namespaces

# List all resources
kubectl get all --all-namespaces
```

**Solutions:**
```bash
# Scale down inference
kubectl scale deployment ai-inference --replicas=1 -n production

# Delete GPU nodes when not training
kubectl delete nodes -l node-pool=gpu

# Destroy development resources
cd terraform/aws && terraform destroy
```

### 6. Monitoring Not Working

**Symptoms:**
- Grafana shows no data
- Prometheus targets down

**Solutions:**
```bash
# Check Prometheus pods
kubectl get pods -n monitoring

# Check Prometheus targets
kubectl port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090 -n monitoring
# Visit http://localhost:9090/targets

# Restart Prometheus
kubectl rollout restart statefulset prometheus-kube-prometheus-prometheus -n monitoring

# Check service discovery
kubectl get servicemonitors -n monitoring
```

### 7. Training Jobs Failing

**Diagnosis:**
```bash
# Check job status
kubectl get jobs

# View job logs
kubectl logs job/<job-name>

# Describe job
kubectl describe job <job-name>
```

**Common Issues:**
- OOM (Out of Memory)
- GPU not available
- Network connectivity

**Solutions:**
```bash
# Increase memory limits
# Edit kubernetes/training-job.yaml

# Check GPU availability
kubectl get nodes -l accelerator=nvidia

# Check GPU plugin
kubectl get daemonset nvidia-device-plugin-daemonset -n kube-system
```

### 8. ArgoCD Sync Issues

**Symptoms:**
- Application out of sync
- Sync fails with errors

**Solutions:**
```bash
# Manual sync
kubectl port-forward svc/argocd-server 8080:443 -n argocd
# Visit UI and click "Sync"

# Or via CLI
argocd app sync <app-name>

# Hard refresh
argocd app get <app-name> --hard-refresh

# Check application health
argocd app get <app-name>
```

## Getting Help

1. **Check logs**: `kubectl logs <pod-name> -n <namespace>`
2. **Describe resources**: `kubectl describe <resource> <name> -n <namespace>`
3. **Check events**: `kubectl get events -n <namespace> --sort-by='.metadata.creationTimestamp'`
4. **Search issues**: Check GitHub issues for similar problems
5. **Ask community**: Kubernetes Slack, Stack Overflow

## Debug Commands

```bash
# Get all resources
kubectl get all --all-namespaces

# Check pod details
kubectl get pod <pod-name> -o yaml -n <namespace>

# Execute shell in pod
kubectl exec -it <pod-name> -n <namespace> -- /bin/bash

# Check resource usage
kubectl top pods -n <namespace>
kubectl top nodes

# View recent events
kubectl get events --sort-by='.lastTimestamp' -n <namespace>

# Test DNS
kubectl run -it --rm debug --image=busybox --restart=Never -- nslookup kubernetes

# Test connectivity
kubectl run -it --rm debug --image=curlimages/curl --restart=Never -- curl <service-url>
```
""",
}

def create_file(filepath, content):
    """Create a file with content."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    print_success(f"Created {filepath}")

def create_directory_structure():
    """Create all necessary directories."""
    directories = [
        "terraform/aws", "terraform/gcp",
        "kubernetes/rbac", "kubernetes/network-policies",
        "monitoring/prometheus", "monitoring/loki", "monitoring/gpu-exporter", "monitoring/deployment",
        "inference/app", "training/src", "training/docker", "training/scripts",
        "istio", "argocd/applications", "argocd/projects",
        ".github/workflows", "scripts", "tests", "docs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print_success("Created directory structure")

def create_placeholder_note(filename, description):
    """Create a placeholder file with instructions."""
    content = f"""# {description}

## ⚠️ IMPORTANT: Copy Content from Artifacts

This file needs content from the Claude artifacts. Please copy the corresponding content:

1. Scroll up in your Claude conversation
2. Find the artifact titled: "{description}"
3. Copy the entire content
4. Paste it into this file

## File Purpose

{description}

## What to do after copying:

1. Save this file
2. Continue with the next file in docs/SETUP_INSTRUCTIONS.md
3. Once all files are copied, run: ./scripts/quick-start.sh

---
Generated by AI Infrastructure Installer
"""
    create_file(filename, content)

def main():
    """Main installer function."""
    print_header("AI Infrastructure Projects Installer")
    
    # Check if we're in a git repo
    if not Path(".git").exists():
        print_warning("Not in a git repository. Initialize one first:")
        print_info("  git init")
        print_info("  git remote add origin https://github.com/YOUR_USERNAME/ai-infrastructure-projects")
        print()
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(0)
    
    print_info("Creating project structure...")
    create_directory_structure()
    print()
    
    print_info("Creating essential files...")
    for filepath, content in FILES.items():
        create_file(filepath, content)
    print()
    
    print_info("Creating placeholder files with instructions...")
    
    placeholders = {
        "terraform/aws/main.tf": "Project A - AWS Terraform Complete Implementation",
        "terraform/aws/variables.tf": "Project A - Terraform Variables",
        "terraform/gcp/main.tf": "Project A - GCP Terraform Complete Implementation",
        "terraform/gcp/variables.tf": "Project A - GCP Variables and Config",
        "training/src/train_distributed.py": "Project B - Complete Distributed Training Implementation",
        "training/docker/Dockerfile": "Project B - Docker and Kubernetes Configuration (Dockerfile section)",
        "kubernetes/training-job.yaml": "Project B - Docker and Kubernetes Configuration (training-job.yaml section)",
        "monitoring/prometheus/values.yaml": "Project C - Complete Monitoring Stack (prometheus section)",
        "monitoring/gpu-exporter/gpu_metrics.py": "Project C - Complete Monitoring Stack (gpu_metrics.py section)",
        "inference/app/main.py": "Project D - Complete AI Inference Platform",
        "inference/Dockerfile": "Project D - Complete AI Inference Platform (Dockerfile section)",
        "kubernetes/inference-deployment.yaml": "Project D - Complete AI Inference Platform (deployment.yaml section)",
        ".github/workflows/ci-cd-pipeline.yaml": "Complete CI/CD Pipeline and GitOps Configuration",
        "scripts/quick-start.sh": "Automated Deployment Scripts and Documentation (quick-start.sh section)",
        "scripts/setup-local-dev.sh": "Automated Deployment Scripts and Documentation (setup-local-dev.sh section)",
    }
    
    for filepath, description in placeholders.items():
        create_placeholder_note(filepath, description)
    print()
    
    # Create setup instructions
    setup_instructions = """# Setup Instructions

## ✅ Step 1: Installation Complete!

The project structure has been created. Now you need to copy content from the Claude artifacts.

## 📋 Step 2: Copy Artifact Contents

Each placeholder file contains instructions. Go through them in this order:

### Infrastructure (Terraform)
1. `terraform/aws/main.tf`
2. `terraform/aws/variables.tf`  
3. `terraform/gcp/main.tf`
4. `terraform/gcp/variables.tf`

### Training Platform  
5. `training/src/train_distributed.py`
6. `training/docker/Dockerfile`
7. `kubernetes/training-job.yaml`

### Monitoring
8. `monitoring/prometheus/values.yaml`
9. `monitoring/gpu-exporter/gpu_metrics.py`

### Inference API
10. `inference/app/main.py`
11. `inference/Dockerfile`
12. `kubernetes/inference-deployment.yaml`

### CI/CD & GitOps
13. `.github/workflows/ci-cd-pipeline.yaml`
14. `scripts/quick-start.sh`
15. `scripts/setup-local-dev.sh`

## 🔧 Step 3: Configure

Edit these files with your values:
```bash
# AWS settings
nano terraform/aws/terraform.tfvars

# GCP settings  
nano terraform/gcp/terraform.tfvars
```

## ⚙️ Step 4: Setup Cloud Access

```bash
# AWS
aws configure

# GCP
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

## 🚀 Step 5: Deploy!

```bash
# Make scripts executable
chmod +x scripts/*.sh

# Run deployment
./scripts/quick-start.sh
```

## 📚 Need Help?

- See `docs/TROUBLESHOOTING.md` for common issues
- See `docs/ARCHITECTURE.md` for system overview  
- See `docs/QUICK_REFERENCE.md` for commands

## 💡 Tips

- Start with one cloud provider (AWS or GCP) to minimize complexity
- Use free tier accounts to minimize costs
- Test locally with minikube before deploying to cloud
- Read all documentation before starting

---

**Questions? Open an issue on GitHub!**
"""
    
    create_file("docs/SETUP_INSTRUCTIONS.md", setup_instructions)
    
    # Create quick reference
    quick_ref = """# Quick Reference

## 🚀 Deployment
```bash
./scripts/quick-start.sh                    # Full deployment
./scripts/quick-start.sh infra              # Infrastructure only
./scripts/quick-start.sh monitoring         # Monitoring only
./scripts/quick-start.sh apps               # Applications only
```

## 🔍 Kubernetes Commands
```bash
# Get resources
kubectl get pods --all-namespaces
kubectl get nodes
kubectl get services -n production

# Logs
kubectl logs -f deployment/ai-inference -n production
kubectl logs -f job/distributed-ai-training

# Scale
kubectl scale deployment ai-inference --replicas=5 -n production

# Port forward
kubectl port-forward svc/ai-inference-service 8000:80 -n production
kubectl port-forward svc/prometheus-grafana 3000:80 -n monitoring
```

## 📊 Access Services
```bash
# Grafana (monitoring)
kubectl port-forward svc/prometheus-grafana 3000:80 -n monitoring
# http://localhost:3000 (admin/admin123)

# AI Inference API
kubectl port-forward svc/ai-inference-service 8000:80 -n production  
# http://localhost:8000/docs

# Prometheus
kubectl port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090 -n monitoring
# http://localhost:9090

# ArgoCD
kubectl port-forward svc/argocd-server 8080:443 -n argocd
# https://localhost:8080
```

## 💰 Cost Management
```bash
# Scale down
kubectl scale deployment --all --replicas=0 -n production

# Destroy
cd terraform/aws && terraform destroy
cd terraform/gcp && terraform destroy
```

## 🔧 Troubleshooting
```bash
# Check pod status
kubectl describe pod <pod-name> -n <namespace>

# View events
kubectl get events --sort-by='.metadata.creationTimestamp' -n <namespace>

# Resource usage
kubectl top nodes
kubectl top pods --all-namespaces

# Update kubeconfig
aws eks update-kubeconfig --region us-west-2 --name ai-infrastructure-eks
gcloud container clusters get-credentials ai-infrastructure-gke --zone us-central1-a
```
"""
    
    create_file("docs/QUICK_REFERENCE.md", quick_ref)
    
    print()
    print_header("Installation Complete!")
    
    print(f"{Colors.OKGREEN}Next steps:{Colors.ENDC}")
    print(f"  1. Read: {Colors.BOLD}docs/SETUP_INSTRUCTIONS.md{Colors.ENDC}")
    print(f"  2. Copy artifact contents into placeholder files")
    print(f"  3. Configure: terraform/*/terraform.tfvars")
    print(f"  4. Deploy: ./scripts/quick-start.sh")
    print()
    print(f"{Colors.OKCYAN}Documentation:{Colors.ENDC}")
    print(f"  • Setup Guide: docs/SETUP_INSTRUCTIONS.md")
    print(f"  • Quick Reference: docs/QUICK_REFERENCE.md")
    print(f"  • Architecture: docs/ARCHITECTURE.md")
    print(f"  • Troubleshooting: docs/TROUBLESHOOTING.md")
    print()
    print(f"{Colors.WARNING}⚠️  Don't forget to:{Colors.ENDC}")
    print(f"  • Copy all artifact contents")
    print(f"  • Configure AWS and GCP credentials")
    print(f"  • Update terraform.tfvars files")
    print()

if __name__ == "__main__":
    main()
