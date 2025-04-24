pipeline {
    agent any

    stages {
        stage('Pull from GitHub') {
            steps {
                git 'https://github.com/I-mgopal/Pratyush_Chatbot'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t chatbot_project .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat '''
                docker tag chatbot_project gopal89/pratyush_chatbot
                docker login -u gopal89 -p %DOCKER_HUB_PASSWORD%
                docker push gopal89/pratyush_chatbot
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                bat '''
                docker stop chatbot_container || true
                docker rm chatbot_container || true
                docker run -d --name chatbot_container -p 5000:5000 \
                  -e GEMINI_API_KEY=$GEMINI_API_KEY chatbot_project
                '''
            }
        }
    }
}
