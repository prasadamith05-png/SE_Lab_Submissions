# Software Engineering Mini-Project: Sports Event Crowd & Resource Management System

**Course:** Software Engineering (UE24CS341A / UE23CS351A)  
**Institution:** Department of Computer Science & Engineering, PES University, Bengaluru  
**Student:** Amith Prasad | **Roll No:** 33 (`PES1UG24AM033`)  
**Project GitHub Repository:** [prasadamith05-png/Sports-Event-Crowd-Resource-Management-System](https://github.com/prasadamith05-png/Sports-Event-Crowd-Resource-Management-System)  

---

## 1. Project Synopsis
The **Sports Event Crowd & Resource Management System** is an enterprise-grade platform designed to streamline match scheduling, high-throughput turnstile ingress, categorized seating allocations, and real-time arena crowd density telemetry.

Modern collegiate tournaments and stadiums experience high-velocity bottlenecks at physical turnstiles, safety risks during surges, and double-booking race conditions. This project resolves these challenges through a modular, decoupled architecture featuring sub-50ms cryptographic ticket scanning, Redis-backed seat holds, and real-time security alerting.

---

## 2. System Architecture & Diagrams

### Core Architecture Artifacts (Included in `architecture/`):
1. **System Architecture Diagram (`architecture/System_Architecture.png`):** High-level multi-tier view showing Next.js frontends, Express API Gateway, Microservice controllers, PostgreSQL, and Redis lock engines.
2. **Entity-Relationship Diagram (`architecture/ER_Diagram.png`):** Comprehensive Crow's Foot ER schema modeling Stadiums, Stands, Matches, Tickets, Turnstiles, Ingress Logs, Security Alerts, and Users.
3. **Relational Schema (`architecture/Relational_Schema.png`):** 3NF normalized tables with foreign key constraints, composite keys, and indexing policies.

---

## 3. Technology Stack
- **Frontend:** Next.js 14, React, Tailwind CSS, Lucide Icons, Canvas / SVG Seating Grid
- **Backend API:** Node.js, Express, TypeScript, RESTful endpoints
- **Database & Cache:** PostgreSQL (Relational schema, triggers, views), Redis (distributed lock for seat holds)
- **Security:** JWT authentication, HMAC-signed ticket QR codes, anti-passback turnstile validation
- **Testing:** Pytest / Jest integration tests

---

## 4. Documentation & Deliverables
- [`architecture/`](architecture/): High-resolution system diagrams.
- [`reports/Project_Report.pdf`](reports/Project_Report.pdf): Complete technical report.
