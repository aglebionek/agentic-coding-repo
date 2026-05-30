Test Driven Development (TDD) - great for AI.

## Allowing the AI to validate itself
Tests are the greatest tool to verify AI's work - a change they've made to a [[Modularity#^cbad56|module]]
might've broken something else in this module, or even a different module.

Creating tests for an existing codebase is a simple enough tasks for an AI.

Any fixed error should have a new test created to not allow it in the future - can be done automatically by an AI after it solved an issue. Can also be done for any new feature it created.

Interconnected and well documented tests and [[Documentation and structure|docs]] help to overcome [[AI Knowledge#^4fefd6|the newcommer problem]] and keep the [[Context Window|context window]] small.

## Red/Green approach - implementation technique 
### Initial step
Create a plan for what the AI is supposed to implement.

### Red
Instead of starting with the code implementation, you start with code test - they should cover everything the plan intends for the code to do, as well as any edge cases.

### Green
Only after the tests are written, the AI creates the code implementation that essentially aims at passing the tests.

## Human oversight
The created tests might be incorrect - be mindful of that. 
The AI might want to modify or altogether remove a correct test - any test modification should be approved by a human, especially if the tests are pre-existing and not created during.
