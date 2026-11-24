// Graph used when the URL has no ?graphid=. Set VITE_GRAPH_ID at build time to change it without editing code.
export const DEFAULT_GRAPH_ID = import.meta.env.VITE_GRAPH_ID || '2017158';

export const graphId = () => new URLSearchParams(window.location.search).get('graphid') || DEFAULT_GRAPH_ID;
