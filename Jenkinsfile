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

        stage('Run Docker Container') {
            steps {
                bat '''
                docker stop chatbot_container || true
                docker rm chatbot_container || true
                docker run -d --name chatbot_container -p 5000:5000 chatbot_project
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat '''
                    docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                    docker tag chatbot_project gopal89/pratyush_chatbot
                    docker push gopal89/pratyush_chatbot
                    '''
                }
            }
        }
    }
}
