# App Store listing content (US-113)

Everything to paste into App Store Connect for Murmur Voice Dictation
(App ID 6801927849, bundle com.labroi.murmur.ios). Character limits are
noted per field and verified by scripts/check-listing.py. Entering this
into ASC and submitting is Labroi's step; this file is the source of truth
for what gets pasted.

## Name (30 max, already set on the app record)

Murmur Voice Dictation

## Subtitle (30 max)

Push to talk. Text appears.

## Category

Primary: Productivity. Secondary: Utilities.

## Promotional text (170 max, editable without a new build)

Dictate in any app with one tap. Murmur types what you say, polished and
punctuated, using your own free Groq key. No accounts, no servers, no
data collected.

## Description (4000 max)

Murmur is push-to-talk dictation for your whole phone. Tap the mic key on
the Murmur keyboard, speak, and your words appear at the cursor in
whatever app you are in, cleaned up, punctuated, and ready to send.

HOW IT WORKS

Your first dictation of a session opens Murmur, which records instantly,
no taps. Swipe back and your text is waiting at the cursor. After that
first take the microphone stays warm for a short window, so every later
dictation records in place, right inside the app you are typing in, with
a live waveform on the keyboard. When the window lapses, Murmur releases
the microphone completely.

YOUR WORDS, ACTUALLY POLISHED

Raw transcription is only the start. Murmur cleans up your speech with
levels you control, from exact words only to light punctuation to full
structure with headings and lists. Spoken commands like "new line" and
"new paragraph" just work. A silence gate refuses empty takes instead of
inventing text, and if cleanup is ever unavailable your raw transcript is
inserted untouched. Your words are never lost.

MAKE IT YOURS

- A personal dictionary teaches the transcriber your names and terms.
- Corrections learn from your edits: fix a word twice in history and
  Murmur remembers it.
- Expansions turn short phrases into full snippets after formatting, and
  their values never leave your phone.
- Dictation history lives on the device, with an off switch.

BRING YOUR OWN KEY

Murmur connects directly from your phone to the transcription service
you configure. The free Groq tier works out of the box: create a key,
paste it into onboarding, done. Any OpenAI-compatible endpoint is
supported, so you choose the provider, the model, and the cost. There is
no Murmur account and no middleman server.

PRIVATE BY ARCHITECTURE

- Audio goes only to the API endpoint you configured, and nowhere else.
- Your API key lives in the iOS Keychain, never in shared storage.
- The keyboard extension contains no networking and no audio code. It
  cannot record and it cannot phone home.
- The developer collects nothing. No analytics, no tracking, no servers.
- While Murmur holds the microphone in the background, the system's
  orange indicator is visible the whole time, and the mic auto-releases
  after an idle window you control, including off.

ALSO IN THE BOX

- A Siri Shortcut and Action Button intent: dictate from anywhere and the
  transcript lands on your clipboard.
- Number formatting options, style presets, and a max take length cap.
- A dictation-first keyboard with space, delete, return, and globe, plus
  an automatic hand-off layout for number and email fields.

Murmur needs a microphone, a transcription API key you supply, and
nothing else. Speak naturally. Send it.

## Keywords (100 max, comma-separated, no spaces after commas)

speech to text,voice typing,whisper,transcribe,talk to text,voice notes,stt,groq,dictate,keyboard

## Support URL

https://lbwalton.github.io/murmur/support (placeholder until the pages
deploy target is confirmed; swap for the Vercel URL if that is chosen)

## Privacy Policy URL

https://lbwalton.github.io/murmur/privacy (same note as above)

## What's New for 0.1.1 (4000 max)

- Long dictations now insert reliably when you return to your app.
- The keyboard recovers instantly if the microphone was taken by a call
  or another app: one tap reopens Murmur.
- Cleanup is stricter about never answering your dictation. Questions you
  speak stay questions in your text.

## App Privacy questionnaire

Data collection: None. The developer collects nothing, runs no servers,
and has no analytics. If review pushes back about the transcription API
call, the fallback declaration is Audio Data, purpose App Functionality,
not linked to identity, no tracking. Both bundles ship
PrivacyInfo.xcprivacy manifests matching this.

## Age rating

No objectionable content in any category. Rates 4+.

## Pricing and availability

Free, all territories. Revisit when the Pro unlock exists.

## App Review notes (paste into the Notes field)

Murmur requires a user-supplied transcription API key (bring your own
key by design; there is no developer server). A test key is provided
below. Setup: open Murmur, paste the key in onboarding step 1, tap Test
connection. To dictate: enable the Murmur keyboard in Settings, General,
Keyboard, Keyboards, and allow Full Access, then open Notes or Messages,
switch to the Murmur keyboard, and tap the large mic key.

Test key (Groq, throwaway, revoked after review): [PASTE KEY HERE]

Background audio (UIBackgroundModes audio): recording is always
user-initiated from the keyboard's mic key or inside the app. The system
orange microphone indicator is visible the entire time the mic is held.
The audio session auto-releases after a short idle window (default 90
seconds, user-configurable, with an Off setting that releases after
every take). No audio is captured outside an explicit dictation.

Keyboard (guideline 4.4.1): the keyboard types, deletes, inserts
newlines, and switches keyboards without Full Access, and shows a clear
explainer when Full Access is off. Full Access is used only to receive
the finished transcript from the containing app through the App Group.
The keyboard extension contains no networking or audio code.

The mic key opens the Murmur app for the first dictation of a session
(the murmur:// flow). Apple forbids microphone access inside keyboard
extensions, so the containing app performs all recording; after the
first take the app records in place from the background as described
above. This is the compliant pattern for keyboard-driven dictation.

## Entry checklist for Labroi

1. ASC, My Apps, Murmur Voice Dictation, the 0.1.1 version page.
2. Paste subtitle, promotional text, description, keywords, URLs.
3. Upload the screenshot set from ios/screenshots/ (6.9 inch).
4. Answer App Privacy (collection: none) and age rating (4+).
5. Create the throwaway Groq key, paste into review notes, save.
6. Select build 0.1.1 (3), choose manual release, submit.
7. After approval: revoke the test key, then release.
