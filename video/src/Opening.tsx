import React from "react";
import { AbsoluteFill, Audio, Sequence, interpolate, useCurrentFrame } from "remotion";
import { VOICEOVER } from "./assets";
import { Background, BrollSlot, Building, CalendarFlip, CandidateCard, Flash, Kinetic } from "./graphics";
import { Cue, Presenter } from "./Presenter";
import { s, theme } from "./theme";

// Beat timings (seconds) are estimates until the ElevenLabs audio is in;
// retime these against the waveform.
const T = {
  sixMonths: 0,
  switchedOn: 2.4,
  brollStart: 5.0,
  why: 7.0,
  whySlam: 8.4,
  nobody: 9.2,
  notIT: 11.3,
  notLawyers: 12.3,
  notSupplier: 13.3,
  notHR: 14.3,
  end: 16,
};

const cues: Cue[] = [
  { at: 0, pose: 0, shot: "full", x: 0.2 },
  { at: s(T.brollStart), pose: 0, shot: "full", x: 0.2, hidden: true },
  { at: s(T.why), pose: 1, shot: "half", x: 0.27 },
  { at: s(T.nobody), pose: 2, shot: "close", x: 0.5 },
  { at: s(T.notIT), pose: 3, shot: "full", x: 0.8 },
  { at: s(T.notHR), pose: 1, shot: "half", x: 0.76 },
];

// A short whole-frame jolt for the "Not even YOUR HR!!" hit.
const useImpact = (at: number) => {
  const frame = useCurrentFrame();
  const e = interpolate(frame - at, [0, 2, 12], [0, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return `translate(${e * 16 * Math.sin(frame * 3.1)}px, ${e * 10 * Math.cos(frame * 2.3)}px)`;
};

export const Opening: React.FC = () => {
  const impact = useImpact(s(T.notHR) + 4);
  return (
    <AbsoluteFill style={{ background: theme.bg }}>
      <AbsoluteFill style={{ transform: impact }}>
        <Background />

        {/* 0–5s: "Six months ago, YOUR company switched on an AI tool…" */}
        <Sequence from={0} durationInFrames={s(T.brollStart)}>
          <Kinetic text="6 MONTHS AGO" at={4} x={1180} y={90} size={84} align="center" />
          <Building
            x={900}
            y={250}
            scale={1}
            at={10}
            windows={[{ label: "IT" }, { label: "LEGAL" }, { label: "SUPPLIER" }, { label: "HR" }]}
            chipAt={s(T.switchedOn)}
            onAt={s(T.switchedOn) + 22}
          />
          <Kinetic text="AI SCREENING TOOL" at={s(T.switchedOn) + 30} x={1180} y={940} size={52} align="center" color={theme.accent} />
        </Sequence>

        {/* 7–9.2s: "…asking YOU a simple question: WHY?" */}
        <Sequence from={s(T.why)} durationInFrames={s(T.nobody - T.why)}>
          <CandidateCard x={1050} y={260} at={0} />
          <CalendarFlip x={1600} y={420} at={4} />
          <Kinetic text="WHY?" at={s(T.whySlam - T.why)} x={1380} y={760} size={200} color={theme.warn} align="center" />
        </Sequence>

        {/* 9.2–11.3s: "And NOBODY in your building can answer." */}
        <Sequence from={s(T.nobody)} durationInFrames={s(T.notIT - T.nobody)}>
          <Kinetic text="NOBODY" at={0} x={960} y={300} size={330} align="center" color={theme.panel} stagger={0} />
        </Sequence>
      </AbsoluteFill>

      {/* Presenter sits above the background layer but under the b-roll. */}
      <AbsoluteFill style={{ transform: impact }}>
        <Sequence from={s(T.notIT)} durationInFrames={s(T.end - T.notIT)}>
          <Building
            x={160}
            y={210}
            scale={1.15}
            at={0}
            windows={[
              { label: "IT", offAt: 8 },
              { label: "LEGAL", offAt: s(T.notLawyers - T.notIT) },
              { label: "SUPPLIER", offAt: s(T.notSupplier - T.notIT) },
              { label: "HR", offAt: s(T.notHR - T.notIT) + 4, danger: true },
            ]}
          />
          <Kinetic text="NOT EVEN YOUR HR!!" at={s(T.notHR - T.notIT) + 4} x={960} y={70} size={110} align="center" color={theme.danger} stagger={3} />
        </Sequence>
        <Presenter cues={cues} />
        <Sequence from={s(T.nobody) + 10} durationInFrames={s(T.notIT - T.nobody) - 10}>
          <Kinetic text="can answer." at={0} x={960} y={900} size={96} align="center" />
        </Sequence>
      </AbsoluteFill>

      {/* 5–7s: b-roll slot */}
      <Sequence from={s(T.brollStart)} durationInFrames={s(T.why - T.brollStart)}>
        <BrollSlot
          id="01"
          note="Close-up: a person at a laptop opening a job rejection email, then pausing, frustrated. Moody office or home lighting."
        />
      </Sequence>

      <Flash at={s(T.notHR) + 4} />
      {VOICEOVER && <Audio src={VOICEOVER} />}
    </AbsoluteFill>
  );
};

export const OPENING_FRAMES = s(T.end);
