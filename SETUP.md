# Setup Guide

This guide will help you set up the optimal environment for viewing and synchronizing these ethical hacking notes.

---

## 📝 Prerequisites

- Windows, macOS, or Linux operating system
- Git installed (for cloning the repository)
- Internet connection

---

## 🔧 Local Setup

### Step 1: Clone the Repository

```bash
# Using HTTPS
git clone https://github.com/usaihack/My-Notes.git

# Or using SSH
git clone git@github.com:usaihack/My-Notes.git

# Navigate to directory
cd My-Notes
```

### Step 2: Install Obsidian

Obsidian provides the best viewing experience for these markdown notes with features like:

- Graph view for note connections
- Backlinks and forward links
- Tags and search functionality
- Custom themes and plugins
- Live preview mode

#### Download Obsidian

1. Visit [obsidian.md](https://obsidian.md/)
2. Download the version for your operating system:
   - **Windows:** `.exe` installer
   - **macOS:** `.dmg` file
   - **Linux:** `.AppImage` or `.deb` package

3. Install following standard procedures for your OS

#### Open Vault in Obsidian

1. Launch Obsidian
2. Click **"Open folder as vault"**
3. Navigate to your cloned `My-Notes` directory
4. Select the folder and click **"Open"**

✅ Your notes are now ready to explore in Obsidian!

---

## 📱 Mobile & Desktop Synchronization

For seamless two-way sync across all your devices, use MEGA Cloud Storage.

### Why MEGA?

- ✅ **Free 20GB** storage
- ✅ **End-to-end encryption** for security
- ✅ **Two-way sync** - Changes sync automatically
- ✅ **Cross-platform** - Windows, macOS, Linux, iOS, Android
- ✅ **Privacy-focused** - Zero-knowledge encryption

### Step 1: Create MEGA Account

1. Visit [mega.io](https://mega.io/)
2. Click **"Create Account"**
3. Enter email and create strong password
4. Verify your email address

### Step 2: Install MEGA Desktop App

#### Windows / macOS / Linux

1. Download from [mega.io/desktop](https://mega.io/desktop)
2. Install the application
3. Log in with your MEGA credentials
4. Complete the setup wizard

#### Configure Sync Folder

1. Open MEGA Desktop app
2. Go to **Settings** → **Syncs**
3. Click **"Add Sync"**
4. **Local folder:** Select your `My-Notes` directory
5. **MEGA folder:** Create/select `EthicalHackingNotes` folder
6. Click **"Add"**

✅ Your notes will now sync to MEGA Cloud!

### Step 3: Install MEGA Mobile App

#### iOS (iPhone/iPad)

1. Open **App Store**
2. Search for **"MEGA"**
3. Install the MEGA app
4. Log in with your account

#### Android

1. Open **Google Play Store**
2. Search for **"MEGA"**
3. Install the MEGA app
4. Log in with your account

#### Mobile Sync Configuration

1. Open MEGA mobile app
2. Navigate to **Settings** → **Camera Uploads** or **Sync**
3. Enable sync for the `EthicalHackingNotes` folder
4. Choose **"Two-way sync"** if available

### Step 4: Install Obsidian Mobile

#### iOS

1. Install **Obsidian** from App Store
2. Open Obsidian
3. Connect to your vault:
   - Use **"Open folder from iCloud"** or
   - Navigate to MEGA synced folder (if accessible via Files app)

#### Android

1. Install **Obsidian** from Google Play Store
2. Open Obsidian
3. Grant storage permissions
4. Open vault from MEGA synced folder

---

## 🔄 Workflow: How It All Works Together

```
┌─────────────────┐
│  Desktop PC     │
│  (Obsidian)     │
└────────┬────────┘
         │
         ↓
    ┌─────────┐
    │  MEGA   │ ← Two-way sync
    │  Cloud  │
    └─────────┘
         ↑
         │
┌────────┴────────┐
│  Mobile Device  │
│  (Obsidian)     │
└─────────────────┘
```

**Flow:**

1. Edit notes on Desktop → Saves to local folder
2. MEGA syncs to cloud automatically
3. Mobile MEGA downloads changes
4. View updated notes in Obsidian Mobile
5. Reverse works the same way!

---

## ⚙️ Recommended Obsidian Settings

### Essential Community Plugins

1. **Dataview** - Query and display notes dynamically
2. **Calendar** - Visualize daily notes
3. **Kanban** - Organize learning tasks
4. **Advanced Tables** - Better table editing
5. **Tag Wrangler** - Manage tags efficiently

### Installation

1. In Obsidian, go to **Settings** → **Community Plugins**
2. Disable **Safe Mode**
3. Click **Browse** and search for plugins
4. Install and enable desired plugins

### Recommended Settings

- **Editor:** Enable **Live Preview** mode
- **Files & Links:** Enable **Automatically update internal links**
- **Appearance:** Choose a dark theme (e.g., "Minimal" or "Cyber Glow")

---

## 🛡️ Security Considerations

### MEGA Encryption

- MEGA uses **zero-knowledge encryption**
- Your password is the encryption key
- **Important:** If you lose your password, data cannot be recovered
- Enable **Two-Factor Authentication** for extra security

### Backup Strategy

While MEGA provides redundancy, consider:

- Keep local Git backups
- Periodically commit and push changes to GitHub
- Export important notes to additional locations

---

## 🐛 Troubleshooting

### Sync Issues

**Problem:** Files not syncing between devices

**Solutions:**

- Check internet connection
- Verify MEGA sync is active (green icon)
- Restart MEGA desktop/mobile app
- Check available storage space
- Force sync: Right-click MEGA icon → **Sync Now**

### Obsidian Not Opening Vault

**Problem:** Vault opens but notes appear corrupted

**Solutions:**

- Ensure all `.md` files are UTF-8 encoded
- Check for conflicting plugins
- Try opening in **Source Mode** instead of Live Preview
- Rebuild index: Settings → Files & Links → **Rebuild index**

### Permission Errors

**Problem:** Cannot edit files

**Solutions:**

- Check file permissions on your OS
- Ensure MEGA isn't locking files during sync
- Try disabling MEGA sync temporarily while editing

---

## 📞 Getting Help

If you encounter issues:

1. **Check Documentation:**
   - [Obsidian Help](https://help.obsidian.md/)
   - [MEGA Support](https://mega.io/help)

2. **Community Support:**
   - [Obsidian Forum](https://forum.obsidian.md/)
   - [Obsidian Discord](https://discord.gg/obsidianmd)

3. **Repository Issues:**
   - Open an issue in this repository

---

## ✅ Setup Checklist

- [ ] Git installed and repository cloned
- [ ] Obsidian installed and vault opened
- [ ] MEGA account created
- [ ] MEGA Desktop app installed and synced
- [ ] MEGA Mobile app installed (if needed)
- [ ] Obsidian Mobile installed (if needed)
- [ ] Recommended plugins installed
- [ ] Sync tested between devices

---

**You're all set! Happy learning! 🚀**
