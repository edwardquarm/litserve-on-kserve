# litserve-on-kserve
A repo to showcase serving models using LitServe on KServe

## Serving LitServe on KServe

Follow these steps to serve a model using LitServe on KServe:

1. **Prepare the Server Code**:
   Ensure your server code (e.g., `server.py`) is ready and properly configured to serve your model.

2. **Generate a Dockerfile**:
   Use the `litserve dockerize` command to generate a Dockerfile for the server:
   ```bash
   litserve dockerize server.py
   ```
   Follow the CLI prompts to select an appropriate base image.

3. **Build the Docker Image**:
   Build the Docker image using Podman:
   ```bash
   podman build -t quay.io/<your-username>/litserve-server .
   ```

4. **Push the Image to Quay**:
   Log in to Quay and push the image:
   ```bash
   podman login quay.io
   podman push quay.io/<your-username>/litserve-server
   ```

5. **Deploy on KServe**:
   Configure KServe to use the image from Quay. Refer to the [KServe documentation](https://kserve.github.io/website/) for deployment instructions.

   ``kubectl apply -f deployment/litserve.yaml``

## Running Locally

To run the server locally, follow these steps:

1. **Install Dependencies**:
   Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Server**:
   Run the server script:
   ```bash
   python server.py
   ```

3. **Test the Server**:
   Use the provided `client.py` script to send requests to the server:
   ```bash
   python client.py
   ```
