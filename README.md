# CI/CD Scripts (ci_cd_scripts)
## CI/CD scripts for FE & BE apps to use with Bitbucket, GitHub, AWS CodeBuild, AWS Pipelines, AWS Elastic Beanstalk, Python Lambda etc.

### AWS Elastic Beanstalk Extensions
Path: laravel_backend/aws_elastic_beanstalk/.ebextensions

### buildspec.yml for AWS CodeBuild projects (Deployment with AWS Pipelines) 
Path: laravel_backend/buildspec.yml

### .gitlab-ci.yml for Nest.js(Node.js) + Mongoose application with GitLab CI/CD
Path: node_backend/gitlab/.gitlab-ci.yml

### bitbucket-pipelines.yml file for React.js application with Bitbucket CI/CD 
Path: reactjs_frontend/bitbucket/bitbucket-pipelines.yml

### buildspec.yml file for React.js application with AWS CodeBuild projects (Deployment with AWS Pipelines)  
Path: reactjs_frontend/aws/buildspec.yml

### Python Lambda function to find and copy AWS artifacts automatically when deploying - triggers on S3 bucket get files from AWS Pipeline
File: copy_artifacts_from_one_bucket_to_multiple.py