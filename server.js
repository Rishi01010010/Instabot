const express = require('express');
const multer = require('multer');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const app = express();
const port = 3000;

const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

app.use(express.static('public'));

app.post('/upload', upload.single('photo'), (req, res) => {
    const tempDir = os.tmpdir();
    const tempFilePath = path.join(tempDir, req.file.originalname);

    // Write the file to a temporary location
    fs.writeFile(tempFilePath, req.file.buffer, (err) => {
        if (err) {
            console.error('Error writing file to temporary location:', err);
            return res.status(500).send('Failed to process the photo.');
        }

        // Spawn the Python script
        const pythonProcess = spawn('python', ['InstaBot.py', tempFilePath]);

        pythonProcess.stdout.on('data', (data) => {
            console.log(`stdout: ${ data }`);
        });

        pythonProcess.stderr.on('data', (data) => {
            console.error(`stderr: ${ data }`);
        });

        pythonProcess.on('close', (code) => {
            // Delete the temporary file after processing
            fs.unlink(tempFilePath, (err) => {
                if (err) {
                    console.error('Error deleting temporary file:', err);
                }
            });

            if (code === 0) {
                res.status(200).send('Photo posted successfully!');
            } else {
                res.status(500).send('Failed to post the photo.');
            }
        });
    });
});

app.listen(port, () => {
    console.log(`Server running at http:;//localhost:${port}`);
});