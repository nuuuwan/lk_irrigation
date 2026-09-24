# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_07:23:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,461 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Pitabeddara — Alert; 🟡 Thawalama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 07:23:05 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.007 |  |
| 2026-09-24 07:19:19 | Panadugama (Nilwala Ganga) | 6.41 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 07:17:51 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-24 07:16:53 | Panadugama (Nilwala Ganga) | 6.41 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 07:16:04 | Urawa (Nilwala Ganga) | 3.04 | 🟡 Alert | -0.105 |  |
| 2026-09-24 07:11:39 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-24 07:10:00 | Thawalama (Gin Ganga) | 5.08 | 🟡 Alert | 0.095 | 🔺 Rising |
| 2026-09-24 07:09:32 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:09:25 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 07:08:53 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.094 | 🔺 Rising |
| 2026-09-24 07:08:16 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | 0.039 | 🔺 Rising |
| 2026-09-24 07:08:11 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-24 07:06:26 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-24 07:06:03 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-09-24 07:06:00 | Nawalapitiya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-24 07:05:51 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-09-24 07:05:34 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:05:34 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | -0.033 |  |
| 2026-09-24 07:05:32 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:04:38 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:04:35 | Pitabeddara (Nilwala Ganga) | 4.56 | 🟡 Alert | 0.133 | 🔺 Rising |
| 2026-09-24 07:04:28 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-09-24 07:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | -0.065 |  |
| 2026-09-24 07:04:05 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-09-24 07:03:54 | Rathnapura (Kalu Ganga) | 5.07 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-09-24 07:03:51 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:03:46 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 07:03:43 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:03:36 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 07:03:20 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:02:37 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-09-24 07:02:34 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:02:15 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:02:14 | Kithulgala (Kelani Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:02:04 | Magura (Kalu Ganga) | 4.50 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-09-24 07:01:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:01:32 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.022 |  |
| 2026-09-24 07:01:14 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 07:01:14 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:00:36 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 07:08:16 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | 0.039 | 🔺 Rising |
| 2026-09-24 07:19:19 | Panadugama (Nilwala Ganga) | 6.41 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 07:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | -0.065 |  |
| 2026-09-24 07:04:35 | Pitabeddara (Nilwala Ganga) | 4.56 | 🟡 Alert | 0.133 | 🔺 Rising |
| 2026-09-24 07:10:00 | Thawalama (Gin Ganga) | 5.08 | 🟡 Alert | 0.095 | 🔺 Rising |
| 2026-09-24 07:08:53 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.094 | 🔺 Rising |
| 2026-09-24 07:02:04 | Magura (Kalu Ganga) | 4.50 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-09-24 07:16:04 | Urawa (Nilwala Ganga) | 3.04 | 🟡 Alert | -0.105 |  |
| 2026-09-24 07:06:03 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-09-24 07:04:28 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-09-24 07:03:54 | Rathnapura (Kalu Ganga) | 5.07 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-09-24 07:06:00 | Nawalapitiya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-24 07:06:26 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-24 07:11:39 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-24 07:03:46 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 07:09:25 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 07:01:14 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 07:08:11 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-24 07:03:36 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 07:17:51 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-24 07:02:14 | Kithulgala (Kelani Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:00:36 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:01:14 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:01:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:03:43 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:04:38 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:09:32 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:02:34 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:03:51 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:03:20 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:05:32 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:05:34 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:02:15 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:23:05 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.007 |  |
| 2026-09-24 07:05:51 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-09-24 07:02:37 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-09-24 07:04:05 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-09-24 07:01:32 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.022 |  |
| 2026-09-24 07:05:34 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | -0.033 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)