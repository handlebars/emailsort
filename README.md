# emailsort
Email address de-dupe

"Write a working function that removes all duplicates from an unsorted list of email addresses, while leaving the remaining list in the original order. Show that this function can handle 100,000 email addresses containing 50% randomly placed duplicates, in under 1 second on a typical laptop."

Input file: Process used to build the test file:
1. Export a list of 50,000 email addresses using a mock data generator found on the web.
2. Copy the entire list and pasting it at the end of the document, to create a 100,000 email address list with half of the email addresses duplicates (but no situations of triplicate, or greater)
3. Use a desktop client text editor (TextMate 2 on MacOS) and used a built-in function to randomize the lines of the file.

(the final large test file, which is only about 2.4 MB, is not included)

Results: Missed the goal by a lot -- takes about 2 minutes to process a list of 100,000 email address, not under 1 second

% time (python3 dedupe.py)
( python3 dedupe.py; )  109.04s user 0.05s system 99% cpu 1:49.35 total

% time (python3 dedupe.py)
( python3 dedupe.py; )  121.29s user 0.04s system 99% cpu 2:01.59 total