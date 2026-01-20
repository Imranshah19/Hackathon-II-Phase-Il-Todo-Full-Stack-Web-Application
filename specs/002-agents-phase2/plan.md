# Implementation Plan: Agents Phase-2

**Branch**: `002-agents-phase2` | **Date**: 2026-01-12 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-agents-phase2/spec.md`

## Summary

Implement a modular agent architecture for the Todo Full-Stack Web Application. The system consists of 7 specialized agents (Orchestrator, Auth, Task, User, AI, Planner, TaskExecutor) that communicate through a standardized protocol. Each agent has defined responsibilities, inputs/outputs, assigned skills, and tools. The architecture enables request routing, workflow coordination, and graceful degradation when services are unavailable.

## Technical Context

**Language/Version**: Python 3.11+ (backend agent runtime)
**Primary Dependencies**: FastAPI, Pydantic, SQLModel, structlog
**Storage**: PostgreSQL (Neon Serverless) via SQLModel ORM
**Testing**: pytest (contract tests, unit tests, integration tests)
**Target Platform**: Linux server (containerized), API-first
**Project Type**: Web application (backend-focused for agent runtime)
**Performance Goals**: API responses <2s, auth operations <1s, 100 concurrent users
**Constraints**: Synchronous agent communication, in-process calls (not over network), single database instance
**Scale/Scope**: 7 agents, 27 skills, 21 functional requirements

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Spec-First Development | ✅ PASS | spec.md created with full agent definitions before plan |
| II. Layered Architecture | ✅ PASS | Orchestrator coordinates domain agents; each agent operates at application layer |
| III. Test-First Development | ✅ PASS | TDD enforced via tasks.md structure |
| IV. Secure by Design | ✅ PASS | Auth validation on every request, error sanitization, correlation IDs |
| V. API-First Integration | ✅ PASS | Standardized AgentRequest/AgentResponse protocol |
| VI. Minimal Viable Diff | ✅ PASS | 7 agents scoped to spec; no speculative features |

**Gate Status**: ✅ ALL GATES PASS — Proceed to implementation

## Project Structure

### Documentation (this feature)

```text
specs/002-agents-phase2/
├── plan.md              # This file
├── spec.md              # Feature specification
├── checklists/          # Requirements checklists
└── tasks.md             # Implementation tasks
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py              # BaseAgent abstract class
│   │   ├── protocol.py          # AgentRequest, AgentResponse models
│   │   ├── registry.py          # Agent discovery and registration
│   │   ├── orchestrator/
│   │   │   ├── __init__.py
│   │   │   └── agent.py         # OrchestratorAgent
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   └── agent.py         # AuthAgent
│   │   ├── task/
│   │   │   ├── __init__.py
│   │   │   └── agent.py         # TaskAgent
│   │   ├── user/
│   │   │   ├── __init__.py
│   │   │   └── agent.py         # UserAgent
│   │   ├── ai/
│   │   │   ├── __init__.py
│   │   │   └── agent.py         # AIAgent
│   │   ├── planner/
│   │   │   ├── __init__.py
│   │   │   └── agent.py         # PlannerAgent
│   │   └── executor/
│   │       ├── __init__.py
│   │       └── agent.py         # TaskExecutorAgent
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── logger.py            # Logger tool
│   │   ├── metrics.py           # MetricsCollector tool
│   │   ├── rate_limiter.py      # RateLimiter tool
│   │   └── circuit_breaker.py   # CircuitBreaker tool
│   └── api/
│       └── agents.py            # Agent invocation endpoints (if needed)
└── tests/
    ├── contract/
    │   └── agents/              # Agent protocol tests
    ├── integration/
    │   └── agents/              # Cross-agent tests
    └── unit/
        └── agents/              # Individual agent tests
```

**Structure Decision**: Web application (Option 2). Agents are backend-only services that process requests and coordinate workflows. The agent runtime lives in `backend/src/agents/` with domain-based organization matching the spec (7 agents). Frontend interacts with agents through the existing API layer.

## Complexity Tracking

> No Constitution Check violations. No complexity justification needed.

## Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Agent communication | In-process function calls | Simplicity, performance, no network overhead |
| Protocol format | Pydantic models | Type safety, validation, serialization |
| Error handling | Correlation IDs + sanitized responses | Traceability without exposing internals |
| Agent discovery | Registry pattern | Loose coupling, testability |
| Workflow state | Request-scoped context | Stateless agents, no cross-request persistence |
| AI integration | Circuit breaker pattern | Graceful degradation, fault isolation |

## Agent Interaction Matrix

| Caller → Target | AuthAgent | TaskAgent | UserAgent | AIAgent | PlannerAgent | TaskExecutorAgent |
|-----------------|-----------|-----------|-----------|---------|--------------|-------------------|
| Orchestrator | validate, authenticate | all CRUD | profile, delete | suggestions | plan | — |
| AuthAgent | — | — | get, create | — | — | — |
| TaskAgent | — | — | — | suggestions | — | — |
| UserAgent | — | delete tasks | — | — | — | — |
| AIAgent | — | — | — | — | — | — |
| PlannerAgent | — | — | — | suggestions | — | execute |
| TaskExecutorAgent | auth ops | CRUD | user ops | — | — | — |

## Protocol Summary

### AgentRequest
```yaml
agent_request:
  id: UUID
  timestamp: ISO8601
  source_agent: string
  target_agent: string
  operation: string
  payload: object
  context:
    user_id: UUID | null
    request_id: UUID
    correlation_id: UUID
```

### AgentResponse
```yaml
agent_response:
  id: UUID
  request_id: UUID
  timestamp: ISO8601
  status: success | error
  payload: object
  error:
    code: string
    message: string
    details: object | null
```

## Next Steps

Run `/sp.tasks` to generate implementation tasks following TDD methodology.
