# @title Generate | Output generated inside "AICoverGen\song_output\random_number"
# @markdown Main Option | You also can input audio path inside "SONG_INPUT"
SONG_INPUT = "https://ai-music-demo.s3.ap-south-1.amazonaws.com/Tum+Itna+Jo+-+Papon+_+MTV+Unplugged.mp3" # @param {type:"string"}
RVC_DIRNAME = "Modi" # @param {type:"string"}
PITCH_CHANGE = 0 # @param {type:"integer"}
PITCH_CHANGE_ALL = 0 # @param {type:"integer"}
# @markdown Voice Conversion Options
INDEX_RATE = 0.5 # @param {type:"number"}
FILTER_RADIUS = 3 # @param {type:"integer"}
PITCH_DETECTION_ALGO = "rmvpe" # @param ["rmvpe", "mangio-crepe"]
CREPE_HOP_LENGTH = 128 # @param {type:"integer"}
PROTECT = 0.33 # @param {type:"number"}
REMIX_MIX_RATE = 0.25  # @param {type:"number"}
# @markdown Audio Mixing Options
MAIN_VOL = 0 # @param {type:"integer"}
BACKUP_VOL = 0 # @param {type:"integer"}
INST_VOL = 0 # @param {type:"integer"}
# @markdown Reverb Control
REVERB_SIZE = 0.15 # @param {type:"number"}
REVERB_WETNESS = 0.2 # @param {type:"number"}
REVERB_DRYNESS = 0.8 # @param {type:"number"}
REVERB_DAMPING = 0.7 # @param {type:"number"}
# @markdown Output Format
OUTPUT_FORMAT = "mp3" # @param ["mp3", "wav"]

import subprocess
# import runpod 
def handler(job):
   
    # if (not job):
    #     return {"error":"Something wrong in the input"}
    # if not job["input"]:
    #     return {"error":"Not getting input"}
    # if not job["input"]["song"]:
    #     return {"error":"Invalid song url input"}
    # if not job["policy"]:
    #     return {"error":"Without policy, execution not allowed"}
    # if not job["policy"]["executionTimeout"]:
    #     return {"error":"Specify the Execution Timeout"}
    # if not job["policy"]["ttl"]:
    #     return {"error":"Specify the Time-to-Live"}
    # if job["policy"]["executionTimeout"]>120000:
    #     return {"error":"Execution Timeout should be under 120000"} 
    # if job["policy"]["ttl"]>60000:
    #     return {"error":"Time-to-Live should be under 60000"}
    
    
    command = [
        "python",
        "src/main.py",
        "-i", SONG_INPUT,
        "-dir", RVC_DIRNAME,
        "-p", str(PITCH_CHANGE),
        "-k",
        "-ir", str(INDEX_RATE),
        "-fr", str(FILTER_RADIUS),
        "-rms", str(REMIX_MIX_RATE),
        "-palgo", PITCH_DETECTION_ALGO,
        "-hop", str(CREPE_HOP_LENGTH),
        "-pro", str(PROTECT),
        "-mv", str(MAIN_VOL),
        "-bv", str(BACKUP_VOL),
        "-iv", str(INST_VOL),
        "-pall", str(PITCH_CHANGE_ALL),
        "-rsize", str(REVERB_SIZE),
        "-rwet", str(REVERB_WETNESS),
        "-rdry", str(REVERB_DRYNESS),
        "-rdamp", str(REVERB_DAMPING),
        "-oformat", OUTPUT_FORMAT
    ]

    # Open a subprocess and capture its output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    # Capture all lines from stdout
    # output_lines = []
    # for line in process.stdout:
    #     output_lines.append(line)

    # # Get the last line from the captured output
    # last_line = output_lines[-1] if output_lines else None

   
    

    # Print the output in real-time
    for line in process.stdout:
        print(line, end='')

    # Wait for the process to finish
    process.wait()
    # return {"url":last_line}

# runpod.serverless.start({
#         "handler": handler,
#         "concurrency_modifier":5
#     })