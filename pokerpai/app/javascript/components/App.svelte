<script>
  import PokerTable from './PokerTable.svelte';
  import { onMount, onDestroy } from 'svelte';
  import { getGameState } from '../stores/gameState.svelte.js';
  import {
    initializeCableConnection,
    destroyCableConnection,
    getConnectionState,
  } from '../stores/cableStore.svelte.js';

  const gameState = getGameState();

  const connectionState = getConnectionState();

  onMount(() => {
    initializeCableConnection();
  });

  onDestroy(() => {
    destroyCableConnection();
  });
</script>

<div class="bg-gray-900 text-gray-200 min-h-screen flex justify-center items-center">
  <PokerTable {gameState} />
</div>
