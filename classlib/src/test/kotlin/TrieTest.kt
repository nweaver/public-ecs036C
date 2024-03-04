import edu.ucdavis.cs.ecs036c.Trie
import edu.ucdavis.cs.ecs036c.hashedTrieOf
import edu.ucdavis.cs.ecs036c.trieOf
import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

class TrieTest {

    @Test
    fun test() {
        var t = trieOf<Int>("fool" to 1, "food" to 2, "bat" to 3, "cat" to 4, "car" to 5, "baz" to 6, "batty" to 7)
        for(x in t) {

        }
        println("$t")
        println(t.getSequence("bat").joinToString(prefix="{", postfix = "}", limit = 100) {
            it.first + "=" + it.second.toString()
        })
    }

    @Test
    fun test2(){
        var t = hashedTrieOf<Int>("fool" to 1, "food" to 2, "bat" to 3, "cat" to 4, "car" to 5, "baz" to 6, "batty" to 7,
            "💩💩" to 8, "💩🤷‍♂️" to 9, "💩.la" to 10)
        for(x in t) {

        }
        println("$t")
        println(t.getSequence("bat").joinToString(prefix="{", postfix = "}", limit = 100) {
            it.first + "=" + it.second.toString()
        })

        println(t.getSequence("").joinToString(prefix="{", postfix = "}", limit = 100) {
            it.first + "=" + it.second.toString()
        })


    }
}