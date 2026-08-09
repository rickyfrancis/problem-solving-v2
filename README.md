# LeetCode Problem Solving

A small workspace for writing, running, and debugging LeetCode solutions in Python, JavaScript, and TypeScript.

## Setup

Install the TypeScript development tools after cloning:

```sh
npm install
```

Python and JavaScript solutions use the system `python3` and `node` commands and need no project dependencies.

## Organization

Keep every problem in its own numbered, kebab-case directory:

```text
problems/
  0001-two-sum/
    solution.py
    solution.js
    solution.ts
```

Only add the languages you actually use for a problem. Starter files live in `templates/`.

## Solve a problem

1. Create a directory for the problem:

   ```sh
   mkdir -p problems/0001-two-sum
   ```

2. Copy the template for your language:

   ```sh
   cp templates/solution.py problems/0001-two-sum/solution.py
   # or: cp templates/solution.js problems/0001-two-sum/solution.js
   # or: cp templates/solution.ts problems/0001-two-sum/solution.ts
   ```

3. Rename `solve`, implement the solution, and replace the example assertions with useful cases from the problem.

4. Run the file:

   ```sh
   ./run problems/0001-two-sum/solution.py
   ./run problems/0001-two-sum/solution.js
   ./run problems/0001-two-sum/solution.ts
   ```

   Extra command-line arguments are forwarded to the solution file when needed.

5. Type-check all TypeScript solutions:

   ```sh
   npm run typecheck
   ```

6. Debug locally with assertions, temporary logging, Python's `breakpoint()`, or your editor's debugger. Before submitting, rerun the solution and add edge cases for empty/minimum input, maximum input, duplicates, and other constraints that matter to the problem.

7. Submit only the LeetCode solution class or function, not the local assertions beneath it.

8. Commit the completed problem:

   ```sh
   git add problems/0001-two-sum
   git commit -m "Solve 0001 two sum"
   ```

## Useful commands

```sh
./run <path-to-solution>   # Run a Python, JavaScript, or TypeScript file
npm run typecheck          # Check every TypeScript solution without emitting files
git status                 # Review changes before committing
```

