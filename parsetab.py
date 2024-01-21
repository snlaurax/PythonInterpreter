
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftGREATER_EQGREATERLESS_EQLESSEQNOT_EQleftPLUSMINUSleftMULTIPLYDIVIDErightUMINUSNOTAND ASSIGN AT COMMA DIVIDE DOT ELSE EQ FALSE FUNC GREATER GREATER_EQ IF LAMBDA LBRACE LESS LESS_EQ LPAREN MINUS MULTIPLY NAME NIL NOT NOT_EQ NUMBER OR PLUS RBRACE REF RETURN RPAREN SEMI STRING TRUE WHILEprogram : funcsfuncs : funcs func\n    | funcfunc : FUNC NAME LPAREN formal_args RPAREN LBRACE statements RBRACE\n    | FUNC NAME LPAREN RPAREN LBRACE statements RBRACElambda : LAMBDA LPAREN formal_args RPAREN LBRACE statements RBRACE\n    | LAMBDA LPAREN RPAREN LBRACE statements RBRACEformal_args : formal_args COMMA formal_arg\n    | formal_argformal_arg : NAMEformal_arg : REF NAMEstatements : statements statement\n    | statementstatement : variable ASSIGN expression SEMIvariable : NAME DOT NAME\n    | NAMEstatement : IF LPAREN expression RPAREN LBRACE statements RBRACE\n    | IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE\n    statement : WHILE LPAREN expression RPAREN LBRACE statements RBRACEstatement : expression SEMIstatement : RETURN expression SEMI\n    | RETURN SEMIexpression : NOT expressionexpression : MINUS expression %prec UMINUSexpression : expression EQ expression\n    | expression GREATER expression\n    | expression LESS expression\n    | expression NOT_EQ expression\n    | expression GREATER_EQ expression\n    | expression LESS_EQ expression\n    | expression PLUS expression\n    | expression MINUS expression\n    | expression MULTIPLY expression\n    | expression DIVIDE expressionexpression : LPAREN expression RPARENexpression : expression OR expression\n    | expression AND expressionexpression : NUMBERexpression : lambdaexpression : TRUE\n    | FALSEexpression : NILexpression : ATexpression : STRINGexpression : variableexpression : NAME LPAREN args RPAREN\n    | NAME LPAREN RPARENexpression : NAME DOT NAME LPAREN args RPAREN\n    | NAME DOT NAME LPAREN RPARENargs : args COMMA expression\n    | expression'
    
_lr_action_items = {'FUNC':([0,2,3,5,44,67,],[4,4,-3,-2,-5,-4,]),'$end':([1,2,3,5,44,67,],[0,-1,-3,-2,-5,-4,]),'NAME':([4,7,12,14,15,17,20,21,22,27,28,29,38,39,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,66,73,89,92,94,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[6,8,16,8,19,19,43,19,-13,43,43,43,19,68,43,-12,43,-20,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-22,8,95,-21,43,43,-14,19,19,19,19,19,19,19,19,-17,-19,19,19,-18,]),'LPAREN':([6,15,17,19,20,21,22,25,26,27,28,29,37,38,40,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,68,89,92,94,95,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[7,20,20,40,20,20,-13,60,61,20,20,20,66,20,20,40,-12,20,-20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-22,92,-21,20,20,92,-14,20,20,20,20,20,20,20,20,-17,-19,20,20,-18,]),'RPAREN':([7,8,9,11,16,18,30,31,32,33,34,35,36,40,41,42,43,64,65,66,69,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,92,93,95,101,102,103,108,112,115,],[10,-10,13,-9,-11,-8,-38,-39,-40,-41,-42,-43,-44,70,72,-45,-16,-23,-24,91,93,-47,-51,-35,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,97,98,99,102,-46,-15,108,-49,-50,-48,-7,-6,]),'REF':([7,14,66,],[12,12,12,]),'COMMA':([8,9,11,16,18,30,31,32,33,34,35,36,42,43,64,65,69,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,90,93,95,101,102,103,108,112,115,],[-10,14,-9,-11,-8,-38,-39,-40,-41,-42,-43,-44,-45,-16,-23,-24,94,-47,-51,-35,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,14,-46,-15,94,-49,-50,-48,-7,-6,]),'LBRACE':([10,13,91,97,98,99,116,],[15,17,100,104,105,106,117,]),'IF':([15,17,21,22,38,45,47,63,89,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[25,25,25,-13,25,-12,-20,-22,-21,-14,25,25,25,25,25,25,25,25,-17,-19,25,25,-18,]),'WHILE':([15,17,21,22,38,45,47,63,89,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[26,26,26,-13,26,-12,-20,-22,-21,-14,26,26,26,26,26,26,26,26,-17,-19,26,26,-18,]),'RETURN':([15,17,21,22,38,45,47,63,89,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[27,27,27,-13,27,-12,-20,-22,-21,-14,27,27,27,27,27,27,27,27,-17,-19,27,27,-18,]),'NOT':([15,17,20,21,22,27,28,29,38,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,89,92,94,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[28,28,28,28,-13,28,28,28,28,28,-12,28,-20,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-22,-21,28,28,-14,28,28,28,28,28,28,28,28,-17,-19,28,28,-18,]),'MINUS':([15,17,19,20,21,22,23,24,27,28,29,30,31,32,33,34,35,36,38,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,95,96,100,102,103,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,],[29,29,-16,29,29,-13,-45,55,29,29,29,-38,-39,-40,-41,-42,-43,-44,29,29,55,-45,-16,-12,29,-20,29,29,29,29,29,29,29,29,29,29,29,29,29,29,55,-22,-23,-24,-15,-47,55,-35,55,55,55,55,55,55,55,-31,-32,-33,-34,55,55,55,55,-21,29,-46,29,-15,-14,29,-49,55,29,29,29,29,-48,29,29,29,-7,-17,-19,-6,29,29,-18,]),'NUMBER':([15,17,20,21,22,27,28,29,38,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,89,92,94,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[30,30,30,30,-13,30,30,30,30,30,-12,30,-20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-22,-21,30,30,-14,30,30,30,30,30,30,30,30,-17,-19,30,30,-18,]),'TRUE':([15,17,20,21,22,27,28,29,38,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,89,92,94,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[32,32,32,32,-13,32,32,32,32,32,-12,32,-20,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-22,-21,32,32,-14,32,32,32,32,32,32,32,32,-17,-19,32,32,-18,]),'FALSE':([15,17,20,21,22,27,28,29,38,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,89,92,94,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[33,33,33,33,-13,33,33,33,33,33,-12,33,-20,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-22,-21,33,33,-14,33,33,33,33,33,33,33,33,-17,-19,33,33,-18,]),'NIL':([15,17,20,21,22,27,28,29,38,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,89,92,94,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[34,34,34,34,-13,34,34,34,34,34,-12,34,-20,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-22,-21,34,34,-14,34,34,34,34,34,34,34,34,-17,-19,34,34,-18,]),'AT':([15,17,20,21,22,27,28,29,38,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,89,92,94,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[35,35,35,35,-13,35,35,35,35,35,-12,35,-20,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-22,-21,35,35,-14,35,35,35,35,35,35,35,35,-17,-19,35,35,-18,]),'STRING':([15,17,20,21,22,27,28,29,38,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,89,92,94,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[36,36,36,36,-13,36,36,36,36,36,-12,36,-20,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-22,-21,36,36,-14,36,36,36,36,36,36,36,36,-17,-19,36,36,-18,]),'LAMBDA':([15,17,20,21,22,27,28,29,38,40,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,89,92,94,96,100,104,105,106,107,109,110,111,113,114,117,118,119,],[37,37,37,37,-13,37,37,37,37,37,-12,37,-20,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-22,-21,37,37,-14,37,37,37,37,37,37,37,37,-17,-19,37,37,-18,]),'DOT':([19,43,],[39,73,]),'ASSIGN':([19,23,68,],[-16,46,-15,]),'SEMI':([19,23,24,27,30,31,32,33,34,35,36,42,43,62,64,65,68,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,93,95,102,108,112,115,],[-16,-45,47,63,-38,-39,-40,-41,-42,-43,-44,-45,-16,89,-23,-24,-15,-47,-35,96,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-46,-15,-49,-48,-7,-6,]),'EQ':([19,23,24,30,31,32,33,34,35,36,41,42,43,62,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,102,103,108,112,115,],[-16,-45,48,-38,-39,-40,-41,-42,-43,-44,48,-45,-16,48,-23,-24,-15,-47,48,-35,48,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,48,48,48,48,-46,-15,-49,48,-48,-7,-6,]),'GREATER':([19,23,24,30,31,32,33,34,35,36,41,42,43,62,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,102,103,108,112,115,],[-16,-45,49,-38,-39,-40,-41,-42,-43,-44,49,-45,-16,49,-23,-24,-15,-47,49,-35,49,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,49,49,49,49,-46,-15,-49,49,-48,-7,-6,]),'LESS':([19,23,24,30,31,32,33,34,35,36,41,42,43,62,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,102,103,108,112,115,],[-16,-45,50,-38,-39,-40,-41,-42,-43,-44,50,-45,-16,50,-23,-24,-15,-47,50,-35,50,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,50,50,50,50,-46,-15,-49,50,-48,-7,-6,]),'NOT_EQ':([19,23,24,30,31,32,33,34,35,36,41,42,43,62,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,102,103,108,112,115,],[-16,-45,51,-38,-39,-40,-41,-42,-43,-44,51,-45,-16,51,-23,-24,-15,-47,51,-35,51,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,51,51,51,51,-46,-15,-49,51,-48,-7,-6,]),'GREATER_EQ':([19,23,24,30,31,32,33,34,35,36,41,42,43,62,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,102,103,108,112,115,],[-16,-45,52,-38,-39,-40,-41,-42,-43,-44,52,-45,-16,52,-23,-24,-15,-47,52,-35,52,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,52,52,52,52,-46,-15,-49,52,-48,-7,-6,]),'LESS_EQ':([19,23,24,30,31,32,33,34,35,36,41,42,43,62,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,102,103,108,112,115,],[-16,-45,53,-38,-39,-40,-41,-42,-43,-44,53,-45,-16,53,-23,-24,-15,-47,53,-35,53,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,53,53,53,53,-46,-15,-49,53,-48,-7,-6,]),'PLUS':([19,23,24,30,31,32,33,34,35,36,41,42,43,62,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,102,103,108,112,115,],[-16,-45,54,-38,-39,-40,-41,-42,-43,-44,54,-45,-16,54,-23,-24,-15,-47,54,-35,54,54,54,54,54,54,54,-31,-32,-33,-34,54,54,54,54,-46,-15,-49,54,-48,-7,-6,]),'MULTIPLY':([19,23,24,30,31,32,33,34,35,36,41,42,43,62,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,102,103,108,112,115,],[-16,-45,56,-38,-39,-40,-41,-42,-43,-44,56,-45,-16,56,-23,-24,-15,-47,56,-35,56,56,56,56,56,56,56,56,56,-33,-34,56,56,56,56,-46,-15,-49,56,-48,-7,-6,]),'DIVIDE':([19,23,24,30,31,32,33,34,35,36,41,42,43,62,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,102,103,108,112,115,],[-16,-45,57,-38,-39,-40,-41,-42,-43,-44,57,-45,-16,57,-23,-24,-15,-47,57,-35,57,57,57,57,57,57,57,57,57,-33,-34,57,57,57,57,-46,-15,-49,57,-48,-7,-6,]),'OR':([19,23,24,30,31,32,33,34,35,36,41,42,43,62,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,102,103,108,112,115,],[-16,-45,58,-38,-39,-40,-41,-42,-43,-44,58,-45,-16,58,-23,-24,-15,-47,58,-35,58,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,58,58,-46,-15,-49,58,-48,-7,-6,]),'AND':([19,23,24,30,31,32,33,34,35,36,41,42,43,62,64,65,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,95,102,103,108,112,115,],[-16,-45,59,-38,-39,-40,-41,-42,-43,-44,59,-45,-16,59,-23,-24,-15,-47,59,-35,59,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,59,-37,59,59,-46,-15,-49,59,-48,-7,-6,]),'RBRACE':([21,22,38,45,47,63,89,96,107,109,110,111,113,114,118,119,],[44,-13,67,-12,-20,-22,-21,-14,112,113,114,115,-17,-19,119,-18,]),'ELSE':([113,],[116,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'funcs':([0,],[2,]),'func':([0,2,],[3,5,]),'formal_args':([7,66,],[9,90,]),'formal_arg':([7,14,66,],[11,18,11,]),'statements':([15,17,100,104,105,106,117,],[21,38,107,109,110,111,118,]),'statement':([15,17,21,38,100,104,105,106,107,109,110,111,117,118,],[22,22,45,45,22,22,22,22,45,45,45,45,22,45,]),'variable':([15,17,20,21,27,28,29,38,40,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,92,94,100,104,105,106,107,109,110,111,117,118,],[23,23,42,23,42,42,42,23,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,23,23,23,23,23,23,23,23,23,23,]),'expression':([15,17,20,21,27,28,29,38,40,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,92,94,100,104,105,106,107,109,110,111,117,118,],[24,24,41,24,62,64,65,24,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,71,103,24,24,24,24,24,24,24,24,24,24,]),'lambda':([15,17,20,21,27,28,29,38,40,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,92,94,100,104,105,106,107,109,110,111,117,118,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'args':([40,92,],[69,101,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> funcs','program',1,'p_program','brewparse.py',27),
  ('funcs -> funcs func','funcs',2,'p_funcs','brewparse.py',32),
  ('funcs -> func','funcs',1,'p_funcs','brewparse.py',33),
  ('func -> FUNC NAME LPAREN formal_args RPAREN LBRACE statements RBRACE','func',8,'p_func','brewparse.py',38),
  ('func -> FUNC NAME LPAREN RPAREN LBRACE statements RBRACE','func',7,'p_func','brewparse.py',39),
  ('lambda -> LAMBDA LPAREN formal_args RPAREN LBRACE statements RBRACE','lambda',7,'p_lambda','brewparse.py',47),
  ('lambda -> LAMBDA LPAREN RPAREN LBRACE statements RBRACE','lambda',6,'p_lambda','brewparse.py',48),
  ('formal_args -> formal_args COMMA formal_arg','formal_args',3,'p_formal_args','brewparse.py',56),
  ('formal_args -> formal_arg','formal_args',1,'p_formal_args','brewparse.py',57),
  ('formal_arg -> NAME','formal_arg',1,'p_formal_arg','brewparse.py',62),
  ('formal_arg -> REF NAME','formal_arg',2,'p_formal_ref_arg','brewparse.py',67),
  ('statements -> statements statement','statements',2,'p_statements','brewparse.py',72),
  ('statements -> statement','statements',1,'p_statements','brewparse.py',73),
  ('statement -> variable ASSIGN expression SEMI','statement',4,'p_statement___assign','brewparse.py',78),
  ('variable -> NAME DOT NAME','variable',3,'p_variable','brewparse.py',83),
  ('variable -> NAME','variable',1,'p_variable','brewparse.py',84),
  ('statement -> IF LPAREN expression RPAREN LBRACE statements RBRACE','statement',7,'p_statement_if','brewparse.py',92),
  ('statement -> IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE','statement',11,'p_statement_if','brewparse.py',93),
  ('statement -> WHILE LPAREN expression RPAREN LBRACE statements RBRACE','statement',7,'p_statement_while','brewparse.py',112),
  ('statement -> expression SEMI','statement',2,'p_statement_expr','brewparse.py',117),
  ('statement -> RETURN expression SEMI','statement',3,'p_statement_return','brewparse.py',122),
  ('statement -> RETURN SEMI','statement',2,'p_statement_return','brewparse.py',123),
  ('expression -> NOT expression','expression',2,'p_expression_not','brewparse.py',132),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','brewparse.py',137),
  ('expression -> expression EQ expression','expression',3,'p_arith_expression_binop','brewparse.py',142),
  ('expression -> expression GREATER expression','expression',3,'p_arith_expression_binop','brewparse.py',143),
  ('expression -> expression LESS expression','expression',3,'p_arith_expression_binop','brewparse.py',144),
  ('expression -> expression NOT_EQ expression','expression',3,'p_arith_expression_binop','brewparse.py',145),
  ('expression -> expression GREATER_EQ expression','expression',3,'p_arith_expression_binop','brewparse.py',146),
  ('expression -> expression LESS_EQ expression','expression',3,'p_arith_expression_binop','brewparse.py',147),
  ('expression -> expression PLUS expression','expression',3,'p_arith_expression_binop','brewparse.py',148),
  ('expression -> expression MINUS expression','expression',3,'p_arith_expression_binop','brewparse.py',149),
  ('expression -> expression MULTIPLY expression','expression',3,'p_arith_expression_binop','brewparse.py',150),
  ('expression -> expression DIVIDE expression','expression',3,'p_arith_expression_binop','brewparse.py',151),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','brewparse.py',156),
  ('expression -> expression OR expression','expression',3,'p_expression_and_or','brewparse.py',161),
  ('expression -> expression AND expression','expression',3,'p_expression_and_or','brewparse.py',162),
  ('expression -> NUMBER','expression',1,'p_expression_number','brewparse.py',167),
  ('expression -> lambda','expression',1,'p_expression_lambda','brewparse.py',172),
  ('expression -> TRUE','expression',1,'p_expression_bool','brewparse.py',177),
  ('expression -> FALSE','expression',1,'p_expression_bool','brewparse.py',178),
  ('expression -> NIL','expression',1,'p_expression_nil','brewparse.py',184),
  ('expression -> AT','expression',1,'p_expression_obj','brewparse.py',189),
  ('expression -> STRING','expression',1,'p_expression_string','brewparse.py',196),
  ('expression -> variable','expression',1,'p_expression_variable','brewparse.py',201),
  ('expression -> NAME LPAREN args RPAREN','expression',4,'p_func_call','brewparse.py',206),
  ('expression -> NAME LPAREN RPAREN','expression',3,'p_func_call','brewparse.py',207),
  ('expression -> NAME DOT NAME LPAREN args RPAREN','expression',6,'p_method_call','brewparse.py',215),
  ('expression -> NAME DOT NAME LPAREN RPAREN','expression',5,'p_method_call','brewparse.py',216),
  ('args -> args COMMA expression','args',3,'p_expression_args','brewparse.py',224),
  ('args -> expression','args',1,'p_expression_args','brewparse.py',225),
]