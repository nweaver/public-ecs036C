plugins {
    kotlin("jvm") version "1.9.21"
}

group = "edu.ucdavis.cs.ecs036c"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.2")

//    testImplementation(kotlin("test"))
//    testImplementation("org.jetbrains.kotlin:kotlin-test")
}

tasks.test {
    useJUnitPlatform()
}
kotlin {
    jvmToolchain(21)
}