# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_03:17:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,910 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 03:17:25 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.036 |  |
| 2026-10-28 03:11:38 | Ellagawa (Kalu Ganga) | 10.42 | 🟡 Alert | 0.000 |  |
| 2026-10-28 03:11:00 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-10-28 03:09:01 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-10-28 03:08:58 | Baddegama (Gin Ganga) | 4.21 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 03:08:38 | Urawa (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-28 03:08:18 | Pitabeddara (Nilwala Ganga) | 2.62 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-10-28 03:08:17 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-10-28 03:08:16 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-10-28 03:07:15 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-28 03:06:52 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:05:55 | Rathnapura (Kalu Ganga) | 6.99 | 🟡 Alert | -0.078 |  |
| 2026-10-28 03:05:48 | Moragaswewa (Deduru Oya) | 3.61 | 🟢 Normal | -0.132 |  |
| 2026-10-28 03:05:06 | Putupaula (Kalu Ganga) | 3.51 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-10-28 03:04:40 | Hanwella (Kelani Ganga) | 4.80 | 🟢 Normal | -0.052 |  |
| 2026-10-28 03:04:25 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:04:17 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:03:54 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-28 03:03:53 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | 0.000 |  |
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

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 03:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.84 | 🟠 Minor Flood | 0.042 | 🔺 Rising |
| 2026-10-28 03:02:28 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-28 03:08:58 | Baddegama (Gin Ganga) | 4.21 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 03:02:35 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.015 |  |
| 2026-10-28 03:05:06 | Putupaula (Kalu Ganga) | 3.51 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-10-28 03:11:38 | Ellagawa (Kalu Ganga) | 10.42 | 🟡 Alert | 0.000 |  |
| 2026-10-28 03:02:58 | Magura (Kalu Ganga) | 4.46 | 🟡 Alert | -0.045 |  |
| 2026-10-28 03:02:45 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | -0.070 |  |
| 2026-10-28 03:05:55 | Rathnapura (Kalu Ganga) | 6.99 | 🟡 Alert | -0.078 |  |
| 2026-10-28 03:08:18 | Pitabeddara (Nilwala Ganga) | 2.62 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-10-28 03:02:50 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-28 03:03:54 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-28 03:08:38 | Urawa (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-28 03:03:04 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-28 03:00:58 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-28 03:07:15 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-28 03:01:43 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:04:25 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:03:53 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:02:51 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:03:01 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:04:17 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-28 03:06:52 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:23:14 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | -0.008 |  |
| 2026-10-28 03:09:01 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-10-28 03:11:00 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-10-28 03:03:38 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-28 03:01:10 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.028 |  |
| 2026-10-28 03:02:12 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.035 |  |
| 2026-10-28 03:17:25 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.036 |  |
| 2026-10-28 03:03:08 | Glencourse (Kelani Ganga) | 12.01 | 🟢 Normal | -0.040 |  |
| 2026-10-28 03:03:24 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.040 |  |
| 2026-10-28 02:06:17 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.048 |  |
| 2026-10-28 03:03:39 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | -0.050 |  |
| 2026-10-28 03:04:40 | Hanwella (Kelani Ganga) | 4.80 | 🟢 Normal | -0.052 |  |
| 2026-10-27 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.059 |  |
| 2026-10-28 03:00:01 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.071 |  |
| 2026-10-28 03:05:48 | Moragaswewa (Deduru Oya) | 3.61 | 🟢 Normal | -0.132 |  |
| 2026-10-27 18:00:41 | Thanthirimale (Malwathu Oya) | 2.72 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)