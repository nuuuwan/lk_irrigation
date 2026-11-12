# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_05:31:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,508 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Rathnapura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 05:31:56 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-12 05:31:28 | Moraketiya (Walawe Ganga) | 3.85 | 🟡 Alert | -0.033 |  |
| 2026-11-12 05:30:59 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.101 |  |
| 2026-11-12 05:25:56 | Magura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.121 | 🔺 Rising |
| 2026-11-12 05:21:51 | Urawa (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.141 |  |
| 2026-11-12 05:18:22 | Pitabeddara (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-12 05:16:56 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-12 05:16:02 | Padiyathalawa (Maduru Oya) | 2.10 | 🟢 Normal | -540.000 |  |
| 2026-11-12 05:16:00 | Padiyathalawa (Maduru Oya) | 2.40 | 🟢 Normal | -540.000 |  |
| 2026-11-12 05:15:02 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-12 05:14:23 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-12 05:11:01 | Magura (Kalu Ganga) | 5.44 | 🟡 Alert | 0.121 | 🔺 Rising |
| 2026-11-12 05:10:55 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-12 05:08:57 | Wellawaya (Kirindi Oya) | 2.25 | 🟢 Normal | -0.090 |  |
| 2026-11-12 05:07:10 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 05:06:22 | Badalgama (Maha Oya) | 4.35 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-11-12 05:04:37 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 05:04:27 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.078 |  |
| 2026-11-12 05:03:56 | Dunamale (Aththanagalu Oya) | 4.12 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-12 05:03:24 | Thawalama (Gin Ganga) | 5.04 | 🟡 Alert | 0.000 |  |
| 2026-11-12 05:03:20 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-11-12 05:03:17 | Peradeniya (Mahaweli Ganga) | 5.51 | 🟡 Alert | -0.109 |  |
| 2026-11-12 05:03:05 | Siyambalanduwa (Heda Oya) | 1.65 | 🟢 Normal | -0.260 |  |
| 2026-11-12 05:02:54 | Giriulla (Maha Oya) | 3.62 | 🟢 Normal | -0.110 |  |
| 2026-11-12 05:02:45 | Norwood (Kelani Ganga) | 1.46 | 🟢 Normal | -0.015 |  |
| 2026-11-12 05:02:28 | Katharagama (Menik Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-11-12 05:02:17 | Hanwella (Kelani Ganga) | 5.53 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-11-12 05:02:15 | Thanamalwila (Kirindi Oya) | 3.90 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-12 05:02:15 | Glencourse (Kelani Ganga) | 13.94 | 🟢 Normal | -0.049 |  |
| 2026-11-12 05:02:11 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.171 |  |
| 2026-11-12 05:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | -0.020 |  |
| 2026-11-12 05:01:44 | Kuda Oya (Kirindi Oya) | 3.65 | 🟢 Normal | -0.446 |  |
| 2026-11-12 05:01:41 | Nakkala (Kumbukkan Oya) | 2.05 | 🟢 Normal | -0.150 |  |
| 2026-11-12 05:01:21 | Moragaswewa (Deduru Oya) | 3.65 | 🟢 Normal | -0.020 |  |
| 2026-11-12 05:01:19 | Holombuwa (Kelani Ganga) | 2.34 | 🟢 Normal | -0.260 |  |
| 2026-11-12 05:01:18 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 05:01:18 | Ellagawa (Kalu Ganga) | 8.34 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 05:07:10 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 05:01:18 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 05:25:56 | Magura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.121 | 🔺 Rising |
| 2026-11-12 05:03:56 | Dunamale (Aththanagalu Oya) | 4.12 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-12 05:15:02 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-12 05:16:56 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-12 05:03:24 | Thawalama (Gin Ganga) | 5.04 | 🟡 Alert | 0.000 |  |
| 2026-11-12 05:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | -0.020 |  |
| 2026-11-12 05:31:28 | Moraketiya (Walawe Ganga) | 3.85 | 🟡 Alert | -0.033 |  |
| 2026-11-12 05:03:17 | Peradeniya (Mahaweli Ganga) | 5.51 | 🟡 Alert | -0.109 |  |
| 2026-11-12 05:06:22 | Badalgama (Maha Oya) | 4.35 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-11-12 05:02:17 | Hanwella (Kelani Ganga) | 5.53 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-11-12 05:31:56 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-12 05:02:15 | Thanamalwila (Kirindi Oya) | 3.90 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-12 05:18:22 | Pitabeddara (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-12 05:10:55 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-12 05:04:37 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-12 04:02:16 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-12 05:14:23 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-12 05:01:18 | Ellagawa (Kalu Ganga) | 8.34 | 🟢 Normal | -0.010 |  |
| 2026-11-12 05:02:45 | Norwood (Kelani Ganga) | 1.46 | 🟢 Normal | -0.015 |  |
| 2026-11-12 05:03:20 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-11-12 05:01:21 | Moragaswewa (Deduru Oya) | 3.65 | 🟢 Normal | -0.020 |  |
| 2026-11-12 05:02:28 | Katharagama (Menik Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-11-12 05:02:15 | Glencourse (Kelani Ganga) | 13.94 | 🟢 Normal | -0.049 |  |
| 2026-11-12 05:04:27 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.078 |  |
| 2026-11-12 05:08:57 | Wellawaya (Kirindi Oya) | 2.25 | 🟢 Normal | -0.090 |  |
| 2026-11-12 05:30:59 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.101 |  |
| 2026-11-12 05:02:54 | Giriulla (Maha Oya) | 3.62 | 🟢 Normal | -0.110 |  |
| 2026-11-12 05:21:51 | Urawa (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.141 |  |
| 2026-11-12 05:01:41 | Nakkala (Kumbukkan Oya) | 2.05 | 🟢 Normal | -0.150 |  |
| 2026-11-12 05:02:11 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.171 |  |
| 2026-11-12 05:03:05 | Siyambalanduwa (Heda Oya) | 1.65 | 🟢 Normal | -0.260 |  |
| 2026-11-12 05:01:19 | Holombuwa (Kelani Ganga) | 2.34 | 🟢 Normal | -0.260 |  |
| 2026-11-12 05:01:44 | Kuda Oya (Kirindi Oya) | 3.65 | 🟢 Normal | -0.446 |  |
| 2026-11-12 05:16:02 | Padiyathalawa (Maduru Oya) | 2.10 | 🟢 Normal | -540.000 |  |

## River Water Level Charts by Station

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)