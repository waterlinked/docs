# Sonar Replay

Sonar Replay allows play back of recordings taken with the [Sonar 3D-15](https://waterlinked.com/3dsonar) directly in your browser. You can access [Sonar Replay here](https://sonar.replay.waterlinked.com). The interface is similar to that of the Sonar 3D-15, but with some changes.

All processing is done in your browser and not uploaded anywhere. 

![Sonar Replay Main View](../img/sonar-replay/landing.png)

!!! Note
    Sonar Replay is still in development. Some features may not be fully functional or implemented yet.

Click the file input to select a file or drag and drop a file onto the browser window. Alternatively use one of the provided examples by clicking "Load demo".

Processing time depends on the file size, device and browser. While processing, an estimated remaining time is shown.

![Sonar Replay Processing Recording](../img/sonar-replay/processing-recording.png)

!!! Note
    We recommend recordings smaller than 300 MB for the best experience.

## Play back
Once processing is complete, the 3D point cloud is shown and play back will start immediately. Scrub through the recording using the play back slider, pause, adjust play back speed and get an overview of the recording with "Chapters".

![Sonar Replay](../img/sonar-replay/playback.png)

## Chapters
Sonar Replay will automatically create chapter previews of the provided recording. Access this by clicking the "Chapters" button or by hitting <code>C</code> on your keyboard. Note that all recorded timestamps are in UTC (Coordinated Universal Time) and reflect the sonar's time settings at the time of recording.

![Sonar Replay](../img/sonar-replay/chapters.png)

!!! Tip
    Quickly jump to a chapter by clicking the preview image.

Chapter preview can be expanded to a larger version by clicking the magnifying glass icon that appears when hovering the chapter preview. 

![Sonar Replay](../img/sonar-replay/chapter-preview.png)

## Adjust settings
Much like the real Sonar 3D-15, settings can be adjusted to better fit your use case and observe the recording. Toggle the settings tray by clicking the "Settings" button or hit <code>S</code> on your keyboard. From here many settings can be adjusted like point size, color palette and toggling elements in the 3D view.

![Sonar Replay](../img/sonar-replay/adjust-settings.png)

## Help
Get a quick overview of all main parts of the interface by clicking the <code>?</code> (Question) icon top left or by hitting <code>H</code> on your keyboard.

![Sonar Replay](../img/sonar-replay/help-overlay.png)