# Implementation Plan: System Design Phase-2

**Branch**: `001-system-design-phase2` | **Date**: 2026-01-12 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-system-design-phase2/spec.md`

## Summary

Transform the Phase-1 in-memory console Todo application into a production-ready, multi-user, persistent full-stack web application. This involves implementing user authentication with Better Auth, CRUD operations for tasks, PostgreSQL persistence via Neon, AI-assisted task suggestions via Claude API, and complete multi-user isolation. The architecture follows a Next.js frontend with FastAPI backend pattern.

## Technical Context

**Language/Version**: Python 3.11+ (backend), TypeScript/Next.js 14+ (frontend)
**Primary Dependencies**: FastAPI, SQLModel, Better Auth, Next.js, React, TailwindCSS
**Storage**: PostgreSQL (Neon Serverless) via SQLModel ORM
**Testing**: pytest (backend), Jest/Vitest (frontend)
**Target Platform**: Web application (Linux server + modern browsers)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: Page load <3s, API responses <2s, 100 concurrent users
**Constraints**: JWT-based auth, multi-user isolation mandatory, AI features optional (graceful degradation)
**Scale/Scope**: 5 user stories, 12 functional requirements, full CRUD + auth + AI

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Spec-First Development | ✅ PASS | spec.md created with full requirements before plan |
| II. Layered Architecture | ✅ PASS | Frontend (Next.js) → API (FastAPI) → Database (PostgreSQL) |
| III. Test-First Development | ✅ PASS | TDD enforced via tasks.md structure |
| IV. Secure by Design | ✅ PASS | Password hashing, JWT tokens, multi-user isolation, rate limiting |
| V. API-First Integration | ✅ PASS | REST API design, OpenAPI specification |
| VI. Minimal Viable Diff | ✅ PASS | Focused on core CRUD + auth, AI as enhancement |

**Gate Status**: ✅ ALL GATES PASS — Proceed to implementation

## Project Structure

### Documentation (this feature)

```text
specs/001-system-design-phase2/
├── plan.md              # This file
├── spec.md              # Feature specification
├── checklists/          # Requirements checklists
└── tasks.md             # Implementation tasks
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   │   ├── user.py              # User SQLModel
│   │   └── task.py              # Task SQLModel
│   ├── services/
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── hashing.py       # Password hashing
│   │   │   └── tokens.py        # JWT token management
│   │   ├── task/
│   │   │   ├── __init__.py
│   │   │   └── crud.py          # Task CRUD operations
│   │   └── ai/
│   │       ├── __init__.py
│   │       └── suggestions.py   # AI task suggestions
│   ├── api/
│   │   ├── auth.py              # Auth endpoints
│   │   ├── tasks.py             # Task endpoints
│   │   └── users.py             # User endpoints
│   └── db/
│       ├── __init__.py
│       ├── engine.py            # Database connection
│       └── migrations/          # Alembic migrations
└── tests/
    ├── contract/
    ├── integration/
    └── unit/

frontend/
├── src/
│   ├── app/
│   │   ├── page.tsx             # Landing/login page
│   │   ├── dashboard/
│   │   │   └── page.tsx         # Main task dashboard
│   │   ├── auth/
│   │   │   ├── login/page.tsx
│   │   │   └── register/page.tsx
│   │   └── layout.tsx
│   ├── components/
│   │   ├── auth/
│   │   │   ├── LoginForm.tsx
│   │   │   └── RegisterForm.tsx
│   │   ├── tasks/
│   │   │   ├── TaskList.tsx
│   │   │   ├── TaskItem.tsx
│   │   │   ├── TaskForm.tsx
│   │   │   └── TaskFilters.tsx
│   │   └── ui/
│   │       └── ...              # Shared UI components
│   ├── lib/
│   │   ├── api.ts               # API client
│   │   └── auth.ts              # Auth utilities
│   └── hooks/
│       ├── useAuth.ts
│       └── useTasks.ts
└── tests/
```

**Structure Decision**: Web application (Option 2). FastAPI backend handles all business logic, authentication, and database operations. Next.js frontend provides responsive UI with client-side state management. This separation enables independent scaling and deployment.

## Complexity Tracking

> No Constitution Check violations. No complexity justification needed.

## Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Auth library | Better Auth | Easy integration, JWT support, session management |
| Password hashing | bcrypt | Industry standard, built-in salting |
| Token storage | HTTP-only cookies | XSS protection, automatic handling |
| Database ORM | SQLModel | Pydantic integration, type safety |
| Frontend framework | Next.js 14 | App router, server components, performance |
| API design | REST | Simple, well-understood, sufficient for CRUD |
| AI integration | Optional/async | Graceful degradation, non-blocking |

## API Summary

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/register` | POST | User registration |
| `/api/auth/login` | POST | User authentication |
| `/api/auth/logout` | POST | Session invalidation |
| `/api/auth/me` | GET | Current user profile |
| `/api/tasks` | GET | List user's tasks |
| `/api/tasks` | POST | Create new task |
| `/api/tasks/{id}` | GET | Get task details |
| `/api/tasks/{id}` | PUT | Update task |
| `/api/tasks/{id}` | DELETE | Delete task |
| `/api/tasks/{id}/complete` | POST | Toggle completion |
| `/api/ai/suggestions` | POST | Get AI task suggestions |

## Security Measures

1. **Authentication**: JWT tokens with expiration, secure HTTP-only cookies
2. **Authorization**: User ownership validation on all task operations
3. **Password Security**: bcrypt hashing, never stored in plaintext
4. **Rate Limiting**: Failed login attempts throttled
5. **Data Isolation**: All queries scoped to authenticated user
6. **Input Validation**: Pydantic schemas for all inputs
7. **Error Handling**: No internal details exposed in responses

## Next Steps

Run `/sp.tasks` to generate implementation tasks following TDD methodology.
