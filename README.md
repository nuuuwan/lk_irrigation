# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_19:08:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Nawalapitiya — Alert; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 19:08:41 | Thawalama (Gin Ganga) | 5.42 | 🟡 Alert | 0.027 | 🔺 Rising |
| 2026-09-20 19:07:50 | Holombuwa (Kelani Ganga) | 2.98 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-09-20 19:07:45 | Panadugama (Nilwala Ganga) | 6.04 | 🟠 Minor Flood | 0.086 | 🔺 Rising |
| 2026-09-20 19:07:39 | Glencourse (Kelani Ganga) | 15.56 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-09-20 19:06:49 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-09-20 19:06:32 | Rathnapura (Kalu Ganga) | 6.69 | 🟡 Alert | -0.057 |  |
| 2026-09-20 19:06:21 | Putupaula (Kalu Ganga) | 2.06 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-20 19:05:29 | Kithulgala (Kelani Ganga) | 2.80 | 🟢 Normal | -0.144 |  |
| 2026-09-20 19:05:00 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:04:55 | Baddegama (Gin Ganga) | 3.56 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-09-20 19:04:30 | Hanwella (Kelani Ganga) | 6.26 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-09-20 19:04:29 | Peradeniya (Mahaweli Ganga) | 5.77 | 🟡 Alert | -0.408 |  |
| 2026-09-20 19:04:17 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.040 |  |
| 2026-09-20 19:04:06 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:04:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:03:35 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:03:11 | Norwood (Kelani Ganga) | 1.89 | 🟡 Alert | -0.170 |  |
| 2026-09-20 19:03:02 | Giriulla (Maha Oya) | 3.50 | 🟢 Normal | 0.390 | 🔺 Rising |
| 2026-09-20 19:02:45 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-20 19:02:43 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-20 19:02:28 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.012 |  |
| 2026-09-20 19:02:25 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-20 19:02:18 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:02:09 | Nawalapitiya (Mahaweli Ganga) | 3.68 | 🟡 Alert | 0.243 | 🔺 Rising |
| 2026-09-20 19:02:04 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-09-20 19:01:51 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 19:01:43 | Magura (Kalu Ganga) | 5.50 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-09-20 19:01:30 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:01:27 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 19:01:22 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:00:53 | Pitabeddara (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.032 |  |
| 2026-09-20 19:00:42 | Thalgahagoda (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-20 19:00:11 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 19:07:45 | Panadugama (Nilwala Ganga) | 6.04 | 🟠 Minor Flood | 0.086 | 🔺 Rising |
| 2026-09-20 19:02:09 | Nawalapitiya (Mahaweli Ganga) | 3.68 | 🟡 Alert | 0.243 | 🔺 Rising |
| 2026-09-20 19:04:55 | Baddegama (Gin Ganga) | 3.56 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-09-20 19:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-09-20 19:01:43 | Magura (Kalu Ganga) | 5.50 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-09-20 19:07:39 | Glencourse (Kelani Ganga) | 15.56 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-09-20 19:08:41 | Thawalama (Gin Ganga) | 5.42 | 🟡 Alert | 0.027 | 🔺 Rising |
| 2026-09-20 19:06:32 | Rathnapura (Kalu Ganga) | 6.69 | 🟡 Alert | -0.057 |  |
| 2026-09-20 19:03:11 | Norwood (Kelani Ganga) | 1.89 | 🟡 Alert | -0.170 |  |
| 2026-09-20 19:04:29 | Peradeniya (Mahaweli Ganga) | 5.77 | 🟡 Alert | -0.408 |  |
| 2026-09-20 19:03:02 | Giriulla (Maha Oya) | 3.50 | 🟢 Normal | 0.390 | 🔺 Rising |
| 2026-09-20 19:07:50 | Holombuwa (Kelani Ganga) | 2.98 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-09-20 19:06:49 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-09-20 19:04:30 | Hanwella (Kelani Ganga) | 6.26 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-09-20 19:02:25 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-20 19:00:42 | Thalgahagoda (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-20 19:02:43 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-20 19:02:45 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 19:06:21 | Putupaula (Kalu Ganga) | 2.06 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-20 19:01:51 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 19:01:27 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 19:03:35 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:00:11 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:02:04 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:01:22 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:04:06 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:02:18 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:05:00 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:04:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 19:01:30 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-20 19:02:28 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.012 |  |
| 2026-09-20 19:00:53 | Pitabeddara (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.032 |  |
| 2026-09-20 19:04:17 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.040 |  |
| 2026-09-20 19:05:29 | Kithulgala (Kelani Ganga) | 2.80 | 🟢 Normal | -0.144 |  |
| 2026-09-20 18:04:16 | Deraniyagala (Kelani Ganga) | 3.61 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)