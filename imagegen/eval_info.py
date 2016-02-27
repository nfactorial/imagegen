class EvalParameter:
    def __init__(self, param):
        self.default_value = param.default_value


class EvalInfo:
    def __init__(self, params):
        self.rotation = 0.0
        self.x = 0.0
        self.y = 0.0
        self.params = {name: EvalParameter(p) for name, p in params}

    def evaluate(self, name, x, y):
        p = self.params[name]
        if p.node is not None:
            # TODO: Create a new EvalInfo for this parameter
            return p.node.evaluate(x, y)
        return p.default_value
