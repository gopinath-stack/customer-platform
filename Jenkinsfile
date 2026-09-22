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

    stage('Deploy DEV') {
        steps {
            bat 'docker compose up -d customer-db-dev customer-app-dev'
        }
    }
}