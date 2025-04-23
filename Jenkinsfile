pipeline {
    agent any

    environment {
        GEMINI_API_KEY = credentials('gemini-api-key') // Create this secret in Jenkins!
    }

    stages {
        stage('Pull from GitHub') {
            steps {
                git 'https://github.com/I-mgopal/Pratyush_Chatbot'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t chatbot_project .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker stop chatbot_container || true
                docker rm chatbot_container || true
                docker run -d --name chatbot_container -p 5000:5000 \
                  -e GEMINI_API_KEY=$GEMINI_API_KEY chatbot_project
                '''
            }
        }
    }
}
