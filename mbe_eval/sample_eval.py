import numpy as np
from scipy.stats import pearsonr
import pingouin as pg
import pandas as pd

def simulate_mbe_evaluation():
    """
    Simulates the Marginal Baseline Eval (MBE) on a dummy representation metric.
    MBE tests whether a proposed metric offers independent predictive signal 
    beyond a trivial baseline (early validation loss).
    """
    print("==================================================")
    print("Marginal Baseline Eval (MBE) - Sample Test Run")
    print("==================================================\n")
    
    # 1. Generate heterogeneous dummy data (simulating 30 training runs)
    np.random.seed(42)
    n_runs = 30
    
    # Underlying true model capability (unobserved)
    true_capability = np.random.randn(n_runs)
    
    # Early Validation Loss (our trivial baseline) perfectly tracks capability + some noise
    early_val_loss = -true_capability + np.random.randn(n_runs) * 0.2
    
    # Final Epoch 200 Accuracy (our target to predict) perfectly tracks capability + some noise
    final_test_acc = true_capability + np.random.randn(n_runs) * 0.1
    
    # Our proposed dummy metric: Gradient L2 Norm
    # IT IS A LOSS PROXY! It mathematically correlates heavily with early val loss.
    proposed_metric = early_val_loss + np.random.randn(n_runs) * 0.3
    
    # 2. Stage 1: Absolute Correlation (The False Assurance)
    # Does the metric predict final accuracy?
    r_metric, p_metric = pearsonr(proposed_metric, final_test_acc)
    print(f"[Stage 1] Absolute Correlation Check:")
    print(f"  Correlation of Proposed Metric with Final Accuracy: r = {r_metric:.3f} (p = {p_metric:.3e})")
    
    if p_metric < 0.05:
        print("  -> RESULT: PASS. Metric correlates significantly with generalization.\n")
    
    # 3. Stage 2: The MBE Partial-Correlation Baseline Control
    # Does the metric offer MARGINAL signal beyond the trivial validation loss baseline?
    print("[Stage 2] The MBE Baseline Control (Partial Correlation):")
    
    df = pd.DataFrame({
        'Final_Acc': final_test_acc,
        'Proposed_Metric': proposed_metric,
        'Baseline_Loss': early_val_loss
    })
    
    # Calculate partial correlation: Metric vs Final Acc, controlling for Baseline Loss
    pcorr_metric = pg.partial_corr(data=df, x='Proposed_Metric', y='Final_Acc', covar='Baseline_Loss')
    r_partial = pcorr_metric['r'].values[0]
    p_partial = pcorr_metric['p-val'].values[0]
    
    print(f"  Marginal Correlation (Controlling for Early Val Loss): r = {r_partial:.3f} (p = {p_partial:.3f})")
    
    if p_partial > 0.05:
        print("  -> RESULT: FAIL. The metric offers NO independent predictive signal.")
        print("  -> DIAGNOSIS: The proposed metric is a disguised Loss Proxy.\n")
    else:
        print("  -> RESULT: PASS. The metric offers independent structural insight.\n")
        
    print("==================================================")
    print("MBE Evaluation Complete.")
    print("==================================================")

if __name__ == "__main__":
    simulate_mbe_evaluation()
