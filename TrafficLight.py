class TrafficLight:
    def __init__(self, signal_id, timing):
        self.signal_id = signal_id
        self.timing = timing  # Timing in seconds
        self.active = True

    def update_timing(self, new_timing):
        self.timing = new_timing

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def __str__(self):
        return f"TrafficLight(signal_id={self.signal_id}, timing={self.timing}, active={self.active})"
class TrafficLightSystem:
    def __init__(self):
        self.lights = {}

    def create_traffic_light(self, signal_id, timing):
        if signal_id not in self.lights:
            self.lights[signal_id] = TrafficLight(signal_id, timing)
            return self.lights[signal_id]
        raise ValueError("Traffic light with this ID already exists.")

    def read_traffic_light(self, signal_id):
        return self.lights.get(signal_id)

    def update_traffic_light(self, signal_id, new_timing):
        if signal_id in self.lights:
            self.lights[signal_id].update_timing(new_timing)
        else:
            raise ValueError("Traffic light not found.")

    def delete_traffic_light(self, signal_id):
        if signal_id in self.lights:
            del self.lights[signal_id]
        else:
            raise ValueError("Traffic light not found.")

    def optimize_traffic_signals(self, signal_id):
        # Simplified optimization: Set timing to a predefined value based on some logic
        if signal_id in self.lights:
            # For demonstration, let's say we optimize to 30 seconds
            self.lights[signal_id].update_timing(30)
            return self.lights[signal_id]
        raise ValueError("Traffic light not found.")

    def analyze_traffic_impact(self, impact_id):
        # Simulated analysis of impact: returning a fake report based on impact_id
        return f"Analysis Report for impact ID {impact_id}: Optimization appears to improve flow."
import unittest

class TestTrafficLightSystem(unittest.TestCase):
    def setUp(self):
        self.system = TrafficLightSystem()
        self.system.create_traffic_light("A", 45)
        self.system.create_traffic_light("B", 60)

    def test_create_traffic_light(self):
        self.system.create_traffic_light("C", 30)
        self.assertEqual(self.system.read_traffic_light("C").timing, 30)

    def test_update_traffic_light(self):
        self.system.update_traffic_light("A", 50)
        self.assertEqual(self.system.read_traffic_light("A").timing, 50)

    def test_delete_traffic_light(self):
        self.system.delete_traffic_light("B")
        self.assertIsNone(self.system.read_traffic_light("B"))

    def test_optimize_traffic_signals(self):
        optimized_light = self.system.optimize_traffic_signals("A")
        self.assertEqual(optimized_light.timing, 30)

    def test_analyze_traffic_impact(self):
        report = self.system.analyze_traffic_impact("1")
        self.assertIn("Analysis Report", report)

    def test_error_on_duplicate_creation(self):
        with self.assertRaises(ValueError):
            self.system.create_traffic_light("A", 20)

    def test_error_on_update_nonexistent(self):
        with self.assertRaises(ValueError):
            self.system.update_traffic_light("Z", 20)

    def test_error_on_delete_nonexistent(self):
        with self.assertRaises(ValueError):
            self.system.delete_traffic_light("Z")

if __name__ == "__main__":
    unittest.main()
