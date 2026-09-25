# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_11:06:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,512 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 11:06:56 | Baddegama (Gin Ganga) | 4.69 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-25 11:06:49 | Peradeniya (Mahaweli Ganga) | 4.30 | 🟢 Normal | -0.051 |  |
| 2026-09-25 11:06:14 | Thawalama (Gin Ganga) | 4.37 | 🟡 Alert | -0.051 |  |
| 2026-09-25 11:06:03 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.061 |  |
| 2026-09-25 11:05:43 | Panadugama (Nilwala Ganga) | 6.49 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-25 11:05:34 | Magura (Kalu Ganga) | 4.82 | 🟡 Alert | 0.000 |  |
| 2026-09-25 11:05:15 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:04:15 | Urawa (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.015 |  |
| 2026-09-25 11:03:49 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 11:03:47 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | -0.039 |  |
| 2026-09-25 11:03:41 | Kithulgala (Kelani Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:03:34 | Rathnapura (Kalu Ganga) | 6.28 | 🟡 Alert | -0.023 |  |
| 2026-09-25 11:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 11:02:51 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:02:51 | Hanwella (Kelani Ganga) | 6.26 | 🟢 Normal | -0.020 |  |
| 2026-09-25 11:02:36 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | -0.137 |  |
| 2026-09-25 11:02:32 | Ellagawa (Kalu Ganga) | 8.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 11:02:29 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:02:28 | Dunamale (Aththanagalu Oya) | 3.03 | 🟢 Normal | -0.040 |  |
| 2026-09-25 11:02:14 | Deraniyagala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-09-25 11:02:07 | Nagalagam Street (Kelani Ganga) | 1.02 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-25 11:02:03 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:01:59 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-25 11:01:29 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-09-25 11:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:01:15 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-09-25 11:01:08 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-25 11:01:05 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:01:02 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:01:01 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.053 |  |
| 2026-09-25 11:00:54 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:00:41 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-25 11:00:16 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:00:11 | Pitabeddara (Nilwala Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-09-25 10:59:26 | Pitabeddara (Nilwala Ganga) | 2.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 11:06:56 | Baddegama (Gin Ganga) | 4.69 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-25 10:05:22 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 11:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 11:05:43 | Panadugama (Nilwala Ganga) | 6.49 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-25 11:05:34 | Magura (Kalu Ganga) | 4.82 | 🟡 Alert | 0.000 |  |
| 2026-09-25 11:03:34 | Rathnapura (Kalu Ganga) | 6.28 | 🟡 Alert | -0.023 |  |
| 2026-09-25 11:03:47 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | -0.039 |  |
| 2026-09-25 11:06:14 | Thawalama (Gin Ganga) | 4.37 | 🟡 Alert | -0.051 |  |
| 2026-09-25 11:01:29 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-09-25 11:02:07 | Nagalagam Street (Kelani Ganga) | 1.02 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-25 11:00:41 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-25 11:01:08 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-25 11:01:59 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-25 10:06:56 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-25 11:02:32 | Ellagawa (Kalu Ganga) | 8.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 11:03:49 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 11:03:41 | Kithulgala (Kelani Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:00:16 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:01:05 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:02:03 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:00:11 | Pitabeddara (Nilwala Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:00:54 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:01:02 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:05:15 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:02:51 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:02:29 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-25 11:01:15 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-09-25 11:04:15 | Urawa (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.015 |  |
| 2026-09-25 11:02:51 | Hanwella (Kelani Ganga) | 6.26 | 🟢 Normal | -0.020 |  |
| 2026-09-25 11:02:14 | Deraniyagala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-09-25 11:02:28 | Dunamale (Aththanagalu Oya) | 3.03 | 🟢 Normal | -0.040 |  |
| 2026-09-25 10:05:54 | Glencourse (Kelani Ganga) | 14.31 | 🟢 Normal | -0.040 |  |
| 2026-09-25 10:06:19 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.048 |  |
| 2026-09-25 11:06:49 | Peradeniya (Mahaweli Ganga) | 4.30 | 🟢 Normal | -0.051 |  |
| 2026-09-25 11:01:01 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.053 |  |
| 2026-09-25 11:06:03 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.061 |  |
| 2026-09-25 10:04:39 | Nawalapitiya (Mahaweli Ganga) | 2.77 | 🟢 Normal | -0.119 |  |
| 2026-09-25 11:02:36 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)