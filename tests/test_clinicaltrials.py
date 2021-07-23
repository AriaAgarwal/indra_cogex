from indra_cogex.sources.clinicaltrials import ClinicaltrialsProcessor
import os


def test_get_nodes():
    path = os.path.join(os.path.dirname(__file__), "test_search_results_4.xml")
    cp = ClinicaltrialsProcessor(path)
    nodes = list(cp.get_nodes())
    assert len(nodes) != 0
    # assert len(nodes) >= len(cp.has_trial_cond_ns) + len(cp.tested_in_int_ns)
    # assert len(cp.has_trial_cond_ns) != 0  # 101
    # assert len(cp.has_trial_cond_ns) == len(cp.has_trial_cond_id)
    # assert len(cp.has_trial_cond_id) == len(cp.has_trial_nct)
    # assert len(cp.tested_in_int_ns) != 0  # 33
    # assert len(cp.tested_in_int_ns) == len(cp.tested_in_int_id)
    # assert len(cp.tested_in_int_id) == len(cp.tested_in_nct)


def test_get_relations():
    path = os.path.join(os.path.dirname(__file__), "test_search_results_4.xml")
    cp = ClinicaltrialsProcessor(path)
    nodes = list(cp.get_nodes())
    relations = list(cp.get_relations())
    assert len(relations) != 0
    assert relations[0].source_ns == "MESH"
    assert relations[0].source_id == "D010468"
    assert relations[0].target_ns == "CLINICALTRIALS"
    assert relations[0].target_id == "NCT04966000"
