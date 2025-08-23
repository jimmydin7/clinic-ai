
  const container = document.getElementById('neuralSphere');
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
  camera.position.z = 120;

  const renderer = new THREE.WebGLRenderer({ alpha: true });
  renderer.setSize(400, 400);
  container.appendChild(renderer.domElement);

  const geometry = new THREE.BufferGeometry();
  const particles = 1000;


  
  const positions = [];

  for (let i = 0; i < particles; i++) {
    const phi = Math.acos(2 * Math.random() - 1);
    const theta = 2 * Math.PI * Math.random();
    const radius = 60;

    const x = radius * Math.sin(phi) * Math.cos(theta);
    const y = radius * Math.sin(phi) * Math.sin(theta);
    const z = radius * Math.cos(phi);

    positions.push(x, y, z);
  }

  geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));

  const material = new THREE.PointsMaterial({
    color: 0x00ffff,
    size: 1.8,
    transparent: true,
    opacity: 0.85
  });

  const points = new THREE.Points(geometry, material);
  scene.add(points);

  function animate() {
    requestAnimationFrame(animate);
    points.rotation.y += 0.002;
    points.rotation.x += 0.001;
    renderer.render(scene, camera);
  }

  animate();