#! /usr/bin/env python3
#


from lexer import *
from text import *


###################################################################
def test_parse(content: bytes, expected: str) -> None:
    lexer = Lexer(content)
    if lexer.parse():
        lhs = "\n".join([str(token) for token in lexer.tokens]).strip()
        rhs = expected.strip()
        if lhs != rhs:
            print("test_parse:\n{}\n{}".format(green(content), blue("success")))
            print("Got:\n{}".format(yellow(lhs)))
            print("Expected:\n{}\n".format(purple(rhs)))
    else:
        print("test_parse:\n{}\n{}".format(green(content), red("failure")))
        lhs = "\n".join([str(token) for token in lexer.tokens]).strip()
        print("Got:\n{}\n".format(yellow(lhs)))


def test_parse_failure(content: bytes) -> None:
    lexer = Lexer(content)
    if lexer.parse():
        lhs = "\n".join([str(token) for token in lexer.tokens]).strip()
        print("test_parse:\n{}\n{}".format(green(content), blue("success")))
        print("Got:\n{}".format(yellow(lhs)))
        print("Expected a failure.\n")


# INCREMENT
# DECREMENT
# ADD
# ADD_ASSIGN
# SUB
# SUB_ASSIGN
# MUL
# MUL_ASSIGN
# DIV
# DIV_ASSIGN
# MOD
# MOD_ASSIGN
# ASSIGN
test_parse(b"++", r"INCREMENT[0,2] b'++'")
test_parse(b"--", r"DECREMENT[0,2] b'--'")
test_parse(b"+", r"ADD[0,1] b'+'")
test_parse(b"+=", r"ADD_ASSIGN[0,2] b'+='")
test_parse(b"-", r"SUB[0,1] b'-'")
test_parse(b"-=", r"SUB_ASSIGN[0,2] b'-='")
test_parse(b"*", r"MUL[0,1] b'*'")
test_parse(b"*=", r"MUL_ASSIGN[0,2] b'*='")
test_parse(b"/", r"DIV[0,1] b'/'")
test_parse(b"/=", r"DIV_ASSIGN[0,2] b'/='")
test_parse(b"%", r"MOD[0,1] b'%'")
test_parse(b"%=", r"MOD_ASSIGN[0,2] b'%='")
test_parse(b"=", r"ASSIGN[0,1] b'='")

# EQ
# GT
# GE
# LT
# LE
# NE
test_parse(b"==", r"EQ[0,2] b'=='")
test_parse(b">", r"GT[0,1] b'>'")
test_parse(b">=", r"GE[0,2] b'>='")
test_parse(b"<", r"LT[0,1] b'<'")
test_parse(b"<=", r"LE[0,2] b'<='")
test_parse(b"!=", r"NE[0,2] b'!='")

# LOGICAL_AND
# LOGICAL_OR
# LOGICAL_NOT
test_parse(b"&&", r"LOGICAL_AND[0,2] b'&&'")
test_parse(b"and", r"LOGICAL_AND[0,3] b'and'")
test_parse(b"||", r"LOGICAL_OR[0,2] b'||'")
test_parse(b"or", r"LOGICAL_OR[0,2] b'or'")
test_parse(b"!", r"LOGICAL_NOT[0,1] b'!'")
test_parse(b"not", r"LOGICAL_NOT[0,3] b'not'")

# BITWISE_AND
# BITWISE_AND_ASSIGN
# BITWISE_OR
# BITWISE_OR_ASSIGN
# BITWISE_XOR
# BITWISE_XOR_ASSIGN
# BITWISE_NOT
# SHIFT_RIGHT
# SHIFT_RIGHT_ASSIGN
# SHIFT_LEFT
# SHIFT_LEFT_ASSIGN
test_parse(b"&", r"BITWISE_AND[0,1] b'&'")
test_parse(b"&=", r"BITWISE_AND_ASSIGN[0,2] b'&='")
test_parse(b"|", r"BITWISE_OR[0,1] b'|'")
test_parse(b"|=", r"BITWISE_OR_ASSIGN[0,2] b'|='")
test_parse(b"^", r"BITWISE_XOR[0,1] b'^'")
test_parse(b"^=", r"BITWISE_XOR_ASSIGN[0,2] b'^='")
test_parse(b"~", r"BITWISE_NOT[0,1] b'~'")
test_parse(b">>", r"SHIFT_RIGHT[0,2] b'>>'")
test_parse(b">>=", r"SHIFT_RIGHT_ASSIGN[0,3] b'>>='")
test_parse(b"<<", r"SHIFT_LEFT[0,2] b'<<'")
test_parse(b"<<=", r"SHIFT_LEFT_ASSIGN[0,3] b'<<='")

# COMMA
# SEMICOLON
# POINTER
# POINTER_STAR
# DOT
# DOT_STAR
# DOUBLE_COLON
# QUESTION
# COLON
# TRIPLE_DOT
test_parse(b",", r"COMMA[0,1] b','")
test_parse(b";", r"SEMICOLON[0,1] b';'")
test_parse(b"->", r"POINTER[0,2] b'->'")
test_parse(b"->*", r"POINTER_STAR[0,3] b'->*'")
test_parse(b".", r"DOT[0,1] b'.'")
test_parse(b".*", r"DOT_STAR[0,2] b'.*'")
test_parse(b"::", r"DOUBLE_COLON[0,2] b'::'")
test_parse(b"?", r"QUESTION[0,1] b'?'")
test_parse(b":", r"COLON[0,1] b':'")
test_parse(b"...", r"TRIPLE_DOT[0,3] b'...'")
test_parse_failure(b"..")

# LEFT_PAREN
# RIGHT_PAREN
# LEFT_BRACKET
# RIGHT_BRACKET
# LEFT_BRACE
# RIGHT_BRACE
test_parse(b"(", r"LEFT_PAREN[0,1] b'('")
test_parse(b")", r"RIGHT_PAREN[0,1] b')'")
test_parse(b"[", r"LEFT_BRACKET[0,1] b'['")
test_parse(b"]", r"RIGHT_BRACKET[0,1] b']'")
test_parse(b"{", r"LEFT_BRACE[0,1] b'{'")
test_parse(b"}", r"RIGHT_BRACE[0,1] b'}'")

# BOOL_LITERAL
test_parse(b"true", r"BOOL_LITERAL[0,4] b'true'")
test_parse(b"false", r"BOOL_LITERAL[0,5] b'false'")

# HEX_INT_LITERAL
# BIN_INT_LITERAL
# OCT_INT_LITERAL
# DEC_INT_LITERAL
test_parse(b"0x0", r"HEX_INT_LITERAL[0,3] b'0x0'")
test_parse(b"0x7ff", r"HEX_INT_LITERAL[0,5] b'0x7ff'")
test_parse(b"0X7'F'F", r'''HEX_INT_LITERAL[0,7] b"0X7'F'F"''')
test_parse_failure(b"0x")
test_parse_failure(b"0x'7ff")
test_parse_failure(b"0X7''FF")

test_parse(b"0b0", r"BIN_INT_LITERAL[0,3] b'0b0'")
test_parse(b"0b111", r"BIN_INT_LITERAL[0,5] b'0b111'")
test_parse(b"0B1'1'1", r'''BIN_INT_LITERAL[0,7] b"0B1'1'1"''')
test_parse_failure(b"0b")
test_parse_failure(b"0b'111")
test_parse_failure(b"0B1''11")

test_parse(b"0", r"OCT_INT_LITERAL[0,1] b'0'")
test_parse(b"0755", r"OCT_INT_LITERAL[0,4] b'0755'")
test_parse(b"0'7'5'5", r'''OCT_INT_LITERAL[0,7] b"0'7'5'5"''')
test_parse_failure(b"0''755")

test_parse(b"755", r"DEC_INT_LITERAL[0,3] b'755'")
test_parse(b"7'5'5", r'''DEC_INT_LITERAL[0,5] b"7'5'5"''')
test_parse_failure(b"7''55")

test_parse(b"0u", r"OCT_INT_LITERAL[0,2] b'0u'")
test_parse(b"0ul", r"OCT_INT_LITERAL[0,3] b'0ul'")
test_parse(b"0uL", r"OCT_INT_LITERAL[0,3] b'0uL'")
test_parse(b"0ull", r"OCT_INT_LITERAL[0,4] b'0ull'")
test_parse(b"0uLL", r"OCT_INT_LITERAL[0,4] b'0uLL'")
test_parse(b"0U", r"OCT_INT_LITERAL[0,2] b'0U'")
test_parse(b"0Ul", r"OCT_INT_LITERAL[0,3] b'0Ul'")
test_parse(b"0UL", r"OCT_INT_LITERAL[0,3] b'0UL'")
test_parse(b"0Ull", r"OCT_INT_LITERAL[0,4] b'0Ull'")
test_parse(b"0ULL", r"OCT_INT_LITERAL[0,4] b'0ULL'")
test_parse(b"0l", r"OCT_INT_LITERAL[0,2] b'0l'")
test_parse(b"0ll", r"OCT_INT_LITERAL[0,3] b'0ll'")
test_parse(b"0lu", r"OCT_INT_LITERAL[0,3] b'0lu'")
test_parse(b"0lU", r"OCT_INT_LITERAL[0,3] b'0lU'")
test_parse(b"0llu", r"OCT_INT_LITERAL[0,4] b'0llu'")
test_parse(b"0llU", r"OCT_INT_LITERAL[0,4] b'0llU'")
test_parse(b"0L", r"OCT_INT_LITERAL[0,2] b'0L'")
test_parse(b"0LL", r"OCT_INT_LITERAL[0,3] b'0LL'")
test_parse(b"0Lu", r"OCT_INT_LITERAL[0,3] b'0Lu'")
test_parse(b"0LU", r"OCT_INT_LITERAL[0,3] b'0LU'")
test_parse(b"0LLu", r"OCT_INT_LITERAL[0,4] b'0LLu'")
test_parse(b"0LLU", r"OCT_INT_LITERAL[0,4] b'0LLU'")

# FLOAT_LITERAL
test_parse(b"0.0", r"FLOAT_LITERAL[0,3] b'0.0'")
test_parse(b"00.00", r"FLOAT_LITERAL[0,5] b'00.00'")
test_parse(b"11.22", r"FLOAT_LITERAL[0,5] b'11.22'")
test_parse(b"1'1.2'2", r'''FLOAT_LITERAL[0,7] b"1'1.2'2"''')
test_parse(b"11.", r"FLOAT_LITERAL[0,3] b'11.'")
test_parse(b".22", r"FLOAT_LITERAL[0,3] b'.22'")
test_parse(b"11.e0", r"FLOAT_LITERAL[0,5] b'11.e0'")
test_parse(b"11.E+00", r"FLOAT_LITERAL[0,7] b'11.E+00'")
test_parse(b"11.E+11", r"FLOAT_LITERAL[0,7] b'11.E+11'")
test_parse(b"11.E-1'1", r'''FLOAT_LITERAL[0,8] b"11.E-1'1"''')
test_parse(b"11e0f", r"FLOAT_LITERAL[0,5] b'11e0f'")
test_parse(b"11E+00F", r"FLOAT_LITERAL[0,7] b'11E+00F'")
test_parse(b"11E+11l", r"FLOAT_LITERAL[0,7] b'11E+11l'")
test_parse(b"11E-1'1L", r'''FLOAT_LITERAL[0,8] b"11E-1'1L"''')
test_parse(b".22f", r"FLOAT_LITERAL[0,4] b'.22f'")
test_parse(b".22F", r"FLOAT_LITERAL[0,4] b'.22F'")
test_parse(b".22l", r"FLOAT_LITERAL[0,4] b'.22l'")
test_parse(b".22L", r"FLOAT_LITERAL[0,4] b'.22L'")

# POINTER_LITERAL
test_parse(b"nullptr", r"POINTER_LITERAL[0,7] b'nullptr'")

# CHAR_LITERAL
test_parse(b"''", r'''CHAR_LITERAL[0,2] b"''"''')
test_parse(b"'123456789'", r'''CHAR_LITERAL[0,11] b"'123456789'"''')
test_parse(b"'123\\ \t\n456\\ \t\n789'", r'''CHAR_LITERAL[0,19] b"'123456789'"''')
test_parse(rb"'\'\"'", r"""CHAR_LITERAL[0,6] b'\'\\\'\\"\''""")
test_parse(rb"'\0\00\000\x00\u0000'", r'''CHAR_LITERAL[0,21] b"'\\0\\00\\000\\x00\\u0000'"''')
test_parse_failure(b"'")
test_parse_failure(b"'\\")

# STRING_LITERAL
test_parse(b'""', r"""STRING_LITERAL[0,2] b'""'""")
test_parse(b'"123456789"', r"""STRING_LITERAL[0,11] b'"123456789"'""")
test_parse(b'"123\\ \t\n456\\ \t\n789"', r"""STRING_LITERAL[0,19] b'"123456789"'""")
test_parse(rb'"\'\""', r"""STRING_LITERAL[0,6] b'"\\\'\\""'""")
test_parse(rb'"\0\00\000\x00\u0000"', r"""STRING_LITERAL[0,21] b'"\\0\\00\\000\\x00\\u0000"'""")
test_parse_failure(b'"')
test_parse_failure(b'"\\')

# RAW_STRING_LITERAL
test_parse(b'R"()"', r"""RAW_STRING_LITERAL[0,5] b'R"()"'""")
test_parse(b'R"(")"', r"""RAW_STRING_LITERAL[0,6] b'R"(")"'""")
test_parse(b'R"())"', r"""RAW_STRING_LITERAL[0,6] b'R"())"'""")
test_parse(b'R"(())"', r"""RAW_STRING_LITERAL[0,7] b'R"(())"'""")
test_parse(b'R"(123456789)"', r"""RAW_STRING_LITERAL[0,14] b'R"(123456789)"'""")
test_parse(b'R"(123("456")789)"', r"""RAW_STRING_LITERAL[0,18] b'R"(123("456")789)"'""")
test_parse(b'''R"(123\\ \t\n456\\ \t\n789)"''', r"""RAW_STRING_LITERAL[0,22] b'R"(123\\ \t\n456\\ \t\n789)"'""")
test_parse(b'R"TAG(123456789)TAG"', r"""RAW_STRING_LITERAL[0,20] b'R"TAG(123456789)TAG"'""")
test_parse(b'R"TAG(123("456)"789)TAG"', r"""RAW_STRING_LITERAL[0,24] b'R"TAG(123("456)"789)TAG"'""")
test_parse(b'R"TAG(123\\ \t\n456\\ \t\n789)TAG"', r"""RAW_STRING_LITERAL[0,28] b'R"TAG(123\\ \t\n456\\ \t\n789)TAG"'""")
test_parse_failure(b'R"')
test_parse_failure(b'R"(')
test_parse_failure(b'R"(123456789')
test_parse_failure(b'R"(123456789)')
test_parse_failure(b'R"TAG(123456789)GAT"')

# C_COMMENT
test_parse(b"/* A */", r"C_COMMENT[0,7] b'/* A */'")
test_parse(b"/** A * B **/", r"C_COMMENT[0,13] b'/** A * B **/'")
test_parse(b"/* A /* B */", r"C_COMMENT[0,12] b'/* A /* B */'")
test_parse(
    b"""/*
 * A B
 */""",
    r"C_COMMENT[0,13] b'/*\n * A B\n */'",
)
test_parse(
    b"""/**
 * A B
 **/""",
    r"C_COMMENT[0,15] b'/**\n * A B\n **/'",
)
test_parse_failure(b"/*")
test_parse_failure(b"/* A")
test_parse_failure(b"/* A *")
test_parse_failure(b"/** A **")

# CC_COMMENT
test_parse(b"//", r"CC_COMMENT[0,2] b'//'")
test_parse(b"// A B", r"CC_COMMENT[0,6] b'// A B'")
test_parse(b"// A / B", r"CC_COMMENT[0,8] b'// A / B'")
test_parse(b"// A // B", r"CC_COMMENT[0,9] b'// A // B'")

# PREPROCESS
test_parse(b"#pragma once", r"PREPROCESS[0,12] b'#pragma once'")

# PREPROCESS_INCLUDE
test_parse(b"#include <stdio.h>", r"PREPROCESS_INCLUDE[0,18] b'#include <stdio.h>' b'stdio.h'")
test_parse(b'#include "stdio.h"', r"""PREPROCESS_INCLUDE[0,18] b'#include "stdio.h"' b'stdio.h'""")
test_parse(b"#include <A/B.h>", r"PREPROCESS_INCLUDE[0,16] b'#include <A/B.h>' b'A/B.h'")
test_parse(b'#include "A//B.h"', r"""PREPROCESS_INCLUDE[0,17] b'#include "A//B.h"' b'A//B.h'""")

# PREPROCESS_DEFINE
test_parse(b"#define A B", r"PREPROCESS_DEFINE[0,11] b'#define A B'")
test_parse(b'#define A "/* B */"', r"""PREPROCESS_DEFINE[0,19] b'#define A "/* B */"'""")
test_parse(b'#define A "// C"', r"""PREPROCESS_DEFINE[0,16] b'#define A "// C"'""")
test_parse(b'#define A "/* B */" "// C"', r"""PREPROCESS_DEFINE[0,26] b'#define A "/* B */" "// C"'""")
test_parse(
    b'#define A B "/* C */" /* C" */',
    r"""
PREPROCESS_DEFINE[0,22] b'#define A B "/* C */" '
C_COMMENT[22,30] b'/* C" */'
""",
)
test_parse(
    b'#define A B "// C" // C"',
    r"""
PREPROCESS_DEFINE[0,19] b'#define A B "// C" '
CC_COMMENT[19,24] b'// C"'
""",
)
test_parse_failure(b'#define A B(")')

# KEYWORD
test_parse(b"try", r"KEYWORD[0,3] b'try'")
test_parse(b"catch", r"KEYWORD[0,5] b'catch'")

# IDENTIFIER
test_parse(b"R", r"IDENTIFIER[0,1] b'R'")

# comprehensive
test_parse(
    b"""std::vector<std::string> vs;
for (size_t i = 0; i < N; ++i) {
  vs.emplace_back(std::to_string(i));
}""",
    r"""
IDENTIFIER[0,3] b'std'
DOUBLE_COLON[3,5] b'::'
IDENTIFIER[5,11] b'vector'
LT[11,12] b'<'
IDENTIFIER[12,15] b'std'
DOUBLE_COLON[15,17] b'::'
IDENTIFIER[17,23] b'string'
GT[23,24] b'>'
IDENTIFIER[25,27] b'vs'
SEMICOLON[27,28] b';'
KEYWORD[29,32] b'for'
LEFT_PAREN[33,34] b'('
IDENTIFIER[34,40] b'size_t'
IDENTIFIER[41,42] b'i'
ASSIGN[43,44] b'='
OCT_INT_LITERAL[45,46] b'0'
SEMICOLON[46,47] b';'
IDENTIFIER[48,49] b'i'
LT[50,51] b'<'
IDENTIFIER[52,53] b'N'
SEMICOLON[53,54] b';'
INCREMENT[55,57] b'++'
IDENTIFIER[57,58] b'i'
RIGHT_PAREN[58,59] b')'
LEFT_BRACE[60,61] b'{'
IDENTIFIER[64,66] b'vs'
DOT[66,67] b'.'
IDENTIFIER[67,79] b'emplace_back'
LEFT_PAREN[79,80] b'('
IDENTIFIER[80,83] b'std'
DOUBLE_COLON[83,85] b'::'
IDENTIFIER[85,94] b'to_string'
LEFT_PAREN[94,95] b'('
IDENTIFIER[95,96] b'i'
RIGHT_PAREN[96,97] b')'
RIGHT_PAREN[97,98] b')'
SEMICOLON[98,99] b';'
RIGHT_BRACE[100,101] b'}'
""",
)
