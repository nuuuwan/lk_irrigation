# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_13:02:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,218 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 13:02:49 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 13:02:43 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.039 |  |
| 2026-11-08 13:02:40 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | -0.053 |  |
| 2026-11-08 13:02:38 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.070 |  |
| 2026-11-08 13:02:37 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 13:02:05 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-08 13:01:47 | Moraketiya (Walawe Ganga) | 3.21 | 🟡 Alert | 0.000 |  |
| 2026-11-08 13:01:43 | Moragaswewa (Deduru Oya) | 3.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 13:01:39 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 13:01:35 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-08 13:01:26 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.084 |  |
| 2026-11-08 13:01:24 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.170 |  |
| 2026-11-08 13:00:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 13:00:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-11-08 13:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 13:01:47 | Moraketiya (Walawe Ganga) | 3.21 | 🟡 Alert | 0.000 |  |
| 2026-11-08 12:10:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.44 | 🟡 Alert | 0.000 |  |
| 2026-11-08 12:10:29 | Dunamale (Aththanagalu Oya) | 3.53 | 🟡 Alert | -0.053 |  |
| 2026-11-08 13:02:40 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | -0.053 |  |
| 2026-11-08 13:00:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-11-08 12:03:16 | Putupaula (Kalu Ganga) | 1.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 12:02:39 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-08 13:02:49 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 12:14:24 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-08 13:01:43 | Moragaswewa (Deduru Oya) | 3.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 12:04:38 | Thalgahagoda (Nilwala Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 12:10:29 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 13:02:05 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:01:36 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:00:58 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:01:15 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-08 13:01:39 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 13:02:37 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:04:50 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-08 13:00:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:04:35 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-08 12:02:14 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-11-08 12:06:09 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-08 12:05:23 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-08 13:01:35 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-08 13:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-11-08 12:07:33 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.038 |  |
| 2026-11-08 13:02:43 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.039 |  |
| 2026-11-08 12:03:11 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.040 |  |
| 2026-11-08 12:09:03 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.049 |  |
| 2026-11-08 13:02:38 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.070 |  |
| 2026-11-08 12:04:23 | Badalgama (Maha Oya) | 3.93 | 🟢 Normal | -0.079 |  |
| 2026-11-08 12:03:32 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.082 |  |
| 2026-11-08 13:01:26 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.084 |  |
| 2026-11-08 12:08:30 | Pitabeddara (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.147 |  |
| 2026-11-08 12:03:38 | Rathnapura (Kalu Ganga) | 4.40 | 🟢 Normal | -0.156 |  |
| 2026-11-08 13:01:24 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.170 |  |
| 2026-11-08 12:01:38 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.201 |  |
| 2026-11-08 12:03:45 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)