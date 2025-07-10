<script>
  import PokerTable from './PokerTable.svelte';
  import { onMount, onDestroy } from 'svelte';
  import consumer from '../services/cable.js';
  import { getGameState, updateGameState } from '../stores/gameState.svelte.js';

  let subscription;

  // Get the reactive game state
  const gameState = getGameState();

  onMount(() => {
    // Set up ActionCable connection
    subscription = consumer.subscriptions.create("MessageChannel", {
      connected() {
        console.log("Connected to MessageChannel");
        // Send a test message once connected
        this.send({ message: "Hello from frontend!" });
      },
      disconnected() {
        console.log("Disconnected from MessageChannel");
        // Clear interval if it exists
        if (this.intervalId) {
          clearInterval(this.intervalId);
        }
      },
      received(data) {
        console.log("Received message:", data);

        // Check if this is a game state message
        if (data.command === "get_game") {
          updateGameState(data);
        }
      }
    });
  });

  onDestroy(() => {
    if (subscription) {
      // Clear interval if it exists
      if (subscription.intervalId) {
        clearInterval(subscription.intervalId);
      }
      subscription.unsubscribe();
    }
  });
</script>

<div class="bg-gray-900 text-gray-200 min-h-screen flex justify-center items-center">
  <PokerTable {gameState} />
</div>
