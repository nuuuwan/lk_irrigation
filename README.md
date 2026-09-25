# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_13:30:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,598 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 13:30:55 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:19:53 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:14:27 | Panadugama (Nilwala Ganga) | 6.47 | 🟠 Minor Flood | -0.008 |  |
| 2026-09-25 13:11:08 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-25 13:10:57 | Thawalama (Gin Ganga) | 4.09 | 🟡 Alert | -0.186 |  |
| 2026-09-25 13:10:11 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-25 13:08:21 | Glencourse (Kelani Ganga) | 14.10 | 🟢 Normal | -0.065 |  |
| 2026-09-25 13:08:05 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | 0.000 |  |
| 2026-09-25 13:08:03 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.038 |  |
| 2026-09-25 13:07:37 | Hanwella (Kelani Ganga) | 6.22 | 🟢 Normal | -0.240 |  |
| 2026-09-25 13:07:01 | Rathnapura (Kalu Ganga) | 6.24 | 🟡 Alert | -0.031 |  |
| 2026-09-25 13:06:22 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | -0.019 |  |
| 2026-09-25 13:05:59 | Urawa (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-09-25 13:05:43 | Kithulgala (Kelani Ganga) | 2.72 | 🟢 Normal | -0.165 |  |
| 2026-09-25 13:05:25 | Holombuwa (Kelani Ganga) | 1.35 | 🟢 Normal | -0.057 |  |
| 2026-09-25 13:05:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:04:56 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 13:04:34 | Baddegama (Gin Ganga) | 4.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 13:04:14 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:04:10 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-09-25 13:03:56 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.039 |  |
| 2026-09-25 13:03:50 | Putupaula (Kalu Ganga) | 2.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 13:03:44 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:03:34 | Ellagawa (Kalu Ganga) | 8.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 13:03:32 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:03:23 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:03:12 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:02:57 | Baddegama (Gin Ganga) | 4.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 13:02:38 | Deraniyagala (Kelani Ganga) | 2.01 | 🟢 Normal | -0.042 |  |
| 2026-09-25 13:02:37 | Hanwella (Kelani Ganga) | 6.24 | 🟢 Normal | -0.240 |  |
| 2026-09-25 13:02:31 | Norwood (Kelani Ganga) | 1.49 | 🟢 Normal | -0.031 |  |
| 2026-09-25 13:02:24 | Pitabeddara (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.011 |  |
| 2026-09-25 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 13:02:16 | Dunamale (Aththanagalu Oya) | 2.93 | 🟢 Normal | -0.040 |  |
| 2026-09-25 13:02:09 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:01:40 | Weraganthota (Mahaweli Ganga) | -2.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 13:01:38 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:01:03 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-25 13:00:54 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-25 13:00:34 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:00:29 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 13:04:34 | Baddegama (Gin Ganga) | 4.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 13:04:56 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 13:14:27 | Panadugama (Nilwala Ganga) | 6.47 | 🟠 Minor Flood | -0.008 |  |
| 2026-09-25 13:08:05 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | 0.000 |  |
| 2026-09-25 13:07:01 | Rathnapura (Kalu Ganga) | 6.24 | 🟡 Alert | -0.031 |  |
| 2026-09-25 13:10:57 | Thawalama (Gin Ganga) | 4.09 | 🟡 Alert | -0.186 |  |
| 2026-09-25 13:00:54 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-25 13:10:11 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-25 13:11:08 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-25 13:03:34 | Ellagawa (Kalu Ganga) | 8.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 13:01:40 | Weraganthota (Mahaweli Ganga) | -2.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 13:03:50 | Putupaula (Kalu Ganga) | 2.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 13:30:55 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:01:38 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:04:14 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:19:53 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:00:29 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:03:23 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:03:12 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:05:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:00:34 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:03:32 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:03:44 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:02:09 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:04:10 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-09-25 13:05:59 | Urawa (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-09-25 13:01:03 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-25 13:02:24 | Pitabeddara (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.011 |  |
| 2026-09-25 13:06:22 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | -0.019 |  |
| 2026-09-25 13:02:31 | Norwood (Kelani Ganga) | 1.49 | 🟢 Normal | -0.031 |  |
| 2026-09-25 13:08:03 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.038 |  |
| 2026-09-25 13:03:56 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.039 |  |
| 2026-09-25 13:02:16 | Dunamale (Aththanagalu Oya) | 2.93 | 🟢 Normal | -0.040 |  |
| 2026-09-25 13:02:38 | Deraniyagala (Kelani Ganga) | 2.01 | 🟢 Normal | -0.042 |  |
| 2026-09-25 13:05:25 | Holombuwa (Kelani Ganga) | 1.35 | 🟢 Normal | -0.057 |  |
| 2026-09-25 13:08:21 | Glencourse (Kelani Ganga) | 14.10 | 🟢 Normal | -0.065 |  |
| 2026-09-25 13:05:43 | Kithulgala (Kelani Ganga) | 2.72 | 🟢 Normal | -0.165 |  |
| 2026-09-25 13:07:37 | Hanwella (Kelani Ganga) | 6.22 | 🟢 Normal | -0.240 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)