# Import the base Python image
FROM python:3

# Add Files to the Image
COPY "Battery App.py" ./
COPY "App Icon.ico" ./
COPY "App Icon.png" ./
COPY "Keyboard Shortcuts.txt" ./
COPY "requirements.txt" ./
COPY "./voices" "./voices"

# Run command to import packages
RUN pip install psutil
RUN pip install pyttsx3

# Run battery app python file
CMD [ "python","./Battery App.py" ]