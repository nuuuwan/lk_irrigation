# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_18:06:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,492 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 18:06:24 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.103 |  |
| 2026-10-28 18:05:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.68 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-28 18:05:37 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 18:05:21 | Ellagawa (Kalu Ganga) | 10.40 | 🟡 Alert | -0.010 |  |
| 2026-10-28 18:04:16 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:03:56 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-28 18:03:39 | Panadugama (Nilwala Ganga) | 6.11 | 🟠 Minor Flood | 0.054 | 🔺 Rising |
| 2026-10-28 18:03:36 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:03:34 | Rathnapura (Kalu Ganga) | 5.89 | 🟡 Alert | -0.065 |  |
| 2026-10-28 18:03:33 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.059 |  |
| 2026-10-28 18:03:20 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 18:02:55 | Hanwella (Kelani Ganga) | 4.27 | 🟢 Normal | -0.010 |  |
| 2026-10-28 18:02:49 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:02:47 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-28 18:02:32 | Magura (Kalu Ganga) | 4.28 | 🟡 Alert | 0.088 | 🔺 Rising |
| 2026-10-28 18:02:29 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:02:25 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:02:21 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-28 18:02:16 | Moragaswewa (Deduru Oya) | 2.95 | 🟢 Normal | -0.051 |  |
| 2026-10-28 18:02:16 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | -0.020 |  |
| 2026-10-28 18:02:12 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | -0.010 |  |
| 2026-10-28 18:02:10 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-28 18:01:41 | Putupaula (Kalu Ganga) | 3.71 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 18:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-10-28 18:01:32 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-28 18:01:29 | Pitabeddara (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-28 18:01:23 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:01:20 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-28 18:01:04 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:00:52 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:00:36 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-28 18:00:27 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-10-28 18:00:25 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-10-28 18:00:10 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.068 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 18:03:39 | Panadugama (Nilwala Ganga) | 6.11 | 🟠 Minor Flood | 0.054 | 🔺 Rising |
| 2026-10-28 18:00:36 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-28 18:05:37 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 18:05:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.68 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-28 18:02:32 | Magura (Kalu Ganga) | 4.28 | 🟡 Alert | 0.088 | 🔺 Rising |
| 2026-10-28 18:01:41 | Putupaula (Kalu Ganga) | 3.71 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 18:05:21 | Ellagawa (Kalu Ganga) | 10.40 | 🟡 Alert | -0.010 |  |
| 2026-10-28 18:03:34 | Rathnapura (Kalu Ganga) | 5.89 | 🟡 Alert | -0.065 |  |
| 2026-10-28 18:01:29 | Pitabeddara (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-28 18:02:21 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-28 18:02:47 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-28 17:02:26 | Galgamuwa (Mee Oya) | 2.35 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-28 18:03:20 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 18:01:23 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:02:49 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:04:16 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:01:32 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:00:52 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:02:25 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:03:36 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:02:29 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:01:20 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:01:04 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:02:10 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 18:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-10-28 18:02:55 | Hanwella (Kelani Ganga) | 4.27 | 🟢 Normal | -0.010 |  |
| 2026-10-28 18:03:56 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-28 18:02:12 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | -0.010 |  |
| 2026-10-28 18:01:32 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-28 18:02:16 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | -0.020 |  |
| 2026-10-28 18:00:27 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-10-28 18:00:25 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-10-28 18:02:16 | Moragaswewa (Deduru Oya) | 2.95 | 🟢 Normal | -0.051 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-28 18:03:33 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.059 |  |
| 2026-10-28 18:00:10 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.068 |  |
| 2026-10-28 18:06:24 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.103 |  |
| 2026-10-28 17:09:48 | Urawa (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)