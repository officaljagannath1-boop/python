[System.Reflection.Assembly]::LoadWithPartialName("System.speech") | Out-Null
$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
$speak.Speak("Hello world, this is a Windows native speech test")
Write-Host "Audio playback completed"
