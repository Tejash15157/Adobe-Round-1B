# Adobe - Connecting the Dots Challenge (Round 1B)

## How to Run

### Prepare persona.json
```json
{
  "persona": "Software Engineer - Backend Development",
  "job": "Python developer with experience in web frameworks like Django or Flask, database management, API development, and cloud deployment"
}
```

### Build Docker Image
```
docker build --platform linux/amd64 -t adobe-round1b .
```

### Run the Solution
```
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none adobe-round1b
```

### Output
Top 10 most relevant sections will be written to `output/output.json`.
