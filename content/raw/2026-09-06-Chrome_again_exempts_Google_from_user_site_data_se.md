# Chrome again exempts Google from user site data settings

URL: https://lapcatsoftware.com/articles/2026/9/1.html

Score: 532

---

Six years ago I published a blog postChrome exempts Google sites from user site data settingsthat received quite a bit of attention:Michael Tsai,Hacker NewsThe Register,The Verge, andGizmodo, among others. The blog post was about a Google Chrome bug that mysteriously exempted Google-owned sites from the setting to automatically delete all site data. Eventually, spurred by my report, Google did fix the bug.
You can probably guess why Iâm writing about the bug again: Iâve noticed Chrome doing something similar now. Iâve reproduced this new issue on two different Macs with Chrome version 152.0.7977.83. For testing purposes, I changed the default search engine in Chrome from Google to DuckDuckGo, just to make sure that this setting was not the cause.
On-device site data settings (chrome://settings/content/siteData) shows that the Default behavior is to Delete data sites have saved to your device when you close all windows.
Iâm not signed into Chrome and indeed disallow Chrome sign-in.
You can see onchrome://settings/content/allthat no site data is saved.
Now I do a Google search.
Then I close the one and only window in Chrome.
Returning tochrome://settings/content/all, I find somegoogle.comsite data! This data persists even if I quit and relaunch Chrome.
If I delete the Google site data and repeat the whole process, the same issue occurs again.
As far as I can tell,www.google.comis the only site exempted by Chrome. Looking inside the~/Library/Application Support/Google/Chrome/Defaultfolder, it appears that the saved site data consists of Cookies, Local Storage, and Session Storage.
Iâm not certain when this issue was introduced. My default web browser is Safari, so I donât use Chrome full-time, though I do use it (and Firefox) frequently for testing.
Iâm personally inclined to citeHanlonâs razorhere rather than engage in conspiracy theories. Nonetheless, Google has no excuse for incompetence either, especially given the amount of money made by the company (which Iâll always call Google, not Alphabet) and its engineers. They can avoid receiving bad publicity from me by improving their QA. Perhaps some kind of unit tests for this feature? Move slower and donât break things.
I wish the government would move fast and break up the Google Search monopoly. Donât even get me started about how when youâre not signed in to Google, all Google Search results are now opaquehttps://www.google.com/goto?url=garbage rather than the site URLs!
