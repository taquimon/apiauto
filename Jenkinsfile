pipeline {
    agent any
    environment {
        TOKEN = '9463fd6e63c3ac3e06372045795ef48264968d2c'
    }
    stages {
        stage('version') {            
            steps{ 
               sh 'python3 --version'
            }
        }    
        stage('Install requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python3 -m nose2'
            }
        }
    }
}
