# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_07:09:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,267 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 07:09:53 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-26 07:09:23 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | -0.044 |  |
| 2026-09-26 07:09:21 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:08:30 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -73.532 |  |
| 2026-09-26 07:08:23 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-26 07:07:59 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:06:55 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:06:28 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:05:22 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | -73.532 |  |
| 2026-09-26 07:05:18 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:05:12 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:05:08 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:05:04 | Baddegama (Gin Ganga) | 4.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 07:04:47 | Rathnapura (Kalu Ganga) | 5.31 | 🟡 Alert | -0.160 |  |
| 2026-09-26 07:04:46 | Peradeniya (Mahaweli Ganga) | 3.68 | 🟢 Normal | -0.020 |  |
| 2026-09-26 07:04:40 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:04:14 | Glencourse (Kelani Ganga) | 13.44 | 🟢 Normal | -0.107 |  |
| 2026-09-26 07:04:09 | Hanwella (Kelani Ganga) | 5.78 | 🟢 Normal | -0.066 |  |
| 2026-09-26 07:04:02 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-26 07:03:47 | Nawalapitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-09-26 07:03:31 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-26 07:03:17 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:03:10 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:03:06 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:03:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-09-26 07:02:47 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:02:45 | Deraniyagala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 07:02:43 | Kithulgala (Kelani Ganga) | 2.82 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-26 07:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 07:02:20 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.092 |  |
| 2026-09-26 07:02:06 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:01:33 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.041 |  |
| 2026-09-26 07:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:00:44 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:00:37 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 07:00:22 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.062 |  |
| 2026-09-26 07:00:21 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 07:05:04 | Baddegama (Gin Ganga) | 4.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 07:00:37 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 07:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 07:09:23 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | -0.044 |  |
| 2026-09-26 07:04:47 | Rathnapura (Kalu Ganga) | 5.31 | 🟡 Alert | -0.160 |  |
| 2026-09-26 07:03:31 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-26 06:06:40 | Pitabeddara (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-26 07:02:43 | Kithulgala (Kelani Ganga) | 2.82 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-26 07:02:45 | Deraniyagala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 07:08:23 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-26 07:02:47 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:00:21 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:04:40 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:05:08 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:00:44 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:02:53 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:03:17 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:02:20 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:03:06 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:03:10 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:09:21 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:06:28 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:05:12 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:07:59 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:06:55 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 07:04:02 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-26 07:09:53 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-26 07:04:46 | Peradeniya (Mahaweli Ganga) | 3.68 | 🟢 Normal | -0.020 |  |
| 2026-09-26 06:04:57 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-09-26 07:03:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-09-26 07:03:47 | Nawalapitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-09-26 07:01:33 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.041 |  |
| 2026-09-26 07:00:22 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.062 |  |
| 2026-09-26 07:04:09 | Hanwella (Kelani Ganga) | 5.78 | 🟢 Normal | -0.066 |  |
| 2026-09-26 06:26:47 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | -0.074 |  |
| 2026-09-26 07:02:20 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.092 |  |
| 2026-09-26 07:04:14 | Glencourse (Kelani Ganga) | 13.44 | 🟢 Normal | -0.107 |  |
| 2026-09-26 07:08:30 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -73.532 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)