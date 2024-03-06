import edu.ucdavis.cs.ecs036c.makeMatrixGraphOf
import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

class MatrixTest {

    @Test
    fun makeMatrixOf() {
        val data = arrayOf(arrayOf(1, 2, 3), arrayOf(4, 5, 6))
        val foo = edu.ucdavis.cs.ecs036c.makeMatrixOf<Int>(*data)
        println("$foo")
        foo[0][0] = 1
        for (a in foo) {
            for (b in a) {
                println("$b")
            }
        }

        val graphData = arrayOf(arrayOf(0.0, 5.0, Double.POSITIVE_INFINITY, 10.0),
            arrayOf(Double.POSITIVE_INFINITY, 0.0, 3.0, Double.POSITIVE_INFINITY),
            arrayOf(Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY, 0.0, 1.0),
            arrayOf(Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY, 0.0))
        val graph = makeMatrixGraphOf(*graphData)
        println("$graph")
        println("${graph.calculateShortestPaths()}")
    }
}