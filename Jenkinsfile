pipeline {
    agent any
    parameters {
        choice(name: 'ENV', choices: ['dev', 'prod'], description: 'Выберите окружение')
    }
    stages {
        stage('Deploy') {
            steps {
                echo "Deploying to ${params.ENV}"
                sh 'rm -rf *'  
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'Prod',
                            transfers: [
                                sshTransfer(sourceFiles: '**/*', remoteDirectory: '/app')
                            ]
                        )
                    ]
                )
            }
        }
    }
}