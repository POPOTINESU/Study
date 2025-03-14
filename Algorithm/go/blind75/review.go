package main

func review(head *ListNode) *ListNode {
	var prev *ListNode
	var next *ListNode

	for head != nil{
		next = head.Next
		head.Next = prev
		prev = head
		head = next
	}

	return prev
}
