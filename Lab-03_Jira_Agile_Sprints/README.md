# Lab 3: Agile Project Management, Jira Sprints & Requirements Engineering

**Course:** Software Engineering (UE24CS341A)  
**Institution:** PES University, Bengaluru  
**Student:** Amith Prasad | **Roll No:** 33 (`PES1UG24AM033`)  

---

## 1. Objective
- Apply modern Agile & Scrum software development lifecycle frameworks.
- Structure project deliverables into Epics, User Stories, Tasks, and Bugs using Jira concepts.
- Estimate complexity using Story Points (Fibonacci scale) and plan 2-week time-boxed Sprints.
- Formulate acceptance criteria using the Gherkin syntax (`Given-When-Then`).

---

## 2. Project Hierarchy & Structure
- **Project Name:** Sports Event Crowd & Resource Management System (`SE-SEMS`)
- **Methodology:** Scrum with 2-week iterations
- **Key Epics:**
  - `EPIC-01`: Core Ticketing & Real-Time Seating Engine
  - `EPIC-02`: High-Speed Ingress & Turnstile Scanning Pipeline
  - `EPIC-03`: Real-Time Arena Crowd Density Monitoring & Safety Alerts

---

## 3. Sprint Planning (Sprint 1: Ingress & Core Booking)
- **Sprint Duration:** 2 Weeks (10 Working Days)
- **Committed Story Points:** 34 Points
- **Velocity Target:** 35 Points

| Issue Key | Type | Summary | Estimate (SP) | Priority |
|---|---|---|---|---|
| `SEMS-101` | Story | As a fan, I want to view a real-time arena seating map so I can choose seats. | 5 | High |
| `SEMS-102` | Story | As a buyer, I want an exclusive 10-minute hold on selected seats during checkout. | 8 | Highest |
| `SEMS-103` | Story | As a spectator, I want a cryptographically signed QR pass on my phone. | 5 | High |
| `SEMS-104` | Story | As a turnstile scanner, I want sub-50ms QR validation to avoid gate bottlenecks. | 8 | Highest |
| `SEMS-105` | Task | Configure Redis cluster with distributed lock manager for seat holds. | 5 | Medium |
| `SEMS-106` | Bug | Fix race condition where simultaneous clicks reserve the same VIP seat. | 3 | Highest |

---

## 4. Key Deliverables
- [`agile_workflow_guide.md`](agile_workflow_guide.md): Guide to Scrum ceremonies and backlog management.
- [`sprint_backlog_and_user_stories.md`](sprint_backlog_and_user_stories.md): Detailed user stories with Gherkin acceptance criteria.
