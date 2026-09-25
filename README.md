# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_05:44:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,283 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Norwood — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 05:44:36 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:16:38 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 05:13:28 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:11:48 | Nawalapitiya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-25 05:11:46 | Baddegama (Gin Ganga) | 4.63 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-25 05:10:30 | Norwood (Kelani Ganga) | 1.82 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-09-25 05:09:23 | Panadugama (Nilwala Ganga) | 6.58 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-25 05:08:24 | Magura (Kalu Ganga) | 4.94 | 🟡 Alert | -0.018 |  |
| 2026-09-25 05:07:38 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.093 |  |
| 2026-09-25 05:07:28 | Glencourse (Kelani Ganga) | 14.61 | 🟢 Normal | -64.800 |  |
| 2026-09-25 05:07:27 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 05:07:23 | Glencourse (Kelani Ganga) | 14.70 | 🟢 Normal | -64.800 |  |
| 2026-09-25 05:07:21 | Rathnapura (Kalu Ganga) | 6.45 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-25 05:07:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.87 | 🟠 Minor Flood | 0.043 | 🔺 Rising |
| 2026-09-25 05:07:01 | Thawalama (Gin Ganga) | 4.25 | 🟡 Alert | -0.030 |  |
| 2026-09-25 05:06:52 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:06:26 | Holombuwa (Kelani Ganga) | 1.63 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-25 05:06:10 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.071 |  |
| 2026-09-25 05:06:08 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-25 05:06:07 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-09-25 05:05:49 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.103 |  |
| 2026-09-25 05:05:48 | Deraniyagala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.022 |  |
| 2026-09-25 05:05:38 | Kithulgala (Kelani Ganga) | 2.97 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-25 05:05:18 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:05:04 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-25 05:04:53 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:04:36 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-25 05:04:18 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-09-25 05:04:18 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-25 05:03:35 | Hanwella (Kelani Ganga) | 6.31 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-25 05:03:04 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 05:07:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.87 | 🟠 Minor Flood | 0.043 | 🔺 Rising |
| 2026-09-25 05:11:46 | Baddegama (Gin Ganga) | 4.63 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-25 05:16:38 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 05:09:23 | Panadugama (Nilwala Ganga) | 6.58 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-25 05:10:30 | Norwood (Kelani Ganga) | 1.82 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-09-25 05:07:21 | Rathnapura (Kalu Ganga) | 6.45 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-25 05:08:24 | Magura (Kalu Ganga) | 4.94 | 🟡 Alert | -0.018 |  |
| 2026-09-25 05:07:01 | Thawalama (Gin Ganga) | 4.25 | 🟡 Alert | -0.030 |  |
| 2026-09-25 05:11:48 | Nawalapitiya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-25 05:05:38 | Kithulgala (Kelani Ganga) | 2.97 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-25 05:06:08 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-25 05:03:35 | Hanwella (Kelani Ganga) | 6.31 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-25 05:06:26 | Holombuwa (Kelani Ganga) | 1.63 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-25 05:05:04 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-25 05:04:36 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-25 05:02:44 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 05:01:10 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:01:55 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:00:41 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:00:54 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:44:36 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:04:53 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:06:52 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:05:18 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-25 05:04:18 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-25 05:03:04 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.020 |  |
| 2026-09-25 05:05:48 | Deraniyagala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.022 |  |
| 2026-09-25 05:06:07 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-09-25 05:04:18 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-09-25 05:02:40 | Dunamale (Aththanagalu Oya) | 3.18 | 🟢 Normal | -0.051 |  |
| 2026-09-25 05:06:10 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.071 |  |
| 2026-09-25 05:07:38 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.093 |  |
| 2026-09-25 05:05:49 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.103 |  |
| 2026-09-25 05:01:08 | Peradeniya (Mahaweli Ganga) | 4.30 | 🟢 Normal | -0.256 |  |
| 2026-09-25 05:07:28 | Glencourse (Kelani Ganga) | 14.61 | 🟢 Normal | -64.800 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)