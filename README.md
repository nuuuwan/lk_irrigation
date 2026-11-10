# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_19:03:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,227 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 19:03:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.123 |  |
| 2026-11-10 19:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-10 19:02:28 | Ellagawa (Kalu Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 19:02:05 | Nakkala (Kumbukkan Oya) | 1.79 | 🟢 Normal | 0.556 | 🔺 Rising |
| 2026-11-10 19:02:03 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-10 19:02:03 | Deraniyagala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.474 |  |
| 2026-11-10 19:01:33 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-11-10 19:01:27 | Pitabeddara (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-11-10 19:01:22 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.061 |  |
| 2026-11-10 19:01:12 | Panadugama (Nilwala Ganga) | 5.75 | 🟡 Alert | 0.000 |  |
| 2026-11-10 19:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 19:00:15 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 18:00:36 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-11-10 18:07:12 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 19:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 18:00:49 | Dunamale (Aththanagalu Oya) | 4.54 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-10 18:10:04 | Moraketiya (Walawe Ganga) | 3.24 | 🟡 Alert | 0.190 | 🔺 Rising |
| 2026-11-10 19:01:12 | Panadugama (Nilwala Ganga) | 5.75 | 🟡 Alert | 0.000 |  |
| 2026-11-10 18:04:01 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | -0.087 |  |
| 2026-11-10 18:02:21 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | 0.725 | 🔺 Rising |
| 2026-11-10 19:02:05 | Nakkala (Kumbukkan Oya) | 1.79 | 🟢 Normal | 0.556 | 🔺 Rising |
| 2026-11-10 18:02:56 | Siyambalanduwa (Heda Oya) | 1.81 | 🟢 Normal | 0.513 | 🔺 Rising |
| 2026-11-10 19:01:27 | Pitabeddara (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-11-10 18:03:39 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-11-10 18:03:57 | Rathnapura (Kalu Ganga) | 4.35 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-11-10 18:02:33 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-11-10 18:04:25 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-10 18:01:19 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-11-10 19:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-10 19:02:03 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-10 18:04:14 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-10 18:02:19 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-10 18:03:23 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 19:00:15 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:11:39 | Hanwella (Kelani Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-10 19:02:28 | Ellagawa (Kalu Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:32 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-10 18:07:48 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-11-10 18:05:36 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-11-10 18:03:10 | Glencourse (Kelani Ganga) | 11.76 | 🟢 Normal | -0.032 |  |
| 2026-11-10 18:09:13 | Badalgama (Maha Oya) | 3.49 | 🟢 Normal | -0.039 |  |
| 2026-11-10 18:02:55 | Giriulla (Maha Oya) | 2.19 | 🟢 Normal | -0.040 |  |
| 2026-11-10 19:01:33 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-11-10 18:06:46 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.048 |  |
| 2026-11-10 19:01:22 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.061 |  |
| 2026-11-10 18:04:59 | Moragaswewa (Deduru Oya) | 3.94 | 🟢 Normal | -0.073 |  |
| 2026-11-10 19:03:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.123 |  |
| 2026-11-10 19:02:03 | Deraniyagala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.474 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)