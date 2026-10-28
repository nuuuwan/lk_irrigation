# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_19:14:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,528 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 19:14:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.67 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-28 19:09:46 | Urawa (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.110 |  |
| 2026-10-28 19:08:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.074 |  |
| 2026-10-28 19:07:39 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-10-28 19:07:15 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.028 |  |
| 2026-10-28 19:06:47 | Putupaula (Kalu Ganga) | 3.71 | 🟡 Alert | 0.000 |  |
| 2026-10-28 19:05:56 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:05:30 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:05:22 | Panadugama (Nilwala Ganga) | 6.13 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-28 19:05:09 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-10-28 19:05:05 | Rathnapura (Kalu Ganga) | 5.86 | 🟡 Alert | -0.029 |  |
| 2026-10-28 19:04:38 | Hanwella (Kelani Ganga) | 4.24 | 🟢 Normal | -0.029 |  |
| 2026-10-28 19:03:57 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:03:54 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-10-28 19:03:26 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | -0.020 |  |
| 2026-10-28 19:03:24 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:03:11 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:03:00 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-28 19:02:59 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-28 19:02:49 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 19:02:37 | Moragaswewa (Deduru Oya) | 2.89 | 🟢 Normal | -0.060 |  |
| 2026-10-28 19:02:34 | Ellagawa (Kalu Ganga) | 10.40 | 🟡 Alert | 0.000 |  |
| 2026-10-28 19:02:31 | Dunamale (Aththanagalu Oya) | 3.18 | 🟢 Normal | -0.070 |  |
| 2026-10-28 19:02:25 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | -0.010 |  |
| 2026-10-28 19:02:22 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 19:02:17 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:02:16 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:02:04 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:02:01 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-28 19:01:51 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-28 19:01:43 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.029 |  |
| 2026-10-28 19:01:40 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:01:30 | Pitabeddara (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.080 |  |
| 2026-10-28 19:00:51 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-28 19:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 19:05:22 | Panadugama (Nilwala Ganga) | 6.13 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-28 19:01:51 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-28 19:02:22 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 19:14:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.67 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-28 19:02:59 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-28 19:02:34 | Ellagawa (Kalu Ganga) | 10.40 | 🟡 Alert | 0.000 |  |
| 2026-10-28 19:06:47 | Putupaula (Kalu Ganga) | 3.71 | 🟡 Alert | 0.000 |  |
| 2026-10-28 19:05:05 | Rathnapura (Kalu Ganga) | 5.86 | 🟡 Alert | -0.029 |  |
| 2026-10-28 19:03:00 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-28 19:02:01 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-28 19:02:49 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-28 18:01:23 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:02:16 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:02:17 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:02:04 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:03:11 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:03:24 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:05:56 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:01:40 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:05:30 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:03:57 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 19:07:39 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-10-28 19:03:54 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-10-28 19:00:51 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-28 19:02:25 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | -0.010 |  |
| 2026-10-28 19:03:26 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | -0.020 |  |
| 2026-10-28 19:07:15 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.028 |  |
| 2026-10-28 19:04:38 | Hanwella (Kelani Ganga) | 4.24 | 🟢 Normal | -0.029 |  |
| 2026-10-28 19:01:43 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.029 |  |
| 2026-10-28 19:05:09 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-28 19:02:37 | Moragaswewa (Deduru Oya) | 2.89 | 🟢 Normal | -0.060 |  |
| 2026-10-28 19:02:31 | Dunamale (Aththanagalu Oya) | 3.18 | 🟢 Normal | -0.070 |  |
| 2026-10-28 19:08:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.074 |  |
| 2026-10-28 19:01:30 | Pitabeddara (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.080 |  |
| 2026-10-28 19:09:46 | Urawa (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.110 |  |

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)