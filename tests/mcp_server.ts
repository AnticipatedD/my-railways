export type DeviceStatus = {
  device_id: string;
  platform: "android" | "ios";
  status: "online" | "offline";
};

export const mockDevices: DeviceStatus[] = [
  { device_id: "demo-device-001", platform: "android", status: "online" },
  { device_id: "demo-device-002", platform: "ios", status: "offline" }
];
