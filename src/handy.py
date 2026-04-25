# handy.py
#
# (c) ClicKill Microbits
def quote_it(s: str) -> str:
	return f'"{s}"'

def single_quote_it(s: str) -> str:
	return f"'{s}'"

def debug(label, value):
	print(f"{label}={value!r}")

def left_str(s: str, num_chars: int) -> str:
	return s[:num_chars]

def right_str(s: str, num_chars: int) -> str:
	minus_n = -1 * num_chars
	return s[minus_n:]

def instr_str_explicit(start_idx: int, s: str, substr: str) -> int:
	if start_idx < 1:
		return 0
	test_str = s
	if start_idx > len(s):
		return 0
	if start_idx > 1:
		test_str = s[start_idx - 1:]
	result = test_str.find(substr) + 1
	return result

def instr_str(s: str, substr: str) -> int:
	return instr_str_explicit(1, s, substr)

def mid_str(s: str, idx: int, num_chars=1) -> str:
	return s[idx-1: (idx+num_chars)-1]
