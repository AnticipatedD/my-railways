export type DeviceCommand = {
  name: string;
  args?: Record<string, unknown>;
};

export function handleMcpRequest(command: DeviceCommand) {
  return {
    ok: true,
    command: command.name,
    status: "queued",
  };
}
