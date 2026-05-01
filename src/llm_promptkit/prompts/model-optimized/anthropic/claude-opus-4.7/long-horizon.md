# Claude Opus 4.7: Long-Horizon Tasks

## Autonomous Feature Development
```
You are implementing a feature end-to-end. You have full autonomy.

Feature: [detailed description]
Repository: [paste structure or working tree]
Test command: [how to run tests]
Lint command: [how to run linter]

Execution protocol:
1. Read all relevant source files
2. Design the implementation approach
3. Implement in logical steps
4. After each step:
   a. Run tests
   b. If tests fail, fix and re-run
   c. Run linter, fix any issues
5. Verify the feature works end-to-end
6. Add/update documentation if applicable
7. Report: what was done, what was tested, any caveats

Do not stop to ask questions. Make reasonable choices and document them.
If you get stuck for more than 3 attempts on one issue, report the blocker.
```

## Multi-Step Migration
```
Migrate [system/component] from [current state] to [target state].

Current: [describe current technology, version, patterns]
Target: [describe target technology, version, patterns]

Migration plan:
1. List all changes needed
2. Order by dependency (what must change first?)
3. For each change:
   - What to change
   - Expected test outcome
   - Rollback plan if it fails
4. Execute each step, verify, proceed

Constraints:
- Zero downtime required
- Backward compatibility during migration
- Tests must pass after each step
- Data integrity must be preserved

Execute the migration step by step.
```

## Documentation Generation
```
Generate comprehensive documentation for: [codebase/API/system]

Source materials: [paste code, specs, or describe what to document]

Generate:
1. **README.md** — Quick start, installation, basic usage
2. **API Reference** — All endpoints/methods with types and examples
3. **Architecture Guide** — System overview, design decisions, data flow
4. **Contributing Guide** — Setup, coding standards, PR process
5. **Changelog** — Recent changes with migration notes

Style:
- Concise but complete
- Code examples for every public interface
- Include common gotchas and troubleshooting
- Architecture diagrams as mermaid/ASCII where helpful
```

## Extended Testing Campaign
```
Write a comprehensive test suite for: [module/feature]

Code under test: [paste or reference]
Existing tests: [describe coverage gaps]

Test categories:
1. Unit tests: every public function, edge cases, error paths
2. Integration tests: component interactions, data flow
3. Property-based tests: invariants that should always hold
4. Performance tests: latency bounds for critical paths
5. Security tests: injection, auth bypass, input validation

For each test:
- Descriptive name (should_x_when_y)
- Arrange-Act-Assert structure
- No dependencies on test order
- Deterministic (no random failures)

Run the full suite after writing. Fix any failures.
```

---
**Claude Opus 4.7 Long-Horizon Tips:**
- Designed for tasks that run for extended periods without supervision
- Self-verifies at checkpoints — it will test before reporting
- Takes instructions literally — provide complete specifications
- Excellent at maintaining consistency across large changesets
- Handles complex multi-step migrations with automatic rollback awareness
- Use for: feature development, migrations, documentation, test campaigns
- Price: $5/M input, $25/M output (same as Opus 4.6)