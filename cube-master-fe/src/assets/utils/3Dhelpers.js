import * as THREE from "three";

export const materials = {
    blue: new THREE.MeshPhysicalMaterial({
        emissive: 0x0051ba,
        metalness: 0.9,
    }),
    red: new THREE.MeshPhysicalMaterial({
        emissive: 0xc41e3a,
        metalness: 0.9,
    }),
    white: new THREE.MeshPhysicalMaterial({
        emissive: 0xffffff,
        metalness: 0.9,
    }),
    green: new THREE.MeshPhysicalMaterial({
        emissive: 0x009b48,
        metalness: 0.9,
    }),
    yellow: new THREE.MeshPhysicalMaterial({
        emissive: 0xffd500,
        metalness: 0.9,
    }),
    orange: new THREE.MeshPhysicalMaterial({
        emissive: 0xff5800,
        metalness: 0.9,
    }),
    black: new THREE.MeshPhysicalMaterial({
        emissive: 0x1a1a1a,
        metalness: 0.9,
    }),
};

export const moveNotationTo3d = {
    f: { position: "front", direction: -1 },
    "f'": { position: "front", direction: 1 },
    u: { position: "top", direction: -1 },
    "u'": { position: "top", direction: 1 },
    r: { position: "right", direction: -1 },
    "r'": { position: "right", direction: 1 },
    l: { position: "left", direction: 1 },
    "l'": { position: "left", direction: -1 },
    b: { position: "back", direction: 1 },
    "b'": { position: "back", direction: -1 },
    d: { position: "bottom", direction: 1 },
    "d'": { position: "bottom", direction: -1 },
    ru: { position: "rotateUp", direction: -1 },
    rd: { position: "rotateDown", direction: 1 },
    rr: { position: "rotateRight", direction: 1 },
    rl: { position: "rotateLeft", direction: -1 },
};

export const opposite_moves = {
    "f": "f'",
    "f'": "f",
    "r": "r'",
    "r'": "r",
    "l": "l'",
    "l'": "l",
    "u": "u'",
    "u'": "u",
    "d": "d'",
    "d'": "d",
    "b": "b'",
    "b'": "b",
    "rr": "rl",
    "rl": "rr",
    "ru": "rd",
    "rd": "ru",
}

export const initialColors = {
    front: [
        "blue",
        "blue",
        "blue",
        "blue",
        "blue",
        "blue",
        "blue",
        "blue",
        "blue",
    ],
    back: [
        "green",
        "green",
        "green",
        "green",
        "green",
        "green",
        "green",
        "green",
        "green",
    ],
    left: [
        "orange",
        "orange",
        "orange",
        "orange",
        "orange",
        "orange",
        "orange",
        "orange",
        "orange",
    ],
    right: ["red", "red", "red", "red", "red", "red", "red", "red", "red"],
    top: [
        "white",
        "white",
        "white",
        "white",
        "white",
        "white",
        "white",
        "white",
        "white",
    ],
    bottom: [
        "yellow",
        "yellow",
        "yellow",
        "yellow",
        "yellow",
        "yellow",
        "yellow",
        "yellow",
        "yellow",
    ],
};
export const stateMap = {
    0: {
        1: { position: "left", no: 6 },
        3: { position: "bottom", no: 6 },
        5: { position: "back", no: 8 },
    },
    1: {
        1: { position: "left", no: 7 },
        3: { position: "bottom", no: 3 },
    },
    2: {
        1: { position: "left", no: 8 },
        3: { position: "bottom", no: 0 },
        4: { position: "front", no: 6 },
    },
    3: {
        1: { position: "left", no: 3 },
        5: { position: "back", no: 5 },
    },
    4: {
        1: { position: "left", no: 4 },
    },
    5: {
        1: { position: "left", no: 5 },
        4: { position: "front", no: 3 },
    },
    6: {
        1: { position: "left", no: 0 },
        2: { position: "top", no: 0 },
        5: { position: "back", no: 2 },
    },
    7: {
        1: { position: "left", no: 1 },
        2: { position: "top", no: 3 },
    },
    8: {
        1: { position: "left", no: 2 },
        2: { position: "top", no: 6 },
        4: { position: "front", no: 0 },
    },
    9: {
        3: { position: "bottom", no: 7 },
        5: { position: "back", no: 7 },
    },
    10: {
        3: { position: "bottom", no: 4 },
    },
    11: {
        3: { position: "bottom", no: 1 },
        4: { position: "front", no: 7 },
    },
    12: {
        5: { position: "back", no: 4 },
    },
    13: {},
    14: {
        4: { position: "front", no: 4 },
    },
    15: {
        2: { position: "top", no: 1 },
        5: { position: "back", no: 1 },
    },
    16: {
        2: { position: "top", no: 4 },
    },
    17: {
        2: { position: "top", no: 7 },
        4: { position: "front", no: 1 },
    },
    18: {
        0: { position: "right", no: 8 },
        3: { position: "bottom", no: 8 },
        5: { position: "back", no: 6 },
    },
    19: {
        0: { position: "right", no: 7 },
        3: { position: "bottom", no: 5 },
    },
    20: {
        0: { position: "right", no: 6 },
        3: { position: "bottom", no: 2 },
        4: { position: "front", no: 8 },
    },
    21: {
        0: { position: "right", no: 5 },
        5: { position: "back", no: 3 },
    },
    22: {
        0: { position: "right", no: 4 },
    },
    23: {
        0: { position: "right", no: 3 },
        4: { position: "front", no: 5 },
    },
    24: {
        0: { position: "right", no: 2 },
        2: { position: "top", no: 2 },
        5: { position: "back", no: 0 },
    },
    25: {
        0: { position: "right", no: 1 },
        2: { position: "top", no: 5 },
    },
    26: {
        0: { position: "right", no: 0 },
        2: { position: "top", no: 8 },
        4: { position: "front", no: 2 },
    },
};

export class Roll {
    constructor(face, direction, scene, group, cubes, step) {
        this.face = face;
        this.stepCount = 0;
        this.active = true;
        this.direction = direction;
        this.scene = scene;
        this.group = group;
        this.cubes = cubes;
        this.step = step;
        this.init();
    }

    init() {
        if (this.face.value) {
            this.cubes.forEach((item) => {
                if (item.position[this.face.axis] == this.face.value) {
                    this.scene.remove(item);
                    this.group.add(item);
                }
            });
        } else {
            this.cubes.forEach((item) => {
                this.scene.remove(item);
                this.group.add(item);
            });
        }
    }

    rollFace() {
        return new Promise((resolve) => {
            if (this.stepCount != 25) {
                this.group.rotation[this.face.axis] += this.direction * this.step;
                this.stepCount += 1;
                resolve(false);
            } else {
                if (this.active) {
                    this.active = false;
                    this.clearGroup();
                }
                resolve(true);
            }
        });
    }

    clearGroup() {
        for (var i = this.group.children.length - 1; i >= 0; i--) {
            let item = this.group.children[i];
            item.getWorldPosition(item.position);
            item.getWorldQuaternion(item.rotation);
            item.position.x = Math.round(item.position.x);
            item.position.y = Math.round(item.position.y);
            item.position.z = Math.round(item.position.z);
            this.group.remove(item);
            this.scene.add(item);
        }
        this.group.rotation[this.face.axis] = 0;
    }
}
