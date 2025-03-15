package main

func review(root *TreeNode) int {
	if root == nil {
		return 0
	}

	leftDepth := review(root.Left)
	rightDepth := review(root.Right)

	// Add 1 to include current node in the depth count
	if leftDepth > rightDepth {
		return leftDepth + 1
	} else {
		return rightDepth + 1
	}
}
