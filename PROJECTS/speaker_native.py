"""Text-to-speech using Windows native API (System.Speech).

More reliable than pyttsx3 on Windows.

Usage:
  python speaker_native.py --text "Hello world"
  python speaker_native.py --list-voices
  python speaker_native.py  (interactive mode)
"""
import argparse
import sys
import subprocess
import tempfile
import os


def list_voices():
    """List available voices using PowerShell."""
    ps_script = r"""
[System.Reflection.Assembly]::LoadWithPartialName("System.speech") | Out-Null
$synthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
$voices = $synthesizer.GetInstalledVoices()
$i = 0
foreach ($voice in $voices) {
    Write-Host "$i : $($voice.VoiceInfo.Name)"
    $i++
}
"""
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_script],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr, file=sys.stderr)
    except Exception as e:
        print(f"Error listing voices: {e}", file=sys.stderr)


def speak_text(text: str, voice_index: int = None, rate: int = None, verbose: bool = False):
    """Speak text using Windows native API."""
    if verbose:
        print(f"Speaking: '{text}'")
    
    # Build PowerShell script
    ps_script = f"""
[System.Reflection.Assembly]::LoadWithPartialName("System.speech") | Out-Null
$synthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
"""
    
    if voice_index is not None:
        ps_script += f"""
$voices = $synthesizer.GetInstalledVoices()
if ($voices.Count -gt {voice_index}) {{
    $synthesizer.SelectVoice($voices[{voice_index}].VoiceInfo.Name)
}}
"""
    
    if rate is not None:
        ps_script += f"$synthesizer.Rate = {rate}\n"
    
    # Escape PowerShell string properly
    escaped_text = text.replace("'", "''")
    ps_script += f"$synthesizer.Speak('{escaped_text}')\n"
    
    if verbose:
        print(f"Rate: {rate if rate else 'default'}")
    
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_script],
            capture_output=True,
            text=True,
            timeout=30
        )
        if verbose:
            print("Audio played successfully")
        if result.stderr:
            print("Warning:", result.stderr, file=sys.stderr)
    except subprocess.TimeoutExpired:
        print("Error: Speech timeout", file=sys.stderr)
    except Exception as e:
        print(f"Error speaking text: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description='Text-to-speech using Windows native API')
    parser.add_argument('-l', '--list-voices', action='store_true', help='List available voices')
    parser.add_argument('-v', '--voice', type=int, help='Voice index (from --list-voices)')
    parser.add_argument('-r', '--rate', type=int, help='Speech rate (-10 to 10, default 0)')
    parser.add_argument('-t', '--text', type=str, help='Text to speak (non-interactive)')
    parser.add_argument('--verbose', action='store_true', help='Show debug messages')
    args = parser.parse_args()
    
    if args.list_voices:
        list_voices()
        return
    
    if args.text:
        speak_text(args.text, voice_index=args.voice, rate=args.rate, verbose=args.verbose)
        return
    
    # Interactive mode
    try:
        if args.verbose:
            print("Entering interactive mode. Type 'exit' to quit.")
        while True:
            user_input = input("Enter text (or 'exit' to quit): ")
            if user_input.strip().lower() in ("exit", "quit"):
                speak_text("Goodbye", voice_index=args.voice, rate=args.rate, verbose=args.verbose)
                break
            if user_input.strip():
                speak_text(user_input, voice_index=args.voice, rate=args.rate, verbose=args.verbose)
    except (KeyboardInterrupt, EOFError):
        print()
        speak_text("Goodbye", voice_index=args.voice, rate=args.rate, verbose=args.verbose)


if __name__ == '__main__':
    main()
