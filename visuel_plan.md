# BobSpec — Visual Design Plan
### IBM Design Language | Team Bobsyourdev

---

## 1. Design Philosophy

BobSpec follows **IBM Carbon Design System** principles:
- **Clarity** — every element has a purpose
- **Efficiency** — minimal clicks, maximum information
- **Consistency** — unified visual language throughout
- **Intelligence** — the UI feels alive and reactive

---

## 2. Color Palette

### Primary (IBM Blue)
```css
--ibm-blue-70:     #0043CE;  /* Primary actions, buttons */
--ibm-blue-60:     #0F62FE;  /* Hover states, links */
--ibm-blue-50:     #4589FF;  /* Active agent glow */
--ibm-blue-20:     #A6C8FF;  /* Subtle highlights */
--ibm-blue-10:     #EDF5FF;  /* Light backgrounds */
```

### Neutrals (IBM Gray)
```css
--ibm-gray-100:    #161616;  /* Main background */
--ibm-gray-90:     #262626;  /* Card backgrounds */
--ibm-gray-80:     #393939;  /* Borders, dividers */
--ibm-gray-60:     #6F6F6F;  /* Secondary text */
--ibm-gray-20:     #E0E0E0;  /* Body text */
--ibm-gray-10:     #F4F4F4;  /* Light surfaces */
```

### Agent Colors
```css
--agent-edge:      #BE95FF;  /* Edge Case — IBM Purple 40 */
--agent-security:  #FF8389;  /* Security   — IBM Red 40   */
--agent-architect: #42BE65;  /* Architect  — IBM Green 40 */
```

### Status Colors
```css
--status-idle:     #6F6F6F;  /* Agent waiting */
--status-active:   #0F62FE;  /* Agent running */
--status-done:     #42BE65;  /* Agent done    */
--status-error:    #FA4D56;  /* Agent error   */
```

---

## 3. Typography

### Font Stack (IBM Plex — Google Fonts)
```css
/* Import in index.html */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;500;600;700&family=IBM+Plex+Serif:wght@300;400&display=swap');

--font-sans:  'IBM Plex Sans',  sans-serif;  /* UI text       */
--font-mono:  'IBM Plex Mono',  monospace;   /* Code, IDs     */
--font-serif: 'IBM Plex Serif', serif;       /* Hero headings */
```

### Type Scale
```css
--text-xs:   0.75rem;   /* 12px — labels, badges  */
--text-sm:   0.875rem;  /* 14px — secondary text  */
--text-base: 1rem;      /* 16px — body text       */
--text-lg:   1.25rem;   /* 20px — card titles     */
--text-xl:   1.5rem;    /* 24px — section headers */
--text-2xl:  2rem;      /* 32px — page title      */
--text-3xl:  3rem;      /* 48px — hero heading    */
```

---

## 4. Spacing & Grid

```css
/* 8px base unit — IBM Carbon standard */
--space-1:   0.25rem;  /*  4px */
--space-2:   0.5rem;   /*  8px */
--space-3:   0.75rem;  /* 12px */
--space-4:   1rem;     /* 16px */
--space-6:   1.5rem;   /* 24px */
--space-8:   2rem;     /* 32px */
--space-12:  3rem;     /* 48px */
--space-16:  4rem;     /* 64px */

/* Layout */
--max-width: 1200px;
--sidebar-width: 320px;
--card-radius: 0px;     /* IBM Carbon uses 0px radius — sharp corners */
```

> ⚠️ IBM Carbon Design uses **0px border-radius** — no rounded corners.
> Sharp edges = professional, enterprise feel.

---

## 5. UI Layout

```
┌─────────────────────────────────────────────────────────────┐
│  HEADER                                                     │
│  ● BobSpec logo (IBM Blue)    [Status: Ready] [IBM Badge]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  HERO SECTION                                               │
│  "Transform your ticket into a complete specification"      │
│  ─────────────────────────────────────────────────────      │
│  [ Ticket textarea — dark background, blue border focus ]   │
│  [ ▶ Analyze with BobSpec                              ]    │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  AGENTS SECTION  (3 cards side by side)                     │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐         │
│  │ 🔍 Edge Case │ │ 🛡 Security  │ │ 🏗 Architect │         │
│  │   Detective  │ │   Analyst    │ │   Blueprint  │         │
│  │              │ │              │ │              │         │
│  │ [ IDLE ]     │ │ [ IDLE ]     │ │ [ IDLE ]     │         │
│  └──────────────┘ └──────────────┘ └──────────────┘         │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SPECIFICATION OUTPUT                                       │
│  (appears after analysis — smooth slide-in)                 │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 📋 Complete Specification                           │    │
│  │ ─────────────────────────                           │    │
│  │ [Edge Cases] [Security] [Architecture] [Export]     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. Component Specifications

### 6.1 Header
```
Height: 48px (IBM Carbon standard)
Background: --ibm-gray-100
Border-bottom: 1px solid --ibm-gray-80
Left: BobSpec wordmark (IBM Plex Mono, --ibm-blue-60)
Right: Status pill + "Powered by IBM Bob" badge
```

### 6.2 Ticket Input
```
Background:   --ibm-gray-90
Border:       1px solid --ibm-gray-80
Border-focus: 2px solid --ibm-blue-60  (no border-radius)
Font:         IBM Plex Mono, 14px
Color:        --ibm-gray-10
Min-height:   160px
Placeholder:  "Paste your ticket here..."
Transition:   border-color 150ms ease
```

### 6.3 Analyze Button
```
Background:      --ibm-blue-60
Background-hover: --ibm-blue-70
Color:           white
Font:            IBM Plex Sans 500, 14px
Padding:         14px 32px
Border-radius:   0px
Transition:      background 150ms ease
Icon:            ▶ (left of text)
Loading state:   Spinner + "Analyzing..." text
```

### 6.4 Agent Card
```
Width:        calc(33.33% - 16px)
Background:   --ibm-gray-90
Border-left:  3px solid [agent color]
Padding:      24px
Font-title:   IBM Plex Mono, 16px, 600
Font-body:    IBM Plex Sans, 14px
Shadow:       none (IBM Carbon style)
```

**States:**
```
IDLE    → border-left: 3px solid --ibm-gray-80
          opacity: 0.6
          icon: ○ (hollow circle)

ACTIVE  → border-left: 3px solid [agent color]
          opacity: 1
          icon: ◉ (pulsing dot — CSS animation)
          background: subtle gradient to agent color at 5%

DONE    → border-left: 3px solid --status-done
          icon: ✓ (checkmark)
          results visible (fade-in)

ERROR   → border-left: 3px solid --status-error
          icon: ✕
```

### 6.5 Specification Output Panel
```
Background:    --ibm-gray-90
Border-top:    2px solid --ibm-blue-60
Padding:       32px
Animation:     slideInUp 300ms ease (on appear)
Tab navigation: Edge Cases | Security | Architecture | Export
Tab-active:    border-bottom: 2px solid --ibm-blue-60, color: white
Tab-inactive:  color: --ibm-gray-60
```

---

## 7. Animations & Transitions

### 7.1 Agent Activation Sequence
When "Analyze" is clicked, agents activate one by one with a 200ms stagger:

```css
/* Agent card activation */
@keyframes agentActivate {
  0%   { border-left-color: var(--ibm-gray-80); opacity: 0.6; }
  50%  { border-left-color: var(--agent-color); opacity: 1;   }
  100% { border-left-color: var(--agent-color); opacity: 1;   }
}

/* Pulsing dot when agent is running */
@keyframes pulse {
  0%, 100% { opacity: 1;   transform: scale(1);    }
  50%       { opacity: 0.4; transform: scale(0.85); }
}

/* Agent card subtle glow */
@keyframes agentGlow {
  0%, 100% { box-shadow: 0 0 0px transparent; }
  50%       { box-shadow: 0 0 20px color-mix(in srgb, var(--agent-color) 20%, transparent); }
}
```

### 7.2 Thinking Dots (Agent Processing)
```css
/* Shows "Analyzing..." with animated dots */
@keyframes thinkingDot {
  0%, 80%, 100% { opacity: 0; transform: translateY(0);    }
  40%           { opacity: 1; transform: translateY(-4px); }
}

.dot-1 { animation: thinkingDot 1.4s infinite 0.0s; }
.dot-2 { animation: thinkingDot 1.4s infinite 0.2s; }
.dot-3 { animation: thinkingDot 1.4s infinite 0.4s; }
```

### 7.3 Results Reveal
```css
/* Each result item fades in with stagger */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0);    }
}

.result-item {
  animation: fadeInUp 300ms ease forwards;
}
.result-item:nth-child(1) { animation-delay: 0ms;   }
.result-item:nth-child(2) { animation-delay: 80ms;  }
.result-item:nth-child(3) { animation-delay: 160ms; }
.result-item:nth-child(4) { animation-delay: 240ms; }
```

### 7.4 Spec Panel Slide In
```css
@keyframes slideInUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0);    }
}

.spec-output {
  animation: slideInUp 400ms cubic-bezier(0.22, 1, 0.36, 1);
}
```

### 7.5 Progress Line (Agent to Agent)
```css
/* Horizontal connector line between agent cards */
/* Fills left to right as agents complete */
@keyframes progressFill {
  from { width: 0%; }
  to   { width: 100%; }
}

.connector-line {
  height: 2px;
  background: --ibm-gray-80;
  position: relative;
}

.connector-line::after {
  content: '';
  position: absolute;
  height: 2px;
  background: --ibm-blue-60;
  animation: progressFill 800ms ease forwards;
}
```

### 7.6 Complexity Badge Entrance
```css
@keyframes badgeScale {
  0%   { transform: scale(0); opacity: 0; }
  70%  { transform: scale(1.15); }
  100% { transform: scale(1); opacity: 1; }
}

.complexity-badge {
  animation: badgeScale 400ms cubic-bezier(0.34, 1.56, 0.64, 1) 600ms forwards;
  opacity: 0;
}
```

---

## 8. External Resources

### Fonts (Google Fonts — Free)
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;500;600;700&family=IBM+Plex+Serif:wght@300;400&display=swap" rel="stylesheet">
```

### Icons (Carbon Icons — IBM Official)
```bash
npm install @carbon/icons-react
```
Icons to use:
- `<Analytics />` — BobSpec logo
- `<CircleDash />` — Agent idle
- `<InProgress />` — Agent running
- `<CheckmarkFilled />` — Agent done
- `<ErrorFilled />` — Agent error
- `<Security />` — Security agent
- `<Blueprint />` — Architect agent
- `<Search />` — Edge Case agent
- `<Download />` — Export button
- `<Copy />` — Copy to clipboard

### IBM Carbon React Components (Optional)
```bash
npm install @carbon/react
```
Use for:
- `<Button>` — Analyze button
- `<TextArea>` — Ticket input
- `<Tabs>` — Specification tabs
- `<Tag>` — Complexity badge
- `<InlineLoading>` — Agent loading state
- `<Notification>` — Success/error toasts

### Animations Library
```bash
npm install framer-motion
```
Use for:
- Agent card state transitions
- Spec panel entrance
- Results list stagger

---

## 9. CSS Variables — Complete Setup

```css
/* styles/variables.css */
:root {
  /* IBM Blues */
  --blue-70:  #0043CE;
  --blue-60:  #0F62FE;
  --blue-50:  #4589FF;
  --blue-20:  #A6C8FF;

  /* IBM Grays */
  --gray-100: #161616;
  --gray-90:  #262626;
  --gray-80:  #393939;
  --gray-60:  #6F6F6F;
  --gray-30:  #C6C6C6;
  --gray-20:  #E0E0E0;
  --gray-10:  #F4F4F4;

  /* Agent Colors */
  --purple-40: #BE95FF;
  --red-40:    #FF8389;
  --green-40:  #42BE65;

  /* Semantic */
  --bg-primary:   var(--gray-100);
  --bg-secondary: var(--gray-90);
  --bg-tertiary:  var(--gray-80);
  --text-primary:   var(--gray-10);
  --text-secondary: var(--gray-60);
  --border-color:   var(--gray-80);
  --accent:         var(--blue-60);

  /* Typography */
  --font-sans:  'IBM Plex Sans', sans-serif;
  --font-mono:  'IBM Plex Mono', monospace;
  --font-serif: 'IBM Plex Serif', serif;

  /* Spacing */
  --space-2:  0.5rem;
  --space-4:  1rem;
  --space-6:  1.5rem;
  --space-8:  2rem;
  --space-12: 3rem;
  --space-16: 4rem;

  /* Transitions */
  --transition-fast:   150ms ease;
  --transition-normal: 300ms ease;
  --transition-slow:   500ms cubic-bezier(0.22, 1, 0.36, 1);
}
```

---

## 10. Responsive Breakpoints

```css
/* Mobile first */
--bp-sm:  640px;   /* Small tablets */
--bp-md:  768px;   /* Tablets */
--bp-lg:  1024px;  /* Desktop */
--bp-xl:  1280px;  /* Wide desktop */

/* Agent cards stack on mobile */
@media (max-width: 768px) {
  .agents-grid {
    flex-direction: column;
  }
}
```

---

## 11. Visual States Summary

| Component | Idle | Active | Done | Error |
|---|---|---|---|---|
| Agent Card | Gray border, 60% opacity | Blue glow, pulse dot | Green border, ✓ | Red border, ✕ |
| Analyze Button | Blue solid | Spinner + "Analyzing..." | Reset to idle | Red flash |
| Connector Line | Gray static | Blue fill animation | Full blue | Red |
| Spec Panel | Hidden | — | Slide in from bottom | Error message |
| Result Items | — | — | Stagger fade in | — |
| Complexity Badge | — | — | Scale bounce in | — |

---

## 12. Page Load Sequence

```
0ms    → Header appears (no animation — instant)
100ms  → Hero text fades in
300ms  → Ticket input slides up
500ms  → Agent cards appear with stagger (100ms each)
700ms  → Analyze button fades in
```

```css
@keyframes pageLoad {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0);    }
}

.hero-text    { animation: pageLoad 400ms ease 100ms both; }
.ticket-input { animation: pageLoad 400ms ease 300ms both; }
.agent-card-1 { animation: pageLoad 400ms ease 500ms both; }
.agent-card-2 { animation: pageLoad 400ms ease 600ms both; }
.agent-card-3 { animation: pageLoad 400ms ease 700ms both; }
.analyze-btn  { animation: pageLoad 400ms ease 800ms both; }
```

---

*BobSpec Visual Design Plan — Team Bobsyourdev*
*IBM Carbon Design System — Dark Theme*
