pipeline {
    agent any

    stages {
        stage('Start') {
            steps {
                echo 'Customer Platform Deployment'
            }
        }

        stage('Build Docker Image') {
        steps {
            bat 'docker build -t customer-platform:1.0 .'
        }
    }
}