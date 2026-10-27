# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_03:03:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Ellagawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 03:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.84 | 🟠 Minor Flood | 0.042 | 🔺 Rising |
| 2026-10-28 03:03:39 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | -0.050 |  |
| 2026-10-28 03:03:38 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-28 03:03:24 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.040 |  |
| 2026-10-28 03:03:08 | Glencourse (Kelani Ganga) | 12.01 | 🟢 Normal | -0.040 |  |
| 2026-10-28 03:03:04 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-28 03:03:01 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:02:58 | Magura (Kalu Ganga) | 4.46 | 🟡 Alert | -0.045 |  |
| 2026-10-28 03:02:51 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:02:50 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-28 03:02:45 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | -0.070 |  |
| 2026-10-28 03:02:35 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.015 |  |
| 2026-10-28 03:02:28 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-28 03:02:12 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.035 |  |
| 2026-10-28 03:01:43 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:01:15 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:01:10 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.028 |  |
| 2026-10-28 03:00:58 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-28 03:00:01 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.071 |  |
| 2026-10-28 02:39:43 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.028 |  |
| 2026-10-28 02:35:29 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.007 |  |
| 2026-10-28 02:26:10 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-28 02:25:35 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | -0.004 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 03:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.84 | 🟠 Minor Flood | 0.042 | 🔺 Rising |
| 2026-10-28 02:02:08 | Baddegama (Gin Ganga) | 4.21 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-28 03:02:28 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-28 03:02:35 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.015 |  |
| 2026-10-28 02:17:55 | Ellagawa (Kalu Ganga) | 10.42 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-10-28 02:21:33 | Putupaula (Kalu Ganga) | 3.46 | 🟡 Alert | 0.000 |  |
| 2026-10-28 03:02:58 | Magura (Kalu Ganga) | 4.46 | 🟡 Alert | -0.045 |  |
| 2026-10-28 03:02:45 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | -0.070 |  |
| 2026-10-28 02:04:24 | Rathnapura (Kalu Ganga) | 7.07 | 🟡 Alert | -0.082 |  |
| 2026-10-28 03:02:50 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-28 03:03:04 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-28 00:09:46 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-28 02:26:10 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-28 03:00:58 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-28 02:12:29 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 02:18:33 | Hanwella (Kelani Ganga) | 4.84 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-28 03:01:43 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:05:08 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:02:51 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:03:01 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:04:16 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:25:35 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | -0.004 |  |
| 2026-10-28 02:35:29 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.007 |  |
| 2026-10-27 18:23:14 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | -0.008 |  |
| 2026-10-28 02:13:41 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.008 |  |
| 2026-10-28 01:06:39 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-28 02:10:42 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-28 03:03:38 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-28 03:01:10 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.028 |  |
| 2026-10-28 03:02:12 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.035 |  |
| 2026-10-28 03:03:08 | Glencourse (Kelani Ganga) | 12.01 | 🟢 Normal | -0.040 |  |
| 2026-10-28 03:03:24 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.040 |  |
| 2026-10-28 02:06:17 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.048 |  |
| 2026-10-28 03:03:39 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | -0.050 |  |
| 2026-10-27 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.059 |  |
| 2026-10-28 03:00:01 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.071 |  |
| 2026-10-28 02:02:00 | Moragaswewa (Deduru Oya) | 3.75 | 🟢 Normal | -0.104 |  |
| 2026-10-27 18:00:41 | Thanthirimale (Malwathu Oya) | 2.72 | 🟢 Normal | -0.133 |  |
| 2026-10-28 02:08:41 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)