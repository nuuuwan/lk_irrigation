# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_03:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,002 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 03:03:20 | Thalgahagoda (Nilwala Ganga) | 1.97 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 03:03:18 | Peradeniya (Mahaweli Ganga) | 3.43 | 🟢 Normal | -0.068 |  |
| 2026-09-27 03:03:05 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:02:59 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-09-27 03:02:59 | Ellagawa (Kalu Ganga) | 8.75 | 🟢 Normal | -0.019 |  |
| 2026-09-27 03:02:40 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:02:34 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:02:23 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:02:20 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.047 |  |
| 2026-09-27 03:02:04 | Thalgahagoda (Nilwala Ganga) | 1.97 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 03:01:29 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-09-27 03:01:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:01:08 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:00:54 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-09-27 03:00:43 | Glencourse (Kelani Ganga) | 12.45 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:00:34 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:00:18 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 03:03:20 | Thalgahagoda (Nilwala Ganga) | 1.97 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 02:10:36 | Baddegama (Gin Ganga) | 4.77 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-27 00:10:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.83 | 🟠 Minor Flood | -0.014 |  |
| 2026-09-27 01:03:10 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | -0.010 |  |
| 2026-09-27 02:03:57 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-09-27 02:10:22 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-27 02:03:34 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 02:01:56 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 03:00:18 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:01:08 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:02:34 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 02:03:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:02:23 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:07:08 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:01:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:00:43 | Glencourse (Kelani Ganga) | 12.45 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:00:34 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:03:05 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 00:03:55 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-27 01:05:55 | Putupaula (Kalu Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-09-27 02:10:58 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:02:40 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-27 02:03:20 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-09-27 03:02:59 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-27 02:45:26 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-09-27 02:17:15 | Deraniyagala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.018 |  |
| 2026-09-27 03:02:59 | Ellagawa (Kalu Ganga) | 8.75 | 🟢 Normal | -0.019 |  |
| 2026-09-27 02:06:32 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-09-27 02:02:36 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-27 03:00:54 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-09-27 03:01:29 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-09-27 01:07:02 | Magura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.037 |  |
| 2026-09-27 02:09:04 | Hanwella (Kelani Ganga) | 4.89 | 🟢 Normal | -0.047 |  |
| 2026-09-27 03:02:20 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.047 |  |
| 2026-09-27 03:03:18 | Peradeniya (Mahaweli Ganga) | 3.43 | 🟢 Normal | -0.068 |  |
| 2026-09-26 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |
| 2026-09-27 02:04:43 | Rathnapura (Kalu Ganga) | 4.28 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)