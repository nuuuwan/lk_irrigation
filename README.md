# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_07:04:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,735 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 07:04:21 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-11-28 07:04:12 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.070 |  |
| 2026-11-28 07:04:09 | Moraketiya (Walawe Ganga) | 3.20 | 🟡 Alert | -0.030 |  |
| 2026-11-28 07:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-28 07:03:33 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.029 |  |
| 2026-11-28 07:02:56 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | -0.052 |  |
| 2026-11-28 07:02:51 | Magura (Kalu Ganga) | 3.86 | 🟢 Normal | -0.038 |  |
| 2026-11-28 07:02:09 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-28 07:02:05 | Kuda Oya (Kirindi Oya) | 2.62 | 🟢 Normal | -0.225 |  |
| 2026-11-28 07:01:49 | Ellagawa (Kalu Ganga) | 7.35 | 🟢 Normal | -0.030 |  |
| 2026-11-28 07:01:46 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.004 |  |
| 2026-11-28 07:01:35 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 07:01:26 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-28 07:01:21 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 07:01:20 | Thanamalwila (Kirindi Oya) | 2.28 | 🟢 Normal | -0.143 |  |
| 2026-11-28 07:01:02 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-28 07:00:50 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-28 07:00:18 | Pitabeddara (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.097 |  |
| 2026-11-28 07:00:16 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-28 06:38:02 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | -0.004 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 06:03:07 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-11-28 06:08:52 | Panadugama (Nilwala Ganga) | 5.57 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-28 04:01:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-11-28 07:04:09 | Moraketiya (Walawe Ganga) | 3.20 | 🟡 Alert | -0.030 |  |
| 2026-11-28 06:03:30 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 5.625 | 🔺 Rising |
| 2026-11-28 07:01:26 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-28 06:02:19 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-28 06:05:25 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-28 06:07:05 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-28 07:00:16 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-28 07:01:35 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 06:05:07 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 07:01:21 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 06:12:05 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-28 07:00:50 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-28 06:07:03 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-28 07:01:46 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.004 |  |
| 2026-11-28 06:38:02 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | -0.004 |  |
| 2026-11-28 07:02:09 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-28 07:01:02 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-28 07:04:21 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-11-28 07:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-28 06:05:02 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-11-28 06:16:38 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.025 |  |
| 2026-11-28 07:03:33 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.029 |  |
| 2026-11-28 07:01:49 | Ellagawa (Kalu Ganga) | 7.35 | 🟢 Normal | -0.030 |  |
| 2026-11-28 07:02:51 | Magura (Kalu Ganga) | 3.86 | 🟢 Normal | -0.038 |  |
| 2026-11-28 07:02:56 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | -0.052 |  |
| 2026-11-28 06:07:05 | Holombuwa (Kelani Ganga) | 1.55 | 🟢 Normal | -0.058 |  |
| 2026-11-28 07:04:12 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.070 |  |
| 2026-11-28 06:01:49 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.088 |  |
| 2026-11-28 07:00:18 | Pitabeddara (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.097 |  |
| 2026-11-28 06:02:21 | Glencourse (Kelani Ganga) | 12.09 | 🟢 Normal | -0.099 |  |
| 2026-11-28 06:06:51 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.109 |  |
| 2026-11-28 06:01:56 | Moragaswewa (Deduru Oya) | 2.35 | 🟢 Normal | -0.109 |  |
| 2026-11-28 06:08:56 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.127 |  |
| 2026-11-28 07:01:20 | Thanamalwila (Kirindi Oya) | 2.28 | 🟢 Normal | -0.143 |  |
| 2026-11-28 06:02:26 | Badalgama (Maha Oya) | 4.32 | 🟢 Normal | -0.218 |  |
| 2026-11-28 07:02:05 | Kuda Oya (Kirindi Oya) | 2.62 | 🟢 Normal | -0.225 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)