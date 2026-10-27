# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_02:26:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,870 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 02:26:10 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-28 02:25:35 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | -0.004 |  |
| 2026-10-28 02:21:36 | Panadugama (Nilwala Ganga) | 6.03 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-28 02:21:33 | Putupaula (Kalu Ganga) | 3.46 | 🟡 Alert | 0.000 |  |
| 2026-10-28 02:18:33 | Hanwella (Kelani Ganga) | 4.84 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-28 02:17:55 | Ellagawa (Kalu Ganga) | 10.42 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-10-28 02:13:41 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.008 |  |
| 2026-10-28 02:12:29 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 02:11:23 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:11:12 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:10:42 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-28 02:09:29 | Magura (Kalu Ganga) | 4.50 | 🟡 Alert | -0.027 |  |
| 2026-10-28 02:08:41 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -72.000 |  |
| 2026-10-28 02:08:40 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -72.000 |  |
| 2026-10-28 02:06:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.80 | 🟠 Minor Flood | 0.055 | 🔺 Rising |
| 2026-10-28 02:06:17 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.048 |  |
| 2026-10-28 02:05:08 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:04:24 | Rathnapura (Kalu Ganga) | 7.07 | 🟡 Alert | -0.082 |  |
| 2026-10-28 02:04:16 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:03:21 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:03:20 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.051 |  |
| 2026-10-28 02:03:17 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.049 |  |
| 2026-10-28 02:03:15 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-28 02:02:34 | Dunamale (Aththanagalu Oya) | 4.45 | 🟠 Minor Flood | -0.060 |  |
| 2026-10-28 02:02:32 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.040 |  |
| 2026-10-28 02:02:21 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:02:08 | Baddegama (Gin Ganga) | 4.21 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-28 02:02:00 | Moragaswewa (Deduru Oya) | 3.75 | 🟢 Normal | -0.104 |  |
| 2026-10-28 02:01:43 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-28 02:01:42 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:01:24 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 02:00:31 | Peradeniya (Mahaweli Ganga) | 3.19 | 🟢 Normal | -0.031 |  |
| 2026-10-28 01:57:32 | Putupaula (Kalu Ganga) | 3.46 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 02:06:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.80 | 🟠 Minor Flood | 0.055 | 🔺 Rising |
| 2026-10-28 02:02:08 | Baddegama (Gin Ganga) | 4.21 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-28 02:01:24 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 02:21:36 | Panadugama (Nilwala Ganga) | 6.03 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-28 02:02:34 | Dunamale (Aththanagalu Oya) | 4.45 | 🟠 Minor Flood | -0.060 |  |
| 2026-10-28 02:17:55 | Ellagawa (Kalu Ganga) | 10.42 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-10-28 02:21:33 | Putupaula (Kalu Ganga) | 3.46 | 🟡 Alert | 0.000 |  |
| 2026-10-28 02:09:29 | Magura (Kalu Ganga) | 4.50 | 🟡 Alert | -0.027 |  |
| 2026-10-28 02:04:24 | Rathnapura (Kalu Ganga) | 7.07 | 🟡 Alert | -0.082 |  |
| 2026-10-28 02:01:43 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-28 00:09:46 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-28 02:26:10 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-28 02:12:29 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 02:18:33 | Hanwella (Kelani Ganga) | 4.84 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-28 01:00:17 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-28 01:18:20 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:05:08 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:02:21 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:11:12 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:01:42 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:04:16 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:11:23 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-28 02:25:35 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | -0.004 |  |
| 2026-10-27 18:23:14 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | -0.008 |  |
| 2026-10-28 02:13:41 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.008 |  |
| 2026-10-28 02:03:15 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-28 01:06:39 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-28 02:10:42 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-28 01:13:47 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-10-28 02:00:31 | Peradeniya (Mahaweli Ganga) | 3.19 | 🟢 Normal | -0.031 |  |
| 2026-10-28 02:02:32 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.040 |  |
| 2026-10-28 02:06:17 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.048 |  |
| 2026-10-28 02:03:17 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.049 |  |
| 2026-10-28 02:03:20 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.051 |  |
| 2026-10-28 01:02:55 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.051 |  |
| 2026-10-27 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.059 |  |
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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)