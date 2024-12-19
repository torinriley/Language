# Pulse API Documentation

## Overview
Pulse supports basic constructs such as variable assignment, loops, conditional execution, type casting, and printing.

## Class: PulseInterpreter

### Methods

#### `tokenize(code: str) -> List[str]`
Tokenizes the input code into a list of tokens.

- **Parameters:**
  - `code` (str): The input code as a string.
- **Returns:**
  - List of tokens (List[str]).

#### `parse(tokens: List[str]) -> List[Dict[str, Any]]`
Parses a list of tokens into an Abstract Syntax Tree (AST).

- **Parameters:**
  - `tokens` (List[str]): The list of tokens.
- **Returns:**
  - AST (List[Dict[str, Any]]).

#### `parse_block(tokens: List[str]) -> List[Dict[str, Any]]`
Parses a block of code until the 'end' token is found.

- **Parameters:**
  - `tokens` (List[str]): The list of tokens.
- **Returns:**
  - AST for the block (List[Dict[str, Any]]).

#### `parse_expression(tokens: List[str]) -> str`
Parses an expression, including operators and variables.

- **Parameters:**
  - `tokens` (List[str]): The list of tokens.
- **Returns:**
  - Parsed expression as a string (str).

#### `execute_ast(ast: List[Dict[str, Any]]) -> str`
Executes the AST and returns the output.

- **Parameters:**
  - `ast` (List[Dict[str, Any]]): The Abstract Syntax Tree.
- **Returns:**
  - Output of the execution (str).

#### `eval_expression(expr: str, variables: Dict[str, Any]) -> Any`
Evaluates an expression, substituting variables where applicable.

- **Parameters:**
  - `expr` (str): The expression to evaluate.
  - `variables` (Dict[str, Any]): The dictionary of variables.
- **Returns:**
  - Evaluated result (Any).

### Example Usage

```python
x = 0
for i in 1 3
    for j in 1 2
        print i
        print j
    end
end
until x > 5
    print "Looping until x > 5"
    x = x + 1
end
@int x
print x