# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_23:44:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,381 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 23:44:42 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:42:57 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:18:49 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-06-25 23:17:45 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.008 |  |
| 2026-06-25 23:12:20 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:10:34 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:10:16 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:08:43 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-25 23:06:55 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:06:27 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:06:17 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:06:10 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-25 23:05:31 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 23:05:19 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-25 23:04:41 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.045 |  |
| 2026-06-25 23:04:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-25 23:04:11 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-25 23:03:50 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:03:29 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.197 |  |
| 2026-06-25 23:02:40 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 23:02:28 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-06-25 23:02:22 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-06-25 23:02:10 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:02:01 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:02:00 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-25 23:01:48 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:01:47 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2026-06-25 23:01:35 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-25 23:00:50 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:00:48 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-06-25 23:00:38 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:00:24 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 23:02:28 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-06-25 23:05:19 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-25 23:02:00 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-25 23:01:35 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-25 23:04:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-25 23:04:11 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-25 23:06:10 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-25 23:02:40 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 23:05:31 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 22:02:06 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 23:00:38 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:02:01 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:42:57 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:05:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:03:50 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:07:55 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:00:50 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:10:16 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:02:10 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:06:27 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:06:55 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:44:42 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:06:17 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:00:24 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:12:20 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:21 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:10:34 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:01:48 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:17:45 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.008 |  |
| 2026-06-25 23:08:43 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:02:25 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 23:00:48 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-06-25 23:18:49 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-06-25 23:02:22 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-06-25 20:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.024 |  |
| 2026-06-25 23:01:47 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2026-06-25 23:04:41 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.045 |  |
| 2026-06-25 23:03:29 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)