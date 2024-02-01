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

    @Test
    fun testShaHash(){
        println("Hello, World!\n".sha256)
    }

    @Test
    fun testSetCoolness(){
        val s1 = setOf(1, 2, 3, 4)
        val s2 = setOf(3,4,5,6)
        println("${s1 + s2}")
        println("${s1 - s2}")
    }

    @Test
    fun testCastingArray(){
        val ar : Array<Int?> = arrayOfNulls(5)
        for(i in 0..<4){
            ar[i] = i
        }
        println(ar[1].toString())
        println(ar[4].toString())
        ar as Array<Int>
        println(ar[1].toString())
        println(ar[4].toString())
    }

    @Test
    fun testCastingArray2(){
        val ar : Array<Int?> = arrayOfNulls(5)
        for(i in 0..<4){
            ar[i] = i
        }
        println(ar[1].toString())
        println(ar[4].toString())
        ar.requireNoNulls()
        println(ar[1].toString())
        println(ar[4].toString())
    }

    @Test
    fun testCastingArray3(){
        val ar : Array<Int?> = arrayOfNulls(5)
        for(i in 0..<4){
            ar[i] = i
        }
        val x = ar[4] as Int
        println(x.toString())
        println(x.toString())
    }

    @Test
    fun iteratorPlayground(){
        class Foo(val max: Int = 5) {
            operator fun iterator() = sequence {
                for (i in 0..<max){
                    yield(i)
                }
            }.iterator()
        }

        for(i in Foo(5)){
            println("$i")
        }
    }

}