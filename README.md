# Body Mass Index

Body Mass Index is a simple calculation using a person’s height and weight. The
formula is BMI = kg/m2 where kg is a person’s weight in kilograms and m2 is their height in meters squared. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9.

## Details

This is complete containerised code with CI including Security. The rest API is publicly available on my Domain over HTTPS. As per the instruction given:

Weight parameter is in cm (Which is actually height)

Height parameter is in Kg (Which is actually Weight)
 

```
https://akashmagrawal.com/?weight=167&height=70
```

## CI/CD
CI including all security is added in github action. Please check the details in file `.github/workflows/ci-security.yml`

## Unit Test Case

```python
1] Weight or Height cannott be zero
2] Weight or Height should be positive number only
3] Weight or Height cannot include any thing apart from number(validation of input)
```

### Security Incorporated in CI
This repo and hosted Url incorporate multiple security checks

```
1] Code Scanning [SAST]
2] Git Secret Scanning
3] Docker Image Vulnerability check 
4] Hosted DNS is on HTTPS [https://akashmagrawal.com/?weight=167&height=70]
5] Hosted DNS has WAF enabled
6] Hosted DNS also have RateLimiting [10 request from same IP within 1 minute]
```

## Sample Output

`https://akashmagrawal.com/?weight=167&height=70`
```
{
  "bmi": "25.10", 
  "label": "overweight"
}
```

`https://akashmagrawal.com/?weight=167&height=0`
```
{
  "Error Message": "Invalid Input: weight/height should be more than 0 and positive"
}
```

`https://akashmagrawal.com/?weight=167&height=a`
```
{
  "Error Message": "Invalid Input: Only Numbers are allowed"
}
```

## DockerImage Url
```
docker pull akashmagrawal1/bodymassindex:latest
```

## How to run the image
```
docker run -d --restart unless-stopped -p 5001:5000 akashmagrawal1/bodymassindex
```
