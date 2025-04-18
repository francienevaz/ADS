using UnityEngine;
using UnityEngine.XR.ARFoundation;

public class DebugARCamera : MonoBehaviour
{
    public ARCameraBackground arCameraBackground;
    
    void Start()
    {
        if (arCameraBackground == null)
            arCameraBackground = GetComponent<ARCameraBackground>();
    }

    void Update()
    {
        if (arCameraBackground != null && arCameraBackground.material != null)
            Debug.Log("Material da câmera AR: " + arCameraBackground.material.name);
        else
            Debug.LogError("Componente ARCameraBackground não configurado!");
    }
}