package main

func review(root *TreeNode, subRoot *TreeNode) bool {
	if root != nil {
		return false
	}

	if sameTree(root, subRoot) {
		return true
	}

	return review(root.Left, subRoot) || review(root.Right, subRoot)
}

func sameTree(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil && subRoot == nil {
		return true
	}
	if root == nil || subRoot == nil {
		return false
	}
	if root.Val != subRoot.Val {
		return false
	}

	return sameTree(root.Left, subRoot.Left) && sameTree(root.Right, subRoot.Right)
}
