# youtube-audio-extract

## Prerequisites
To run this script, install the following modules:
```
apt-get -y install ffmpeg
pip3 install youtube_dl
pip3 install mutagen
```

## Test Locallyly
```
./youtube-audio-extract.py --workpath . https://www.youtube.com/watch?v=ZTdOMV-yTRg Marillion Lavender
```
## GIThub project
[https://github.com/eg1972/youtube-audio-extract](https://github.com/eg1972/youtube-audio-extract)

- click "Actions" in the top bar
- if a new commit is pushed, execution will start automatically
- click the job name "test" to follow the execution
<<<<<<< HEAD

## Workflow documentation
[Workflow syntax for GitHub Actions](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions)

# Appendix A: Test for workshop
1. Open resources:
   - GIThub [youtube-audio-extract](https://github.com/eg1972/youtube-audio-extract)
2. Change something in the GITLab project:
3. Commit and push the changes

   ```
   cd /home/eddgest/PycharmProjects/youtube-audio-extract
   git commit -am "testing for workshop xx"
   git push origin master 
   ```
5. Observe Actions: [Actions](https://github.com/eg1972/youtube-audio-extract/actions)
   - click reload until the upper most action shows a yellow button
   - open the job in a different tab
   - click on "test-script" in the left frame
