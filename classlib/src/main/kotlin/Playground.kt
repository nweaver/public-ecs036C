package edu.ucdavis.cs.ecs036c
import java.security.MessageDigest

fun allPositiveNumbers(): Sequence<Long> {
    class Numbers(var at: Long):AbstractIterator<Long>(){
        override fun computeNext(){
            setNext(at)
            at++
        }
    }
    return Numbers(1).asSequence()
}


val String.sha256: String
    get() {
        val bytes = MessageDigest.getInstance("SHA256").digest(this.toByteArray())
        return bytes.joinToString("") { "%02x".format(it) }
    }