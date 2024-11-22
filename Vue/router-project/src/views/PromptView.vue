<template>
    # Chat Interface

    <div class="flex flex-col h-screen p-4">
        <div class="flex-1 overflow-y-auto bg-gray-100 p-4 rounded-lg shadow-md">
            <div class="chat-history">
                <!-- Chat messages will be dynamically inserted here -->
                <div class="message mb-2">
                    <span class="font-bold">User:</span> Hello, how can I help you?
                </div>
                <div class="message mb-2">
                    <span class="font-bold">Bot:</span> I am here to assist you with your queries.
                </div>
            </div>
        </div>
        <div class="flex items-center mt-4">
            <textarea class="flex-1 p-2 border rounded-lg" rows="2" placeholder="Type your message..."></textarea>
            <button class="ml-2 p-2 bg-blue-500 text-white rounded-lg">
                <i class="fas fa-paper-plane"></i>
            </button>
        </div>
    </div>

</template>

<script>
export default {

}
</script>

<style></style>