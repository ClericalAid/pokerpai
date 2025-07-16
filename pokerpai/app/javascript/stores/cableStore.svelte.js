import consumer from '../services/cable.js';
import { updateGameState } from './gameState.svelte.js';

let connectionState = $state({
  isConnected: false,
  isConnecting: false,
  error: null
});

let subscription = null;

export function initializeCableConnection() {
  if (subscription) {
    console.warn('Cable connection already initialized');
    return;
  }

  connectionState.isConnecting = true;
  connectionState.error = null;

  subscription = consumer.subscriptions.create("MessageChannel", {
    connected() {
      console.log("Connected to MessageChannel");
      connectionState.isConnected = true;
      connectionState.isConnecting = false;
      connectionState.error = null;

      this.send({ message: "Hello from frontend!" });
    },

    disconnected() {
      console.log("Disconnected from MessageChannel");
      connectionState.isConnected = false;
      connectionState.isConnecting = false;
    },

    received(data) {
      console.log("Received message:", data);

      if (data.command === "get_game") {
        updateGameState(data);
      }
    }
  });
}

export function destroyCableConnection() {
  if (subscription) {
    subscription.unsubscribe();
    subscription = null;
  }

  connectionState.isConnected = false;
  connectionState.isConnecting = false;
  connectionState.error = null;
}

export function sendMessage(data) {
  if (!subscription) {
    console.error('Cable connection not initialized');
    return false;
  }

  if (!connectionState.isConnected) {
    console.error('Cable connection not established');
    return false;
  }

  subscription.send(data);
  return true;
}

export function getConnectionState() {
  return connectionState;
}

export function getSubscription() {
  return subscription;
}

export function isConnected() {
  return connectionState.isConnected;
}

export function isConnecting() {
  return connectionState.isConnecting;
}

export function hasError() {
  return connectionState.error !== null;
}
