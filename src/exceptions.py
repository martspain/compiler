class UnbanlancedParenthesis(Exception):
  def __init__(self, expression, openingParenth, closingParenth, message="Expression's parenthesis are not balanced."):
    self.expression = expression
    self.message = message + f" Please check expression {expression} is written correctly. Opening parenthesis: {openingParenth}, closing parenthesis: {closingParenth}"
    super().__init__(self.message)
