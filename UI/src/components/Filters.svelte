<script>
  import { createEventDispatcher } from "svelte";

  export let duration = "Month";
  const dispatch = createEventDispatcher();
</script>

<h5>
  <i class="fas fa-list" />
  <input
    type="radio"
    name="duration"
    bind:group={duration}
    id="today"
    value="today"
  />
  <label for="today">Today</label>
  <input
    type="radio"
    name="duration"
    bind:group={duration}
    id="month"
    value="month"
  />
  <label for="month">This Month</label>
  <input
    type="radio"
    name="duration"
    bind:group={duration}
    id="year"
    value="year"
  />
  <label for="year">This Year</label>
  <i class="fas fa-download export" on:click={() => dispatch("export")} />
</h5>

<style>
  h5 {
    display: flex;
    align-items: center;
    color: var(--heading);
    margin-top: 0;
  }
  h5 > * {
    margin-right: 1rem;
    padding-bottom: 0.25rem;
    cursor: pointer;
  }
  input {
    margin: 0;
    padding: 0;
    width: 10px;
    visibility: hidden;
  }
  input:checked + label {
    color: var(--secondary);
    border-bottom: 2px solid var(--heading);
  }
</style>
