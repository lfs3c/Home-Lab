# Uploading Photos to PhotoPrism Using the Mobile App (Android)

This guide explains how to upload photos from a **mobile phone**** to a **PhotoPrism server / NAS** using the official Android client.

> ⚠️ **Platform note**  
> - All screenshots and step-by-step instructions in this document were created using an **Android device** (Samsung Galaxy S23).  
> - The workflow on iOS is expected to be **very similar**, but it has not been tested or documented here.

---

## Prerequisites

Before starting, make sure you have:

- A working **PhotoPrism server** (local NAS or server)
- Access to PhotoPrism via browser (e.g. `http://localhost` or local IP)
- Valid **PhotoPrism user credentials**
- An **Android smartphone** connected to the same network (or VPN, if applicable)

---

## Step 1 — Install the PhotoPrism mobile app (Android)

Install the app **Gallery for PhotoPrism** from the **Google Play Store**.

After installation:
1. Open the app
2. Log in using the **same credentials** you use to access PhotoPrism via the web interface (browser)

> ℹ️ The mobile app acts only as a **client** for your PhotoPrism server.  
> It does not create new accounts and does not send data to external servers.

**Screenshot:**  
<p align="center">
  <img src="https://github.com/user-attachments/assets/f59d8394-d4c0-4dd4-aba4-195eb338ee63" width="350">
</p>


---

## Step 2 — Select photos in the Android gallery

Open the **Android photo gallery** and manually select the photos you want to upload.

- You can select **one or multiple images**
- Long-press on an image to enable multi-selection mode

All screenshots in this guide were captured on a **Samsung Galaxy S23**, but the process is similar on other Android devices.

**Screenshot:**  
<p align="center">
  <img src="https://github.com/user-attachments/assets/3f45d871-abb2-4a16-bdee-fa2322b7b01c" width="350">
</p>


---

## Step 3 — Share photos to PhotoPrism

With the photos selected:

1. Tap **Share**
2. From the list of apps, select **PhotoPrism – Import**

This sends the selected images directly to your PhotoPrism server using the configured connection.

> 💡 If the option **PhotoPrism – Import** does not appear immediately, scroll the list or tap **More** to display additional apps.

**Screenshot:**  
<p align="center">
  <img src="https://github.com/user-attachments/assets/0ea80006-e910-48a1-a6bd-a1a45b6283ae" width="350">
</p>

---

## Step 4 — Confirm the import

A confirmation screen will appear showing:

- The **PhotoPrism server URL**
- Number of selected files
- Total upload size
- Optional album assignment

To start the upload, tap **Start import**.

**Screenshot:**  
<p align="center">
  <img src="https://github.com/user-attachments/assets/26b97941-e849-4bb2-b156-0d4092915507" width="350">
</p>

---

## Step 5 — Verify the uploaded photos

After a short time, the uploaded photos will automatically appear:

- In the **PhotoPrism mobile app**
- In the **PhotoPrism web interface** (browser)

The time required depends on:
- Number of photos
- File sizes
- Server/NAS performance

During this process, PhotoPrism may perform background tasks such as:
- Indexing
- Thumbnail generation
- Metadata analysis

**Screenshot:**  
<p align="center">
  <img src="https://github.com/user-attachments/assets/089a8cb6-f8b3-4be0-b0c8-198b216940d7" width="350">
</p>

---

## Summary

This method provides a **simple and user-friendly way** to upload photos to a PhotoPrism NAS without accessing Samba shares or file managers.

It is especially useful for:
- Non-technical users
- Quick uploads from mobile devices
- Keeping the PhotoPrism library organized and up to date

---

## Platform disclaimer (important)

- ✅ Fully tested and documented on **Android**
- ⚠️ **Not tested on iOS**
- 📱 iOS users should expect a similar experience, but UI elements and app names may differ

---

**Author environment:**  
- Device: Samsung Galaxy S23  
- Platform: Android  
- PhotoPrism: Self-hosted NAS / local server


###Thank you for taking the time to read this guide.
If you have any questions, suggestions, or improvements to share, feel free to open an issue or reach out. Feedback is always welcome.
