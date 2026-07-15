class V2FunCharacterAnimatorClient:
    def animate_character(self, image_keypoints: list[dict]) -> dict:
        return {"skeleton_pose_map": {"joints_count": len(image_keypoints), "rigging_status": "rigged_successfully"}}