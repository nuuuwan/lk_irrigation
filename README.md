# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_12:09:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,838 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 12:09:46 | Panadugama (Nilwala Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:07:03 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-22 12:06:17 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.039 |  |
| 2026-09-22 12:06:16 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:06:08 | Panadugama (Nilwala Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:05:59 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-22 12:05:54 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-09-22 12:05:19 | Holombuwa (Kelani Ganga) | 1.96 | 🟢 Normal | -0.149 |  |
| 2026-09-22 12:05:13 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | -0.011 |  |
| 2026-09-22 12:05:05 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:04:58 | Glencourse (Kelani Ganga) | 12.59 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-09-22 12:04:17 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:04:08 | Putupaula (Kalu Ganga) | 2.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 12:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 12:03:56 | Rathnapura (Kalu Ganga) | 4.44 | 🟢 Normal | -0.061 |  |
| 2026-09-22 12:03:55 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-09-22 12:03:51 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:03:43 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-22 12:03:31 | Deraniyagala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-09-22 12:03:24 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:03:13 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-22 12:03:12 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-22 12:03:02 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 12:02:53 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:02:50 | Ellagawa (Kalu Ganga) | 8.92 | 🟢 Normal | -0.021 |  |
| 2026-09-22 12:02:49 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:02:44 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.927 |  |
| 2026-09-22 12:02:43 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-22 12:02:30 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:02:22 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-22 12:02:07 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 12:01:38 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:01:27 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:01:20 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.074 |  |
| 2026-09-22 12:01:19 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | 0.000 |  |
| 2026-09-22 12:01:15 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.041 |  |
| 2026-09-22 12:01:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-09-22 12:00:38 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:00:12 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:57:09 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 12:03:02 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 12:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 12:01:19 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | 0.000 |  |
| 2026-09-22 12:03:55 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-09-22 12:04:58 | Glencourse (Kelani Ganga) | 12.59 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-09-22 12:03:31 | Deraniyagala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-09-22 12:03:43 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-22 12:02:07 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 12:07:03 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-22 12:02:43 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-22 12:04:08 | Putupaula (Kalu Ganga) | 2.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 12:00:38 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:01:38 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:01:27 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:02:30 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:05:05 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:09:46 | Panadugama (Nilwala Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:06:16 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:02:49 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:03:51 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:03:24 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:04:17 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:00:12 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 12:02:53 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 11:05:33 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-09-22 12:05:54 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-09-22 12:02:22 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-22 12:03:13 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-22 12:03:12 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-22 12:05:13 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | -0.011 |  |
| 2026-09-22 12:05:59 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-22 12:01:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-09-22 12:02:50 | Ellagawa (Kalu Ganga) | 8.92 | 🟢 Normal | -0.021 |  |
| 2026-09-22 12:06:17 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.039 |  |
| 2026-09-22 12:01:15 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.041 |  |
| 2026-09-22 12:03:56 | Rathnapura (Kalu Ganga) | 4.44 | 🟢 Normal | -0.061 |  |
| 2026-09-22 12:01:20 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.074 |  |
| 2026-09-22 12:05:19 | Holombuwa (Kelani Ganga) | 1.96 | 🟢 Normal | -0.149 |  |
| 2026-09-22 12:02:44 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.927 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)