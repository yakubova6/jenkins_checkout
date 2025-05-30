pipeline {
    agent any

    parameters {
        choice(name: 'ENV', choices: ['dev', 'prod'], description: 'Выберите окружение')
        string(name: 'FILE_NAME', defaultValue: '**', description: 'Файлы для отправки')
    }

    stages {
        stage('Info') {
            steps {
                echo "Deploying to ${params.ENV}"
            }
        }

        stage('Cleanup') {
            steps {
                deleteDir()
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
                                    sourceFiles: "${params.FILE_NAME}"
                                )
                            ]
                        )
                    ]
                )
            }
        }
    }
}