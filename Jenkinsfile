pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'python -m pytest test_app.py -v'
            }
        }

        stage('Build') {
            steps {
                echo 'Build successful! App is ready.'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check the logs.'
        }
    }
}