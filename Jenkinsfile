pipeline {
  agent { docker { image 'python:3.9-slim' } }
  stages {
    stage('build') {
      steps {
        sh '''
          python -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt'
        '''
      }
    }
    stage('test') {
      steps {
        sh 'python test_simpleapp.py'
      }   
    }
  }
}
