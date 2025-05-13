# 🐧 Bash Scripting - Infrastructure Automation (IaC)

Repository dedicated to Bash automation exercises developed during [Digital Innovation One (DIO)](https://www.dio.me) courses.

## 🛠️ Projects

### 1. **Apache Server Automation**  
`[dio-apache-setup.sh]`  
📌 **Purpose**: Automated web server provisioning (Ubuntu)  
✅ **Features**:
- Apache installation and configuration
- Web service initialization

### 2. **User Environment Automation (IaC)**

📌 **Purpose**: Infrastructure-as-Code implementation for user management in Linux
✅ **Features**:
- User/Groups: Automated creation with useradd, groupadd
- Permission Control: chown and chmod commands
- Idempotency: Checks existing users/groups before creation

```bash
# How to run:
chmod +x dio-apache-setup.sh
sudo ./dio-apache-setup.sh

## 📚 References
- [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/)
- [DIO - Linux Experience](https://web.dio.me/course/linux-experience)
