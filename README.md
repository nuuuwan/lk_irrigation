# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_01:18:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,517 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Baddegama — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 01:18:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.10 | 🟡 Alert | 0.000 |  |
| 2026-09-21 01:13:47 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:12:44 | Putupaula (Kalu Ganga) | 2.32 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-21 01:11:09 | Baddegama (Gin Ganga) | 3.75 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-09-21 01:10:26 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-21 01:08:57 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-21 01:08:31 | Rathnapura (Kalu Ganga) | 6.40 | 🟡 Alert | -0.061 |  |
| 2026-09-21 01:08:02 | Glencourse (Kelani Ganga) | 15.46 | 🟡 Alert | -0.085 |  |
| 2026-09-21 01:07:42 | Magura (Kalu Ganga) | 5.64 | 🟡 Alert | 0.025 | 🔺 Rising |
| 2026-09-21 01:07:32 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | -0.256 |  |
| 2026-09-21 01:06:34 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:05:43 | Kithulgala (Kelani Ganga) | 2.40 | 🟢 Normal | -0.102 |  |
| 2026-09-21 01:05:41 | Badalgama (Maha Oya) | 4.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 01:05:30 | Panadugama (Nilwala Ganga) | 6.14 | 🟠 Minor Flood | -0.029 |  |
| 2026-09-21 01:05:25 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-21 01:04:50 | Hanwella (Kelani Ganga) | 6.83 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-21 01:04:19 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:04:12 | Thawalama (Gin Ganga) | 5.37 | 🟡 Alert | -0.030 |  |
| 2026-09-21 01:04:09 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.023 |  |
| 2026-09-21 01:04:05 | Peradeniya (Mahaweli Ganga) | 4.90 | 🟢 Normal | -0.103 |  |
| 2026-09-21 01:04:03 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-09-21 01:04:02 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:03:59 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-09-21 01:03:37 | Giriulla (Maha Oya) | 3.32 | 🟢 Normal | -0.099 |  |
| 2026-09-21 01:03:31 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.030 |  |
| 2026-09-21 01:03:27 | Deraniyagala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.190 |  |
| 2026-09-21 01:03:19 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:03:09 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:02:30 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:02:27 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.150 |  |
| 2026-09-21 01:02:07 | Nawalapitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.198 |  |
| 2026-09-21 01:01:58 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:01:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:00:43 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:00:14 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:00:14 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 01:05:30 | Panadugama (Nilwala Ganga) | 6.14 | 🟠 Minor Flood | -0.029 |  |
| 2026-09-21 01:11:09 | Baddegama (Gin Ganga) | 3.75 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-09-21 01:04:03 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-09-21 01:07:42 | Magura (Kalu Ganga) | 5.64 | 🟡 Alert | 0.025 | 🔺 Rising |
| 2026-09-21 01:08:57 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-21 01:18:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.10 | 🟡 Alert | 0.000 |  |
| 2026-09-21 01:04:12 | Thawalama (Gin Ganga) | 5.37 | 🟡 Alert | -0.030 |  |
| 2026-09-21 01:03:31 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.030 |  |
| 2026-09-21 01:08:31 | Rathnapura (Kalu Ganga) | 6.40 | 🟡 Alert | -0.061 |  |
| 2026-09-21 01:08:02 | Glencourse (Kelani Ganga) | 15.46 | 🟡 Alert | -0.085 |  |
| 2026-09-21 01:10:26 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-21 01:12:44 | Putupaula (Kalu Ganga) | 2.32 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-21 01:04:50 | Hanwella (Kelani Ganga) | 6.83 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-21 01:05:25 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 01:05:41 | Badalgama (Maha Oya) | 4.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 01:00:14 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:04:02 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:01:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:04:15 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:06:34 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:00:14 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:04:19 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:00:43 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:13:47 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:03:09 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:01:58 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 01:03:19 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-21 01:04:09 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.023 |  |
| 2026-09-21 01:03:59 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-09-21 01:03:37 | Giriulla (Maha Oya) | 3.32 | 🟢 Normal | -0.099 |  |
| 2026-09-21 01:05:43 | Kithulgala (Kelani Ganga) | 2.40 | 🟢 Normal | -0.102 |  |
| 2026-09-21 01:04:05 | Peradeniya (Mahaweli Ganga) | 4.90 | 🟢 Normal | -0.103 |  |
| 2026-09-21 01:02:27 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.150 |  |
| 2026-09-21 01:03:27 | Deraniyagala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.190 |  |
| 2026-09-21 01:02:07 | Nawalapitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.198 |  |
| 2026-09-21 01:07:32 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | -0.256 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)