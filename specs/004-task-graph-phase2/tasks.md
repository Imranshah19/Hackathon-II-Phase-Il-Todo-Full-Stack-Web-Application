# Tasks: Task Graph Phase-2

**Input**: Design documents from `/specs/004-task-graph-phase2/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/

**Tests**: REQUIRED per Constitution (Principle III: Test-First Development)

**Organization**: Tasks grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1-US5)
- Include exact file paths in descriptions

## Path Conventions

- **Backend**: `backend/src/`, `backend/tests/`
- **Frontend**: `frontend/src/`, `frontend/tests/`
- **Graph Services**: `backend/src/services/graph/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create graph services package in backend/src/services/graph/
- [ ] T002 [P] Create graph components directory in frontend/src/components/graph/
- [ ] T003 [P] Install React Flow dependency in frontend/package.json
- [ ] T004 [P] Configure graph-specific test directories in backend/tests/ and frontend/tests/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Create TaskDependency model in backend/src/models/task_dependency.py
- [ ] T006 Create Alembic migration for task_dependencies table
- [ ] T007 Add unique constraint (source_task_id, target_task_id) to migration
- [ ] T008 Add foreign key constraints to tasks table in migration
- [ ] T009 [P] Create DependencyCreate schema in backend/src/services/graph/schemas.py
- [ ] T010 [P] Create DependencyResponse schema in backend/src/services/graph/schemas.py
- [ ] T011 [P] Create GraphNode schema in backend/src/services/graph/schemas.py
- [ ] T012 [P] Create GraphEdge schema in backend/src/services/graph/schemas.py
- [ ] T013 Create graph services __init__.py in backend/src/services/graph/__init__.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Define Task Dependencies (Priority: P1)

**Goal**: Users can specify that certain tasks must be completed before others

**Independent Test**: Create two tasks, link them, verify dependency stored and displayed

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T014 [P] [US1] Contract test for POST /tasks/{id}/dependencies in backend/tests/contract/graph/test_create_dependency.py
- [ ] T015 [P] [US1] Contract test for GET /tasks/{id}/dependencies in backend/tests/contract/graph/test_list_dependencies.py
- [ ] T016 [P] [US1] Contract test for DELETE /tasks/{id}/dependencies/{dep_id} in backend/tests/contract/graph/test_delete_dependency.py
- [ ] T017 [P] [US1] Unit test for cycle detection algorithm in backend/tests/unit/graph/test_cycle_detection.py
- [ ] T018 [US1] Integration test for dependency CRUD in backend/tests/integration/graph/test_dependency_crud.py

### Implementation for User Story 1

- [ ] T019 Create dependency CRUD service in backend/src/services/graph/dependency.py
- [ ] T020 [US1] Implement create_dependency() with validation in backend/src/services/graph/dependency.py
- [ ] T021 [US1] Implement get_dependencies() method in backend/src/services/graph/dependency.py
- [ ] T022 [US1] Implement delete_dependency() method in backend/src/services/graph/dependency.py
- [ ] T023 [US1] Create cycle detection module in backend/src/services/graph/cycle_detection.py
- [ ] T024 [US1] Implement DFS-based cycle detection in backend/src/services/graph/cycle_detection.py
- [ ] T025 [US1] Integrate cycle check into create_dependency() in backend/src/services/graph/dependency.py
- [ ] T026 [US1] Implement POST /tasks/{id}/dependencies endpoint in backend/src/api/graph.py
- [ ] T027 [US1] Implement GET /tasks/{id}/dependencies endpoint in backend/src/api/graph.py
- [ ] T028 [US1] Implement DELETE /tasks/{id}/dependencies/{dep_id} endpoint in backend/src/api/graph.py
- [ ] T029 [US1] Add warning on task deletion with dependents in backend/src/api/tasks.py

**Checkpoint**: User Story 1 complete - dependencies can be created and managed

---

## Phase 4: User Story 2 - View Task Graph Visualization (Priority: P1)

**Goal**: Users can see tasks as a visual graph with nodes and edges

**Independent Test**: Create tasks with dependencies and verify graph renders correctly

### Tests for User Story 2

- [ ] T030 [P] [US2] Contract test for GET /tasks/graph in backend/tests/contract/graph/test_get_graph.py
- [ ] T031 [P] [US2] Component test for TaskGraph in frontend/tests/components/graph/TaskGraph.test.tsx
- [ ] T032 [P] [US2] Component test for TaskNode in frontend/tests/components/graph/TaskNode.test.tsx
- [ ] T033 [US2] Integration test for full graph rendering in frontend/tests/integration/graph/test_graph_view.tsx

### Implementation for User Story 2

- [ ] T034 [US2] Implement GET /tasks/graph endpoint in backend/src/api/graph.py
- [ ] T035 [US2] Create graph data transformer in backend/src/services/graph/transformer.py
- [ ] T036 [P] [US2] Create TaskGraph component wrapper in frontend/src/components/graph/TaskGraph.tsx
- [ ] T037 [P] [US2] Create TaskNode custom node component in frontend/src/components/graph/TaskNode.tsx
- [ ] T038 [P] [US2] Create GraphControls component in frontend/src/components/graph/GraphControls.tsx
- [ ] T039 [US2] Create graph API client in frontend/src/services/graph-api.ts
- [ ] T040 [US2] Create graph page in frontend/src/app/graph/page.tsx
- [ ] T041 [US2] Implement zoom and pan controls in frontend/src/components/graph/GraphControls.tsx
- [ ] T042 [US2] Add visual distinction for completed tasks in frontend/src/components/graph/TaskNode.tsx
- [ ] T043 [US2] Add hover tooltip with task details in frontend/src/components/graph/TaskNode.tsx
- [ ] T044 [US2] Add click handler to navigate to task edit in frontend/src/components/graph/TaskNode.tsx

**Checkpoint**: User Story 2 complete - interactive graph visualization

---

## Phase 5: User Story 3 - Get Recommended Task Order (Priority: P2)

**Goal**: System suggests optimal task completion order based on dependencies

**Independent Test**: Create tasks with dependencies, request order, verify sequence respects dependencies

### Tests for User Story 3

- [ ] T045 [P] [US3] Unit test for topological sort algorithm in backend/tests/unit/graph/test_topological.py
- [ ] T046 [P] [US3] Unit test for parallel task identification in backend/tests/unit/graph/test_topological.py
- [ ] T047 [P] [US3] Contract test for GET /tasks/graph/recommended-order in backend/tests/contract/graph/test_recommended_order.py
- [ ] T048 [US3] Integration test for recommended order in backend/tests/integration/graph/test_recommended_order.py

### Implementation for User Story 3

- [ ] T049 Create topological sort module in backend/src/services/graph/topological.py
- [ ] T050 [US3] Implement Kahn's algorithm for topological sort in backend/src/services/graph/topological.py
- [ ] T051 [US3] Implement parallel group identification in backend/src/services/graph/topological.py
- [ ] T052 [US3] Implement GET /tasks/graph/recommended-order endpoint in backend/src/api/graph.py
- [ ] T053 [US3] Create RecommendedOrder component in frontend/src/components/graph/RecommendedOrder.tsx
- [ ] T054 [US3] Add recommended order view to graph page in frontend/src/app/graph/page.tsx

**Checkpoint**: User Story 3 complete - recommended task order available

---

## Phase 6: User Story 4 - Filter and Focus Graph View (Priority: P2)

**Goal**: Users can filter graph to focus on specific subsets

**Independent Test**: Apply filters and verify only matching tasks appear

### Tests for User Story 4

- [ ] T055 [P] [US4] Component test for GraphFilters in frontend/tests/components/graph/GraphFilters.test.tsx
- [ ] T056 [US4] Integration test for filtered graph in frontend/tests/integration/graph/test_graph_filters.tsx

### Implementation for User Story 4

- [ ] T057 [US4] Create GraphFilters component in frontend/src/components/graph/GraphFilters.tsx
- [ ] T058 [US4] Implement status filter (all, incomplete, completed) in frontend/src/components/graph/GraphFilters.tsx
- [ ] T059 [US4] Implement focus mode (task + related) in frontend/src/components/graph/TaskGraph.tsx
- [ ] T060 [US4] Add filter state management to graph page in frontend/src/app/graph/page.tsx
- [ ] T061 [US4] Implement clear filters functionality in frontend/src/components/graph/GraphFilters.tsx

**Checkpoint**: User Story 4 complete - graph filtering available

---

## Phase 7: User Story 5 - Bulk Dependency Management (Priority: P3)

**Goal**: Power users can quickly define multiple dependencies at once

**Independent Test**: Select multiple tasks and create dependencies in one operation

### Tests for User Story 5

- [ ] T062 [P] [US5] Contract test for POST /tasks/dependencies/bulk in backend/tests/contract/graph/test_bulk_create.py
- [ ] T063 [US5] Integration test for bulk operations in backend/tests/integration/graph/test_bulk_operations.py

### Implementation for User Story 5

- [ ] T064 [US5] Implement bulk dependency creation in backend/src/services/graph/dependency.py
- [ ] T065 [US5] Implement POST /tasks/dependencies/bulk endpoint in backend/src/api/graph.py
- [ ] T066 [US5] Create BulkDependencyManager component in frontend/src/components/graph/BulkDependencyManager.tsx
- [ ] T067 [US5] Implement "set as sequence" feature in frontend/src/components/graph/BulkDependencyManager.tsx
- [ ] T068 [US5] Implement "set all dependent on X" feature in frontend/src/components/graph/BulkDependencyManager.tsx
- [ ] T069 [US5] Add multi-select mode to graph in frontend/src/components/graph/TaskGraph.tsx

**Checkpoint**: User Story 5 complete - bulk dependency management available

---

## Phase 8: Validation & Edge Cases

**Purpose**: Handle edge cases and data integrity

- [ ] T070 [P] Implement POST /tasks/graph/validate endpoint in backend/src/api/graph.py
- [ ] T071 [P] Add orphan dependency cleanup on task deletion in backend/src/services/graph/dependency.py
- [ ] T072 Implement completion warning when prerequisites incomplete in frontend/src/components/tasks/TaskItem.tsx
- [ ] T073 Add confirmation dialog for deleting tasks with dependents in frontend/src/components/tasks/TaskItem.tsx
- [ ] T074 Handle large graph pagination/clustering in frontend/src/components/graph/TaskGraph.tsx

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and improvements

- [ ] T075 [P] Add loading states to graph components in frontend/src/components/graph/
- [ ] T076 [P] Add error handling for graph API calls in frontend/src/services/graph-api.ts
- [ ] T077 [P] Add keyboard navigation support to graph in frontend/src/components/graph/TaskGraph.tsx
- [ ] T078 Performance optimization for graph rendering in frontend/src/components/graph/TaskGraph.tsx
- [ ] T079 Run quickstart.md validation scenarios
- [ ] T080 Security review: verify user-scoped graph access
- [ ] T081 Performance validation: graph render <2s for 100 tasks

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup - BLOCKS all user stories
- **User Stories (Phases 3-7)**: All depend on Foundational phase completion
  - US1 (Dependencies): No dependencies on other stories - REQUIRED FIRST
  - US2 (Visualization): Depends on US1 (needs dependencies to visualize)
  - US3 (Recommended Order): Depends on US1 (needs dependencies for sorting)
  - US4 (Filtering): Depends on US2 (needs visualization to filter)
  - US5 (Bulk): Depends on US1 (needs dependency creation)
- **Validation (Phase 8)**: Depends on US1-US5
- **Polish (Phase 9)**: Depends on all phases complete

### Recommended Execution Order

1. Phase 1 (Setup) - Parallel
2. Phase 2 (Foundational) - Parallel where marked
3. Phase 3 (US1 - Dependencies) - Required first
4. Phase 4 (US2 - Visualization) - Parallel with US3 and US5
5. Phase 5 (US3 - Recommended Order) - Parallel with US2
6. Phase 6 (US4 - Filtering) - After US2
7. Phase 7 (US5 - Bulk) - Parallel with US2, US3
8. Phase 8 (Validation)
9. Phase 9 (Polish)

### Parallel Opportunities

**Within Foundational (Phase 2):**
```
T009, T010, T011, T012 can run in parallel (after T005-T008)
```

**Across User Stories:**
```
US2 (Visualization) || US3 (Order) || US5 (Bulk) can run in parallel after US1 complete
```

**Frontend components are highly parallelizable within each story**

---

## Summary

| Metric | Value |
|--------|-------|
| Total Tasks | 81 |
| Setup Tasks | 4 |
| Foundational Tasks | 9 |
| US1 (Dependencies) Tasks | 16 |
| US2 (Visualization) Tasks | 15 |
| US3 (Recommended Order) Tasks | 10 |
| US4 (Filtering) Tasks | 7 |
| US5 (Bulk) Tasks | 8 |
| Validation Tasks | 5 |
| Polish Tasks | 7 |
| Parallel Opportunities | 40+ tasks |

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story
- Tests MUST be written and FAIL before implementation (TDD per Constitution)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- React Flow handles most graph rendering complexity - focus on data transformation
