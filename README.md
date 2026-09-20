# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_21:18:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,373 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thawalama — Alert; 🟡 Glencourse — Alert; 🟡 Baddegama — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 21:18:16 | Panadugama (Nilwala Ganga) | 6.16 | 🟠 Minor Flood | 0.059 | 🔺 Rising |
| 2026-09-20 21:10:45 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-20 21:09:40 | Rathnapura (Kalu Ganga) | 6.59 | 🟡 Alert | -0.040 |  |
| 2026-09-20 21:08:36 | Baddegama (Gin Ganga) | 3.61 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-20 21:07:25 | Holombuwa (Kelani Ganga) | 3.11 | 🟡 Alert | -0.051 |  |
| 2026-09-20 21:06:59 | Putupaula (Kalu Ganga) | 2.17 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-20 21:06:32 | Glencourse (Kelani Ganga) | 15.60 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-09-20 21:06:28 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-09-20 21:06:22 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:05:54 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | -0.117 |  |
| 2026-09-20 21:05:36 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | 0.496 | 🔺 Rising |
| 2026-09-20 21:05:36 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-20 21:05:15 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:04:48 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-20 21:04:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.02 | 🟡 Alert | 0.048 | 🔺 Rising |
| 2026-09-20 21:04:18 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.058 |  |
| 2026-09-20 21:04:01 | Peradeniya (Mahaweli Ganga) | 5.25 | 🟡 Alert | -0.226 |  |
| 2026-09-20 21:04:01 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:03:58 | Norwood (Kelani Ganga) | 1.72 | 🟡 Alert | -0.088 |  |
| 2026-09-20 21:03:52 | Thawalama (Gin Ganga) | 5.48 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-20 21:03:49 | Hanwella (Kelani Ganga) | 6.55 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-20 21:03:47 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-20 21:03:46 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:03:37 | Pitabeddara (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.129 |  |
| 2026-09-20 21:03:20 | Deraniyagala (Kelani Ganga) | 2.71 | 🟢 Normal | -0.101 |  |
| 2026-09-20 21:02:50 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 21:02:44 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:02:20 | Dunamale (Aththanagalu Oya) | 3.26 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-20 21:01:52 | Nawalapitiya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.284 |  |
| 2026-09-20 21:01:27 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-20 21:01:24 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-09-20 21:01:22 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:00:39 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 21:00:24 | Magura (Kalu Ganga) | 5.56 | 🟡 Alert | 0.000 |  |
| 2026-09-20 20:59:39 | Magura (Kalu Ganga) | 5.56 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 21:18:16 | Panadugama (Nilwala Ganga) | 6.16 | 🟠 Minor Flood | 0.059 | 🔺 Rising |
| 2026-09-20 21:04:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.02 | 🟡 Alert | 0.048 | 🔺 Rising |
| 2026-09-20 21:03:52 | Thawalama (Gin Ganga) | 5.48 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-20 21:06:32 | Glencourse (Kelani Ganga) | 15.60 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-09-20 21:08:36 | Baddegama (Gin Ganga) | 3.61 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-20 21:00:24 | Magura (Kalu Ganga) | 5.56 | 🟡 Alert | 0.000 |  |
| 2026-09-20 21:09:40 | Rathnapura (Kalu Ganga) | 6.59 | 🟡 Alert | -0.040 |  |
| 2026-09-20 21:07:25 | Holombuwa (Kelani Ganga) | 3.11 | 🟡 Alert | -0.051 |  |
| 2026-09-20 21:03:58 | Norwood (Kelani Ganga) | 1.72 | 🟡 Alert | -0.088 |  |
| 2026-09-20 21:04:01 | Peradeniya (Mahaweli Ganga) | 5.25 | 🟡 Alert | -0.226 |  |
| 2026-09-20 21:05:36 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | 0.496 | 🔺 Rising |
| 2026-09-20 21:03:49 | Hanwella (Kelani Ganga) | 6.55 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-20 21:02:20 | Dunamale (Aththanagalu Oya) | 3.26 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-20 21:10:45 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-20 21:05:36 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-20 21:06:59 | Putupaula (Kalu Ganga) | 2.17 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-20 21:04:48 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 21:02:50 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 21:00:39 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 21:02:44 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 20:43:02 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:04:01 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:01:22 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:05:15 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:03:46 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:06:22 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 21:03:47 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-20 21:01:27 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-20 21:01:24 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-09-20 21:06:28 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-09-20 21:04:18 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.058 |  |
| 2026-09-20 21:03:20 | Deraniyagala (Kelani Ganga) | 2.71 | 🟢 Normal | -0.101 |  |
| 2026-09-20 21:05:54 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | -0.117 |  |
| 2026-09-20 21:03:37 | Pitabeddara (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.129 |  |
| 2026-09-20 21:01:52 | Nawalapitiya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.284 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)