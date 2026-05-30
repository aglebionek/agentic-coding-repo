## What is a module ^cbad56
A **module** is any unit of code (function, class, file, helper) that can be expressed as a clear public API: defined input → defined output. The internal implementation doesn't matter; only the contract does. This makes [[Testing|tests]] trivial to write and the code easy to [[Documentation and structure]]document and hand off.

The output type should always be **data** (plain objects / typed configs), never UI components or side effects. This keeps the pure function free of framework dependencies and makes it directly unit-testable.