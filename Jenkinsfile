pipeline {
  agent none
  stages {
    stage('build') {
      agent any
      steps {
        git(url: 'https://github.com/JiansuanTech/DAIBench.git', poll: true, branch: 'jenkins-test')
      }
    }

    stage('test') {
      agent any
      steps {
        sh 'cd hardware/cpu-bandwidth && sh run.sh'
      }
    }

  }
}