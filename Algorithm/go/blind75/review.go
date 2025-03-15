package main

func review(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	left := review(root.Left)
	right := review(root.Right)

	// invert tree
	root.Left = right
	root.Right = left

	return root
}
