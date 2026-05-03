pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                sh 'pip install pytest'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest test_login.py -v'
            }
        }
    }
    post {
        success { echo 'All tests passed!' }
        failure { echo 'Tests failed!' }
    }
}