# Heavily modified from the script created by Aaron Cheung under MIT License
# Original repo: https://github.com/AaronCheung430/txt-TO-srt

import sys, os   # for folders and os info and stuff
import argparse  # for command line arguments
import re        # for regex

from timecode import Timecode

def read_file(input_file, verbose=False):
    """
    Reads the input file and returns the lines
    """

    # Open the input file for reading
    md_file = open(input_file,"r")
    # read in lines of the slides.md file
    md_lines = md_file.readlines()

    # Optionally print first few lines
    if verbose:
        print("Here's what the input file says: \n",md_lines[:6])
    
    # Close the file
    md_file.close()

    return md_lines

def collect_caps_VO(md_lines, verbose=False):
    """
    Go through the lines of the slides.md and collect (+return) caption and voiceover content.
    """

    # Lists of collected caption and voiceover content
    caps = []
    VO = []

    # By default no content is taken
    copy_captions = False
    copy_speech = False

    # Go through all lines in slides.md
    for line in md_lines:
        # When collecting caps is off see if it should be on
        if not copy_captions:
            if line == ":::info (speech)\n":
                if verbose:
                    print("Recording captions")
                copy_captions = True
        # When copying caps is on see if it should be off
        elif line == ":::\n":
            copy_captions = False
        # When copying caps is on copy caps
        else:
            caps.append(line)
            #caps.append("\n")
            if verbose:
                print("To caps:",line)

        # Collect slide titles to VO
        if line.startswith('# '):
            if verbose:
                print("Title found:", line)
            # Remove leading space and add dot before the new line
            line = "{}.\n".format(line[1:-1])
            VO.append("\n")
            VO.append(line[1:])

        # When collecting VO is off see if it should be on
        if not copy_speech:
            if line == ":::info (speech)\n":
                if verbose:
                    print("Recording speech txt")
                copy_speech = True
        # When copying VO is on see if it should be off
        elif line == ":::\n":
            copy_speech = False
        # When copying VO is on copy VO
        else:
            VO.append(line)
            #VO.append("\n")
            if verbose:
                print("To speech:",line)

    return caps, VO

def create_SRT(caps, verbose=False):
    """
    Go through captions content and generate SRT-format where the captions are between 6 seconds.
    Return lines of the SRT-file.
    """
    
    # Lines of SRT-file as a list
    srt = []

    # Generate timecodes
    tc = Timecode('30', '00:00:00.000')
    tc_step1 = Timecode('30', '00:00:05.000')
    tc_step2 = Timecode('30', '00:00:06.000')
    tc.set_fractional(True)
    tc_step1.set_fractional(True)
    tc_step2.set_fractional(True)

    # Number of caption lines for iteration
    caps_n = len(caps)

    # Go through the caption lines and insert SRT stuff
    for i in range(caps_n):
        # First in SRT is the line number
        srt_line1 = "{}\n".format(i+1)
        # caption ending timecode
        tc2 = tc + tc_step1
        tc2.set_fractional(True)
        # Second in SRT is the start and end times
        srt_line2 = "{} --> {}\n".format(tc,tc2)
        # Third in SRT is the actual text
        text = caps[i]
        # Advance timecode for next iteration
        tc = tc + tc_step2
        tc.set_fractional(True)

        # Add SRT content to the lines of SRT-file
        srt.append(srt_line1)
        srt.append(srt_line2)
        srt.append(text)
        srt.append("\n")
    
    return srt

def create_VOs(VO, verbose=False):
    """
    Go through voiceover content and generate a voiceover file.
    The details of the file depend on the operating system: MacOS includes own Text-to-Speech engine and thus has a spesific functions here.
    """
    # Copy VO to have another version for macOS
    VO_mac = VO.copy()

    # Lines of VO-file as list
    speech = []
    speech_mac = []

    
    # Go through voiceover lines for macOS
    for line in VO_mac:
        # Make word replacements for nicer pronounciation
        line = line.replace(" {.title}", "") 
        line = line.replace(" 1/2", "") 
        line = line.replace(" 2/2", "") 
        line = line.replace("Puhti", "Puyh.ti")
        line = line.replace("puhti", "puyh.ti")
        line = line.replace("Mahti", "Mah.ti")
        line = line.replace("mahti", "mah.ti")
        line = line.replace("Pouta", "Pawta")
        line = line.replace("pouta", "pawta")
        line = line.replace("Kaivos", "Kiavos")
        line = line.replace("kaivos", "kiavos")
        line = line.replace("rtools", "RTools")
        line = line.replace("rsync", "RSync")
        line = line.replace("rclone", "RClone")
        line = line.replace("bashrc", "bashRC")
        line = line.replace("NVMe", "NVME")
        line = line.replace("SBATCH", "SBatch")
        line = line.replace("sbatch", "SBatch")
        line = line.replace("squeue", "SQueue")
        line = line.replace("scontrol", "SControl")
        line = line.replace("scancel", "SCancel")
        line = line.replace(".sh", "dot SH")
        line = line.replace("-u", "dash U")
        line = line.replace("$USER", "dollar user")
        line = line.replace("JOBID", "jobID")
        line = line.replace("job ID", "jobID")

        line = line.replace("YOURCSCUSERNAME", "your CSC username")
        line = line.replace("MyCSC", "my CSC")

        # Add one second pause after each line
        speech_mac.append("[[slnc 1000]]")
        # Add text
        speech_mac.append(line)
        # Add new line
        speech_mac.append("\n")

    # Go through voiceover lines
    for line in VO:
        # Make word replacements for nicer pronounciation
        line = line.replace(" {.title}", "")
        line = line.replace(" 1/2", "") 
        line = line.replace(" 2/2", "") 
        line = line.replace("Puhti", "Pouhti")
        line = line.replace("puhti", "Pouhti")
        line = line.replace("Pouta", "Pauwta")
        line = line.replace("pouta", "Pauwta")
        #line = line.replace("Mahti", "Mah:ti") # for speechelo non-PRO voices
        line = line.replace("mahti", "Mahti")
        #line = line.replace("Kaivos", "Kai:voss") # for speechelo non-PRO voices
        line = line.replace("kaivos", "Kaivos")
        line = line.replace("rtools", "r-tools")
        line = line.replace("rclone", "r-clone")
        line = line.replace("rsync", "r-sync")
        line = line.replace("bashrc", "bash RC")
        line = line.replace("NVMe", "NVME")
        line = line.replace("SBATCH", "S-BATCH")
        line = line.replace("sbatch", "s-batch")
        line = line.replace("squeue", "S-Queue")
        line = line.replace("scontrol", "S-Control")
        line = line.replace("scancel", "S-Cancel")
        #line = line.replace(".sh", "dot SH")
        line = line.replace("-u", "dash U")
        line = re.sub('\.\\b', ' dot ', line)           # Replace .x with dot x
        #line = re.sub(' \-\\b', ' dash ', line)         # Replace -x with dash x ### Does not work with "CSC-accounts and -projects"
        line = re.sub(' \-\-\\b', ' dash dash ', line)  # Replace --x with dash dash x
        line = line.replace("$USER", "dollar user")
        line = line.replace("JOBID", "job ID")
        line = line.replace("YOURCSCUSERNAME", "your CSC username")
        #line = line.replace("MyCSC", "my CSC")

        # Add text
        speech.append(line)
        # Add new line
        #speech.append("\n")

    return speech, speech_mac


def main(argv, verbose=True):
    
    # Parser for arguments
    parseri = argparse.ArgumentParser(description='Generate voiceover and captions from slide.md file that includes tags.')
    # Add arguments
    parseri.add_argument('mdslide_path', metavar='path_to_input_md', type=str, help='Path to the slide.md')
    # parseri.add_argument('newfolder', metavar='newtargetfolder', type=bool, default=False, choices=['True','False'], required=False, help='Default: False. If True creates a new folder for output files. Use False if input file is in a new folder already.') # Did not get to work. Script always creates a new target folder.
    # parse args
    args=parseri.parse_args()

       
    # Get the path for slides.md
    input_file = args.mdslide_path
    input_filename = os.path.basename(input_file)
    input_path = os.path.dirname(input_file)
    # If path is not given in args, current folder is assumed
    if not input_path or input_path=='.':
        input_path = os.getcwd()

    # Stop here if input file does not exist
    if not os.path.exists(os.path.join(input_path,input_filename)):
        print("The input file does not exist. Check the input argument!!!")
        sys.exit()

    # A foldername for output files will include the original name without extension
    output_folder = "{0}_files".format(os.path.splitext(input_filename)[0])
    # Output folder path is the same as input path but creates a new folder inside
    output_path = os.path.join(input_path, output_folder)
    # Create a folder for output files if not exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Read input file sldes.md and output as lines
    md_lines = read_file(input_file, verbose=verbose)
    # Go through lines and collect captions and VO content
    captions, VOs = collect_caps_VO(md_lines, verbose=False)
    # Go through caption content and generate SRT lines
    srt_lines = create_SRT(captions, verbose=verbose)
    # Go through voiceover content and generate VO lines
    VO_lines, VO_lines_mac = create_VOs(VOs, verbose=verbose)

    # Parts of slides.md that goes to captions go to this file
    captions_filename = "{0}_captions.srt".format(os.path.splitext(input_filename)[0])
    # Parts of slides.md that goes to voiceover go to this file
    VOs_filename = "{0}_voiceover.txt".format(os.path.splitext(input_filename)[0])
    VOs_filename_mac = "{0}_voiceover_mac.txt".format(os.path.splitext(input_filename)[0])
    audio_filename = "{0}_voiceover.aiff".format(os.path.splitext(input_filename)[0])  # Used only in MacOS
    # Parts of slides.md that goes to transcribt go to this file
    transcribt_filename = "{0}_transcribt.txt".format(os.path.splitext(input_filename)[0])

    #print(input_file)  # Original argument. Useful when figuring out the input paths
    if verbose:
        print('Input file is', input_filename)
        print('Output path is', output_path)
        print('Output files are', captions_filename, "and", VOs_filename, "and", VOs_filename_mac, "and", transcribt_filename)
    
    
    # Create new SRT file and write down the SRT lines
    srt_file = open(os.path.join(output_path, captions_filename) , "w")
    srt_file.writelines(srt_lines) 
    srt_file.close()
    if verbose:
        print("New captions file created.")

    # Create new transcribt file and write down the VO lines
    transcribt_file = open(os.path.join(output_path, transcribt_filename) , "w")
    transcribt_file.writelines(VOs) 
    transcribt_file.close()
    if verbose:
        print("New transcribt text file created.")

    # Create new voiceover file and write down the VO lines
    VOs_file = open(os.path.join(output_path, VOs_filename) , "w")
    VOs_file.writelines(VO_lines) 
    VOs_file.close()
    if verbose:
        print("New voiceover text file created.")

    # Create new voiceover file and write down the VO lines
    VOs_file_mac = open(os.path.join(output_path, VOs_filename_mac) , "w")
    VOs_file_mac.writelines(VO_lines_mac) 
    VOs_file_mac.close()
    if verbose:
        print("New voiceover text file created for Mac reader.")

    
    # In mac should additionally call 'say' with Daniel and correct parameters
    if sys.platform == "darwin":
        os.system("say -f {0} -o {1} -r 44 -v Daniel".format(os.path.join(output_path, VOs_filename_mac),os.path.join(output_path, audio_filename)))
        print("New voiceover audio file created.")
    else:
        print("Find the {0} file and run in through a Text-to-Speech engine of your choice.".format(VOs_filename))

    print("Captions and VO extracted from {0}".format(input_filename))


if __name__ == "__main__":
    main(sys.argv, verbose=False)