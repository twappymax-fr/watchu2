# VPS Setup Checklist for Docker + Django (Production Ready)

## 1. Initial system update
```bash
apt update && apt upgrade -y
```

## 2. Install essential tools
```bash
apt install -y curl git ufw ca-certificates gnupg lsb-release
```

## 3. Install Docker (official way)
```bash
install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo $VERSION_CODENAME) stable" \
> /etc/apt/sources.list.d/docker.list

apt update

apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## 4. Enable Docker
```bash
systemctl enable docker
systemctl start docker

docker --version
docker compose version
```

## 5. Clone project
```bash
git clone <your-repo-url>
cd <your-project-folder>
```

## 6. Create environment file
```bash
nano .env.prod
```

Example:
```env
POSTGRES_DB=mydb
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
DEBUG=0
SECRET_KEY=your-secret-key
```

## 7. Firewall setup
```bash
ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

sudo ufw reload
ufw enable

````
## Verify:

```bash
sudo ufw status
```

```

## 8. Fix permissions
```bash
chmod +x entrypoint.sh
dos2unix entrypoint.sh
```

## 9. Run containers
```bash
docker compose up --build -d
```

## 10. Useful commands
```bash
docker ps
docker compose logs -f
docker compose down -v
docker compose up --build -d
```

## 11. Optional: Add swap (prevents OOM crashes)
```bash
fallocate -l 1G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile

echo '/swapfile none swap sw 0 0' >> /etc/fstab
```

## Quick deploy
```bash
git clone <repo> && cd <project> && docker compose up --build -d
```
