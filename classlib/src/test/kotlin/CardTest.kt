import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

import edu.ucdavis.cs.ecs036c.*
import org.junit.jupiter.api.Timeout

import java.security.SecureRandom
import java.time.Duration
import kotlin.random.asKotlinRandom


class CardTest {

    @Test
    fun testDeck(){
        val d1 = Deck()
        val d2 = Deck()
        assert(d1 == d2)
        println("$d1")
        d1.shuffle()
        println("$d1")
        assert(d1 != d2)
        assert(d1.isValidDeck())
        val c = d1[1]
        assert(d1[0] != d1[1])
        d1[0] = d1[1]
        assert(!d1.isValidDeck())
        assert(d1[0] == c)
        var x = 0
        for(card in d2) {
            assert(d2[x] == card)
            x++
        }
    }
    @Test
    fun testToString() {
        val c = Card(Face.TEN,Suite.HEART)
        assert(c.toString() == "10:♥")
    }

    @Test
    fun testEquals() {
    }

    @Test
    fun testHashCode() {
    }

    @Test
    fun getFace() {
    }

    @Test
    fun getSuite() {
    }


    /*
     * This does NOT ACTUALLY WORK because JUnit5 Timeout is NOT actually
     * enforced by killing the offending thread.  You HAVE to use assertTimeoutPreemptively!
     *
     * Worse, the LATEST version of JUnit5 is up to date, but the kotlin testing framework is not...
     * threadMode = Timeout.ThreadMode.SEPARATE_THREAD would work but hey...
     *
     */
    // @Test
    fun testTimeout(){
        while(true) {

        }
    }

    @Test
    @Timeout(1, threadMode = Timeout.ThreadMode.SEPARATE_THREAD)
    fun testTimeoutAssertion(){
        testTimeout()
        print("Test done")
    }
}