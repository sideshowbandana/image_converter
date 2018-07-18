# ImageConverter

AWS Lambda project to convert svg to jpg. Uses apex for deployment and versioning.

## Deployment:

```
export AWS_PROFILE=YOUR_PROFILE
export AWS_REGION=us-east-1
apex deploy
```

## Test:

```
echo '{"image": "'$(cat sample_images/glyph.svg | openssl base64 | tr -d '\n')'"}'  | apex invoke -L to_jpg
```
