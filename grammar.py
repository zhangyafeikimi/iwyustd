#! /usr/bin/env python3
#


from enum import IntEnum
from typing import List
from lexer import *
from text import *


###################################################################
__all__ = [
    "SymbolType",
    "Symbol",
    "Grammar",
]


###################################################################
class SymbolType(IntEnum):
    INVALID = 0
    NON_STD = 1
    STD = 2


###################################################################
class Symbol(object):
    _type: SymbolType
    _begin: int  # begin offset
    _end: int  # end offset
    _raw_content: bytes  # raw content
    _content: bytes  # canonicalized content

    @property
    def type(self) -> SymbolType:
        return self._type

    @property
    def begin(self) -> int:
        return self._begin

    @property
    def end(self) -> int:
        return self._end

    @property
    def raw_content(self) -> bytes:
        return self._raw_content

    @property
    def content(self) -> bytes:
        return self._content

    def __init__(self, tokens: List[Token]):
        self._type = SymbolType.INVALID

        # some reasonable filter
        if len(tokens) == 1:
            t0 = tokens[0]
            content = t0.content
            if len(content) > 2 and not content.endswith(b"_"):
                self._type = SymbolType.NON_STD
                self._begin = t0.begin
                self._end = t0.end
                self._raw_content = t0.raw_content
                self._content = t0.content
        else:
            t0 = tokens[0]
            t1 = tokens[1]
            if t0.type == TokenType.IDENTIFIER and t0.content == b"std" and t1.type == TokenType.DOUBLE_COLON:
                self._type = SymbolType.STD
                self._begin = t0.begin
                self._end = tokens[-1].end
                self._raw_content = b"".join([_.raw_content for _ in tokens])
                self._content = b"".join([_.content for _ in tokens])

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{}[{},{}] {}".format(self.type.name, self.begin, self.end, self.content)


###################################################################
class Grammar(object):
    _tokens: List[Token]
    _symbols: List[str]
    _token_stack: List[Token]
    _offset: int  # current offset
    _token: Token  # current token

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    @property
    def symbols(self) -> List[Symbol]:
        return self._symbols

    ###################################################################
    def __init__(self, tokens: List[Token]):
        self._tokens = tokens
        self._symbols = []
        self._token_stack = []
        self._offset = 0
        self._token = None

    ###################################################################
    def _get_token(self) -> None:
        self._token = self._tokens[self._offset]
        self._offset += 1

    def _unget_token(self) -> None:
        self._offset -= 1
        self._token = self._tokens[self._offset]

    ###################################################################
    def parse(self) -> None:
        self._symbols.clear()
        self._token_stack.clear()
        self._offset = 0
        self._token = None
        while self._offset < len(self._tokens):
            self._on_token()

    ###################################################################
    def _on_token(self) -> None:
        self._get_token()
        if len(self._token_stack) == 0:
            if self._token.type == TokenType.IDENTIFIER:
                self._token_stack.append(self._token)
        else:
            last_token_type = self._token_stack[-1].type
            if last_token_type == TokenType.IDENTIFIER:
                if self._token.type in [
                    TokenType.POINTER,
                    TokenType.POINTER_STAR,
                    TokenType.DOT,
                    TokenType.DOT_STAR,
                    TokenType.DOUBLE_COLON,
                ]:
                    self._token_stack.append(self._token)
                else:
                    self._on_symbol()
                    self._token_stack.clear()
                    self._unget_token()
            else:
                if self._token.type == TokenType.IDENTIFIER:
                    self._token_stack.append(self._token)
                else:
                    self._token_stack.clear()

    def _on_symbol(self) -> None:
        symbol = Symbol(self._token_stack)
        if symbol.type != SymbolType.INVALID:
            self._symbols.append(symbol)


###################################################################
if __name__ == "__main__":
    import sys

    for file in sys.argv[1:]:
        lexer = Lexer(open(file, "rb").read())
        print('Parsing "{}"...'.format(file))
        if not lexer.parse():
            print('Failed to parse "{}".'.format(file))
            if len(lexer.tokens) > 0:
                hl = Highlighter(lexer.content)
                last_token = lexer.tokens[-1]
                print(hl.highlight(last_token.begin, last_token.end), end="")
            sys.exit(1)

        grammar = Grammar(lexer.tokens)
        grammar.parse()
        for symbol in grammar.symbols:
            print(symbol)
