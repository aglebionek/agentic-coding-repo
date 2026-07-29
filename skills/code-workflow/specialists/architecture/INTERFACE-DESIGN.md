# Architecture Interface Design

Use this reference only from the architecture planner after selecting a valid
`ARCH-*` finding or inseparable cluster. The report must not perform interface
design.

## Frame the design problem

Establish before proposing structures:

- the responsibility and approved ownership authority;
- current callers and the knowledge each caller must coordinate;
- public contracts, effects, errors, ordering, data and compatibility surfaces;
- dependency categories and justified seams;
- required public reading entrypoint and documentation impact;
- behavior and existing test evidence that must remain valid.

Stop rather than invent an absent responsibility boundary, public contract,
migration intent, or decision authority.

## Design at least twice

Produce at least two materially different module/interface structures. Changing
only names, file layout, or parameter spelling does not count. Useful contrasts
include:

- a minimal facade that owns common orchestration versus a richer interface
  supporting distinct caller workflows;
- one responsibility with private child modules versus collaborating public
  modules with explicit seams;
- an inline dependency hidden by the module versus a port with justified
  adapters.

For each design, specify:

1. primary public interface, including invariants, effects, ordering, and error
   behavior;
2. hidden implementation knowledge and nested internal APIs;
3. seam placement and dependency strategy;
4. representative caller usage;
5. compatibility and migration approach;
6. test surface under the shared testing authority;
7. documentation and public-reading impact;
8. tradeoffs in depth, locality, leverage, responsibility ownership,
   navigability, testing, and migration cost.

Compare the designs, recommend one, and resolve every material choice
interactively with the user. The final plan records one selected structure, not
a menu. Parallel agents are optional and may be used only when the user
explicitly requests delegation.
