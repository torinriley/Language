import re

class PulseInterpreter:
    @staticmethod
    def tokenize(code):
        return re.findall(r'\b\d+\b|@\w+|[a-zA-Z_][a-zA-Z0-9_]*|[=+-><:*()]|".*?"|\S', code)

    @staticmethod
    def parse(tokens):
        ast = []
        while tokens:
            token = tokens.pop(0)
            if token == "print":
                value = PulseInterpreter.parse_expression(tokens)
                ast.append({"type": "print", "value": value})
            elif token == "for":
                loop_var = tokens.pop(0)
                if tokens[0] == "in":
                    tokens.pop(0)
                    start = int(tokens.pop(0))
                    end = int(tokens.pop(0))
                else:
                    start = 0
                    end = 10
                block = PulseInterpreter.parse_block(tokens)
                ast.append({"type": "for", "loop_var": loop_var, "start": start, "end": end, "block": block})
            elif token == "until":
                condition = PulseInterpreter.parse_expression(tokens)
                block = PulseInterpreter.parse_block(tokens)
                ast.append({"type": "until", "condition": condition, "block": block})
            elif token.startswith("@"):
                cast_type = token[1:]
                variable = tokens.pop(0)
                ast.append({"type": "cast", "cast_type": cast_type, "variable": variable})
            elif tokens and tokens[0] == "=":
                variable = token
                tokens.pop(0)
                value = PulseInterpreter.parse_expression(tokens)
                ast.append({"type": "assign", "variable": variable, "value": value})
            else:
                raise ValueError(f"Unexpected token: {token}")
        return ast

    @staticmethod
    def parse_block(tokens):
        block_tokens = []
        while tokens and tokens[0] != "end":
            block_tokens.append(tokens.pop(0))
        if tokens:
            tokens.pop(0)
        return PulseInterpreter.parse(block_tokens)

    @staticmethod
    def parse_expression(tokens):
        expression = []
        while tokens and tokens[0] not in ("print", "end", "until", "for", "@", "="):
            expression.append(tokens.pop(0))
        return " ".join(expression)

    @staticmethod
    def execute_ast(ast):
        variables = {}
        output = []

        for node in ast:
            if node["type"] == "assign":
                var = node["variable"]
                value = PulseInterpreter.eval_expression(node["value"], variables)
                variables[var] = value
            elif node["type"] == "print":
                value = PulseInterpreter.eval_expression(node["value"], variables)
                output.append(str(value))
            elif node["type"] == "for":
                loop_var = node["loop_var"]
                start = node["start"]
                end = node["end"]
                for i in range(start, end + 1):
                    variables[loop_var] = i
                    output.append(PulseInterpreter.execute_ast(node["block"]))
            elif node["type"] == "until":
                condition = node["condition"]
                while not PulseInterpreter.eval_expression(condition, variables):
                    output.append(PulseInterpreter.execute_ast(node["block"]))
            elif node["type"] == "cast":
                cast_type = node["cast_type"]
                variable = node["variable"]
                if variable not in variables:
                    raise ValueError(f"Variable '{variable}' not defined.")
                value = variables[variable]
                try:
                    if cast_type == "int":
                        variables[variable] = int(value)
                    elif cast_type == "str":
                        variables[variable] = str(value)
                    elif cast_type == "bool":
                        variables[variable] = bool(value)
                    elif cast_type == "float":
                        variables[variable] = float(value)
                    else:
                        raise ValueError(f"Invalid cast type: {cast_type}")
                except ValueError:
                    raise ValueError(f"Cannot cast variable '{variable}' to {cast_type}.")
        return "\n".join(output)

    @staticmethod
    def eval_expression(expr, variables):
        for var in variables:
            expr = expr.replace(var, str(variables[var]))
        try:
            if expr.lower() in ("true", "false"):
                return expr.lower() == "true"
            if expr.startswith('"') and expr.endswith('"'):
                return expr.strip('"')
            return eval(expr)
        except Exception as e:
            raise ValueError(f"Invalid expression: {expr}. Error: {str(e)}")
