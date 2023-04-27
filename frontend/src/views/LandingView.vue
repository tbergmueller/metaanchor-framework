<template>
    <div>
       
        <br>

        <label for="text-sip">SIP-Token</label>
        <input type="text" id="text-sip" name="text-sip" v-model="sipToken" disabled>
        <br><br>
        <br>
        <div>
            <label for="text-input">Enter Wallet-Address</label>
            <input type="text" id="text-beneficiary" name="text-beneficiary" v-model="beneficiary">
            <button @click="dropAnchor">Drop Anchor</button>
        </div>
        <div>
            <textarea id="output_window" cols="50" rows="20" v-model="logOutput"></textarea>
        </div>
        

    </div>
  </template>
  
  <script>
  import axios from 'axios';

    const apiClient = axios.create({
    withCredentials: false,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
    },
    });
    
  
  export default {
    data() {
      return {
        data: null,
        isLoading: false,
        error: null,
        logOutput: "Waiting for output..",
        queryParams: {},
        sipToken: null,
        beneficiary: "",
      };
    },
    created() {
        const params = new URLSearchParams(window.location.search);
            for (const [key, value] of params.entries()) {
            this.queryParams[key] = value;
            }
            this.outputSip()
            this.beneficiary = this.queryParams['av_beneficiary']
          
    },
    methods: {
      async dropAnchor() {
        this.clearOutput()
        if (!this.sipToken || !this.sipToken.startsWith('v2.local')) {
				this.appendOutput("ERROR: SIP-Token via GET-Parameter not retrieved correctly. Supposed to be in av_sip and being in format v2.local.*")
				return
			}

			if(!this.isValidEthereumAddress(this.beneficiary)) {
				this.appendOutput("ERROR: Please enter a wallet adress in format 0xabc..123")
				return				
			}

			let bodyParams = {
                "sip_token": this.sipToken,
                "beneficiary": this.beneficiary
			}

			this.appendOutput("Starting to drop anchor.. this may take a while")

      apiClient.post('/drop/', bodyParams) // FIXME this needs configuration!
				.then(response => this.appendOutput(JSON.stringify(response.data)))
				.catch(error => this.appendOutput(error));
            

      },
      outputSip() {
            this.sipToken= this.queryParams['av_sip'];		
		},
        clearOutput() {
            this.logOutput = ""
            this.appendOutput("Start dropping anchor..")

        },
        appendOutput(text) {
			let curText = this.logOutput;
			curText = curText + "\n" + text
            this.logOutput = curText			
		},
        isValidEthereumAddress(address) {
			const regex = /^0x[0-9a-fA-F]{40}$/;
			return regex.test(address);
		},
    },
  };
  </script>