# AWS Serverless Text-to-Speech Pipeline

This project implements a fully serverless text-to-speech pipeline using AWS services. It allows you to upload a text from a book, article, and/or any website and transform that into an mp3 file where then you are able to listen to as well as change the voice appropriately. 

## Services Used
- Amazon S3 – input/output storage
- AWS Lambda – event-driven processing
- Amazon Polly – text-to-speech synthesis
- IAM – secure permissions
- CloudWatch – logging and monitoring

## How It Works
1. A .txt file is uploaded to an S3 input bucket
2. The upload triggers a Lambda function
3. Lambda reads and chunks the text
4. Amazon Polly converts each chunk into speech
5. Audio files are saved to an output S3 bucket

## Key Features
- Event-driven serverless architecture
- Automatic chunking to handle long articles (may need to increase time/space based on the size of file) 
- IAM least-privilege security
- Scales without managing servers

## Example Use Cases
- Article narration
- Audiobook generation
- Accessibility tools
- Voice-enabled content pipelines
