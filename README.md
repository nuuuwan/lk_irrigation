# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_20:15:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,963 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 20:15:39 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:13:58 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:10:31 | Panadugama (Nilwala Ganga) | 6.75 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-24 20:10:25 | Kithulgala (Kelani Ganga) | 3.53 | 🟡 Alert | -0.203 |  |
| 2026-09-24 20:09:10 | Pitabeddara (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.147 |  |
| 2026-09-24 20:07:39 | Rathnapura (Kalu Ganga) | 6.03 | 🟡 Alert | 0.099 | 🔺 Rising |
| 2026-09-24 20:07:29 | Baddegama (Gin Ganga) | 4.50 | 🟠 Minor Flood | 0.018 | 🔺 Rising |
| 2026-09-24 20:07:14 | Norwood (Kelani Ganga) | 1.51 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-09-24 20:06:20 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 20:06:07 | Urawa (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-09-24 20:05:55 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:05:27 | Glencourse (Kelani Ganga) | 14.09 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-24 20:04:52 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:04:23 | Deraniyagala (Kelani Ganga) | 4.33 | 🟢 Normal | -0.069 |  |
| 2026-09-24 20:03:59 | Holombuwa (Kelani Ganga) | 2.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 20:03:29 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-09-24 20:03:26 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-24 20:03:16 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-09-24 20:03:06 | Thawalama (Gin Ganga) | 5.14 | 🟡 Alert | -0.040 |  |
| 2026-09-24 20:02:50 | Nawalapitiya (Mahaweli Ganga) | 3.70 | 🟡 Alert | -0.180 |  |
| 2026-09-24 20:02:49 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:02:46 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-24 20:02:40 | Peradeniya (Mahaweli Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:02:22 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-09-24 20:02:11 | Hanwella (Kelani Ganga) | 5.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-24 20:02:10 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-09-24 20:02:02 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:01:54 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-24 20:01:50 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-09-24 20:01:32 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:01:20 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-09-24 20:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.76 | 🟠 Minor Flood | 0.033 | 🔺 Rising |
| 2026-09-24 20:00:50 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:00:26 | Magura (Kalu Ganga) | 5.04 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-24 20:00:09 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 20:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.76 | 🟠 Minor Flood | 0.033 | 🔺 Rising |
| 2026-09-24 20:01:50 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-09-24 20:07:29 | Baddegama (Gin Ganga) | 4.50 | 🟠 Minor Flood | 0.018 | 🔺 Rising |
| 2026-09-24 20:10:31 | Panadugama (Nilwala Ganga) | 6.75 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-24 20:07:39 | Rathnapura (Kalu Ganga) | 6.03 | 🟡 Alert | 0.099 | 🔺 Rising |
| 2026-09-24 20:07:14 | Norwood (Kelani Ganga) | 1.51 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-09-24 20:00:26 | Magura (Kalu Ganga) | 5.04 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-24 20:03:06 | Thawalama (Gin Ganga) | 5.14 | 🟡 Alert | -0.040 |  |
| 2026-09-24 20:02:50 | Nawalapitiya (Mahaweli Ganga) | 3.70 | 🟡 Alert | -0.180 |  |
| 2026-09-24 20:10:25 | Kithulgala (Kelani Ganga) | 3.53 | 🟡 Alert | -0.203 |  |
| 2026-09-24 20:03:29 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-09-24 20:05:27 | Glencourse (Kelani Ganga) | 14.09 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-24 20:02:11 | Hanwella (Kelani Ganga) | 5.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-24 20:03:26 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-24 20:01:54 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-24 20:02:46 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-24 20:00:09 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 20:06:20 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 20:03:59 | Holombuwa (Kelani Ganga) | 2.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:00:50 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:15:39 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:13:58 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:05:55 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:02:49 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:01:32 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:04:52 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:02:40 | Peradeniya (Mahaweli Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:02:02 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 20:03:16 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-09-24 20:02:10 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-09-24 20:02:22 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-09-24 20:01:20 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-09-24 20:06:07 | Urawa (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-09-24 20:04:23 | Deraniyagala (Kelani Ganga) | 4.33 | 🟢 Normal | -0.069 |  |
| 2026-09-24 20:09:10 | Pitabeddara (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)