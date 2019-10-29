
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url: 'shoot.auth0.com', // the auth0 domain prefix
    audience: 'https://myappapiidurl', // the api audience set for the auth0 app
    clientId: 'Q2lozWrvvtEMtaltHDEC1FL1F5K07Me7', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:4200', // the base url of the running angular application. 
  }
};
