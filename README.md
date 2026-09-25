# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_23:04:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,961 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 23:04:27 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:03:59 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:03:53 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-25 23:03:20 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.059 |  |
| 2026-09-25 23:03:17 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.048 |  |
| 2026-09-25 23:03:10 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 23:03:10 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-25 23:02:49 | Deraniyagala (Kelani Ganga) | 2.28 | 🟢 Normal | -0.209 |  |
| 2026-09-25 23:02:27 | Rathnapura (Kalu Ganga) | 5.78 | 🟡 Alert | -0.064 |  |
| 2026-09-25 23:02:25 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.021 |  |
| 2026-09-25 23:01:55 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.08 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 23:01:38 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:01:29 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:01:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:00:43 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 23:03:10 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 22:06:33 | Baddegama (Gin Ganga) | 4.76 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 23:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.08 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 22:02:37 | Panadugama (Nilwala Ganga) | 6.27 | 🟠 Minor Flood | -0.031 |  |
| 2026-09-25 22:06:49 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | -0.010 |  |
| 2026-09-25 22:07:13 | Kithulgala (Kelani Ganga) | 3.03 | 🟡 Alert | -0.039 |  |
| 2026-09-25 23:02:27 | Rathnapura (Kalu Ganga) | 5.78 | 🟡 Alert | -0.064 |  |
| 2026-09-25 22:03:45 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-25 22:04:25 | Peradeniya (Mahaweli Ganga) | 4.08 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-25 22:04:03 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-25 23:03:53 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-25 22:01:04 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 23:01:29 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:00:43 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:04:27 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:03:59 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:00:40 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:01:55 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:02:16 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:01:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:07:30 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:05:20 | Putupaula (Kalu Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-09-25 22:04:53 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:01:38 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 23:03:10 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-25 22:19:54 | Pitabeddara (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.015 |  |
| 2026-09-25 22:06:31 | Hanwella (Kelani Ganga) | 5.84 | 🟢 Normal | -0.019 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-25 22:08:46 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-09-25 23:02:25 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.021 |  |
| 2026-09-25 22:06:16 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -0.022 |  |
| 2026-09-25 22:05:22 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-09-25 23:03:17 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.048 |  |
| 2026-09-25 23:03:20 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.059 |  |
| 2026-09-25 22:02:36 | Nawalapitiya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.114 |  |
| 2026-09-25 23:02:49 | Deraniyagala (Kelani Ganga) | 2.28 | 🟢 Normal | -0.209 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)