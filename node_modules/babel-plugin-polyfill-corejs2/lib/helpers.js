"use strict";

exports.__esModule = true;
exports.hasMinVersion = hasMinVersion;
var _semverV = _interopRequireDefault(require("@nicolo-ribaudo/semver-v6"));
function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }
/// <reference path="../../../lib/semver.d.ts" />

function hasMinVersion(minVersion, runtimeVersion) {
  // If the range is unavailable, we're running the script during Babel's
  // build process, and we want to assume that all versions are satisfied so
  // that the built output will include all definitions.
  if (!runtimeVersion || !minVersion) return true;

  // semver.intersects() has some surprising behavior with comparing ranges
  // with preprelease versions. We add '^' to ensure that we are always
  // comparing ranges with ranges, which sidesteps this logic.
  // For example:
  //
  //   semver.intersects(`<7.0.1`, "7.0.0-beta.0") // false - surprising
  //   semver.intersects(`<7.0.1`, "^7.0.0-beta.0") // true - expected
  //
  // This is because the first falls back to
  //
  //   semver.satisfies("7.0.0-beta.0", `<7.0.1`) // false - surprising
  //
  // and this fails because a prerelease version can only satisfy a range
  // if it is a prerelease within the same major/minor/patch range.
  //
  // Note: If this is found to have issues, please also revist the logic in
  // babel-core's availableHelper() API.
  if (_semverV.default.valid(runtimeVersion)) runtimeVersion = `^${runtimeVersion}`;
  return !_semverV.default.intersects(`<${minVersion}`, runtimeVersion) && !_semverV.default.intersects(`>=8.0.0`, runtimeVersion);
}