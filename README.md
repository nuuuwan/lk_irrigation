# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_08:11:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,775 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 08:11:49 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:08:25 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | -0.048 |  |
| 2026-09-21 08:07:49 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.028 |  |
| 2026-09-21 08:07:39 | Badalgama (Maha Oya) | 3.83 | 🟢 Normal | -0.094 |  |
| 2026-09-21 08:07:28 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 08:07:17 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-09-21 08:07:03 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:07:00 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:06:41 | Thalgahagoda (Nilwala Ganga) | 1.43 | 🟡 Alert | -0.018 |  |
| 2026-09-21 08:06:40 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-09-21 08:05:46 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.040 |  |
| 2026-09-21 08:05:42 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-21 08:05:23 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:05:16 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-09-21 08:04:57 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | -0.040 |  |
| 2026-09-21 08:04:52 | Baddegama (Gin Ganga) | 3.89 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-21 08:04:32 | Thanthirimale (Malwathu Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-21 08:04:29 | Hanwella (Kelani Ganga) | 6.64 | 🟢 Normal | -0.079 |  |
| 2026-09-21 08:04:25 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:04:09 | Glencourse (Kelani Ganga) | 14.18 | 🟢 Normal | -0.258 |  |
| 2026-09-21 08:03:58 | Rathnapura (Kalu Ganga) | 5.87 | 🟡 Alert | -0.094 |  |
| 2026-09-21 08:03:39 | Thawalama (Gin Ganga) | 3.94 | 🟢 Normal | -0.320 |  |
| 2026-09-21 08:03:33 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-09-21 08:03:01 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.148 |  |
| 2026-09-21 08:03:01 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-21 08:02:39 | Magura (Kalu Ganga) | 5.61 | 🟡 Alert | -0.033 |  |
| 2026-09-21 08:02:21 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-09-21 08:01:49 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-09-21 08:01:49 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 08:01:43 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:01:35 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:01:34 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:01:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:01:26 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 08:00:54 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:00:35 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-09-21 08:00:16 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 08:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-09-21 08:04:52 | Baddegama (Gin Ganga) | 3.89 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-21 08:06:41 | Thalgahagoda (Nilwala Ganga) | 1.43 | 🟡 Alert | -0.018 |  |
| 2026-09-21 08:02:39 | Magura (Kalu Ganga) | 5.61 | 🟡 Alert | -0.033 |  |
| 2026-09-21 08:04:57 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | -0.040 |  |
| 2026-09-21 08:08:25 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | -0.048 |  |
| 2026-09-21 08:03:58 | Rathnapura (Kalu Ganga) | 5.87 | 🟡 Alert | -0.094 |  |
| 2026-09-21 08:07:17 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-09-21 08:05:42 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-21 08:03:01 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-21 08:01:49 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 08:07:28 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 08:01:26 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 08:03:33 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:01:43 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:07:03 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:00:54 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:01:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:07:00 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:11:49 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:01:35 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:05:23 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:04:25 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:01:34 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 08:04:32 | Thanthirimale (Malwathu Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-21 08:00:35 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-09-21 08:05:16 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-09-21 08:00:16 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-09-21 08:02:21 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-09-21 08:01:49 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-09-21 08:07:49 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.028 |  |
| 2026-09-21 08:06:40 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-09-21 08:05:46 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.040 |  |
| 2026-09-21 07:19:56 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.072 |  |
| 2026-09-21 08:04:29 | Hanwella (Kelani Ganga) | 6.64 | 🟢 Normal | -0.079 |  |
| 2026-09-21 08:07:39 | Badalgama (Maha Oya) | 3.83 | 🟢 Normal | -0.094 |  |
| 2026-09-21 08:03:01 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.148 |  |
| 2026-09-21 08:04:09 | Glencourse (Kelani Ganga) | 14.18 | 🟢 Normal | -0.258 |  |
| 2026-09-21 08:03:39 | Thawalama (Gin Ganga) | 3.94 | 🟢 Normal | -0.320 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)