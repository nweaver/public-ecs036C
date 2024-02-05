package edu.ucdavis.cs.ecs036c

import jdk.incubator.vector.VectorOperators.Binary


class BinaryTreeNode<T>(val data: T, var left: BinaryTreeNode<T>?, var right: BinaryTreeNode<T>?) {
    fun toStringInternal(previouslyPrinted: MutableSet<BinaryTreeNode<T>>): String {
        if (this in previouslyPrinted) {
            return "ERROR:ALREADY_VISITED{Data: $data}"
        }
        previouslyPrinted.add(this)
        var res = "("
        if (left != null) {
            res += left?.toStringInternal(previouslyPrinted) + " "
        }
        res += data.toString()
        if (right != null) {
            res += " " + right?.toStringInternal(previouslyPrinted)
        }
        return res + ")"
    }

    override fun toString() = toStringInternal(mutableSetOf<BinaryTreeNode<T>>())

    fun wellFormed(visited: MutableSet<BinaryTreeNode<T>> = mutableSetOf<BinaryTreeNode<T>>()): Boolean {
        if (this in visited) return false
        visited.add(this)
        return (left?.wellFormed(visited) ?: true) &&
                (right?.wellFormed(visited) ?: true)
    }

    fun inOrderTraversal(): Sequence<T> = sequence {
        val workStack = ArrayDeque<BinaryTreeNode<T>>()
        var currentNode: BinaryTreeNode<T>? = this@BinaryTreeNode
        while (!workStack.isEmpty() || currentNode != null) {
            // The logic:  We examine the current node.  IF there
            // is stuff to the left, we push ourselves onto the stack
            // and update the current node
            if (currentNode != null) {
                workStack.addLast(currentNode)
                currentNode = currentNode.left
            } else {
                currentNode = workStack.removeLast()
                yield(currentNode.data)
                currentNode = currentNode.right
            }
        }
    }

    fun preOrderTraversal(): Sequence<T> = sequence {
        val workStack = ArrayDeque<BinaryTreeNode<T>>()
        workStack.addLast(this@BinaryTreeNode)
        while (!workStack.isEmpty()) {
            val currentNode = workStack.removeLast()
            yield(currentNode.data)
            if(currentNode.right != null){
                workStack.addLast(currentNode.right!!)
            }
            if(currentNode.left != null){
                workStack.addLast(currentNode.left!!)
            }
        }
    }

    // Post order is a bit trickier...
    // We have our current node and our stack, and we check to see if the
    // right subtree is on the top of the stack.
    fun postOrderTraversal(): Sequence<T> = sequence {
        val workStack = ArrayDeque<BinaryTreeNode<T>>()
        var current: BinaryTreeNode<T>? = this@BinaryTreeNode
        while (!workStack.isEmpty() || current != null) {
            if (current == null) {
                current = workStack.removeLast()
                if (!workStack.isEmpty() &&
                    current.right == workStack.get(workStack.lastIndex)
                ) {
                    val tmp = current
                    current = workStack.removeLast()
                    workStack.addLast(tmp)
                } else {
                    yield(current.data)
                    current = null
                }
            } else {
                if(current.right != null){
                    workStack.addLast(current.right!!)
                }
                workStack.addLast(current)
                current = current.left
            }
        }
    }

    fun levelOrderTraversal(): Sequence<T> = sequence {
        val workQueue = ArrayDeque<BinaryTreeNode<T>>()
        workQueue.addLast(this@BinaryTreeNode)
        while (!workQueue.isEmpty()) {
            val current = workQueue.removeFirst()
            yield(current.data)
            if (current.left != null) {
                workQueue.addLast(current.left!!)
            }
            if (current.right != null) {
                workQueue.addLast(current.right!!)
            }
        }
    }



        operator fun iterator() = inOrderTraversal().iterator()

}


class OrderedBinaryTree<T: Comparable<T>> {
    var root : BinaryTreeNode<T>? = null

    operator fun iterator() = root?.inOrderTraversal()?.iterator() ?: emptySequence<T>().iterator()

    override fun toString() = root?.toString() ?: "NULL"

    fun insert(data: T) {
        fun insertInternal(at: BinaryTreeNode<T>?): BinaryTreeNode<T>{
            if (at == null){
                return BinaryTreeNode(data, null, null)
            }
            else if (data < at.data){
                at.left = insertInternal(at.left)
            } else {
                at.right = insertInternal(at.right)
            }
            return at
        }
        root = insertInternal(root)
    }

    operator fun contains(data: T) : Boolean {
        fun containsInternal(at: BinaryTreeNode<T>?) : Boolean{
            if (at == null) return false
            if (at.data == data) return true
            if (data < at.data) return containsInternal(at.left)
            return containsInternal(at.right)
        }
        return containsInternal(root)
    }
}

fun <T: Comparable<T>>toOrderedTree(vararg data : T) : OrderedBinaryTree<T> {
    val retVal = OrderedBinaryTree<T>()
    for(element in data){
        retVal.insert(element)
    }
    return retVal
}