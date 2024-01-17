package edu.ucdavis.cs.ecs036c

import java.security.SecureRandom
import kotlin.random.asKotlinRandom

/**
 *
 *
 */

/**
 * This Enumeration class handles the suite, with a nice toString function
 * that prints out the actual suite character.
 *
 * Enumeration classes come with a lot of nice built-in features
 * such as comparisons and equality, hash codes,
 * and a way to conveniently enumerate all the options.
 */
enum class Suite {
    CLUB, DIAMOND, HEART, SPADE ;

    override fun toString(): String {
        return when(this) {
            HEART -> "♥"
            SPADE -> "♠"
            CLUB -> "♣"
            DIAMOND -> "♦"
        }
    }
}

/**
 * And the similar enumeration for the face value.
 *
 * Ace is considered the high value in this comparison.
 *
 */
enum class Face {
    TWO, THREE, FOUR,
    FIVE, SIX, SEVEN, EIGHT,
    NINE, TEN, JACK, QUEEN, KING, ACE ;
    override fun toString(): String {
        return when (this) {
            ACE -> "A"
            TWO -> "2"
            THREE -> "3"
            FOUR -> "4"
            FIVE -> "5"
            SIX -> "6"
            SEVEN -> "7"
            EIGHT -> "8"
            NINE -> "9"
            TEN -> "10"
            JACK -> "J"
            QUEEN -> "Q"
            KING -> "K"
        }
    }
}

/**
 * And this is a class for an individual card.
 *
 * In particular it has a nice customized toString,
 * an overriden equals function, and a comparison function
 * that prioritizes the face value (ace is high) and then the
 * suite value in case of ties.
 */
class Card(val face:Face,val suite:Suite){
    override fun toString(): String {
        return face.toString() + ":" + suite.toString()
    }

    /**
     * This looks like a lot of code to have to "remember" to write but...
     *
     * A:  If I made this a data class this would already be done for me.
     *
     * B:  It was actually generated for me by IntelliJ.
     */
    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (javaClass != other?.javaClass) return false

        other as Card

        if (face != other.face) return false
        if (suite != other.suite) return false

        return true
    }

    /**
     * Java's HashCode for integers is Not That Good™:
     * It uses the integer value itself.  BUT in this construction
     * we are actually OK-ish (aka, good for normal hash tables, not good
     * for cuckoo hash tables), because no two cards with different values
     * will end up with the same hashCode.
     */
    override fun hashCode(): Int {
        var result = face.hashCode()
        result = 31 * result + suite.hashCode()
        return result
    }

    /*
     * This gives us a comparison operation between cards.
     *
     * This uses the convention that ace is high
     */
    fun compareTo(b: Card) : Int{
        if (this == b) return 0
        if (this.face < b.face) return -1
        if (this.face > b.face) return 1
        if (this.suite < b.suite) return -1
        return 1
    }
}

/*
 * I don't trust any RNG that isn't the cryptographically secure version
 * So this is a wrapper for Java's SecureRandom into a Kotlin random
 * object to use in the code
 */
private val secureRNG = SecureRandom().asKotlinRandom()


class Deck(){
    /*
     * Initializes the cards array.  The trick here is the {} is a lambda expression
     * that is evaluated to actually create the deck of cards and initialize it to
     * the proper entries.  Thus it is maximally efficient (using a static array
     * rather than a Collection) while also being fully type safe as the
     * cards array has no null entries even if the initial value started
     * by taking an array of null entries and asssigning them
     */
    val cards : Array<Card> = {
        val emptyCards : Array<Card?> = arrayOfNulls(52)
        var x = 0;
        for (face in Face.entries){
            for (suite in Suite.entries){
                emptyCards[x] = Card(face,suite)
                x++
            }
        }
        emptyCards.requireNoNulls()
    }()

    /**
     * Checks if the deck is valid by ensuring that there are exactly 52 cards
     * and that every face/suite is present.
     *
     * This is not particularly efficient (as this ends up O(n^2) because
     * we do n comparisons and each is O(n).
     */
    fun isValidDeck(): Boolean {
        if(cards.size != 52) return false
        for (face in Face.entries){
            for (suite in Suite.entries){
                if (Card(face,suite) !in cards) return false
            }
        }
        return true
    }

    /**
     * The toString function in Kotlin is particularly important
     * for debugging, since the IDE calls toString for visibility
     * in the debugger.  So this is one that just prints the whole
     * deck
     */
    override fun toString(): String {
        return cards.contentToString()
    }

    /**
     * This is an example of an overloaded operator in Kotlin,
     * allowing us to go deck[index] to get the card at that
     * point in the deck.
     */
    operator fun get(index: Int) : Card{
        return cards[index]
    }

    /**
     * And THIS function allows us to set the card value at
     * deck[index]
     */
    operator fun set(index: Int, c: Card){
        cards[index] = c
    }

    /**
     * This shuffles the deck of cards using SecureRandom.
     * SecureRandom is used to ensure that the shuffle really is
     * always good, as Java SecureRandom is the pRNG that should
     * always be used within Java environments
     */
    fun shuffle() {
        cards.shuffle(secureRNG)
    }

    /**
     * Our equality function for two decks. It
     * is only equal if two decks have the same order
     * of cards.  A few things to observe here:
     * the === is "Object equality", if the two
     * decks are the same object of course they are equal.
     *
     * If the two decks are of a different class than they are
     * clearly not equal.
     *
     * Finally, the compiler knows that after the check we can
     * treat other as a Deck object as well, so we do
     * a deep array equality that compares each element.
     */
    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (javaClass != other?.javaClass) return false

        other as Deck

        return cards.contentEquals(other.cards)
    }

    /**
     * This is what provides the ability to say "for(card in deck)" and
     * have it work: we just return the iterator for the underlying
     * array.
     */
    operator fun iterator(): Iterator<Card>{
        return cards.iterator()
    }

}