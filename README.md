# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_10:17:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 10:17:42 | Giriulla (Maha Oya) | 3.95 | 🟢 Normal | -0.057 |  |
| 2026-11-27 10:17:02 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:14:32 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:13:02 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:10:19 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-27 10:09:59 | Badalgama (Maha Oya) | 4.90 | 🟢 Normal | -0.039 |  |
| 2026-11-27 10:09:40 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | -0.058 |  |
| 2026-11-27 10:08:32 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 10:08:12 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.028 |  |
| 2026-11-27 10:07:49 | Kuda Oya (Kirindi Oya) | 2.61 | 🟢 Normal | -0.044 |  |
| 2026-11-27 10:07:49 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-27 10:07:32 | Moragaswewa (Deduru Oya) | 3.44 | 🟢 Normal | -0.037 |  |
| 2026-11-27 10:06:53 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-11-27 10:05:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-11-27 10:05:42 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.040 |  |
| 2026-11-27 10:04:51 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.178 |  |
| 2026-11-27 10:04:16 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-11-27 10:04:00 | Galgamuwa (Mee Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:03:55 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.129 |  |
| 2026-11-27 10:03:19 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-27 10:03:03 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.040 |  |
| 2026-11-27 10:02:57 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:02:55 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.000 |  |
| 2026-11-27 10:02:49 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.073 |  |
| 2026-11-27 10:02:44 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | -0.040 |  |
| 2026-11-27 10:02:39 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.122 |  |
| 2026-11-27 10:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:02:17 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-27 10:02:13 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | 0.000 |  |
| 2026-11-27 10:02:09 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.062 |  |
| 2026-11-27 10:01:48 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | -0.129 |  |
| 2026-11-27 10:01:43 | Thanamalwila (Kirindi Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:01:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-11-27 10:01:29 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.059 |  |
| 2026-11-27 10:01:08 | Moraketiya (Walawe Ganga) | 3.77 | 🟡 Alert | -0.032 |  |
| 2026-11-27 10:00:48 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:00:36 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 10:02:55 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.000 |  |
| 2026-11-27 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | 0.000 |  |
| 2026-11-27 10:01:08 | Moraketiya (Walawe Ganga) | 3.77 | 🟡 Alert | -0.032 |  |
| 2026-11-27 10:01:48 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | -0.129 |  |
| 2026-11-27 10:02:17 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-27 10:10:19 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-27 10:07:49 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-27 10:08:32 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 10:00:48 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:04:00 | Galgamuwa (Mee Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:13:02 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:14:32 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:03:19 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-27 10:01:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-11-27 10:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:17:02 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:02:57 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:02:13 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:01:43 | Thanamalwila (Kirindi Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:08:12 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.028 |  |
| 2026-11-27 10:06:53 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-11-27 10:04:16 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-11-27 10:00:36 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.030 |  |
| 2026-11-27 10:05:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-11-27 10:07:32 | Moragaswewa (Deduru Oya) | 3.44 | 🟢 Normal | -0.037 |  |
| 2026-11-27 10:09:59 | Badalgama (Maha Oya) | 4.90 | 🟢 Normal | -0.039 |  |
| 2026-11-27 10:05:42 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.040 |  |
| 2026-11-27 10:03:03 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.040 |  |
| 2026-11-27 10:02:44 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | -0.040 |  |
| 2026-11-27 10:07:49 | Kuda Oya (Kirindi Oya) | 2.61 | 🟢 Normal | -0.044 |  |
| 2026-11-27 10:17:42 | Giriulla (Maha Oya) | 3.95 | 🟢 Normal | -0.057 |  |
| 2026-11-27 10:09:40 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | -0.058 |  |
| 2026-11-27 10:01:29 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.059 |  |
| 2026-11-27 10:02:09 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.062 |  |
| 2026-11-27 09:04:33 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.073 |  |
| 2026-11-27 10:02:49 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.073 |  |
| 2026-11-27 10:02:39 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.122 |  |
| 2026-11-27 10:03:55 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.129 |  |
| 2026-11-27 10:04:51 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)