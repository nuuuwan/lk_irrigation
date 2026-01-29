# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_14:32:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,893 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 14:32:27 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:30:30 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:22:55 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:18:20 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:11:34 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-01-29 14:10:15 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-01-29 14:09:17 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:08:26 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:08:05 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:07:02 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.039 |  |
| 2026-01-29 14:06:46 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-29 14:05:40 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.080 |  |
| 2026-01-29 14:05:23 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-29 14:05:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-01-29 14:04:22 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-29 14:03:57 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:03:52 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 14:03:52 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-01-29 14:03:43 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:03:38 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.031 |  |
| 2026-01-29 14:03:26 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:03:21 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:03:13 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 14:03:00 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-29 14:02:57 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:02:49 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-29 14:02:28 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:02:24 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-29 14:02:14 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | -0.194 |  |
| 2026-01-29 14:01:57 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | -0.010 |  |
| 2026-01-29 14:01:56 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.041 |  |
| 2026-01-29 14:01:32 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:01:24 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 14:01:15 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:01:11 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:01:05 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-29 14:01:01 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 14:05:23 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-29 14:03:13 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 14:02:49 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-29 14:03:00 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-29 14:06:46 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-29 14:01:01 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 14:01:24 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 14:03:52 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 14:01:32 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:10 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:03:57 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:00:43 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:22:55 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:32:27 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:03:43 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:08:05 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:18:20 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:03:26 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:02:57 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:09:17 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:02:28 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:01:11 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:08:26 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:03:21 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:30:30 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:01:15 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:10:15 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-01-29 14:01:05 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-29 14:02:24 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-29 14:01:57 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | -0.010 |  |
| 2026-01-29 14:04:22 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-29 14:11:34 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-01-29 14:05:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-01-29 14:03:52 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-01-29 14:03:38 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.031 |  |
| 2026-01-29 14:07:02 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.039 |  |
| 2026-01-29 14:01:56 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.041 |  |
| 2026-01-29 14:05:40 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.080 |  |
| 2026-01-29 14:02:14 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)