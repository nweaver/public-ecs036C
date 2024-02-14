package edu.ucdavis.cs.ecs036c

import org.junit.jupiter.api.Test

fun testTree(): BinaryTreeNode<String> =
    BinaryTreeNode(
        "A",
        BinaryTreeNode(
            "B",
            BinaryTreeNode(
                "D", null,
                BinaryTreeNode("H", null, null)
            ),
            BinaryTreeNode(
                "E",
                BinaryTreeNode("I", null, null),
                BinaryTreeNode(
                    "J", null,
                    BinaryTreeNode("K", null, null)
                )
            )
        ),
        BinaryTreeNode(
            "C",
            BinaryTreeNode("F", null, null),
            BinaryTreeNode("G", null, null)
        )
    )


class BinaryTreeNodeTest {
    @Test
    fun testTreeCode(){
        val goodTree = testTree()
        assert(goodTree.toString() == "(((D (H)) B ((I) E (J (K)))) A ((F) C (G)))")
        assert(goodTree.wellFormed())
        val badTree = testTree()
        badTree.left?.left = badTree
        assert(!badTree.wellFormed())
        println(badTree.toString())

        println(goodTree.inOrderTraversal().joinToString { it })
        assert(goodTree.inOrderTraversal().joinToString { it } == "D, H, B, I, E, J, K, A, F, C, G")
        println(goodTree.preOrderTraversal().joinToString { it })
        assert(goodTree.preOrderTraversal().joinToString { it } == "A, B, D, H, E, I, J, K, C, F, G")
        println(goodTree.postOrderTraversal().joinToString { it })
        assert(goodTree.postOrderTraversal().joinToString { it } == "H, D, I, K, J, E, B, F, G, C, A")
        println(goodTree.levelOrderTraversal().joinToString { it })
        assert(goodTree.levelOrderTraversal().joinToString { it } == "A, B, C, D, E, F, G, H, I, J, K")

        for(x in 0..<100){
            for(y in 0..<100){
                val testData : Array<Int?> = arrayOfNulls(x)
                for(z in 0..<x){
                    testData[z] = z
                }
                @Suppress("UNCHECKED_CAST")
                testData as Array<Int>
                testData.shuffle()
                val testTree = toOrderedTree(*testData)
                var i = 0
                for (data in testTree){
                    assert(i == data)
                    assert(i in testTree)
                    assert((i + x) !in testTree)
                    i++
                }
                testData.shuffle()
                for (data in testData){
                    assert(data in testTree)
                    testTree.remove(data)
                    assert(data !in testTree)
                    var a = -1
                    for (b in testTree){
                        assert(a < b)
                        a = b
                    }
                }
            }
        }

    }

}