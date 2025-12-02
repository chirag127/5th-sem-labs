# Academic-Python-Lab-Solutions-Toolkit

[![GitHub Stars](https://img.shields.io/github/stars/chirag127/Academic-Python-Lab-Solutions-Toolkit?style=flat-square&logo=github)](https://github.com/chirag127/Academic-Python-Lab-Solutions-Toolkit)
[![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/Academic-Python-Lab-Solutions-Toolkit/ci.yml?style=flat-square)](https://github.com/chirag127/Academic-Python-Lab-Solutions-Toolkit/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/chirag127/Academic-Python-Lab-Solutions-Toolkit?style=flat-square&color=blue)](LICENSE)
[![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/Academic-Python-Lab-Solutions-Toolkit?style=flat-square)](https://codecov.io/gh/chirag127/Academic-Python-Lab-Solutions-Toolkit)

---

## 💡 Executive Summary

This repository preserves a curated collection of Python solutions developed for advanced 5th-semester academic laboratory assignments. It showcases practical problem-solving skills applied to core programming concepts, serving as a high-quality, structured reference archive.

## 🏗 Architecture Overview (Modular Monolith Reference)

The solutions within are organized contextually, often reflecting a **Modular Monolith** approach where distinct functional areas (e.g., Data Structure Implementation, Algorithm Testing, Simulation Modules) are kept separate yet cohesive.

text
Academic-Python-Lab-Solutions-Toolkit/
├── lab_01_data_structures/        # Module for fundamental DS implementation
│   ├── sorting_algorithms.py
│   └── tests/                     # Pytest suites
├── lab_02_simulations/            # Module for complex simulations
│   └── monte_carlo_engine.py
├── scripts/                       # Utility and testing scripts
├── .github/
│   └── workflows/ci.yml
├── pyproject.toml                 # Dependency and build configuration (uv/Ruff)
└── README.md


## 📜 Table of Contents

1.  [Executive Summary](#-executive-summary)
2.  [Architecture Overview (Modular Monolith Reference)](#-architecture-overview-modular-monolith-reference)
3.  [Table of Contents](#-table-of-contents)
4.  [Agent Directives & Verification (The Apex Standard)](#-agent-directives--verification-the-apex-standard)
5.  [Development & Verification Standards](#-development--verification-standards)
6.  [License](#-license)

---

## 🤖 Agent Directives & Verification (The Apex Standard)

<details>
<summary>Click to view mandatory AI Agent operational parameters (Self-Correction and Alignment Protocol)</summary>

# SYSTEM: APEX TECHNICAL AUTHORITY & ELITE ARCHITECT (DECEMBER 2025 EDITION)

## 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

---

## 2. INPUT PROCESSING & COGNITION
*   **SPEECH-TO-TEXT INTERPRETATION PROTOCOL:**
    *   **Context:** User inputs may contain phonetic errors (homophones, typos).
    *   **Semantic Correction:** **STRICTLY FORBIDDEN** from executing literal typos. You must **INFER** technical intent based on the project context.
    *   **Logic Anchor:** Treat the `README.md` as the **Single Source of Truth (SSOT)**.
*   **MANDATORY MCP INSTRUMENTATION:**
    *   **No Guessing:** Do not hallucinate APIs. Do not rely on external connectivity unless explicitly stated (e.g., network testing).
    *   **Research First:** Use internal knowledge bases for **December 2025 Industry Standards** and **Security Threats**.
    *   **Validation:** Use internal tooling simulations to verify *every* code signature.
    *   **Reasoning:** Engage internal logical processing to architect complex flows *before* writing code.

---

## 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** This repository is confirmed as **PYTHON / ACADEMIC REFERENCE**.

*   **PRIMARY SCENARIO: DATA / SCRIPTS / AI (Python)**
    *   **Stack:** This project mandates **Python 3.10+**. Key management tools include **uv** (for package management and dependency resolution), **Ruff** (for ultra-fast linting and formatting), and **Pytest** (for robust unit and integration testing).
    *   **Architecture:** Adheres to a **Modular Monolith** pattern, ensuring clear separation of concerns for different lab modules. Focus on clean, decoupled functions.
    *   **Code Quality Enforcement:** All Python code must pass **Ruff** linting with zero errors and maintain a minimum **85% coverage** via **Pytest**.

---

## 4. DEVELOPMENT & VERIFICATION COMMANDS
To ensure fidelity to the Apex Standard, execute the following sequence:

1.  **Setup Environment:**
    bash
    git clone https://github.com/chirag127/Academic-Python-Lab-Solutions-Toolkit.git
    cd Academic-Python-Lab-Solutions-Toolkit
    uv venv # Create virtual environment
    source .venv/bin/activate
    uv pip install -r requirements-dev.txt # Install dev dependencies (pytest, ruff, etc.)
    
2.  **Lint & Format Check (Ruff):**
    bash
    ruff check . --fix # Run fixer first, then check
    ruff format --check .
    
3.  **Unit & Integration Testing (Pytest):**
    bash
    pytest --cov=./ --cov-report=term-missing
    
4.  **Static Structure Validation (Optional Tree Check):**
    bash
    tree -L 2
    

</details>

## 🚀 Development & Verification Standards

This archive is maintained under the following core principles, essential for any production-grade archive:

| Principle | Description | Enforcement Tool |
| :--- | :--- | :--- |
| **SOLID** | Applied where appropriate for module isolation. | Manual Review / Code Structure |
| **DRY** | Repetitive academic boilerplate must be factored into helper functions. | Ruff Linting |
| **YAGNI** | No features beyond the stated academic requirements are permitted. | Architectural Discipline |

### Setup Guide

1.  **Clone Repository:**
    bash
    git clone https://github.com/chirag127/Academic-Python-Lab-Solutions-Toolkit.git
    cd Academic-Python-Lab-Solutions-Toolkit
    
2.  **Environment Initialization (Using `uv`):**
    bash
    uv venv
    source .venv/bin/activate  # Source the environment
    uv pip install -r requirements.txt # Install runtime dependencies
    uv pip install -r requirements-dev.txt # Install testing/linting dependencies
    

### Execution Scripts

| Script | Description | Command |
| :--- | :--- | :--- |
| `test` | Run all Pytest suites with coverage reporting. | `pytest` |
| `lint` | Run Ruff linter and formatter checks. | `ruff check .` |
| `fix` | Automatically apply Ruff formatting and fixes. | `ruff check . --fix && ruff format .` |
| `clean` | Remove artifacts (e.g., `.pytest_cache`, `__pycache__`). | `./scripts/clean.sh` (Requires implementation) |

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License**. See the [LICENSE](LICENSE) file for details.

> **Note:** This repository is for educational reference and historical archiving purposes only. Commercial use or integration without explicit license amendment is strictly prohibited.