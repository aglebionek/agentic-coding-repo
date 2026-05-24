# Progress Strategy: Finish NSFW Chrome Monitor (Strict MVP)

## Locked decisions from grill
1. Ship strict MVP scope (all planned areas).
2. Test bar: high (unit + integration + Android smoke).
3. Lock scope updated to PIN-only for v1 (override biometric+PIN).
4. On capture unreliability: degrade gracefully with detection-unavailable status.
5. Export: JSON full metadata, including window title.
6. Setup blockers: Accessibility + Notifications + PIN configured.
7. Battery behavior: configurable threshold + toggle.
8. Test stack: Jest + ts-jest + Android instrumentation smoke.
9. Docs cadence: update Obsidian after each major module merge.

## Build list (missing work)

1. **Refactor monitoring into a testable core module**
   - Extract pure decision functions from orchestrator (`shouldPause`, `shouldTrigger`, `buildEvent`, `nextAction`).
   - Inject clock/scheduler/storage/native ports (no hidden globals).
   - Add exhaustive unit tests for pure logic and edge cases.

2. **Wire orchestrator to app lifecycle**
   - Connect `startMonitoring()`/stop path to UI state.
   - Add explicit monitoring state machine (`idle`, `blocked_setup`, `running`, `paused_battery`, `degraded_capture`).
   - Add integration tests for state transitions.

3. **Implement real battery provider + settings**
   - Replace stub battery provider with native-backed adapter.
   - Add configurable battery threshold + enable/disable toggle.
   - Test pause/resume behavior across threshold/charging transitions.

4. **Complete capture pipeline with graceful degradation**
   - Keep Chrome gating, add best-effort domain extraction.
   - Surface capability status (`capture_supported`, `capture_unavailable`, reason code).
   - Ensure metadata-only mode still logs correctly without false “detection” claims.
   - Add adapter tests for null/partial payloads.

5. **Finish detection execution path**
   - Define behavior when image missing/unavailable (explicit non-detection outcome).
   - Keep `DetectionEngine` swappable; enforce stable normalized output contract.
   - Add contract tests for engine adapter and label normalization.

6. **Implement secure app lock (PIN-only v1)**
   - Add PIN setup, verify, lock screen, failed-attempt handling, relock-after-5-min inactivity.
   - Gate sensitive screens/actions (logs detail + export) behind unlocked state.
   - Add unit/integration tests for lock state and relock timing.

7. **Upgrade storage to secure persistence**
   - Move settings/log-sensitive fields from plain AsyncStorage to encrypted storage adapter.
   - Keep storage behind interface for testability.
   - Add storage adapter tests and migration behavior tests.

8. **Complete logs domain + export use cases**
   - Keep 24h retention pruning.
   - Add list/detail query APIs and JSON export flow (including window title).
   - Enforce unlock requirement before export.
   - Add tests for retention cutoff and export authorization.

9. **Build strict setup checklist gating**
   - Checklist module with required checks: accessibility, notifications, PIN configured.
   - Block monitoring toggle until all required checks pass.
   - Add integration tests for blocked/unblocked transitions.

10. **Build control panel UI**
    - ON/OFF monitoring toggle, threshold/cadence controls, battery controls, service/capture status, logs browser.
    - Show degraded mode clearly when detection unavailable.
    - Add component tests for critical interactions.

11. **Native service hardening**
    - Validate foreground service behavior and privacy-safe alerts under real lifecycle conditions.
    - Ensure proper permission/error surfacing to JS.
    - Add Android instrumentation smoke tests for service start/stop + alert publish.

12. **Feasibility validation suite**
    - Add repeatable validation script/protocol for latency/noise/battery checks.
    - Capture run artifacts/log summaries for go/no-go decisions.
    - Document measured outcomes in vault notes.

13. **grow-docs updates after each major module**
    - Add/refresh Obsidian notes for: monitoring state model, lock model, storage architecture, native bridges, test strategy, known constraints.
    - Maintain cross-links and decisions log as implementation evolves.
