from rest_framework import serializers
from .models import User
from schools.models import School


class RPCreateSerializer(serializers.ModelSerializer):
    school_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), source='school', write_only=True)
    school_name = serializers.CharField(source='school.name', read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'school_id', 'school_name']

    def validate(self, data):
        return data

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            school=validated_data['school'],
            role='rp'
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CoderCreateSerializer(serializers.ModelSerializer):
    rp = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='rp'))
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'rp', 'school']

    def validate(self, data):
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data, role='coder')
        user.set_password(password)
        user.save()
        return user


class EmpresaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['company_name', 'nif', 'email', 'password']

    def validate(self, data):
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data, role='empresa')
        user.set_password(password)
        user.save()
        return user


class RPUpdateSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=False)
    confirm_new_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'profile_picture', 'description', 'school',
                  'new_password', 'confirm_new_password']
        extra_kwargs = {field: {'required': False} for field in fields}

    def validate(self, data):
        if 'new_password' in data and data['new_password'] != data.get('confirm_new_password'):
            raise serializers.ValidationError('Las nuevas contraseñas no coinciden')
        return data

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.description = validated_data.get('description', instance.description)
        instance.school = validated_data.get('school', instance.school)

        new_password = validated_data.get('new_password')
        if new_password:
            instance.set_password(new_password)

        instance.save()
        return instance


class CoderUpdateSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=False)
    confirm_new_password = serializers.CharField(write_only=True, required=False)
    rp = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='rp'), required=False)
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'profile_picture', 'description', 'linkedin', 'github',
                  'rp', 'cv', 'school', 'new_password', 'confirm_new_password']
        extra_kwargs = {field: {'required': False} for field in fields}

    def validate(self, data):
        if 'new_password' in data and data['new_password'] != data.get('confirm_new_password'):
            raise serializers.ValidationError('Las nuevas contraseñas no coinciden')
        return data

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.description = validated_data.get('description', instance.description)
        instance.linkedin = validated_data.get('linkedin', instance.linkedin)
        instance.github = validated_data.get('github', instance.github)
        instance.rp = validated_data.get('rp', instance.rp)
        instance.cv = validated_data.get('cv', instance.cv)
        instance.school = validated_data.get('school', instance.school)

        new_password = validated_data.get('new_password')
        if new_password:
            instance.set_password(new_password)

        instance.save()
        return instance


class EmpresaUpdateSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=False)
    confirm_new_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['company_name', 'nif', 'email', 'profile_picture', 'description', 'phone', 'website',
                  'new_password', 'confirm_new_password']
        extra_kwargs = {field: {'required': False} for field in fields}

    def validate(self, data):
        if 'new_password' in data and data['new_password'] != data.get('confirm_new_password'):
            raise serializers.ValidationError('Las nuevas contraseñas no coinciden')
        return data

    def update(self, instance, validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.nif = validated_data.get('nif', instance.nif)
        instance.email = validated_data.get('email', instance.email)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.description = validated_data.get('description', instance.description)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.website = validated_data.get('website', instance.website)

        new_password = validated_data.get('new_password')
        if new_password:
            instance.set_password(new_password)

        instance.save()
        return instance


class GetRPSerializer(serializers.ModelSerializer):
    school = serializers.SlugRelatedField(slug_field='name', queryset=School.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'profile_picture',
                  'description', 'school']


class GetCoderSerializer(serializers.ModelSerializer):
    school = serializers.SlugRelatedField(slug_field='name', queryset=School.objects.all(), required=False)
    rp = serializers.SlugRelatedField(slug_field='first_name', queryset=User.objects.filter(role='rp'), required=False)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'profile_picture',
                  'description', 'linkedin', 'github', 'cv', 'school', 'rp']


class GetEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'company_name', 'nif', 'email', 'profile_picture',
                  'description', 'phone', 'website']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
