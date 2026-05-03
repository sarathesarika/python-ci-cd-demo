pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                bat 'pip install pytest playwright'
                bat 'python -m playwright install'
            }
        }
        stage('Test') {
            steps {
                bat 'pytest test_firstprogram.py -v'
            }
        }
    }
    post {
        success { echo 'All tests passed!' }
        failure { echo 'Tests failed!' }
    }
}