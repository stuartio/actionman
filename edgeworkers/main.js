export function onClientResponse(request, response) {
  response.addHeader('EdgeWorkers', 'Version 0.1.4')
}