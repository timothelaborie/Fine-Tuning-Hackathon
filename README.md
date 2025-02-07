<!-- PROJECT TITLE -->
  <h1 align="center">Lec to Learn</h1>
 <h2 2 align="center">
    Lectures Simplified, Learning Amplified
    <br />
    </h2>

## Application Description

Lec to Learn is a tool to generate learning objectives given the text of a lecture.
- I downloaded all of the textbooks from opentextbc
- I used regex and bs4 to extract pairs of lectures and learning objectives
- I fine-tuned the [phi-1.5 model](https://huggingface.co/microsoft/phi-1_5) on the dataset using a custom prompt
- [Code to download textbooks](https://github.com/timothelaborie/Fine-Tuning-Hackathon/blob/main/download.ipynb)
- [Code to process textbooks](https://github.com/timothelaborie/Fine-Tuning-Hackathon/blob/main/process_learning_objectives.ipynb)
- [Code to train the model](https://github.com/timothelaborie/Fine-Tuning-Hackathon/blob/main/main.ipynb)

## Demo App URL:
https://timothelaborie.github.io/Fine-Tuning-Hackathon/

Note: Due to the very high cost of hosting a custom model, the demo has been changed to use the GPT-3.5 API instead

## Video Demo

View the [demo video](https://storage.googleapis.com/lablab-video-submissions/clm99g3av0000356wwlv2honr/raw/submission-video-x-clm99g3av0000356wwlv2honr-clmjei66v001i356rz9djvyu6_aa1k41n6k.mp4)

## Cover
![y1](https://github.com/faranbutt/Fine-Tuning-Hackathon/blob/main/cover.png)

## Technology Stack

| Technology       | Description                                   |
| ---------------- | --------------------------------------------- |
| Phi-1.5     |   Fine-tuned model that generates the objectives                           |
| Vercel functions       |   Backend                              |

## How to use the app

**Step #1** - Clone the project

Copy-paste your lectures in the input, click the button, wait 20 seconds and you will see the generated learning objectives`

## Collaborators

| Name            | Link                                   | Contribution                                   |
| --------------- | -------------------------------------- |----- |
| Timothé Laborie  | https://www.linkedin.com/in/timothe-laborie/ | Full stack coding and deployment |
| Faran Taimoor Butt | https://www.linkedin.com/in/faranbutt/ | CSS and Cover image |
| Homan M | https://www.linkedin.com/in/homan-mirgolbabaee/ | Presentation slides |
| Dhairya Shah | https://www.linkedin.com/in/dhairya-shah/ | Presentation slides |


## Hackathon Link

Hackathon [Submission](https://lablab.ai/event/fine-tuning-24-hours-challenge/finetuners/lec2learn-finetuning-ai-models)

## License

[![GitLicense](https://img.shields.io/badge/License-MIT-lime.svg)](https://github.com/sandramsc/CultiVate/blob/master/LICENSE.md)



