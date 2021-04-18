import Backendless from "backendless";

const APP_ID = "5CAB1EEE-A293-4B63-8B9D-53F3E0E80B48";
const API_KEY = "B31B1CDC-FDF9-4B20-98A0-3DF0D48BCC1A";
Backendless.serverURL = "https://eu-api.backendless.com";
Backendless.initApp(APP_ID, API_KEY);

export default Backendless;
