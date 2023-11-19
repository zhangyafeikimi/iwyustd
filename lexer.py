#! /usr/bin/env python3
#


import re
from enum import IntEnum
from typing import Any, List, Optional, Set, Union
from text import *


###################################################################
__all__ = [
    "TokenType",
    "Token",
    "Lexer",
]


###################################################################
SPACE_CHARS = set([ord(" "), ord("\t")])
LF = ord("\n")
DIGIT_CHARS = set([ord(_) for _ in "0123456789"])
FLOAT_LITERL_EXPONENT_CHARS = set([ord(_) for _ in "eE"])
FLOAT_LITERL_EXPONENT_SIGN_CHARS = set([ord(_) for _ in "+-"])
FLOAT_LITERL_SUFFIX_CHARS = set([ord(_) for _ in "flFL"])
xX_CHARS = set([ord(_) for _ in "xX"])
bB_CHARS = set([ord(_) for _ in "bB"])
uU_CHARS = set([ord(_) for _ in "uU"])
l_CHAR = ord("l")
L_CHAR = ord("L")
HEX_INT_LITERAL_CHARS = set([ord(_) for _ in "0123456789abcdefABCDEF"])
BIN_INT_LITERAL_CHARS = set([ord(_) for _ in "01"])
OCT_INT_LITERAL_CHARS = set([ord(_) for _ in "01234567"])
SYMBOL_BEGIN_CHARS = set([ord(_) for _ in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"])
SYMBOL_CHARS = set([ord(_) for _ in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"])


###################################################################
PREPROCESS_INCLUDE_PATTERN = re.compile(rb"^[ \t]*#[ \t]*include[ \t]*(<.*?>|\".*?\")")
PREPROCESS_DEFINE_PATTERN = re.compile(rb"^[ \t]*#[ \t]*define[ \t]*")


def get_include(s: bytes) -> Optional[bytes]:
    match = PREPROCESS_INCLUDE_PATTERN.match(s)
    if match:
        return match.groups()[0][1:-1]
    else:
        return None


def is_define(s: bytes) -> bool:
    return PREPROCESS_DEFINE_PATTERN.match(s) is not None


###################################################################
class TokenType(IntEnum):
    INCREMENT = 1  # ++
    DECREMENT = 2  # --
    ADD = 3  # +
    ADD_ASSIGN = 4  # +=
    SUB = 5  # -
    SUB_ASSIGN = 6  # -=
    MUL = 7  # *
    MUL_ASSIGN = 8  # *=
    DIV = 9  # /
    DIV_ASSIGN = 10  # /=
    MOD = 11  # %
    MOD_ASSIGN = 12  # %=
    ASSIGN = 13  # =

    EQ = 20  # ==
    GT = 21  # >
    GE = 22  # >=
    LT = 23  # <
    LE = 24  # <=
    NE = 25  # !=

    LOGICAL_AND = 30  # &&
    LOGICAL_OR = 31  # ||
    LOGICAL_NOT = 32  # !

    BITWISE_AND = 40  # &
    BITWISE_AND_ASSIGN = 41  # &=
    BITWISE_OR = 42  # |
    BITWISE_OR_ASSIGN = 43  # |=
    BITWISE_XOR = 44  # ^
    BITWISE_XOR_ASSIGN = 45  # ^=
    BITWISE_NOT = 46  # ~
    SHIFT_RIGHT = 47  # >>
    SHIFT_RIGHT_ASSIGN = 48  # >>=
    SHIFT_LEFT = 49  # <<
    SHIFT_LEFT_ASSIGN = 50  # <<=

    COMMA = 60  # ,
    SEMICOLON = 61  # ;
    POINTER = 62  # ->
    POINTER_STAR = 63  # ->*
    DOT = 64  # .
    DOT_STAR = 65  # .*
    DOUBLE_COLON = 66  # ::
    QUESTION = 67  # ?
    COLON = 68  # :
    TRIPLE_DOT = 69  # ...

    LEFT_PAREN = 70  # (
    RIGHT_PAREN = 71  # )
    LEFT_BRACKET = 72  # [
    RIGHT_BRACKET = 73  # ]
    LEFT_BRACE = 74  # {
    RIGHT_BRACE = 75  # }

    BOOL_LITERAL = 80
    HEX_INT_LITERAL = 81
    BIN_INT_LITERAL = 82
    OCT_INT_LITERAL = 83
    DEC_INT_LITERAL = 84
    FLOAT_LITERAL = 85
    POINTER_LITERAL = 86
    CHAR_LITERAL = 87
    STRING_LITERAL = 88
    RAW_STRING_LITERAL = 89

    C_COMMENT = 100
    CC_COMMENT = 101
    PREPROCESS = 102
    PREPROCESS_INCLUDE = 103
    PREPROCESS_DEFINE = 104

    KEYWORD = 200
    IDENTIFIER = 201

    UNKNOWN = 10000


SYMBOL_2_TOKEN_TYPE = {
    b"and": TokenType.LOGICAL_AND,
    b"or": TokenType.LOGICAL_OR,
    b"not": TokenType.LOGICAL_NOT,
    b"false": TokenType.BOOL_LITERAL,
    b"true": TokenType.BOOL_LITERAL,
    b"nullptr": TokenType.POINTER_LITERAL,
    b"alignas": TokenType.KEYWORD,
    b"alignof": TokenType.KEYWORD,
    b"asm": TokenType.KEYWORD,
    b"auto": TokenType.KEYWORD,
    b"bool": TokenType.KEYWORD,
    b"break": TokenType.KEYWORD,
    b"case": TokenType.KEYWORD,
    b"catch": TokenType.KEYWORD,
    b"char": TokenType.KEYWORD,
    b"char16_t": TokenType.KEYWORD,
    b"char32_t": TokenType.KEYWORD,
    b"class": TokenType.KEYWORD,
    b"const": TokenType.KEYWORD,
    b"const_cast": TokenType.KEYWORD,
    b"constexpr": TokenType.KEYWORD,
    b"continue": TokenType.KEYWORD,
    b"decltype": TokenType.KEYWORD,
    b"default": TokenType.KEYWORD,
    b"delete": TokenType.KEYWORD,
    b"do": TokenType.KEYWORD,
    b"double": TokenType.KEYWORD,
    b"dynamic_cast": TokenType.KEYWORD,
    b"else": TokenType.KEYWORD,
    b"enum": TokenType.KEYWORD,
    b"explicit": TokenType.KEYWORD,
    b"export": TokenType.KEYWORD,
    b"extern": TokenType.KEYWORD,
    b"final": TokenType.KEYWORD,
    b"float": TokenType.KEYWORD,
    b"for": TokenType.KEYWORD,
    b"friend": TokenType.KEYWORD,
    b"goto": TokenType.KEYWORD,
    b"if": TokenType.KEYWORD,
    b"inline": TokenType.KEYWORD,
    b"int": TokenType.KEYWORD,
    b"long": TokenType.KEYWORD,
    b"mutable": TokenType.KEYWORD,
    b"namespace": TokenType.KEYWORD,
    b"new": TokenType.KEYWORD,
    b"noexcept": TokenType.KEYWORD,
    b"operator": TokenType.KEYWORD,
    b"override": TokenType.KEYWORD,
    b"private": TokenType.KEYWORD,
    b"protected": TokenType.KEYWORD,
    b"public": TokenType.KEYWORD,
    b"register": TokenType.KEYWORD,
    b"reinterpret_cast": TokenType.KEYWORD,
    b"return": TokenType.KEYWORD,
    b"short": TokenType.KEYWORD,
    b"signed": TokenType.KEYWORD,
    b"sizeof": TokenType.KEYWORD,
    b"static": TokenType.KEYWORD,
    b"static_assert": TokenType.KEYWORD,
    b"static_cast": TokenType.KEYWORD,
    b"struct": TokenType.KEYWORD,
    b"switch": TokenType.KEYWORD,
    b"template": TokenType.KEYWORD,
    b"this": TokenType.KEYWORD,
    b"thread_local": TokenType.KEYWORD,
    b"throw": TokenType.KEYWORD,
    b"try": TokenType.KEYWORD,
    b"typedef": TokenType.KEYWORD,
    b"typeid": TokenType.KEYWORD,
    b"typename": TokenType.KEYWORD,
    b"union": TokenType.KEYWORD,
    b"unsigned": TokenType.KEYWORD,
    b"using": TokenType.KEYWORD,
    b"virtual": TokenType.KEYWORD,
    b"void": TokenType.KEYWORD,
    b"volatile": TokenType.KEYWORD,
    b"wchar_t": TokenType.KEYWORD,
    b"while": TokenType.KEYWORD,
}


###################################################################
class Token(object):
    _type: TokenType
    _begin: int  # begin offset
    _end: int  # end offset
    _raw_content: bytes  # raw content
    _content: bytes  # canonicalized content
    _extra: Optional[Any]  # type specific data

    @property
    def type(self) -> TokenType:
        return self._type

    @type.setter
    def type(self, type: TokenType) -> None:
        assert self._type is None, self._type.name
        self._type = type

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

    @property
    def extra(self) -> Optional[Any]:
        return self._extra

    @extra.setter
    def extra(self, extra: Any) -> None:
        assert self._extra is None, self._extra
        self._extra = extra

    def __init__(self, type: Optional[TokenType], begin: int, end: int, content: bytes):
        self._type = type
        self._begin = begin
        self._end = end
        self._raw_content = content[begin:end]
        self._content = remove_line_continuation(self._raw_content)
        self._extra = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.type == TokenType.RAW_STRING_LITERAL:
            return "{}[{},{}] {}".format(self.type.name, self.begin, self.end, self.raw_content)
        elif self.extra is not None:
            return "{}[{},{}] {} {}".format(self.type.name, self.begin, self.end, self.content, self.extra)
        else:
            return "{}[{},{}] {}".format(self.type.name, self.begin, self.end, self.content)


###################################################################
class Lexer(object):
    _content: bytes
    _tokens: List[Token]
    _offset_stack: List[int]
    _c_stack: List[int]
    _offset: int  # current char offset
    _c: int  # current char
    _begin: int  # char offset of current token

    @property
    def content(self) -> bytes:
        return self._content

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    @property
    def offset(self) -> int:
        return self._offset

    @property
    def c(self) -> int:
        return self._c

    ###################################################################
    def __init__(self, content: bytes):
        self._content = canonicalize(content)
        self._tokens = []
        self._offset_stack = []
        self._c_stack = []
        self._offset = 0
        self._c = 0
        self._begin = 0

    ###################################################################
    def _getc(self) -> None:
        assert self._offset < len(self._content)
        self._offset_stack.append(self._offset)
        self._c_stack.append(self._c)

        c = self._content[self._offset]
        offset = self._offset + 1
        if c != ord("\\"):
            self._c = c
            self._offset = offset
            return

        # Try to skip line continuations.
        # "\\" [ \t]* "\n"
        while offset < len(self._content):
            c = self._content[offset]
            offset += 1
            if c == LF:
                self._c = self._content[offset]
                self._offset = offset + 1
                return
            elif c not in SPACE_CHARS:
                self._c = self._content[self._offset]
                self._offset += 1
                return

    def _ungetc(self) -> None:
        self._offset = self._offset_stack.pop()
        self._c = self._c_stack.pop()

    def _rewind_to_begin(self) -> None:
        while True:
            self._offset = self._offset_stack.pop()
            self._c = self._c_stack.pop()
            if self._begin == self._offset:
                break

    def _emit_token(self, tt: Union[TokenType, Token]) -> None:
        if isinstance(tt, TokenType):
            token = Token(tt, self._begin, self._offset, self._content)
        elif isinstance(tt, Token):
            token = tt
        else:
            assert False
        self._tokens.append(token)
        self._begin = self._offset

    def _skip_token(self) -> None:
        self._begin = self._offset

    def _pop_token(self) -> None:
        token = self._tokens.pop()
        self._begin = token.begin

    def _fatal(self) -> None:
        raise RuntimeError()

    ###################################################################
    def parse(self) -> bool:
        self._tokens.clear()
        self._offset_stack.clear()
        self._c_stack.clear()
        self._offset = 0
        self._c = 0
        self._begin = 0
        try:
            while self._offset < len(self._content):
                self._on_c()
            return True
        except RuntimeError:
            return False

    ###################################################################
    def _on_c(self) -> None:
        self._getc()
        if self._c in SPACE_CHARS or self._c == LF:
            self._skip_token()
        elif self._c == ord("+"):
            self._on_add()
        elif self._c == ord("-"):
            self._on_sub()
        elif self._c == ord("*"):
            self._on_mul()
        elif self._c == ord("/"):
            self._on_div()
        elif self._c == ord("%"):
            self._on_mod()
        elif self._c == ord("="):
            self._on_assign()
        elif self._c == ord(">"):
            self._on_gt()
        elif self._c == ord("<"):
            self._on_lt()
        elif self._c == ord("!"):
            self._on_logical_not()
        elif self._c == ord("&"):
            self._on_bitwise_and()
        elif self._c == ord("|"):
            self._on_bitwise_or()
        elif self._c == ord("^"):
            self._on_bitwise_xor()
        elif self._c == ord("~"):
            self._emit_token(TokenType.BITWISE_NOT)
        elif self._c == ord(","):
            self._emit_token(TokenType.COMMA)
        elif self._c == ord(";"):
            self._emit_token(TokenType.SEMICOLON)
        elif self._c == ord("."):
            self._on_dot()
        elif self._c == ord("?"):
            self._emit_token(TokenType.QUESTION)
        elif self._c == ord(":"):
            self._on_colon()
        elif self._c == ord("("):
            self._emit_token(TokenType.LEFT_PAREN)
        elif self._c == ord(")"):
            self._emit_token(TokenType.RIGHT_PAREN)
        elif self._c == ord("["):
            self._emit_token(TokenType.LEFT_BRACKET)
        elif self._c == ord("]"):
            self._emit_token(TokenType.RIGHT_BRACKET)
        elif self._c == ord("{"):
            self._emit_token(TokenType.LEFT_BRACE)
        elif self._c == ord("}"):
            self._emit_token(TokenType.RIGHT_BRACE)
        elif self._c in DIGIT_CHARS:
            self._on_digit()
        elif self._c == ord("'"):
            self._on_char_literal()
        elif self._c == ord('"'):
            self._on_string_literal()
        elif self._c == ord("R"):
            self._on_R()
        elif self._c == ord("#"):
            self._on_preprocess()
        elif self._c in SYMBOL_BEGIN_CHARS:
            self._on_symbol()
        else:
            self._emit_token(TokenType.UNKNOWN)

    def _on_add(self) -> None:
        self._getc()
        if self._c == ord("+"):
            # "++"
            self._emit_token(TokenType.INCREMENT)
        elif self._c == ord("="):
            # "+="
            self._emit_token(TokenType.ADD_ASSIGN)
        else:
            # "+"
            self._ungetc()
            self._emit_token(TokenType.ADD)

    def _on_sub(self) -> None:
        self._getc()
        if self._c == ord(">"):
            self._getc()
            if self._c == ord("*"):
                # "->*"
                self._emit_token(TokenType.POINTER_STAR)
            else:
                # "->"
                self._ungetc()
                self._emit_token(TokenType.POINTER)
        elif self._c == ord("-"):
            # "--"
            self._emit_token(TokenType.DECREMENT)
        elif self._c == ord("="):
            # "-="
            self._emit_token(TokenType.SUB_ASSIGN)
        else:
            # "-"
            self._ungetc()
            self._emit_token(TokenType.SUB)

    def _on_mul(self) -> None:
        self._getc()
        if self._c == ord("="):
            # "*="
            self._emit_token(TokenType.MUL_ASSIGN)
        else:
            # "*"
            self._ungetc()
            self._emit_token(TokenType.MUL)

    def _on_div(self) -> None:
        self._getc()
        if self._c == ord("*"):
            # "/*"
            self._on_c_comment()
        elif self._c == ord("/"):
            # "//"
            self._on_cc_comment()
        elif self._c == ord("="):
            # "/="
            self._emit_token(TokenType.DIV_ASSIGN)
        else:
            # "/"
            self._ungetc()
            self._emit_token(TokenType.DIV)

    def _on_mod(self) -> None:
        self._getc()
        if self._c == ord("="):
            # "%="
            self._emit_token(TokenType.MOD_ASSIGN)
        else:
            # "%"
            self._ungetc()
            self._emit_token(TokenType.MOD)

    def _on_assign(self) -> None:
        self._getc()
        if self._c == ord("="):
            # "=="
            self._emit_token(TokenType.EQ)
        else:
            # "="
            self._ungetc()
            self._emit_token(TokenType.ASSIGN)

    def _on_gt(self) -> None:
        self._getc()
        if self._c == ord(">"):
            self._getc()
            if self._c == ord("="):
                # ">>="
                self._emit_token(TokenType.SHIFT_RIGHT_ASSIGN)
            else:
                # ">>"
                self._ungetc()
                self._emit_token(TokenType.SHIFT_RIGHT)
        elif self._c == ord("="):
            # ">="
            self._emit_token(TokenType.GE)
        else:
            # ">"
            self._ungetc()
            self._emit_token(TokenType.GT)

    def _on_lt(self) -> None:
        self._getc()
        if self._c == ord("<"):
            self._getc()
            if self._c == ord("="):
                # "<<="
                self._emit_token(TokenType.SHIFT_LEFT_ASSIGN)
            else:
                # "<<"
                self._ungetc()
                self._emit_token(TokenType.SHIFT_LEFT)
        elif self._c == ord("="):
            # "<="
            self._emit_token(TokenType.LE)
        else:
            # "<"
            self._ungetc()
            self._emit_token(TokenType.LT)

    def _on_logical_not(self) -> None:
        self._getc()
        if self._c == ord("="):
            # "!="
            self._emit_token(TokenType.NE)
        else:
            # "!"
            self._ungetc()
            self._emit_token(TokenType.LOGICAL_NOT)

    def _on_bitwise_and(self) -> None:
        self._getc()
        if self._c == ord("&"):
            # "&&"
            self._emit_token(TokenType.LOGICAL_AND)
        elif self._c == ord("="):
            # "&="
            self._emit_token(TokenType.BITWISE_AND_ASSIGN)
        else:
            # "&"
            self._ungetc()
            self._emit_token(TokenType.BITWISE_AND)

    def _on_bitwise_or(self) -> None:
        self._getc()
        if self._c == ord("|"):
            # "||"
            self._emit_token(TokenType.LOGICAL_OR)
        elif self._c == ord("="):
            # "|="
            self._emit_token(TokenType.BITWISE_OR_ASSIGN)
        else:
            # "|"
            self._ungetc()
            self._emit_token(TokenType.BITWISE_OR)

    def _on_bitwise_xor(self) -> None:
        self._getc()
        if self._c == ord("="):
            # "^="
            self._emit_token(TokenType.BITWISE_XOR_ASSIGN)
        else:
            # "^"
            self._ungetc()
            self._emit_token(TokenType.BITWISE_XOR)

    def _on_dot(self) -> None:
        self._getc()
        if self._c == ord("*"):
            # ".*"
            self._emit_token(TokenType.DOT_STAR)
        elif self._c == ord("."):
            self._getc()
            if self._c == ord("."):
                # "..."
                self._emit_token(TokenType.TRIPLE_DOT)
            else:
                # ".."
                self._fatal()
        elif self._c in DIGIT_CHARS:
            # "." [0-9]
            self._ungetc()
            self._ungetc()
            self._on_float_literal(1)
        else:
            # "."
            self._ungetc()
            self._emit_token(TokenType.DOT)

    def _on_colon(self) -> None:
        self._getc()
        if self._c == ord(":"):
            # "::"
            self._emit_token(TokenType.DOUBLE_COLON)
        else:
            # ":"
            self._ungetc()
            self._emit_token(TokenType.COLON)

    def _on_digit(self) -> None:
        type = self._guess_numeric_literal_type()
        self._rewind_to_begin()
        if type == 1:
            self._on_int_literal()
        elif type == 2:
            self._on_float_literal(1)
        else:
            self._on_float_literal(2)

    def _guess_numeric_literal_type(self) -> int:
        while self._offset < len(self._content):
            self._getc()
            if self._c == ord("."):
                # [0-9] ("'"? [0-9])* "."
                return 2
            elif self._c in FLOAT_LITERL_EXPONENT_CHARS:
                # [0-9] ("'"? [0-9])* [eE]
                return 3
            elif self._c == ord("'"):
                self._getc()
                if self._c not in DIGIT_CHARS:
                    self._fatal()
            elif self._c not in DIGIT_CHARS:
                # [0-9] ("'"? [0-9])*
                return 1

    def _on_int_literal(self) -> None:
        self._getc()
        if self._c == ord("0"):
            self._getc()
            if self._c in xX_CHARS:
                # 0[xX]
                token_type = TokenType.HEX_INT_LITERAL
                self._on_int_literal_hex_bin(HEX_INT_LITERAL_CHARS)
            elif self._c in bB_CHARS:
                # 0[bB]
                token_type = TokenType.BIN_INT_LITERAL
                self._on_int_literal_hex_bin(BIN_INT_LITERAL_CHARS)
            else:
                # 0
                self._ungetc()
                token_type = TokenType.OCT_INT_LITERAL
                self._on_int_literal_oct_dec(OCT_INT_LITERAL_CHARS)
        else:
            # [1-9]
            token_type = TokenType.DEC_INT_LITERAL
            self._on_int_literal_oct_dec(DIGIT_CHARS)
        self._emit_token(token_type)

    def _on_int_literal_hex_bin(self, chars: Set[int]) -> None:
        # 0[xX] [0-9a-fA-F] ("'"? [0-9a-fA-F])* suffix?
        # 0[bB] [01] ("'"? [01])* suffix?
        self._getc()
        if self._c not in chars:
            self._fatal()
        while self._offset < len(self._content):
            self._getc()
            if self._c == ord("'"):
                self._getc()
                if self._c not in chars:
                    self._fatal()
            else:
                if self._c not in chars:
                    break
        self._ungetc()
        self._on_int_literal_suffix()

    def _on_int_literal_oct_dec(self, chars: Set[int]) -> None:
        # 0 ("'"? [0-7])* suffix?
        # [1-9] ("'"? [0-9])* suffix?
        while self._offset < len(self._content):
            self._getc()
            if self._c == ord("'"):
                self._getc()
                if self._c not in chars:
                    self._fatal()
            else:
                if self._c not in chars:
                    break
        self._ungetc()
        self._on_int_literal_suffix()

    def _on_int_literal_suffix(self) -> None:
        self._getc()
        if self._c in uU_CHARS:
            self._getc()
            if self._c == l_CHAR:
                self._getc()
                if self._c == l_CHAR:
                    # [uU]]ll
                    pass
                else:
                    # [uU]l
                    self._ungetc()
            elif self._c == L_CHAR:
                self._getc()
                if self._c == L_CHAR:
                    # [uU]LL
                    pass
                else:
                    # [uU]L
                    self._ungetc()
            else:
                # [uU]
                self._ungetc()
        elif self._c == l_CHAR:
            self._getc()
            if self._c in uU_CHARS:
                # l[uU]
                pass
            elif self._c == l_CHAR:
                self._getc()
                if self._c in uU_CHARS:
                    # ll[uU]
                    pass
                else:
                    # ll
                    self._ungetc()
            else:
                # l
                self._ungetc()
        elif self._c == L_CHAR:
            self._getc()
            if self._c in uU_CHARS:
                # L[uU]
                pass
            elif self._c == L_CHAR:
                self._getc()
                if self._c in uU_CHARS:
                    # LL[uU]
                    pass
                else:
                    # LL
                    self._ungetc()
            else:
                # L
                self._ungetc()
        else:
            # no suffix
            self._ungetc()

    def _on_float_literal(self, type: int) -> None:
        if type == 1:
            # float_literal_type1: (digit_seq? "." digit_seq | digit_seq ".") exponent? suffix?
            has_seq1 = self._on_float_literal_digit_seq()
            self._getc()
            if self._c != ord("."):
                self._fatal()
            has_seq2 = self._on_float_literal_digit_seq()
            if not has_seq1 and not has_seq2:
                self._fatal()
            self._on_float_literal_exponent()
            self._on_float_literal_suffix()
        else:
            # float_literal_type2: digit_seq exponent suffix?
            if not self._on_float_literal_digit_seq():
                self._fatal()
            if not self._on_float_literal_exponent():
                self._fatal()
            self._on_float_literal_suffix()
        self._emit_token(TokenType.FLOAT_LITERAL)

    def _on_float_literal_digit_seq(self) -> bool:
        # digit_seq: [0-9] ("'"? [0-9])*
        self._getc()
        if self._c not in DIGIT_CHARS:
            self._ungetc()
            return False

        while self._offset < len(self._content):
            self._getc()
            if self._c == ord("'"):
                self._getc()
                if self._c not in DIGIT_CHARS:
                    self._fatal()
            else:
                if self._c not in DIGIT_CHARS:
                    break
        self._ungetc()
        return True

    def _on_float_literal_exponent(self) -> bool:
        # exponent: [eE] [+-]? digit_seq
        self._getc()
        if self._c not in FLOAT_LITERL_EXPONENT_CHARS:
            self._ungetc()
            return False

        self._getc()
        if self._c not in FLOAT_LITERL_EXPONENT_SIGN_CHARS:
            self._ungetc()
        if not self._on_float_literal_digit_seq():
            self._fatal()
        return True

    def _on_float_literal_suffix(self) -> None:
        # suffix: [flFL]
        self._getc()
        if self._c not in FLOAT_LITERL_SUFFIX_CHARS:
            self._ungetc()

    def _on_char_literal(self) -> None:
        # TODO(kimi): not fully supported
        while self._offset < len(self._content):
            self._getc()
            if self._c == ord("\\"):
                self._getc()
            elif self._c == ord("'"):
                self._emit_token(TokenType.CHAR_LITERAL)
                return
        self._fatal()

    def _on_string_literal(self) -> None:
        # TODO(kimi): not fully supported
        while self._offset < len(self._content):
            self._getc()
            if self._c == ord("\\"):
                self._getc()
            elif self._c == ord('"'):
                self._emit_token(TokenType.STRING_LITERAL)
                return
        self._fatal()

    def _on_R(self) -> None:
        self._getc()
        if self._c == ord('"'):
            # 'R"'
            self._on_raw_string_literal()
            return
        self._ungetc()
        self._on_symbol()

    def _on_raw_string_literal(self) -> None:
        # TODO(kimi): not fully supported
        i = self._content.find(b"(", self._offset)
        if i == -1:
            self._fatal()
        elif i == self._offset:
            # 'R"(' .*? ')"'
            end_tag = b')"'
        else:
            # 'R"' TAG "(" .*? ")" TAG '"'
            end_tag = b")" + self._content[self._offset : i] + b'"'
        j = self._content.find(end_tag, i)
        if j == -1:
            self._fatal()
        self._offset = j + len(end_tag)
        self._emit_token(TokenType.RAW_STRING_LITERAL)

    def _on_c_comment(self) -> None:
        while self._offset < len(self._content):
            self._getc()
            if self._c == ord("*"):
                self._getc()
                if self._c == ord("/"):
                    self._emit_token(TokenType.C_COMMENT)
                    return
                else:
                    self._ungetc()
        self._fatal()

    def _on_cc_comment(self) -> None:
        while self._offset < len(self._content):
            self._getc()
            if self._c == LF:
                self._ungetc()
                break
        self._emit_token(TokenType.CC_COMMENT)

    def _on_preprocess(self) -> None:
        while self._offset < len(self._content):
            self._getc()
            if self._c == ord("'"):
                # Skip char literals, they are part of current token.
                self._on_char_literal()
                self._pop_token()
            elif self._c == ord('"'):
                # Skip string literals, they are part of current token.
                self._on_string_literal()
                self._pop_token()
            elif self._c == ord("/"):
                self._getc()
                if self._c == ord("*"):
                    # Meet C comments not in char/string literals, they are the next token.
                    self._ungetc()
                    self._ungetc()
                    break
                elif self._c == ord("/"):
                    # Meet C++ comments not in char/string literals, they are the next token.
                    self._ungetc()
                    self._ungetc()
                    break
                else:
                    self._ungetc()
            elif self._c == LF:
                self._ungetc()
                break
        token = Token(None, self._begin, self._offset, self._content)
        include = get_include(token.content)
        if include:
            token.type = TokenType.PREPROCESS_INCLUDE
            token.extra = include
        elif is_define(token.content):
            token.type = TokenType.PREPROCESS_DEFINE
        else:
            token.type = TokenType.PREPROCESS
        self._emit_token(token)

    def _on_symbol(self) -> None:
        # [a-zA-Z_] [0-9a-zA-Z_]*
        while self._offset < len(self._content):
            self._getc()
            if self._c not in SYMBOL_CHARS:
                self._ungetc()
                break
        token = Token(None, self._begin, self._offset, self._content)
        token.type = SYMBOL_2_TOKEN_TYPE.get(token.content, TokenType.IDENTIFIER)
        self._emit_token(token)


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

        for token in lexer.tokens:
            print(token)
