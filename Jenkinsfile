pipeline {
    agent any

    tools {
        python "Python3"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/zuhaibmushtaq/my_portfolio_automation_selenium'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt || pip install selenium pytest pytest-html pyyaml'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --html=reports/report.html --self-contained-html -v'
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report'
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**/*.html', fingerprint: true
        }
    }
}
