# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_15:17:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,000 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 15:17:21 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-11 15:11:04 | Magura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.083 |  |
| 2026-11-11 15:10:01 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-11-11 15:08:49 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:08:19 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:08:01 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-11 15:07:02 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 15:06:39 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.072 |  |
| 2026-11-11 15:06:18 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-11 15:06:15 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-11 15:06:12 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.057 |  |
| 2026-11-11 15:05:30 | Badalgama (Maha Oya) | 3.54 | 🟢 Normal | -0.072 |  |
| 2026-11-11 15:05:27 | Panadugama (Nilwala Ganga) | 5.50 | 🟡 Alert | -0.039 |  |
| 2026-11-11 15:04:56 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:04:29 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 15:04:27 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-11 15:04:20 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.039 |  |
| 2026-11-11 15:04:06 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:03:50 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-11-11 15:03:47 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:03:38 | Dunamale (Aththanagalu Oya) | 3.84 | 🟡 Alert | -0.074 |  |
| 2026-11-11 15:03:32 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | -0.031 |  |
| 2026-11-11 15:03:30 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.093 |  |
| 2026-11-11 15:03:28 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 15:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.53 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-11 15:03:11 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.059 |  |
| 2026-11-11 15:03:04 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-11-11 15:02:58 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 15:02:49 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:02:48 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-11-11 15:02:41 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.078 |  |
| 2026-11-11 15:02:39 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:02:15 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 15:02:05 | Moragaswewa (Deduru Oya) | 3.22 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-11 15:01:58 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:01:29 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-11-11 15:01:26 | Ellagawa (Kalu Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:00:50 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-11 15:00:26 | Wellawaya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.210 |  |
| 2026-11-11 15:00:14 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 15:03:28 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 15:07:02 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 15:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.53 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-11 15:05:27 | Panadugama (Nilwala Ganga) | 5.50 | 🟡 Alert | -0.039 |  |
| 2026-11-11 15:03:38 | Dunamale (Aththanagalu Oya) | 3.84 | 🟡 Alert | -0.074 |  |
| 2026-11-11 15:06:18 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-11 15:02:05 | Moragaswewa (Deduru Oya) | 3.22 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-11 15:17:21 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-11 15:06:15 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-11 15:02:15 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 15:08:01 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-11 15:02:58 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 15:04:29 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 15:04:06 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:01:58 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:02:49 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:01:26 | Ellagawa (Kalu Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:04:56 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:02:39 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:03:47 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:08:49 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:10:01 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-11-11 15:04:27 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-11 15:00:50 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-11 15:03:04 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-11-11 15:02:48 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-11-11 15:03:50 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-11-11 15:01:29 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-11-11 15:00:14 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.022 |  |
| 2026-11-11 15:03:32 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | -0.031 |  |
| 2026-11-11 15:04:20 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.039 |  |
| 2026-11-11 15:06:12 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.057 |  |
| 2026-11-11 15:03:11 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.059 |  |
| 2026-11-11 15:05:30 | Badalgama (Maha Oya) | 3.54 | 🟢 Normal | -0.072 |  |
| 2026-11-11 15:06:39 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.072 |  |
| 2026-11-11 15:02:41 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.078 |  |
| 2026-11-11 15:11:04 | Magura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.083 |  |
| 2026-11-11 15:03:30 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.093 |  |
| 2026-11-11 15:00:26 | Wellawaya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)