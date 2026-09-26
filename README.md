# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_04:03:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,042 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 04:03:26 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | -0.080 |  |
| 2026-09-27 04:03:25 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-09-27 04:03:04 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | -0.052 |  |
| 2026-09-27 04:02:54 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:02:52 | Thalgahagoda (Nilwala Ganga) | 1.97 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 04:02:37 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-27 04:02:24 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:02:17 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-09-27 04:02:00 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:01:53 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 04:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.79 | 🟠 Minor Flood | -0.014 |  |
| 2026-09-27 04:01:47 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:01:30 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:01:13 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:01:06 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | -0.031 |  |
| 2026-09-27 04:00:52 | Glencourse (Kelani Ganga) | 12.45 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:00:23 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 03:05:05 | Baddegama (Gin Ganga) | 4.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 04:02:52 | Thalgahagoda (Nilwala Ganga) | 1.97 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 04:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.79 | 🟠 Minor Flood | -0.014 |  |
| 2026-09-27 03:07:13 | Panadugama (Nilwala Ganga) | 5.64 | 🟡 Alert | -0.048 |  |
| 2026-09-27 03:15:13 | Deraniyagala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-27 03:16:18 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-09-27 04:00:23 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 04:01:53 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 03:05:47 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:01:13 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:02:54 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:04:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:02:23 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:01:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:00:52 | Glencourse (Kelani Ganga) | 12.45 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:00:34 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:01:30 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:02:24 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:11:11 | Putupaula (Kalu Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:12:54 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:02:00 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:01:47 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:04:48 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-09-27 04:03:25 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-09-27 04:02:17 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-09-27 03:02:59 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-09-27 04:02:37 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-27 03:16:00 | Magura (Kalu Ganga) | 3.31 | 🟢 Normal | -0.019 |  |
| 2026-09-27 03:00:54 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-09-27 04:01:06 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | -0.031 |  |
| 2026-09-27 03:02:20 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.047 |  |
| 2026-09-27 04:03:04 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | -0.052 |  |
| 2026-09-27 03:03:55 | Hanwella (Kelani Ganga) | 4.84 | 🟢 Normal | -0.055 |  |
| 2026-09-27 03:04:02 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.065 |  |
| 2026-09-27 03:14:15 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.069 |  |
| 2026-09-27 04:03:26 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | -0.080 |  |
| 2026-09-26 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)