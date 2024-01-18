"""Device handler for Tuya ZG-205Z-A Mini 24Ghz human presence sensor."""
"""https://github.com/zigpy/zha-device-handlers/issues/2551#issuecomment-1826440010 """

from typing import Dict
from zigpy.profiles import zgp, zha
from zigpy.quirks import CustomDevice
import zigpy.types as t

from zigpy.zcl.clusters.general import Basic, Identify, GreenPowerProxy, AnalogOutput
from zigpy.zcl.clusters.security import IasZone
from zigpy.zcl.clusters.measurement import (
    IlluminanceMeasurement,
    OccupancySensing,
)

from zhaquirks import MotionWithReset
from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.tuya import TuyaLocalCluster, TuyaNewManufCluster, TuyaZBE000Cluster
from zhaquirks.tuya.mcu import (
    DPToAttributeMapping,
    TuyaAttributesCluster,
    TuyaMCUCluster,
)

class MotionCluster(MotionWithReset):
    """Motion cluster."""

    reset_s: int = 60

class TuyaOccupancySensing(OccupancySensing, TuyaLocalCluster):
    """Tuya local OccupancySensing cluster."""

class TuyaMmwRadarFadingTime(TuyaAttributesCluster, AnalogOutput):
    """AnalogOutput cluster for fading time."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self._update_attribute(self.attributes_by_name["description"].id, "Fading time")
        self._update_attribute(self.attributes_by_name["min_present_value"].id, 0)
        self._update_attribute(self.attributes_by_name["max_present_value"].id, 600)
        self._update_attribute(self.attributes_by_name["resolution"].id, 1)
        self._update_attribute(
            self.attributes_by_name["engineering_units"].id, 73
        )

class TuyaMmwRadarLargeMotionDetectionSensitivity(TuyaAttributesCluster, AnalogOutput):
    """AnalogOutput cluster for Large motion detection sensitivity."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self._update_attribute(self.attributes_by_name["description"].id, "Large motion sensitivity")
        self._update_attribute(self.attributes_by_name["min_present_value"].id, 0)
        self._update_attribute(self.attributes_by_name["max_present_value"].id, 10)
        self._update_attribute(self.attributes_by_name["resolution"].id, 1)


class TuyaMmwRadarLargeMotionDetectionDistance(TuyaAttributesCluster, AnalogOutput):
    """AnalogOutput cluster for Large motion detection distance."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self._update_attribute(self.attributes_by_name["description"].id, "Large motion detection distance")
        self._update_attribute(self.attributes_by_name["min_present_value"].id, 0)
        self._update_attribute(self.attributes_by_name["max_present_value"].id, 1000)
        self._update_attribute(self.attributes_by_name["resolution"].id, 10)
        self._update_attribute(
            self.attributes_by_name["engineering_units"].id, 118
        )

class TuyaMmwRadarSmallMotionDetectionSensitivity(TuyaAttributesCluster, AnalogOutput):
    """AnalogOutput cluster for Small motion detection sensitivity."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self._update_attribute(self.attributes_by_name["description"].id, "Small motion sensitivity")
        self._update_attribute(self.attributes_by_name["min_present_value"].id, 0)
        self._update_attribute(self.attributes_by_name["max_present_value"].id, 10)
        self._update_attribute(self.attributes_by_name["resolution"].id, 1)


class TuyaMmwRadarSmallMotionDetectionDistance(TuyaAttributesCluster, AnalogOutput):
    """AnalogOutput cluster for Small motion detection distance."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self._update_attribute(self.attributes_by_name["description"].id, "Small motion detection distance")
        self._update_attribute(self.attributes_by_name["min_present_value"].id, 0)
        self._update_attribute(self.attributes_by_name["max_present_value"].id, 600)
        self._update_attribute(self.attributes_by_name["resolution"].id, 10)
        self._update_attribute(
            self.attributes_by_name["engineering_units"].id, 118
        )

class TuyaMmwRadarStaticMotionDetectionSensitivity(TuyaAttributesCluster, AnalogOutput):
    """AnalogOutput cluster for Static motion detection sensitivity."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self._update_attribute(self.attributes_by_name["description"].id, "Static motion sensitivity")
        self._update_attribute(self.attributes_by_name["min_present_value"].id, 0)
        self._update_attribute(self.attributes_by_name["max_present_value"].id, 10)
        self._update_attribute(self.attributes_by_name["resolution"].id, 1)


class TuyaMmwRadarStaticMotionDetectionDistance(TuyaAttributesCluster, AnalogOutput):
    """AnalogOutput cluster for Static motion detection distance."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self._update_attribute(self.attributes_by_name["description"].id, "Static motion detection distance")
        self._update_attribute(self.attributes_by_name["min_present_value"].id, 0)
        self._update_attribute(self.attributes_by_name["max_present_value"].id, 600)
        self._update_attribute(self.attributes_by_name["resolution"].id, 10)
        self._update_attribute(
            self.attributes_by_name["engineering_units"].id, 118
        )


class MmwRadarManufCluster(TuyaMCUCluster):
    """Tuya ZG-205Z-A Mini 24Ghz human presence sensor cluster."""

    attributes = TuyaMCUCluster.attributes.copy()
    attributes.update(
        {
            # ramdom attribute IDs
            #0xEF02: ("motion_detection_sensitivity", t.uint32_t, True),
            0xEF03: ("mov_minimum_distance", t.uint32_t, True),
            #0xEF04: ("motion_detection_distance", t.uint32_t, True),
            0xEF05: ("human_motion_state", t.enum8, True),
            #0xEF65: ("fading_time", t.uint32_t, True),
            0xEF66: ("motion_false_detection", t.uint32_t, True),
            #0xEF67: ("small_motion_detection_distance", t.uint32_t, True),
            #0xEF69: ("small_motion_detection_sensitivity", t.uint32_t, True),
            0xEF6A: ("illuminance_value", t.uint32_t, True),
            0xEF6B: ("indicator", t.enum8, True),
            #0xEF6C: ("static_detection_distance", t.uint32_t, True),
            #0xEF06: ("static_detection_sensitivity", t.uint32_t, True),
            0xEF07: ("micro_minimum_distance", t.uint32_t, True),
            0xEF08: ("motionless_minimum_distance", t.uint32_t, True),
            0xEF09: ("reset_setting", t.uint32_t, True),
            0xEF0A: ("breathe_false_detection", t.uint32_t, True),
            0xEF0B: ("time", t.uint32_t, True),
            0xEF0C: ("alarm_time", t.uint32_t, True),
            0xEF0D: ("alarm_volume", t.enum8, True),
            0xEF0E: ("working_mode", t.enum8, True),
            0xEF0F: ("auto1", t.uint32_t, True),
            0xEF10: ("auto2", t.uint32_t, True),
            0xEF11: ("auto3", t.uint32_t, True),
        }
    )

    dp_to_attribute: Dict[int, DPToAttributeMapping] = {
        1: DPToAttributeMapping(
            TuyaOccupancySensing.ep_attribute,
            "occupancy",
        ),
        2: DPToAttributeMapping(
            TuyaMmwRadarLargeMotionDetectionSensitivity.ep_attribute,
            "present_value",
        ),
        3: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "mov_minimum_distance",
        ),
        4: DPToAttributeMapping(
            TuyaMmwRadarLargeMotionDetectionDistance.ep_attribute,
            "present_value",
        ),
        101: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "human_motion_state",
        ),
        102: DPToAttributeMapping(
            TuyaMmwRadarFadingTime.ep_attribute,
            "present_value",
        ),
        103: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "motion_false_detection",
        ),
        104: DPToAttributeMapping(
            TuyaMmwRadarSmallMotionDetectionDistance.ep_attribute,
            "present_value",
        ),
        105: DPToAttributeMapping(
            TuyaMmwRadarSmallMotionDetectionSensitivity.ep_attribute,
            "present_value",
        ),
        106: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "illuminance_value",
        ),
        107: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "indicator",
        ),
        108: DPToAttributeMapping(
            TuyaMmwRadarStaticMotionDetectionDistance.ep_attribute,
            "present_value",
        ),
        109: DPToAttributeMapping(
            TuyaMmwRadarStaticMotionDetectionSensitivity.ep_attribute,
            "present_value",
        ),
        110: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "micro_minimum_distance",
        ),
        111: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "motionless_minimum_distance",
        ),
        112: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "reset_setting",
        ),
        113: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "breathe_false_detection",
        ),
        114: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "time",
        ),
        115: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "alarm_time",
        ),
        116: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "alarm_volume",
        ),
        117: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "working_mode",
        ),
        118: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "auto1",
        ),
        119: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "auto2",
        ),
        120: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "auto3",
        ),
    }

    data_point_handlers = {
        1: "_dp_2_attr_update",
        2: "_dp_2_attr_update",
        3: "_dp_2_attr_update",
        4: "_dp_2_attr_update",
        101: "_dp_2_attr_update",
        102: "_dp_2_attr_update",
        103: "_dp_2_attr_update",
        104: "_dp_2_attr_update",
        105: "_dp_2_attr_update",
        106: "_dp_2_attr_update",
        107: "_dp_2_attr_update",
        108: "_dp_2_attr_update",
        109: "_dp_2_attr_update",
        110: "_dp_2_attr_update",
        111: "_dp_2_attr_update",
        112: "_dp_2_attr_update",
        113: "_dp_2_attr_update",
        114: "_dp_2_attr_update",
        115: "_dp_2_attr_update",
        116: "_dp_2_attr_update",
        117: "_dp_2_attr_update",
        118: "_dp_2_attr_update",
        119: "_dp_2_attr_update",
        120: "_dp_2_attr_update",
    }

class TS0225Radar(CustomDevice):
    """Quirk for Tuya ZG-205Z-A Mini 5.8Ghz human presence sensor."""

    signature = {
        #  endpoint=1, profile=260, device_type=1026, device_version=1,
        #  input_clusters=["0x0000", "0x0003", "0x0400", "0x0500","0xe000","0xe002", "0xee00", "0xef00"], output_clusters=[])
        #  "0x0003", "0xe000", "0xe002", "0xee00", "0xef00"
        MODELS_INFO: [("_TZE200_2aaelwxk", "TS0225")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.IAS_ZONE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    IlluminanceMeasurement.cluster_id,
                    IasZone.cluster_id,
                    TuyaZBE000Cluster.cluster_id,
                    0xE002, # Unknown
                    0xEE00, # Unknown
                    TuyaNewManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    TuyaZBE000Cluster.cluster_id,
                    0xE002, # Unknown
                    0xEE00, # Unknown
                    TuyaNewManufCluster.cluster_id,
                ],
            },
            242: {
                # "profile_id": "0xA1E0", "device_type": "0x0061",
                # "in_clusters": [], "out_clusters": ["0x0021"]
                PROFILE_ID: zgp.PROFILE_ID,
                DEVICE_TYPE: zgp.DeviceType.PROXY_BASIC,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    IlluminanceMeasurement.cluster_id,
                    MotionCluster,
                    TuyaZBE000Cluster,
                    MmwRadarManufCluster,
                    TuyaOccupancySensing,

                ],
                OUTPUT_CLUSTERS: [],
            },
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.COMBINED_INTERFACE,
                INPUT_CLUSTERS: [
                    TuyaMmwRadarFadingTime,
                ],
                OUTPUT_CLUSTERS: [],
            },
            3: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.COMBINED_INTERFACE,
                INPUT_CLUSTERS: [
                    TuyaMmwRadarLargeMotionDetectionSensitivity,
                ],
                OUTPUT_CLUSTERS: [],
            },
            4: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.COMBINED_INTERFACE,
                INPUT_CLUSTERS: [
                    TuyaMmwRadarLargeMotionDetectionDistance,
                ],
                OUTPUT_CLUSTERS: [],
            },
            5: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.COMBINED_INTERFACE,
                INPUT_CLUSTERS: [
                    TuyaMmwRadarSmallMotionDetectionSensitivity,
                ],
                OUTPUT_CLUSTERS: [],
            },
            6: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.COMBINED_INTERFACE,
                INPUT_CLUSTERS: [
                    TuyaMmwRadarSmallMotionDetectionDistance,
                ],
                OUTPUT_CLUSTERS: [],
            },
            7: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.COMBINED_INTERFACE,
                INPUT_CLUSTERS: [
                    TuyaMmwRadarStaticMotionDetectionSensitivity,
                ],
                OUTPUT_CLUSTERS: [],
            },
            8: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.COMBINED_INTERFACE,
                INPUT_CLUSTERS: [
                    TuyaMmwRadarStaticMotionDetectionDistance,
                ],
                OUTPUT_CLUSTERS: [],
            },
            242: {
                PROFILE_ID: zgp.PROFILE_ID,
                DEVICE_TYPE: zgp.DeviceType.PROXY_BASIC,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }
