import pyparsing
import functools
import operator

def day7(text, initialVariables=None):
    statements = []
    for gateDescription in text.split("\n"):
        statements.append(_parseGate(gateDescription))

    variables = {} if initialVariables is None else initialVariables
    while len(statements) > 0:
        statements = [stmt for stmt in statements if not _tryEvalStatement(stmt, variables)]

    return variables

def day7_part2(text):
    variables = day7(text)
    return day7(text, { 'b' : variables['a'] })

def _tryEvalStatement(statement, variables):
    try:
        statement(variables)
        return True
    except KeyError:
        return False

def _defineGateGrammarAndEvaluator():
    # this is a helper that allows associating a parse action to a pyparsing object that evaluates the expression
    # the action should be a function t, d -> result, where t are the child tokens, and d is the dictionary of variables
    def action(pyparsingObject, actionFunction):
        return pyparsingObject.setParseAction(lambda s, l, t: functools.partial(actionFunction, t))

    def stmtAction(t, d):
        name = t[2]
        if name in d: print "WARNING: gate '%s' is already defined" % name
        else:         d[name] = t[0](d)
        return d

    binOpMap = {
        'AND'    : operator.__and__,
        'OR'     : operator.__or__,
        'RSHIFT' : operator.rshift,
        'LSHIFT' : operator.lshift,
    }
    binOp   = pyparsing.oneOf(" ".join(binOpMap.keys()))

    number  = action(pyparsing.Word(pyparsing.nums),    lambda t, d: int(t[0]))
    varExpr = action(pyparsing.Word(pyparsing.alphas),  lambda t, d: d[t[0]])
    value   = (number | varExpr)

    binExpr = action(value + binOp + value,             lambda t, d: binOpMap[ t[1] ]( t[0](d), t[2](d) ) & 0xffff)
    notExpr = action(pyparsing.Literal("NOT") + value,  lambda t, d: t[1](d) ^ 0xffff)
    expr    = binExpr | notExpr | value

    stmt    = action(expr + pyparsing.Literal("->") + pyparsing.Word(pyparsing.alphas), stmtAction)
    return stmt

_stmt = _defineGateGrammarAndEvaluator()

def _parseGate(gateDescription):
    return _stmt.parseString(gateDescription)[0]

file = open("inputs/day7.txt").read()
variables = day7(file)

print variables["a"]

variables = day7_part2(file)

print variables["a"]