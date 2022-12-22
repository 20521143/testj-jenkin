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
                    sh 'python manage.py test'
                }
        }
        
    }
    post
    {
        always
        {
           mail bcc: '', body: 'BUILD AND TEST SUCCESS', cc: '20521081@gm.uit.edu.vn,nguyenthanhcong012002@gmail.com', from: '', replyTo: '', subject: 'Build notifacation', to: '20521143@gm.uit.edu.vn'
        }
    }
}
