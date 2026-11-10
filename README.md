# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_12:10:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 12:10:53 | Baddegama (Gin Ganga) | 4.22 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 12:09:27 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.078 |  |
| 2026-11-10 12:08:08 | Magura (Kalu Ganga) | 4.84 | 🟡 Alert | -0.053 |  |
| 2026-11-10 12:08:05 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.097 |  |
| 2026-11-10 12:06:58 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:06:25 | Glencourse (Kelani Ganga) | 12.55 | 🟢 Normal | -0.257 |  |
| 2026-11-10 12:06:12 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:05:33 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:05:30 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.039 |  |
| 2026-11-10 12:04:49 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 12:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.61 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-11-10 12:04:04 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:03:46 | Hanwella (Kelani Ganga) | 5.60 | 🟢 Normal | -0.160 |  |
| 2026-11-10 12:03:38 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:03:28 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-10 12:03:24 | Rathnapura (Kalu Ganga) | 4.54 | 🟢 Normal | -0.099 |  |
| 2026-11-10 12:03:13 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.022 |  |
| 2026-11-10 12:03:10 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 12:02:57 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:02:53 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-10 12:02:50 | Moragaswewa (Deduru Oya) | 4.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-10 12:02:33 | Panadugama (Nilwala Ganga) | 5.92 | 🟡 Alert | -0.043 |  |
| 2026-11-10 12:02:30 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-11-10 12:02:27 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.133 |  |
| 2026-11-10 12:02:19 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:02:14 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-10 12:02:06 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-10 12:01:57 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.052 |  |
| 2026-11-10 12:01:56 | Giriulla (Maha Oya) | 2.46 | 🟢 Normal | -0.085 |  |
| 2026-11-10 12:01:38 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:01:35 | Moraketiya (Walawe Ganga) | 2.93 | 🟢 Normal | -0.020 |  |
| 2026-11-10 12:01:25 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.050 |  |
| 2026-11-10 12:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-10 12:01:22 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-11-10 12:01:11 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | -0.069 |  |
| 2026-11-10 12:01:06 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-10 12:00:43 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-11-10 12:00:30 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.000 |  |
| 2026-11-10 12:00:17 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 12:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.61 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-11-10 12:10:53 | Baddegama (Gin Ganga) | 4.22 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 12:03:10 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 12:00:30 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.000 |  |
| 2026-11-10 12:02:33 | Panadugama (Nilwala Ganga) | 5.92 | 🟡 Alert | -0.043 |  |
| 2026-11-10 12:08:08 | Magura (Kalu Ganga) | 4.84 | 🟡 Alert | -0.053 |  |
| 2026-11-10 12:02:06 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-10 12:02:14 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-10 12:01:06 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-10 12:02:53 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-10 12:02:50 | Moragaswewa (Deduru Oya) | 4.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-10 12:04:49 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 12:02:19 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:01:38 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:02:57 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:03:38 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:06:58 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:05:33 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:06:12 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-10 12:02:30 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-11-10 12:03:28 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-10 12:00:17 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-11-10 12:00:43 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-11-10 12:01:35 | Moraketiya (Walawe Ganga) | 2.93 | 🟢 Normal | -0.020 |  |
| 2026-11-10 12:01:22 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-11-10 12:03:13 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.022 |  |
| 2026-11-10 12:05:30 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.039 |  |
| 2026-11-10 12:01:25 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.050 |  |
| 2026-11-10 12:01:57 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.052 |  |
| 2026-11-10 12:01:11 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | -0.069 |  |
| 2026-11-10 12:09:27 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.078 |  |
| 2026-11-10 12:01:56 | Giriulla (Maha Oya) | 2.46 | 🟢 Normal | -0.085 |  |
| 2026-11-10 12:08:05 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.097 |  |
| 2026-11-10 12:03:24 | Rathnapura (Kalu Ganga) | 4.54 | 🟢 Normal | -0.099 |  |
| 2026-11-10 12:02:27 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.133 |  |
| 2026-11-10 12:03:46 | Hanwella (Kelani Ganga) | 5.60 | 🟢 Normal | -0.160 |  |
| 2026-11-10 12:06:25 | Glencourse (Kelani Ganga) | 12.55 | 🟢 Normal | -0.257 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)