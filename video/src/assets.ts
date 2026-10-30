import { staticFile } from "remotion";

// Drop the presenter PNGs into public/presenter/ and list them here in order.
// While this list is empty, a placeholder presenter is drawn instead.
export const PRESENTER_POSES: string[] = [
  // staticFile("presenter/pose1.png"),
];

// ElevenLabs voiceover; set to staticFile("audio/voiceover.mp3") once added.
export const VOICEOVER: string | null = null;

export { staticFile };
