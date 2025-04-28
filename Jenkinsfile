pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "gopal89/chatbot"
    }
    stages {
        stage('Pull from GitHub') {
            steps {
                git branch: 'main', 
                url: 'https://github.com/I-mgopal/Chat_application',
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    bat '''
                    docker stop chatbot_container || true
                    docker rm chatbot_container || true
                    docker run -d --name chatbot_container -p 5000:80 ${DOCKER_IMAGE}:${BUILD_ID}
                    '''
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    script {
                        bat """
                        docker login -u ${env.DOCKER_USER} -p ${env.DOCKER_PASS}
                        docker tag ${env.DOCKER_IMAGE}:${env.BUILD_ID} ${env.DOCKER_IMAGE}:latest
                        docker push ${env.DOCKER_IMAGE}:latest
                        """
                    }
                }
            }
        }
    }
}
