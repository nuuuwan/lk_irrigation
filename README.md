# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_21:07:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,581 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 21:07:31 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | -0.028 |  |
| 2026-09-28 21:07:21 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.010 |  |
| 2026-09-28 21:06:54 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:06:41 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:06:24 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-09-28 21:06:14 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-09-28 21:05:42 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:05:40 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 21:05:33 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:05:30 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-09-28 21:05:28 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:04:39 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:04:21 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-09-28 21:04:01 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:04:00 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:03:59 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-28 21:03:51 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-28 21:03:40 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-09-28 21:03:37 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-09-28 21:03:32 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 21:03:26 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.149 |  |
| 2026-09-28 21:03:22 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-09-28 21:03:09 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:02:34 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.057 |  |
| 2026-09-28 21:02:30 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:02:17 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:02:16 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:02:09 | Hanwella (Kelani Ganga) | 3.02 | 🟢 Normal | -0.050 |  |
| 2026-09-28 21:01:31 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | -0.010 |  |
| 2026-09-28 21:00:55 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 21:00:22 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 20:59:28 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 21:07:31 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | -0.028 |  |
| 2026-09-28 20:01:54 | Baddegama (Gin Ganga) | 3.68 | 🟡 Alert | -0.050 |  |
| 2026-09-28 21:04:21 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-09-28 20:24:51 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-28 21:03:51 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-28 21:00:55 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 21:03:32 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 21:03:59 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-28 21:05:40 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 21:00:22 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:04:39 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:02:17 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:02:30 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:04:00 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:06:54 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:05:33 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:04:01 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:05:42 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:06:41 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:05:28 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:02:16 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:03:09 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 21:05:30 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-09-28 21:07:21 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.010 |  |
| 2026-09-28 21:01:31 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | -0.010 |  |
| 2026-09-28 21:06:24 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-09-28 21:03:22 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-28 20:59:28 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.011 |  |
| 2026-09-28 21:03:37 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-09-28 21:03:40 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-09-28 20:04:50 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | -0.048 |  |
| 2026-09-28 19:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.048 |  |
| 2026-09-28 21:02:09 | Hanwella (Kelani Ganga) | 3.02 | 🟢 Normal | -0.050 |  |
| 2026-09-28 21:02:34 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.057 |  |
| 2026-09-28 21:06:14 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-09-28 21:03:26 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)