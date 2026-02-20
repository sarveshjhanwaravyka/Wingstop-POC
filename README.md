# Java Maven App

A simple Java application built with Maven, including unit tests and Docker support.

## Prerequisites

- Java 17 or higher
- Maven 3.8 or higher
- Docker (optional, for containerized execution)

## Build and Run Locally

1.  **Build the project:**
    ```bash
    mvn clean package
    ```

2.  **Run the application:**
    ```bash
    java -jar target/java-maven-app-*.jar
    ```

3.  **Run tests:**
    ```bash
    mvn test
    ```

4.  **Run linting (Checkstyle):**
    ```bash
    mvn checkstyle:check
    ```

## Docker Support

1.  **Build the Docker image:**
    ```bash
    docker build -t java-maven-app .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run java-maven-app
    ```

## Project Structure

- `src/main/java`: Source code
- `src/test/java`: Unit tests
- `pom.xml`: Maven configuration
- `Dockerfile`: Multi-stage Docker build configuration
