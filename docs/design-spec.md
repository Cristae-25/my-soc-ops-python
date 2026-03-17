# Card Deck Shuffle - Design Specification

## Overview

New game mode "Card Deck Shuffle" for Seahawks Bingo app. Players tap to reveal random cards with single prompts.

## Design Vision

**Aesthetic:** Clean, tactile card interface matching Seahawks branding. Emphasize the satisfying feel of flipping through cards with smooth, responsive animations. Focus on clarity and mobile-friendly spacing.

**Colors:**

- Primary: Seahawks Navy (#002244) - Headers, text
- Accent: Seahawks Green (#69BE28) - Call-to-action buttons
- Secondary: Seahawks Blue (#0C2C56) - Accents, borders
- Background: Light (#E8F0F5) - Base background

## Components

### 1. Card UI Component

**Location:** `app/templates/components/card_reveal.html`

**Features:**

- Large, tappable card displaying one prompt
- Responsive design (works on mobile/desktop)
- Visual progress indicator (e.g., "Card X of 24")
- Subtle shadow/depth to emphasize card as a tactile element
- Accessible touch targets

**Design Details:**

- Card size: Responsive (max ~400px width on desktop, full width on mobile)
- Text: Large, readable (18-20px), navy color
- Progress: Subtle counter at bottom (gray text)
- Spacing: Generous padding around text for readability
- Border: Subtle Seahawks blue accent border

### 2. Game Mode Selection

**Location:** `app/templates/components/start_screen.html` (update)

**Changes:**

- Add third button: "🃏 Card Shuffle"
- Maintain consistent button styling with existing modes
- Update description text to include Card Shuffle

### 3. Game Screen for Card Shuffle

**Location:** `app/templates/components/game_screen.html` (update)

**Features:**

- Header with back button
- Instruction text: "Tap the card to reveal your next prompt!"
- Centered card component
- Win modal when all 24 cards viewed (same as other modes)

### 4. Animations

**CSS-based only** (no JavaScript complexity)

**Animations:**

- Card reveal: Subtle fade-in + slight scale (0.95 -> 1.0) on new card
- Button tap: Opacity change on hover/active
- Progress counter update: Subtle color pulse or brief highlight

**Timing:**

- Reveal animation: 300ms ease-out
- No overly complex transitions—keep it snappy

## Data Structure

### Models

- Extend `GameMode` enum to include `CARD_SHUFFLE`
- Add to `GameSession`: `current_card_index`, `viewed_card_ids`

### Game Logic

- Generate 24 random prompts from QUESTIONS list
- Track which cards have been shown
- Next card: Pick random from unviewed cards
- Win condition: All 24 cards viewed

## Implementation Steps (Pixel Jam)

1. ✅ Phase 1: Update models and create base card component UI
   - Extended GameMode enum with CARD_SHUFFLE
   - Updated GameSession with card_deck, current_card_index, viewed_cards
   - Created generate_card_deck() logic
   - Built card_reveal.html component with progress indicator
   - Added CSS animations (.card-reveal-animation)
   - Updated start_screen with "Card Shuffle" button
   - Integrated card component into game_screen
   - All tests passing ✓

2. ⏳ Phase 2: Browser testing and visual refinement
   - Take browser screenshot and verify styling
   - Review card animations in browser
   - Refine spacing, colors, and responsiveness
   - Test card reveal interaction
3. ⏳ Phase 3: Interaction testing and edge cases
   - Test rapid taps
   - Test progress tracking
   - Test win condition
   - Verify modal displays correctly

4. ⏳ Phase 4: Mobile responsiveness polish
   - Check mobile viewport
   - Adjust touch target sizing
   - Optimize card dimensions for small screens

5. ⏳ Phase 5: Final polish and feedback
   - Animation timing refinement
   - Color and contrast review
   - Accessibility check

---

## Design Decisions

### Why Card-Based?

Provides a different feel from BINGO's spatial grid and Scavenger Hunt's checklist. Focuses user on single prompt at a time.

### Typography

Using system fonts (existing in app.css) for consistency. Large prompt text (20px) ensures readability on phones.

### Color Strategy

Using navy for text (high contrast), green for CTA buttons, blue for subtle accents. Consistent with existing Seahawks branding in app.

### Animation Philosophy

CSS-only, minimal complexity. One key moment: the card reveal animation. Avoid micro-interactions that don't add value.

---

## Notes

- All 24 QUESTIONS reused from existing data
- No new backend dependencies required
- Leverage existing session middleware
- Match existing win modal pattern
