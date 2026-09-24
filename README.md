# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_15:10:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,774 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 15:10:40 | Panadugama (Nilwala Ganga) | 6.73 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-24 15:09:15 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:09:02 | Thalgahagoda (Nilwala Ganga) | 1.67 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-09-24 15:08:39 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 15:08:08 | Thawalama (Gin Ganga) | 5.32 | 🟡 Alert | -0.021 |  |
| 2026-09-24 15:07:32 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:07:24 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:06:33 | Pitabeddara (Nilwala Ganga) | 4.21 | 🟡 Alert | -0.084 |  |
| 2026-09-24 15:05:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:05:42 | Urawa (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.108 |  |
| 2026-09-24 15:05:42 | Rathnapura (Kalu Ganga) | 5.99 | 🟡 Alert | -0.020 |  |
| 2026-09-24 15:05:25 | Ellagawa (Kalu Ganga) | 8.03 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 15:04:56 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-09-24 15:04:50 | Nawalapitiya (Mahaweli Ganga) | 2.77 | 🟢 Normal | -0.117 |  |
| 2026-09-24 15:04:42 | Hanwella (Kelani Ganga) | 5.13 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-09-24 15:04:39 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-24 15:04:38 | Baddegama (Gin Ganga) | 4.40 | 🟠 Minor Flood | 0.033 | 🔺 Rising |
| 2026-09-24 15:04:34 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-24 15:04:31 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-24 15:04:30 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:04:21 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:04:16 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:03:47 | Glencourse (Kelani Ganga) | 13.68 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-09-24 15:03:39 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-09-24 15:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 15:03:19 | Holombuwa (Kelani Ganga) | 2.04 | 🟢 Normal | -0.162 |  |
| 2026-09-24 15:03:15 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 15:03:03 | Deraniyagala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.040 |  |
| 2026-09-24 15:02:46 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 15:02:35 | Peradeniya (Mahaweli Ganga) | 4.22 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-24 15:02:33 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:02:25 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:02:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:02:05 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-24 15:01:56 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:01:39 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:01:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:01:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:00:44 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:00:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:00:19 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 15:04:38 | Baddegama (Gin Ganga) | 4.40 | 🟠 Minor Flood | 0.033 | 🔺 Rising |
| 2026-09-24 15:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 15:10:40 | Panadugama (Nilwala Ganga) | 6.73 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-24 15:03:39 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-09-24 15:09:02 | Thalgahagoda (Nilwala Ganga) | 1.67 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-09-24 15:05:42 | Rathnapura (Kalu Ganga) | 5.99 | 🟡 Alert | -0.020 |  |
| 2026-09-24 15:08:08 | Thawalama (Gin Ganga) | 5.32 | 🟡 Alert | -0.021 |  |
| 2026-09-24 15:06:33 | Pitabeddara (Nilwala Ganga) | 4.21 | 🟡 Alert | -0.084 |  |
| 2026-09-24 15:03:47 | Glencourse (Kelani Ganga) | 13.68 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-09-24 15:04:42 | Hanwella (Kelani Ganga) | 5.13 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-09-24 15:02:35 | Peradeniya (Mahaweli Ganga) | 4.22 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-24 15:05:25 | Ellagawa (Kalu Ganga) | 8.03 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 15:04:39 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-24 15:04:31 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-24 15:04:34 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-24 15:08:39 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 15:02:46 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 15:03:15 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 15:00:19 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:00:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:09:15 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:01:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:00:44 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:05:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:04:30 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:07:24 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:07:32 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:01:39 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:04:16 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:02:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:01:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:04:21 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:02:33 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-24 15:02:05 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-24 15:04:56 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-09-24 15:03:03 | Deraniyagala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.040 |  |
| 2026-09-24 15:05:42 | Urawa (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.108 |  |
| 2026-09-24 15:04:50 | Nawalapitiya (Mahaweli Ganga) | 2.77 | 🟢 Normal | -0.117 |  |
| 2026-09-24 15:03:19 | Holombuwa (Kelani Ganga) | 2.04 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)