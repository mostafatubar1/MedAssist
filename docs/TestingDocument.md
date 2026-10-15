# Testing Document — MedAssist

## 1. Test Plan

### 1.1 Objectives
_TODO_

### 1.2 Scope
_TODO_

### 1.3 Test Levels
- Unit testing
- API/integration testing
- Frontend component/system testing
- End-to-end validation
- RAG evaluation harness (plain vs agentic)

### 1.4 Environments and Test Data
_TODO_

### 1.5 Entry / Exit Criteria
_TODO_

## 2. Validation Test Cases

> Sommerville distinction: validation testing demonstrates that the system meets user/system requirements. Maintain **one row per functional requirement**.

| Test ID | Requirement ID | Scenario | Preconditions | Steps/Input | Expected Result | Status |
|---|---|---|---|---|---|---|
| VAL-FR-P-001 | FR-P-001 | _TODO_ | _TODO_ | _TODO_ | _TODO_ | Not run |

## 3. Defect Test Cases

> Defect testing is designed to expose faults using boundaries, invalid states, malformed inputs, concurrency, authorization violations, and failure paths.

| Test ID | Target | Fault hypothesis / edge case | Input | Expected defensive behavior | Status |
|---|---|---|---|---|---|
| DEF-AUTH-001 | Auth | Duplicate email | Same signup twice | HTTP 409 | Automated |
| DEF-AUTH-002 | RBAC | Patient calls doctor dashboard | Valid patient JWT | HTTP 403 | Automated |
| DEF-001 | _TODO_ | _TODO_ | _TODO_ | _TODO_ | Not run |

## 4. Automated Test Organization

```text
backend/tests/
  auth/
    test_auth_validation.py
    test_auth_defects.py
```

Replicate that naming split in each domain as feature branches are implemented.

## 5. Test Coverage Summary

| Area | Validation tests | Defect tests | Coverage / evidence | Owner |
|---|---:|---:|---|---|
| Auth | 1 | 3 | _TODO CI result_ | Shared foundation |
| RAG Core | 0 | 0 | _TODO_ | Mostafa |
| Body Map | 0 | 0 | _TODO_ | Adham |
| Patient Memory | 0 | 0 | _TODO_ | Omar |
| Security/Consent | 0 | 0 | _TODO_ | Ziad |
| Dashboard/Eval | 0 | 0 | _TODO_ | Nour |

## 6. RAG Evaluation Plan

_TODO: define versioned evaluation dataset, answer/reference policy, faithfulness metric, accuracy metric, latency/cost metrics, and a controlled plain-RAG vs agentic-RAG comparison._
