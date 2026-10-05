# Tableau Publishing Guide: Step-by-Step Instructions

This guide provides exact, beginner-friendly instructions to save, extract, and publish your Tableau workbook to **Tableau Public** so that it can be shared, embedded into your Flask web application, and submitted for your Skill Wallet evaluation.

---

## Prerequisites
* A free **Tableau Public** account (Sign up at [public.tableau.com](https://public.tableau.com) if you do not have one).
* Your completed workbook in Tableau Desktop or Tableau Public App containing your 8 worksheets, 1 dashboard, and 1 story.

---

## Step 1: Save Local Workbook
1. In Tableau, click **File** in the top menu bar.
2. Select **Save As...**
3. Choose the project directory: `D:\Skill wallet\tableau\`
4. Enter File Name: `Student_Mental_Health_Analytics.twbx`
   *(Tip: Always save as `.twbx` - Tableau Packaged Workbook, as this packages the dataset directly inside the file so it never breaks).*
5. Click **Save**.

---

## Step 2: Create Data Extract (If using Tableau Desktop Professional)
*(Note: If you are using the free Tableau Public desktop application, it extracts data automatically when saving. If you are using Tableau Desktop Professional, follow this quick step):*
1. In the top menu, click **Data** -> `student_mental_health_cleaned` -> **Extract Data...**
2. Click **Extract** in the popup window.
3. Save the extract file in your data folder when prompted.

---

## Step 3: Publish to Tableau Public
1. In the top menu of Tableau, click **Server**.
2. Hover over **Tableau Public** -> click **Save to Tableau Public As...**
   *(Or click the small Tableau Public icon on the toolbar).*
3. A login window will appear:
   * Enter your Tableau Public email and password.
   * Click **Sign In**.
4. A publishing dialog will appear:
   * **Workbook Title:** `Student Mental Health and Academic Well-Being Analytics`
5. Click **Save**.
6. Tableau will upload the workbook and automatically open your default web browser displaying your published dashboard!

---

## Step 4: Configure Permissions & Copy Share URLs
Once your dashboard opens in the web browser on `public.tableau.com`:
1. Scroll down to the bottom right of the visualization toolbar on the webpage.
2. Click the **Edit Details** (pencil) icon:
   * Ensure **Show sheets as tabs** is checked (this allows evaluators to toggle between Dashboard and Story).
   * Ensure **Allow others to download the workbook and its data** is checked (proves genuine work).
   * Click **Save**.
3. Click the **Share** icon (looks like three connected dots or an arrow) at the bottom right:
   * You will see two boxes: **Embed Code** and **Link**.
   * Click the copy button next to **Link**.
   * This is your **Tableau Public Dashboard URL**! (e.g., `https://public.tableau.com/views/StudentMentalHealthAnalytics/Dashboard`)
4. Now click on the **Story** tab on the web page:
   * Click the **Share** icon again.
   * Copy the **Link** for the Story.
   * This is your **Tableau Public Story URL**!

---

## Step 5: Update Your Project Links
1. Open `config.py` in your project workspace.
2. Paste the copied URLs into `TABLEAU_DASHBOARD_URL` and `TABLEAU_STORY_URL`.
3. Open `README.md` and replace the placeholder text with your live URLs:
   ```markdown
   Tableau Public Dashboard:
   https://public.tableau.com/views/...

   Tableau Story:
   https://public.tableau.com/views/...
   ```

---

## Security & Privacy Reminder
* Never enter your Tableau password into plain text files or git commits.
* Tableau Public workbooks are viewable by anyone with the link; because our dataset is fully synthetic and anonymized (`STU1001` - `STU1080`), it is 100% compliant with privacy and academic ethics standards.
