package edu.ucdavis.cs.ecs036c

fun allPositiveNumbers(): Sequence<Long> {
    class Numbers(var at: Long):AbstractIterator<Long>(){
        override fun computeNext(){
            setNext(at)
            at++
        }
    }
    return Numbers(1).asSequence()
}
