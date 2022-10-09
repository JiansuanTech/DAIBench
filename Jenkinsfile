pipeline {
  agent none
  stages {
    stage('Build') {
      agent any
      steps {
        git(url: 'https://github.com/JiansuanTech/DAIBench.git', poll: true, branch: 'jenkins-test')
      }
    }

    stage('Test') {
      agent any
      steps {
        sh 'cd hardware/cpu-bandwidth && sh run.sh'
        archiveArtifacts 'hardware/cpu-bandwidth/mlc.log'
      }
    }

  }
}