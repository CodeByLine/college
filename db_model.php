<?php
class DB_Model extends CI_Model {

  public function get_row($query) { // generic get a row
    $sql = $this->db->query($query);
    if ($sql->num_rows() > 0) {
      return $sql->row_array(); 
    } else {
      return FALSE;
    }
  }

/* obsolete
  public function toggle_grad($id) {
    $query = "UPDATE applicant set college_app_graduated=1-college_app_graduated WHERE ID=$id";
    return $this->db->query($query);
  }
*/

  public function toggle_macandidate($rk) {
    $query = "UPDATE personnel set ses_macandidate=1-ses_macandidate WHERE rk=$rk";
    return $this->db->query($query);
  }

  public function toggle_paid($rk) {
    $sql = $this->db->query("SELECT app_tuition FROM personnel WHERE rk=$rk");
    $student = $sql->row_array();
    if (strtolower($student["app_tuition"]=="no")) {
      $query = "UPDATE personnel set app_tuition='paid' WHERE rk=$rk";
    } else {
      $query = "UPDATE personnel set app_tuition='no' WHERE rk=$rk";
    }
    return $this->db->query($query);
  }

  public function set_new_row($table,$data=array()) { // generic insert row in table
  	return $this->db->insert($table, $data);
  }

  // this function doesn't work
  public function return_insert($table,$data=array()) { // returns query string. does not execute an insert.
    return $this->db->set($data)->get_compiled_insert($table);
  }

  public function delete_row($query) { // generic delete a row
    return $this->db->query($query);
  }

  public function insert_ignore($table,$query) { // generic query -- does anything
    $insert_query = $this->db->insert_string($table, $query);
    $insert_query = str_replace('INSERT INTO','INSERT IGNORE INTO',$insert_query);
    $query = $this->db->query($insert_query);
    return $query;
  }

  public function get_list($query) { // generic get one or more rows
    $sql = $this->db->query($query);
    if ($sql->num_rows() > 0) {
      return $sql->result_array();
    } else {
      return FALSE;
    }
  }

  public function set_row($table,$data,$key="",$keyvalue="",$key2="",$keyvalue2="") { // generic update
    if ($key>"") $this->db->where($key,$keyvalue);
    if ($key2>"") $this->db->where($key2,$keyvalue2); // appends WHERE with AND 
    $this->db->update($table, $data); 
  }

  public function set_new_application($values=array()) {
    $_POST['faculty_mentor_biopic'] = ''; // set default value
    $_POST['faculty_comment'] = ''; // set default value
    $_POST['faculty_pw_blob'] = ''; // set default value
    $_POST['faculty_active'] = 0; // set default value
    $_POST['faculty_intern'] = 0; // set default value
    $_POST['faculty_mentor'] = 0; // set default value
    $_POST['faculty_tutor'] = 0; // set default value
    $_POST['faculty_dean'] = 0; // set default value
    $_POST['faculty_fcsp'] = 0; // set default value
    $_POST['ma_status_notes'] = ''; // set default value
    $_POST['app_assigned'] = "";
    $_POST['dob'] = date("Y-n-d",strtotime($_POST['dob']));
    $app_plantostart = date("n/d/Y",strtotime($_POST['app_plantostart']));
    $_POST['app_plantostart'] = ($app_plantostart=="$app_plantostart") ? "" : $app_plantostart ;
    $_POST['app_date'] = date("Y-m-d");
    return $this->db->insert('personnel', $_POST);
  }

  public function set_new_student($data) {
    $data['faculty_mentor_biopic'] = ''; // set default value
    $data['faculty_comment'] = ''; // set default value
    $data['faculty_pw_blob'] = ''; // set default value
    $data['faculty_active'] = 0; // set default value
    $data['faculty_intern'] = 0; // set default value
    $data['faculty_mentor'] = 0; // set default value
    $data['faculty_tutor'] = 0; // set default value
    $data['faculty_dean'] = 0; // set default value
    $data['faculty_fcsp'] = 0; // set default value
    $data['ma_status_notes'] = ''; // set default value
    $data['app_assigned'] = "";
    $data['prep_teacher'] = "";
    $data['prep_grad_date'] = "";
    $data['dob'] = date("Y-n-d",strtotime($data['dob']));
    $app_plantostart = date("n/d/Y",strtotime($data['app_plantostart']));
    $data['app_plantostart'] = ($app_plantostart=="$app_plantostart") ? "" : $app_plantostart ;
    $data['app_date'] = date("Y-m-d");
    return $this->db->insert('personnel', $data);
  }
  
}
?>