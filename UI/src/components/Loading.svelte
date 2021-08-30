<div />

<style>
  div {
    border: 16px solid var(--bg);
    border-top: 16px solid var(--primary);
    border-radius: 50%;
    width: 48px;
    height: 48px;
    margin: auto;
    animation: spin 1s linear infinite;
  }
  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
</style>
