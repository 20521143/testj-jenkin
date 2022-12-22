pipeline {
    agent any
    stages {
         stage('Clone')
        {
            steps
            {
              git branch: 'main', url: 'https://github.com/20521143/testj-jenkin.git'
            }
        }
        stage('Test') {
                steps {
                    sh 'python app/manage.py test'
                }
        }
        
    }
}
