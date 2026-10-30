// Placeholder palette. Swap for WINC Wire's brand colours once confirmed.
export const theme = {
  bg: "#0B1530",
  bg2: "#13224A",
  panel: "#1B2E5E",
  ink: "#F4F6FB",
  dim: "#9AA8C7",
  accent: "#2EC4B6",
  warn: "#FFB547",
  danger: "#FF5A5F",
  font: "Inter, sans-serif",
};

export const FPS = 30;
export const s = (seconds: number) => Math.round(seconds * FPS);
