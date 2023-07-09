"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.hasMinVersion = hasMinVersion;
var _semverV = require("@nicolo-ribaudo/semver-v6");
function hasMinVersion(minVersion, runtimeVersion) {
  if (!runtimeVersion) return true;
  if (_semverV.valid(runtimeVersion)) runtimeVersion = `^${runtimeVersion}`;
  return !_semverV.intersects(`<${minVersion}`, runtimeVersion) && !_semverV.intersects(`>=8.0.0`, runtimeVersion);
}

//# sourceMappingURL=helpers.js.map
