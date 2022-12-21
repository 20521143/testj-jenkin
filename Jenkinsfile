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
         post
        {
            always
            {
                mail bcc: '', body: '''Congratulation...
                BUILD SUCCESSFULLY!''', cc: '', from: '', replyTo: '', subject: 'Build Notification', to: 'nguyenthanhcong012002@gmail.com'
            }
        }
    }
}
