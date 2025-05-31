pipeline {
    agent any

    parameters {
        choice(name: 'ENV', choices: ['dev', 'prod'], description: 'Выберите окружение')
    }

    stages {
        stage('Info') {
            steps {
                echo "Deploying to ${params.ENV}"
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Send over SSH') {
            steps {
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'Prod',
                            transfers: [
                                sshTransfer(
                                    sourceFiles: '**',
                                    removePrefix: '',
                                    remoteDirectory: '/home/proger/jenkins_checkout'
                                )
                            ]
                        )
                    ]
                )
            }
        }

        stage('Cleanup') {
            steps {
                deleteDir()
            }
        }
    }
}