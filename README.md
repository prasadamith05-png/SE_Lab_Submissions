# Software Engineering Lab Submissions Portfolio

**Institution:** PES University, Bengaluru  
**Department:** Computer Science and Engineering  
**Course:** Software Engineering (Course Code: `UE24CS341A` / Classroom Section `pesse A`)  
**Classroom URL:** [https://classroom.google.com/u/0/c/ODU1ODc4NDg5OTc3](https://classroom.google.com/u/0/c/ODU1ODc4NDg5OTc3)  
**Student Name:** Amith Prasad  
**Roll Number:** 33 (`PES1UG24AM033`)  
**GitHub Profile:** [prasadamith05-png](https://github.com/prasadamith05-png)  

---

## Master Portfolio Overview

This unified repository consolidates all laboratory submissions, assignments, and mini-project deliverables for the **Software Engineering** course at PES University. Each folder contains production-grade code, test suites, architecture diagrams, formal specifications, and technical evaluation reports.

---

## Repository Table of Contents

| Lab / Module | Title & Focus | Tools & Frameworks | Key Deliverables & Artifacts | Status |
|:---|:---|:---|:---|:---:|
| [**Lab 01**](Lab-01_UseCase_Diagrams/) | **Use Case Diagrams & Requirements Modeling** | UML, PlantUML, Mermaid | Detailed Use Case Specs (`UC-02`, `UC-05`), Actor Definitions, UML Diagrams | **Completed** |
| [**Lab 02**](Lab-02_Component_Diagrams/) | **Component Diagrams & Architecture** | UML, PlantUML, Mermaid | Component Interface Contracts, Lollipop-Socket Diagrams, Microservices Layout | **Completed** |
| [**Lab 03**](Lab-03_Jira_Agile_Sprints/) | **Jira Agile Sprints & Requirements** | Jira, Scrum, Gherkin | 2-Week Sprint Backlog, Epics, User Stories with INVEST & Acceptance Criteria | **Completed** |
| [**Lab 04**](Lab-04_Vibe_Coding/) | **Vibe Coding with AI (Missile Command)** | Python, Pygame, LLM Pair | Battery Selection Bug Fix, Dynamic Thermal Explosions, City Rebuild Milestone | **Completed** |
| [**Assignment**](Assignment_DVC_and_MLflow/) | **Data Version Control & MLflow Tracking** | DVC, MLflow, Scikit-learn | `data.txt.dvc` Tracking, Iris RF Model Training, Parameters & Metric Logging | **Completed** |
| [**Lab 05**](Lab-05_Static_Code_Analysis/) | **Static Code Analysis (Movie Reviews)** | Pylint, Bandit, Flake8 | Pylint Score **10.00/10**, 0 Bandit Vulns, Clean PEP 8, `issues.md`, Reflection | **Completed** |
| [**Lab 06**](Lab-06_Coverage_Analysis/) | **Code & Branch Coverage Analysis** | Coverage.py, Pytest | **100% Statement Coverage**, **100% Branch Coverage (26/26)**, Visual Reports | **Completed** |
| [**Lab 07**](Lab-07_Fuzz_Testing/) | **Fuzz Testing & Input Validation** | Hypothesis, Pytest | Automated Property-Based Testing, 3 Bug Remediations, Guard Clauses | **Completed** |
| [**Mini-Project**](Mini_Project-01/) | **Sports Event Crowd Management System** | Next.js, PostgreSQL, Redis | System Architecture, ER Diagrams, Relational Schema, Project Report | **Completed** |

---

## Laboratory Summaries

### [Lab 1: Use Case Modeling](Lab-01_UseCase_Diagrams/)
- Requirements engineering for a distributed sports stadium platform.
- Modeled interactions across Spectators, Organizers, Turnstile Security Staff, and Emergency Teams.
- Formalized preconditions, main flows, extensions, and postconditions.

### [Lab 2: Component Architecture](Lab-02_Component_Diagrams/)
- Structural design decoupling Client applications, API Gateway, Ticketing Service, Ingress Controller, and Telemetry Engine.
- Interface contracts defined using Provided/Required interfaces and gRPC/REST protocols.

### [Lab 3: Jira & Agile Sprints](Lab-03_Jira_Agile_Sprints/)
- 2-week time-boxed sprint planning with 34 committed story points.
- Acceptance testing formatted using Gherkin syntax (`Given-When-Then`).

### [Lab 4: Vibe Coding (Missile Command)](Lab-04_Vibe_Coding/)
- Pair programming with AI to repair a single-file Pygame arcade simulation.
- Fixed nearest-battery target allocation bug, implemented smooth 3-stage thermal explosion color mapping, and added score-based city restoration.

### [Assignment: DVC and MLflow](Assignment_DVC_and_MLflow/)
- Data Version Control (`DVC`) integration for tracking binary data without bloating git history.
- Experiment tracking and model registry using `MLflow` for machine learning classifier runs.

### [Lab 5: Static Code Analysis (Movie Reviews)](Lab-05_Static_Code_Analysis/)
- Multi-linter security and quality audit of `movie_reviews.py`.
- **Bandit:** Eliminated all 4 security flaws (insecure random generation, assert usages).
- **Pylint:** Raised rating from **5.47/10** to a perfect **10.00/10**.
- **Flake8:** Resolved all PEP 8 violations while preserving identical runtime functionality.

### [Lab 6: Code & Branch Coverage Analysis](Lab-06_Coverage_Analysis/)
- Rigorous white-box test suite for `spam_scoring.py`.
- Generated HTML and terminal coverage reports achieving:
  - **Statement Coverage:** `100%` (Exceeding the $\ge 90\%$ rubric threshold)
  - **Branch Coverage:** `100%` (`26/26` branches covered)

### [Lab 7: Fuzz Testing with Hypothesis](Lab-07_Fuzz_Testing/)
- Automated property-based fuzz testing uncovering `IndexError`, `ValueError`, and `ZeroDivisionError` crashes under adversarial input payloads.
- Hardened all functions with defensive programming guard clauses, verifying 100% test pass rate under thousands of synthetic examples.

### [Mini Project 1: Sports Event Crowd Management System](Mini_Project-01/)
- Comprehensive system design, ER diagram, 3NF relational schema, and project report.

---

## Quick Start & Verification

### Running Test Suites
```bash
# 1. Verify Lab 6 Coverage Tests
cd Lab-06_Coverage_Analysis
python -m pytest CodeCoverageTest_spam_scoring.py BranchCoverageTest_spam_scoring.py -v

# 2. Verify Lab 7 Hypothesis Fuzz Tests
cd ../Lab-07_Fuzz_Testing
python -m pytest test_spam_scoring_hypothesis.py -v

# 3. Launch Lab 4 Pygame Missile Command
cd ../Lab-04_Vibe_Coding
python game.py

# 4. Run Lab 5 Movie Review System & Static Lint
cd ../Lab-05_Static_Code_Analysis
python movie_reviews.py
python -m pylint movie_reviews.py
```

---

## Author & Academic Integrity
- **Name:** Amith Prasad
- **SRN / Roll:** PES1UG24AM033 (Roll: 33)
- **Institution:** PES University, RR Campus, Bengaluru
