/** @odoo-module **/

// the above @odoo-module line tells odoo that this file is to be integrated
// into the odoo ecosystem

import publicWidget from "@web/legacy/js/public/public_widget";
import {
    ConnectionAbortedError,
    ConnectionLostError,
    RPCError,
    rpc,
    rpcBus,
} from "@web/core/network/rpc";

const MyListWidget = publicWidget.Widget.extend({
    selector: '#dynamic_list_container', // This widget will be active for this selector
    
    start: async function () {
        console.log("Custom JS: MyListWidget started. Making RPC call...");

        try {
            const result = await rpc('/my_list_content', {
                params: {} // The `params` key is required for a JSON-RPC call
            });

            console.log("Custom JS: RPC call successful. Result:", result);
            if (result && result.html) {
                this.$el.html(result.html);
            } else {
                this.$el.html("Error: Could not load list.");
            }
        } catch (error) {
            console.error("Custom JS: RPC Error:", error);
            this.$el.html(`Error: An error occurred while loading the list. See console for details.`);
        }
    },
});

// Register the widget so Odoo's frontend framework can find and use it.
publicWidget.registry.myListWidget = MyListWidget;