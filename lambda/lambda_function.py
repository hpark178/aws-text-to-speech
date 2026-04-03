import os
import boto3
from urllib.parse import unquote_plus

s3 = boto3.client("s3")
polly = boto3.client("polly")

INPUT_BUCKET = os.environ["INPUT_BUCKET"]
OUTPUT_BUCKET = os.environ["OUTPUT_BUCKET"]
VOICE_ID = os.environ.get("VOICE_ID", "Joanna")

MAX_CHARS = 2800  # safe chunk size under Polly limits


def split_text(text: str, max_chars: int = MAX_CHARS):
    text = text.strip()
    chunks = []
    while len(text) > max_chars:
        cut = text.rfind(" ", 0, max_chars)
        if cut == -1:
            cut = max_chars
        chunks.append(text[:cut].strip())
        text = text[cut:].strip()
    if text:
        chunks.append(text)
    return chunks


def lambda_handler(event, context):
    # S3 event
    record = event["Records"][0]
    bucket = record["s3"]["bucket"]["name"]
    key = unquote_plus(record["s3"]["object"]["key"])

    # Only process .txt
    if not key.lower().endswith(".txt"):
        return {"ignored": key}

    # Read text from S3 (use env bucket, but fall back to event bucket)
    src_bucket = INPUT_BUCKET or bucket
    obj = s3.get_object(Bucket=src_bucket, Key=key)
    text = obj["Body"].read().decode("utf-8", errors="replace")

    parts = split_text(text)
    base_name = key.split("/")[-1].rsplit(".", 1)[0]

    output_keys = []

    # Amazon Polly datapipeline 
    for i, part in enumerate(parts, start=1):
        resp = polly.synthesize_speech(
            Text=part,
            OutputFormat="mp3",
            VoiceId=VOICE_ID,
            Engine="standard"
        )
        audio_bytes = resp["AudioStream"].read()

        out_key = f"audio/{base_name}_part{i:03d}.mp3"
        s3.put_object(
            Bucket=OUTPUT_BUCKET,
            Key=out_key,
            Body=audio_bytes,
            ContentType="audio/mpeg"
        )
        output_keys.append(out_key)

    return {"ok": True, "input_key": key, "output_files": output_keys}
