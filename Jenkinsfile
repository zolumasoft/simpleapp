pipeline {
  agent { docker { image 'python:3.9-slim' } }
  stages {
    stage('test') {
      steps {
        sh '''
          python -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt
          python test_simpleapp.py
        '''
      }
    }
  }
}
