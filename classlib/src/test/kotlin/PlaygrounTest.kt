package edu.ucdavis.cs.ecs036c

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test


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

}