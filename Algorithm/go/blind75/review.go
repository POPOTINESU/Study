package main

func review(s string) bool {
	stack := []rune{}

	for _, r := range s {
		if r == '(' || r == '[' || r == '{' {
			stack = append(stack, r)
		} else {
			if len(stack) == 0 {
				return false
			}

			top := stack[len(stack)-1]
			if (r == ')' && top != '(') ||
				(r == '}' && top != '{') ||
				(r == ']' && top != '[') {
				return false
			}

			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}
