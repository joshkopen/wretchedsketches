import React, { Component } from "react";
import socketIOClient from "socket.io-client";

function ListenForEvent(listener_event, socket_endpoint, outcome_function) {
  state = {
    response: false,
    endpoint: socket_endpoint
  };
  const socket = socketIOClient(endpoint);
  socket.on(listener_event, data => {
    //call the main funciton to come get this state
    outcome_function(data);
  });
}

export default ListenForEvent;