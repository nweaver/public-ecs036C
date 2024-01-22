package edu.ucdavis.cs.ecs036c

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test
import java.util.Arrays.asList


class PlaygroundTest{
    @Test
    fun testNumbers(){
        fun <T>prettyPrint(s: Sequence<T>) = s.joinToString(prefix = "[", postfix = "]", limit =10){it.toString()}
        println(prettyPrint(allPositiveNumbers()))
        println(prettyPrint(allPositiveNumbers().map{it * it}))
        println(prettyPrint(allPositiveNumbers().filter{it % 2 == 0L}))
    }

    @Test
    fun testRecursion(){
        fun recursive(i: Int) {
            print(i)
            recursive(i+1)
            print(i)
        }
        // Wolud cause a StackOverflowError
        // recursive(1)
    }

    @Test
    fun showFoldCoolness(){
        val data = asList(1, 2, 3, 4, 5, 6)
        println(data)
        val sum = data.fold(1){x, y -> x * y}
        println(sum)
    }
}