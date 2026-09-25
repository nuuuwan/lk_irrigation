# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_22:07:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,941 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 22:07:30 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:07:13 | Kithulgala (Kelani Ganga) | 3.03 | 🟡 Alert | -0.039 |  |
| 2026-09-25 22:06:49 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | -0.010 |  |
| 2026-09-25 22:06:33 | Baddegama (Gin Ganga) | 4.76 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 22:06:31 | Hanwella (Kelani Ganga) | 5.84 | 🟢 Normal | -0.019 |  |
| 2026-09-25 22:06:17 | Rathnapura (Kalu Ganga) | 5.84 | 🟡 Alert | -0.040 |  |
| 2026-09-25 22:06:16 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -0.022 |  |
| 2026-09-25 22:05:54 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 22:05:48 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.028 |  |
| 2026-09-25 22:05:22 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-09-25 22:05:20 | Putupaula (Kalu Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:04:53 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:04:32 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-09-25 22:04:25 | Peradeniya (Mahaweli Ganga) | 4.08 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-25 22:04:03 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-25 22:03:45 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-25 22:03:42 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:03:39 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.015 |  |
| 2026-09-25 22:02:55 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:02:46 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | -0.040 |  |
| 2026-09-25 22:02:37 | Panadugama (Nilwala Ganga) | 6.27 | 🟠 Minor Flood | -0.031 |  |
| 2026-09-25 22:02:36 | Nawalapitiya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.114 |  |
| 2026-09-25 22:02:26 | Deraniyagala (Kelani Ganga) | 2.49 | 🟢 Normal | -0.111 |  |
| 2026-09-25 22:02:16 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:01:54 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:01:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:01:13 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:01:13 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:01:04 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 22:00:45 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:00:40 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:00:24 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 21:59:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.08 | 🟠 Minor Flood | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 21:59:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.08 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-09-25 22:05:54 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 22:06:33 | Baddegama (Gin Ganga) | 4.76 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 22:02:37 | Panadugama (Nilwala Ganga) | 6.27 | 🟠 Minor Flood | -0.031 |  |
| 2026-09-25 22:06:49 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | -0.010 |  |
| 2026-09-25 22:07:13 | Kithulgala (Kelani Ganga) | 3.03 | 🟡 Alert | -0.039 |  |
| 2026-09-25 22:06:17 | Rathnapura (Kalu Ganga) | 5.84 | 🟡 Alert | -0.040 |  |
| 2026-09-25 22:03:45 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-25 22:04:25 | Peradeniya (Mahaweli Ganga) | 4.08 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-25 22:04:03 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-25 22:00:24 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 22:01:04 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 22:01:13 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:00:45 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:01:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:03:42 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:01:54 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:00:40 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:02:16 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:02:55 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:07:30 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:05:20 | Putupaula (Kalu Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:04:53 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:01:13 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:03:39 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.015 |  |
| 2026-09-25 21:08:43 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-09-25 22:06:31 | Hanwella (Kelani Ganga) | 5.84 | 🟢 Normal | -0.019 |  |
| 2026-09-25 22:04:32 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-25 21:01:49 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-09-25 22:06:16 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -0.022 |  |
| 2026-09-25 22:05:48 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.028 |  |
| 2026-09-25 22:05:22 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-09-25 22:02:46 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | -0.040 |  |
| 2026-09-25 22:02:26 | Deraniyagala (Kelani Ganga) | 2.49 | 🟢 Normal | -0.111 |  |
| 2026-09-25 22:02:36 | Nawalapitiya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.114 |  |
| 2026-09-25 21:01:53 | Pitabeddara (Nilwala Ganga) | 2.36 | 🟢 Normal | -1.264 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)