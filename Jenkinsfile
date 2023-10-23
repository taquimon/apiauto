pipeline {
    agent any
       
    stages {
        stage('version') {            
            steps{ 
               sh 'python3 --version'
            }
        }            
        stage('Run Python Script') {
            steps {
                withPythonEnv('python3') {
                     sh 'pip install -r requirements.txt'                
                     sh 'python3 -m nose2 --allure'
                }
            }
        }
        stage('reports') {
            steps {
            script {
                    allure([
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: 'allure-result']]
                    ])
            }
            }
        }
    }
}
