# Software updates

We recommend running the latest DVL software where possible. Software updates are done from the web GUI **About** page. The latest software can be obtained [automatically](#automatic-software-update) or [manually](#offline-software-update).

The release notes for each release are found here:

* [DVL A50/A125 changelog](./dvl-a50_a125-changelog.md)
* [DVL A100/A250 changelog](./dvl-a250_a100-changelog.md)

!!! warning
    During the software update, the thermal protection feature is turned off. To prevent the DVL from overheating, keep the DVL submerged in water throughout the update process.

    If the DVL is switched off during an update, it might be permanently damaged.

## Automatic software update

The DVL web GUI automatically checks and indicates if a new software version is available from the **About** page.

* Connect the DVL over Ethernet to a network connected to the internet. If you use a personal computer, it may be necessary to make a network bridge between a network interface with internet access, such as Wi-Fi, and the Ethernet interface connected to the DVL.
* Open the DVL web GUI in a web browser.
* Go to the **About** page.
* If a new version is available, start the software update from the **About** page.

## Offline software update

If it is not possible to connect the DVL to the internet, use an offline software update.

* Find the current version and chip ID of the DVL on the **About** page in the web GUI.
* Manually download an update package (`.wlup`) from the [update server](https://update.waterlinked.com/) using the chip ID.
* Verify whether the downloaded version is newer than the currently running version.
* Set the system time as described below.
* Open the DVL web GUI in a web browser.
* Go to the **About** page.
* Select **Manual upload** and then upload the downloaded `.wlup` file.

### Failure during update (set system time)

When performing an offline software update, the following error might occur: `Failed: Error upgrading: resize: non-zero exit code: exit status 1`. This error is resolved by setting the system time before performing an update.

* Go to the DVL web GUI and click **Configuration** or **Settings** in the left menu.
* Open the **Advanced configuration** menu.
* Scroll to **System time configuration**.
* Select **Manual time** in **System time source** and click **Set manual time**.
* Click **About** in the left menu and click **Software upgrade**.
* Perform the update again.
