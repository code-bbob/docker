from rest_framework import serializers
from .models import Repair,Outside



class AdminRepairSerializer(serializers.ModelSerializer):
    repaired_by_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Repair
        fields = [
            'id',
            'repair_id',
            'customer_name',
            'customer_phone_number',
            'phone_model',
            'repair_problem',
            'repair_description',
            'imei_number',
            'model_number',
            'sim_tray',
            'sim',
            'SD_card',
            'phone_cover',
            'phone_condition',
            'total_amount',
            'advance_paid',
            'due',
            'received_date',
            'received_by',
            'repaired_by',
            'outside_repair',
            'repair_status',
            'amount_paid',
            'repair_cost_price',
            'cost_price_description',
            'repair_profit',
            'technician_profit',
            'my_profit',
            'admin_only_profit',
            'outside',
            'outside_name',
            'outside_desc',
            'taken_by',
            'outside_taken_date',
            'returned_by',
            'outside_returned_date',
            'outside_cost',
            'delivery_date',
            'updated_at',
            'repaired_by_name',
            'credit_due',
            'credit_paid'

        ]

    def get_repaired_by_name(self, obj):
        return obj.repaired_by.user.name if obj.repaired_by and obj.repaired_by.user else None
    

class TechnicianRepairSerializer(serializers.ModelSerializer):
    repaired_by_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Repair
        fields = [
            'id',
            'repair_id',
            'customer_name',
            'customer_phone_number',
            'phone_model',
            'repair_problem',
            'repair_description',
            'imei_number',
            'model_number',
            'sim_tray',
            'sim',
            'SD_card',
            'phone_cover',
            'phone_condition',
            'total_amount',
            'advance_paid',
            'due',
            'received_date',
            'received_by',
            'repaired_by',
            'outside_repair',
            'repair_status',
            'amount_paid',
            'repair_cost_price',
            'cost_price_description',
            'repair_profit',
            'technician_profit',
            'my_profit',
            'admin_only_profit',
            'outside',
            'outside_name',
            'outside_desc',
            'taken_by',
            'outside_taken_date',
            'returned_by',
            'outside_returned_date',
            'outside_cost',
            'delivery_date',
            'updated_at',
            'repaired_by_name',
            'credit_due',
            'credit_paid'

        ]

    def get_repaired_by_name(self, obj):
        return obj.repaired_by.user.name 
    
class StaffRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        exclude = ['repair_cost_price','cost_price_description','repair_profit','technician_profit','my_profit','outside_cost']

