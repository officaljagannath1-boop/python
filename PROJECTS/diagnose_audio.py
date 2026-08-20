"""Diagnostic tool to check Windows audio configuration."""
import subprocess
import sys


def check_audio_devices():
    """List all audio devices."""
    print("=" * 60)
    print("AUDIO DEVICES")
    print("=" * 60)
    
    ps_script = r"""
Get-PnpDevice -PresentationOrder | Where-Object {$_.Class -eq "MEDIA"}
"""
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_script],
            capture_output=True,
            text=True,
            timeout=10
        )
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except Exception as e:
        print(f"Error: {e}")


def check_default_audio():
    """Check default audio output device."""
    print("\n" + "=" * 60)
    print("DEFAULT AUDIO DEVICE")
    print("=" * 60)
    
    ps_script = r"""
$device = Get-PnpDevice -PresentationOrder | Where-Object {$_.Class -eq "MEDIA" -and $_.Status -eq "OK"} | Select-Object -First 1
if ($device) {
    Write-Host "Device: $($device.Name)"
    Write-Host "Status: $($device.Status)"
} else {
    Write-Host "No audio devices found or all are disabled"
}
"""
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_script],
            capture_output=True,
            text=True,
            timeout=10
        )
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except Exception as e:
        print(f"Error: {e}")


def check_volume():
    """Check system volume level."""
    print("\n" + "=" * 60)
    print("SYSTEM VOLUME")
    print("=" * 60)
    print("Check taskbar volume icon for:")
    print("  ✓ Volume is not muted")
    print("  ✓ Volume level is above 0%")
    print("  ✓ No 'Do Not Disturb' mode active")


def test_native_speech():
    """Quick test of native speech API."""
    print("\n" + "=" * 60)
    print("NATIVE SPEECH TEST")
    print("=" * 60)
    print("Playing 'Audio test' (you should hear this)...")
    
    ps_script = r"""
[System.Reflection.Assembly]::LoadWithPartialName("System.speech") | Out-Null
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.Volume = 100
$synth.Rate = 0
$synth.Speak("Audio test")
Write-Host "Test complete"
"""
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_script],
            capture_output=True,
            text=True,
            timeout=10
        )
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except Exception as e:
        print(f"Error: {e}")


def main():
    print("WINDOWS AUDIO DIAGNOSTICS")
    print("=" * 60)
    
    check_audio_devices()
    check_default_audio()
    check_volume()
    test_native_speech()
    
    print("\n" + "=" * 60)
    print("TROUBLESHOOTING STEPS")
    print("=" * 60)
    print("""
1. Check Volume:
   - Click the volume icon in the taskbar (bottom right)
   - Ensure volume is not muted and set to at least 50%

2. Check Audio Device:
   - Settings → Sound → Volume and device preferences
   - Verify speakers/headphones are selected as output device
   - Try unplugging and replugging speakers/headphones

3. Check Application Audio:
   - Settings → Sound → Volume mixer
   - Find Python and ensure it's not muted

4. Test with Built-in App:
   - Try Windows Narrator (Win + A) to confirm audio works

5. Restart Audio Service:
   - Open Services (services.msc)
   - Find "Windows Audio"
   - Right-click → Restart

6. Check Audio Drivers:
   - Device Manager → Sound, video, game controllers
   - Right-click audio device → Update driver
""")


if __name__ == '__main__':
    main()
