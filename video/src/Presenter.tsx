import React from "react";
import { Img, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { PRESENTER_POSES } from "./assets";
import { theme } from "./theme";

// Framing presets. The character is drawn with its origin at the feet
// (bottom-centre); `feetY` is where the feet land in the 1080p frame.
export const SHOTS = {
  full: { scale: 1, feetY: 1050 },
  half: { scale: 1.75, feetY: 1700 },
  close: { scale: 2.6, feetY: 2420 },
} as const;
export type ShotName = keyof typeof SHOTS;

export type Cue = {
  at: number; // frame the pose switches
  pose: number;
  shot: ShotName;
  x: number; // horizontal centre, 0..1 of frame width
  hidden?: boolean;
};

const CHAR_H = 860;
const SHAKE_BEFORE = 4;
const SHAKE_AFTER = 9;

const activeIndex = (cues: Cue[], frame: number) => {
  let i = 0;
  cues.forEach((c, idx) => {
    if (c.at <= frame) i = idx;
  });
  return i;
};

// Envelope peaking at the swap frame, so the pose change hides inside the shake.
const shakeEnvelope = (frame: number, at: number) =>
  interpolate(frame - at, [-SHAKE_BEFORE, 0, SHAKE_AFTER], [0, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

export const Presenter: React.FC<{ cues: Cue[] }> = ({ cues }) => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const i = activeIndex(cues, frame);
  const cue = cues[i];
  const prev = cues[Math.max(0, i - 1)];

  // Camera move between framings: a quick spring that rides the shake.
  const move = i === 0 ? 1 : spring({ frame: frame - cue.at, fps, config: { damping: 18, stiffness: 160 } });
  const from = SHOTS[prev.shot];
  const to = SHOTS[cue.shot];
  const scale = interpolate(move, [0, 1], [from.scale, to.scale]);
  const feetY = interpolate(move, [0, 1], [from.feetY, to.feetY]);
  const x = interpolate(move, [0, 1], [prev.x, cue.x]) * width;

  // Shake around every pose change (including the one just ahead).
  const next = cues[i + 1];
  const env = Math.max(shakeEnvelope(frame, cue.at), next ? shakeEnvelope(frame, next.at) : 0);
  const shakeX = env * 14 * Math.sin(frame * 2.7);
  const shakeRot = env * 2.4 * Math.sin(frame * 2.1 + 1);
  const pop = 1 + env * 0.035;

  // Constant subtle idle wiggle so the presenter never sits dead still.
  const idleRot = 0.6 * Math.sin(frame / 23) + 0.3 * Math.sin(frame / 11 + 1.3);
  const idleY = 4 * Math.sin(frame / 17);
  const breathe = 1 + 0.006 * Math.sin(frame / 13);

  if (cue.hidden && env === 0) return null;

  return (
    <div
      style={{
        position: "absolute",
        left: x + shakeX,
        top: feetY + idleY,
        transform: `scale(${scale * pop}) rotate(${idleRot + shakeRot}deg) scaleY(${breathe})`,
        transformOrigin: "0 0",
        opacity: cue.hidden ? 0 : 1,
      }}
    >
      <div style={{ position: "absolute", left: 0, bottom: 0, transform: "translateX(-50%)", height: CHAR_H }}>
        {PRESENTER_POSES.length > 0 ? (
          <Img src={PRESENTER_POSES[cue.pose % PRESENTER_POSES.length]} style={{ height: CHAR_H, width: "auto", display: "block" }} />
        ) : (
          <PlaceholderPresenter pose={cue.pose} />
        )}
      </div>
    </div>
  );
};

// Stand-in figure until the real PNG poses are added.
const PlaceholderPresenter: React.FC<{ pose: number }> = ({ pose }) => {
  const arms: Record<number, { l: string; r: string }> = {
    0: { l: "M150,300 L110,470", r: "M250,300 L290,470" },
    1: { l: "M150,300 L110,470", r: "M250,300 L330,260 L360,230" },
    2: { l: "M150,300 L70,260 L50,200", r: "M250,300 L330,260 L350,200" },
    3: { l: "M150,300 L110,470", r: "M250,300 L360,320 L400,300" },
  };
  const a = arms[pose % 4];
  return (
    <svg viewBox="0 0 400 860" height={CHAR_H} style={{ display: "block", overflow: "visible" }}>
      <path d="M160,560 L150,840 M240,560 L250,840" stroke="#2A3A66" strokeWidth={46} strokeLinecap="round" />
      <path d={a.l} stroke={theme.accent} strokeWidth={36} strokeLinecap="round" strokeLinejoin="round" fill="none" />
      <path d={a.r} stroke={theme.accent} strokeWidth={36} strokeLinecap="round" strokeLinejoin="round" fill="none" />
      <rect x={135} y={270} width={130} height={310} rx={50} fill={theme.accent} />
      <circle cx={200} cy={190} r={78} fill="#F2C9A0" />
      <text x={200} y={460} textAnchor="middle" fontFamily={theme.font} fontWeight={800} fontSize={30} fill={theme.bg}>
        POSE {(pose % 4) + 1}
      </text>
    </svg>
  );
};
