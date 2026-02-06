# AWS Serverless Text-to-Speech Pipeline

This project implements a fully serverless text-to-speech pipeline using AWS services.  
Uploaded text articles are automatically converted into narrated audio files.

## Architecture
S3 (Input) into AWS Lambda into Amazon Polly and then back to S3 (Output)

## Services Used
- Amazon S3 – input/output storage
- AWS Lambda – event-driven processing
- Amazon Polly – text-to-speech synthesis
- IAM – secure permissions
- CloudWatch – logging and monitoring

## How It Works
1. A `.txt` file is uploaded to an S3 input bucket
2. The upload triggers a Lambda function
3. Lambda reads and chunks the text
4. Amazon Polly converts each chunk into speech
5. Audio files are saved to an output S3 bucket

## Key Features
- Event-driven serverless architecture
- Automatic chunking to handle long articles
- IAM least-privilege security
- Scales without managing servers

## Example Use Cases
- Article narration
- Audiobook generation
- Accessibility tools
- Voice-enabled content pipelines

## Deployment Notes
- Lambda timeout increased to support long articles
- Supports large inputs via text chunking
- Polly Standard voice (configurable)

## Author
Hoyoung Park
