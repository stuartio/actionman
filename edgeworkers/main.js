export function onClientResponse(request, response) {
  response.addHeader('EdgeWorkers', 'Yeehah!')
}