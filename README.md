# 🧠 LF-Home-Lab

 <!--Badges -->                                                
![Debian](https://img.shields.io/badge/Debian-12%20Bookworm-A81D33?logo=debian&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-2%20Nodes-C51A4A?logo=raspberry-pi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![Pi-hole](https://img.shields.io/badge/Pi--hole-DNS%20Filtering-96060C?logo=pi-hole&logoColor=white)
![N8N](https://img.shields.io/badge/N8N-Automation-EA4B71?logo=n8n&logoColor=white)
![PhotoPrism](https://img.shields.io/badge/PhotoPrism-Media-00ADD8?logo=google-photos&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Hardened-28A745?logo=security&logoColor=green)
![Syslog](https://img.shields.io/badge/Syslog-Monitoring-5E5E5E?logo=elastic-stack&logoColor=blue)
![Ollama](https://img.shields.io/badge/Ollama-LLM-000000?logo=ollama&logoColor=white)
![Stable Diffusion](https://img.shields.io/badge/Stable%20Diffusion-AI-FF6F00?logo=stable-diffusion&logoColor=white)
![License](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)
![Last Commit](https://img.shields.io/github/last-commit/LFreitas88/LF-Home-Lab)
![Repo Size](https://img.shields.io/github/repo-size/LFreitas88/LF-Home-Lab) 


> **Cybersecurity homelab documentation: Debian server hardening, self-hosted services, Raspberry Pi infrastructure, and real-world security projects**  

---

## 👨‍💻 About Me

**Leandro Freitas** | Cybersecurity Student @ Bergen Community College
📍 New Jersey, USA | 🎓 Graduating 2027
💼 Career transition: CNC Programmer → IT/Cybersecurity

This repository documents my hands-on learning journey building and securing real infrastructure. Everything here runs on actual hardware and reflects real decisions

---

## 💡 Repository Purpose

**What this is:**
- Working documentation for my production homelab                             
- Portfolio of applied security concepts
- Learning journal with real implementations                                  
                                                                                
**Current infrastructure:**                                                   
- Debian 12 server (server-lf1) running Pi-hole + N8N                         
- Raspberry Pi NAS with PhotoPrism + Samba                                    
- Raspberry Pi syslog sensor (Blue Team practice)                             
- Flipper Zero security testing                                               
- Self-hosted AI models (Ollama, Stable Diffusion)                            
                                                                              
**Goals:**                                                                    
- Apply classroom concepts to real systems                                    
- Build maintainable, documented infrastructure                               
- Create technical portfolio for career transition **What this is:**

---

## 🧩 Repository Structure

| Folder | Description | Status |
|--------|-------------|--------|
| [**CollegePythonScripts/**](CollegePythonScripts) | Collection of Python scripts from my academic journey (INF-103) — includes exercises, automations, and OOP projects with full documentation |
| [**server_setup/**](server_setup) | Configuration files, hardening reports, and documentation for my Debian-based home server | 

---

## 🏗️ Lab Infrastructure

### Server-LF1 (Debian 12)                                                    
**Services:**                                                                 
- 🛡️ **Pi-hole** - Network-wide DNS filtering (ports 53, 80)                  
- ⚙️ **N8N** - Workflow automation (port 5678)                                
- 🐳 **Docker** - Container orchestration                                     

**Security measures:**                                                        
- SSH key-only authentication                                                 
- UFW firewall configuration                                                  
- Documented hardening process                                                

### Raspberry Pi Projects                                                     
**NAS/Media Server:**                                                         
- Samba file sharing                                                          
- PhotoPrism photo management                                                 
- External HDD storage (no SD writes)                                         

**Blue Team Sensor:**                                                         
- Centralized syslog collection                                               
- Fail2Ban implementation                                                     
- Lightweight passive monitoring                                              

---                                                                           

## 🎓 Academic Work                                                           

**Python Fundamentals (INF-103)**                                             
- 16+ functional scripts documented with learning context                     
- OOP project: Mobile phone management system                                 
- Topics: file handling, automation, Caesar cipher, password generation       

---                                                                           

## ⚖️ License                                                                 
                                                                                
**CC0-1.0 License (Public Domain)** unless specified otherwise.               
Free to use for educational or personal purposes.                             

---                                                                           
                                                                                
## 💬 Contact                                                                 

Questions or suggestions? Open an issue or reach out.                         

**Last updated:** January 2026         
