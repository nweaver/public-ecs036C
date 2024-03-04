package edu.ucdavis.cs.ecs036c

/*
 * This is an implementation of a Trie for a map (key/value store)
 */

/*
 * The maximum character we support in our Trie is 1 less than this
 */
val maxCharVal = 128

data class TrieNode<T>(var terminal: Boolean = false, var data: T? = null){
    val children = arrayOfNulls<TrieNode<T>>(maxCharVal)
}

class Trie<T> {

    // The Character name on the root doesn't matter
    val root = TrieNode<T>()

    operator fun set(s: String, data: T){
        var atNode = root
        for (char in s){
            val index = char.code
            if(index >= maxCharVal) throw Error("Character out of range for a trie: ASCII characters only")
            if(atNode.children[index] == null){
                atNode.children[index] = TrieNode()
            }
            atNode = atNode.children[index]!!
        }
        atNode.terminal = true
        atNode.data = data
    }
    operator fun get(s: String) : T? {
        var atNode = root
        for (char in s){
            val index = char.code
            if(index >= maxCharVal) throw Error("Character out of range for a trie: ASCII characters only")
            if(atNode.children[index] == null){
                return null
            }
            atNode = atNode.children[index]!!
        }
        if (atNode.terminal) return atNode.data
        return null
    }

    operator fun contains(s: String) : Boolean {
        var atNode = root
        for (char in s){
            val index = char.code
            if(index >= maxCharVal) throw Error("Character out of range for a trie: ASCII characters only")
            if(atNode.children[index] == null){
                return false
            }
            atNode = atNode.children[index]!!
        }
        if (atNode.terminal) return true
        return false
    }


    fun getSequence(start : String = "") = sequence {
        /*
         * We need to construct this sequence using an explicit
         * stack, which we push on pairs of String, Node, and where on the node we are at
         */
        var startNode = root
        for (char in start) {
            val index = char.code
            if(index >= maxCharVal) throw Error("Character out of range for a trie")
            if(startNode.children[index] == null) return@sequence
            startNode = startNode.children[index]!!
        }
        val stack = mutableListOf(Triple(start, startNode, 0))
        while (true){
            if (stack.size == 0) return@sequence
            val (atString, atNode, index) = stack.removeLast()
            if(atNode.terminal && index == 0) yield(Pair(atString, atNode.data as T))
            for (i in index..< maxCharVal){
                if (atNode.children[i] != null){
                    val newstring = atString + i.toChar()
                    stack.add(Triple(atString, atNode, i+1))
                    stack.add(Triple(newstring, atNode.children[i]!!, 0))
                    break
                }
            }
        }
    }

    operator fun iterator() = getSequence().iterator()

    override fun toString()  =  getSequence().joinToString(prefix="{", postfix = "}", limit = 100) {
            it.first + "=" + it.second.toString()
        }

}

fun <T>trieOf(vararg data: Pair<String, T>) : Trie<T>{
    val retval = Trie<T>()
    data.forEach { retval[it.first] = it.second }
    return retval
}

data class HashedTrieNode<T>(var terminal: Boolean = false, var data: T? = null){
    val children = mutableMapOf<Char, HashedTrieNode<T>>().toSortedMap()
}

class HashedTrie<T> {
    val root = HashedTrieNode<T>()

    operator fun set(s: String, data: T){
        var atNode = root
        for (char in s){
            if(char !in atNode.children) atNode.children[char] = HashedTrieNode()
            atNode = atNode.children[char]!!
        }
        atNode.terminal = true
        atNode.data = data
    }
    operator fun get(s: String) : T? {
        var atNode = root
        for (char in s){
            if(char !in atNode.children) return null
            atNode = atNode.children[char]!!
        }
        if (atNode.terminal) return atNode.data
        return null
    }

    operator fun contains(s: String) : Boolean {
        var atNode = root
        for (char in s){
            if(char !in atNode.children) return false
            atNode = atNode.children[char]!!
        }
        if (atNode.terminal) return true
        return false
    }


    /*
     *
     */
    fun getSequence(start : String = "") = sequence {
        /*
         * We need to construct this sequence using an explicit
         * stack, which we push on pairs of String, Node, and where on the node we are at
         */
        data class StackEntry(
            val atString: String,
            val atNode: HashedTrieNode<T>,
            val childChars: List<Char>,
            val index: Int)
        var startNode = root
        for (char in start) {
            if(startNode.children[char] == null) return@sequence
            startNode = startNode.children[char]!!
        }
        val stack = mutableListOf(StackEntry(start,
            startNode,
            startNode.children.toList().map{ it.first },
            0))
        while (true){
            if (stack.size == 0) return@sequence
            val (atString, atNode, childChars, index) = stack.removeLast()
            if(index == 0 && atNode.terminal) {
                @Suppress("UNCHECKED_CAST")
                yield(Pair(atString, atNode.data as T))
            }
            if(index < childChars.size) {
                val c = childChars[index]
                stack.add(StackEntry(atString, atNode, childChars, index+1))
                stack.add(StackEntry(atString + c,
                    atNode.children[c]!!,
                    atNode.children[c]!!.children.toList().map{it.first},
                    0))
            }
        }
    }

    operator fun iterator() = getSequence().iterator()

    override fun toString()  =  getSequence().joinToString(prefix="{", postfix = "}", limit = 100) {
        it.first + "=" + it.second.toString()
    }

}

fun <T>hashedTrieOf(vararg data: Pair<String, T>) : HashedTrie<T>{
    val retval = HashedTrie<T>()
    data.forEach { retval[it.first] = it.second }
    return retval
}