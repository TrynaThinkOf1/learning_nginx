![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)
![Flask](https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff)
![Node.js](https://img.shields.io/badge/Node.js-6DA55F?logo=node.js&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white&style=for-the-badge)

# Learn Docker & NginX: Cross-Platform Installation and Setup Guide

## 📋 Table of Contents
- [Debian Installation](#debian-installation)
- [Ubuntu Installation](#ubuntu-installation)
- [Project Access](#project-access)
- [SSL Certificate Handling](#ssl-certificate-warnings)

## 🐧 Debian Installation {#debian-installation}

### 1. Install Docker
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### 2. Install Docker Compose
```bash
sudo apt install docker-compose -y
```

### 3. Install Nginx
```bash
sudo apt install nginx -y
```

### 4. Enable Services
```bash
sudo systemctl enable nginx
sudo systemctl enable docker
```

### 5. Reboot
```bash
sudo reboot
```

## 🟠 Ubuntu Installation {#ubuntu-installation}

### 1. Install Docker
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### 2. Install Docker Compose
```bash
sudo apt install docker-compose -y
```

### 3. Install Nginx
```bash
sudo apt install nginx -y
```

### 4. Enable Services
```bash
sudo systemctl enable nginx
sudo systemctl enable docker
```

### 5. Reboot
```bash
sudo reboot
```

## 🚀 Project Setup {#project-access}

### Clone Repository
```bash
git clone https://www.github.com/trynathinkof1/learning_nginx
cd learning_nginx/[project_directory]
```

### Build and Run Project
For Debian:
```bash
sudo docker-compose up --build -d
```

For Ubuntu:
```bash
sudo docker compose up --build -d
```

### Reload Nginx
```bash
sudo nginx -s reload
```

## 🌐 Accessing Your Project

### Remote Server
- Open a web browser
- Navigate to: `https://<your_server_ip_address>`

### Local Machine
- Open a web browser
- Navigate to: `https://127.0.0.1` or `https://localhost`

## 🔐 SSL Certificate Warnings {#ssl-certificate-warnings}

When accessing your site, you may encounter a security warning due to a self-signed SSL certificate. This is normal for development environments.

### Browser Navigation
1. Click "Advanced"
2. Choose "Proceed to website" or "Accept the Risk and Continue"

## 📝 Notes
- Ensure you're logged in after system reboot
- Use strong, unique passwords
- Keep systems and Docker images updated