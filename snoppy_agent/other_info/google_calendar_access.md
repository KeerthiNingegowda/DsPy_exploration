## Google Calendar API Setup

### Step 1 -- Google Cloud Console
- Go to [console.cloud.google.com](https://console.cloud.google.com)
- Create a new project

### Step 2 -- Enable Calendar API
- APIs and Services -> Library
- Search "Google Calendar API" -> Enable

### Step 3 -- Create OAuth Credentials
- APIs and Services -> Credentials -> Create Credentials -> OAuth 2.0 Client ID
- Application type: Desktop app
- Download the JSON file and save as `credentials.json` in project root

### Step 4 -- Configure Consent Screen
- APIs and Services -> OAuth consent screen
- User type: External
- Fill in app name and developer email
- Scroll to bottom -> Test users -> Add users
- Add your own Gmail address

### Step 5 -- Install Dependencies
```bash
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Step 6 -- First Run Authentication
Run the test script once. A browser window will open asking you to authorize.
After authorization `token.json` is created automatically in your project root.

### Important
Add both files to `.gitignore` -- never commit them to your repo:
```
credentials.json
token.json
```