import os
import subprocess


def batch_mux_mp4_srt(directory):
    # Change to the target directory
    os.chdir(directory)

    # Get all mp4 files in the directory
    files = [f for f in os.listdir() if f.endswith('.mp4')]

    for video in files:
        base_name = os.path.splitext(video)[0]
        srt_file = f"{base_name}.srt"
        output_mkv = f"{base_name}.mkv"

        # Check if matching subtitle file exists
        if os.path.exists(srt_file):
            print(f"Muxing: {video} + {srt_file} -> {output_mkv}")

            # FFmpeg command to mux files losslessly
            # -c copy: copies video/audio without re-encoding
            # -c:s srt: ensures the subtitle format is handled correctly
            cmd = [
                'ffmpeg', '-i', video, '-i', srt_file,
                '-c', 'copy', '-c:s', 'srt', '-map', '0', '-map', '1', output_mkv
            ]

            try:
                subprocess.run(cmd, check=True)
                print(f"Successfully created {output_mkv}")
            except subprocess.CalledProcessError as e:
                print(f"Error processing {video}: {e}")
        else:
            print(f"No subtitle found for {video}, skipping...")

if __name__ == "__main__":
    # Update this path to your folder containing the files
    #target_dir = r'H:\TV Shows\fist-of-the-north-star-1984\Fist of the North Star (1984)\Season 1'
    target_dir = input("Input target directory: ")
    batch_mux_mp4_srt(target_dir)
