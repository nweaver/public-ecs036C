package edu.ucdavis.cs.ecs036c


class Matrix<T>(val y : Int,val x : Int) {
    @Suppress("UNCHECKED_CAST")
    val storage : Array<T?> = arrayOfNulls<Any?>(x * y) as Array<T?>

    class MatrixSlice<T>(val row: Int, val parent: Matrix<T>) {
        operator fun get(index: Int): T? = parent.storage[parent.x * row + index]


        operator fun set(index: Int, value: T) {
            parent.storage[parent.x * row + index] = value
        }

        operator fun iterator() = getSequence().iterator()

        fun getSequence() = sequence<T?> {
            for (j in 0..<parent.x) {
                yield(get(j))
            }
        }


        override fun toString(): String {
            return getSequence().joinToString(prefix = "[", postfix = "]", separator = ", ", limit = 100) {
                it.toString()
            }
        }

    }
    operator fun get(index: Int) = MatrixSlice(index, this)

    operator fun iterator() = sequence {
        for (i in 0..<y) yield(get(i))
    }.iterator()

    override fun toString(): String {
        return this.iterator().asSequence().joinToString(prefix = "[", postfix = "]", separator = ",\n", limit=100) {
            it.toString()
        }
    }

}

fun <T>makeMatrixOf(vararg data: Array<T>) : Matrix<T> {
    val ySize = data.size
    val xSize = data[0].size
    val retval = Matrix<T>(ySize, xSize)
    for(j in data.indices){
        if(data[j].size != xSize) throw Exception ("All entries must be the same length")
        for(i in data[j].indices){
            retval[j][i] = data[j][i]
        }
    }
    return retval

}

class MatrixGraph(val size : Int){
    val matrix = Matrix<Double>(size, size)

    override fun toString(): String {
        return "Graph: $matrix"
    }

    fun calculateShortestPaths(): Matrix<Double> {
        val retval = Matrix<Double>(size, size)
        for (i in 0..<size) {
            for (j in 0..< size) {
                retval[i][j] = matrix[i][j]!!
            }
        }
        for(k in 0..<size){
            for(i in 0..<size){
                for(j in 0..<size){
                    val new = retval[i][k]!! + retval[k][j]!!
                    val old = retval[i][j]!!
                    if(new < old) {
                        retval[i][j] = new
                    }
                }
            }
        }
        return retval
    }
}

fun makeMatrixGraphOf(vararg data: Array<Double>) : MatrixGraph {
    val retval = MatrixGraph(data.size)
    for(i in data.indices) {
        if (data[i].size != data.size) throw Error("Wrong size")
        for(j in data[i].indices) retval.matrix[i][j] = data[i][j]
    }
    return retval
}