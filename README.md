# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_06:37:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,328 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 06:37:10 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.005 |  |
| 2026-01-12 06:19:04 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:14:18 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:10:52 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 06:10:43 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.453 | 🔺 Rising |
| 2026-01-12 06:10:24 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.009 |  |
| 2026-01-12 06:09:14 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.062 |  |
| 2026-01-12 06:08:11 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:06:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:06:51 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-01-12 06:06:38 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:06:17 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:06:08 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:05:56 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:05:51 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:05:31 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:04:47 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:04:40 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | -0.170 |  |
| 2026-01-12 06:04:21 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.011 |  |
| 2026-01-12 06:04:08 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-12 06:04:00 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 15.429 | 🔺 Rising |
| 2026-01-12 06:03:43 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:03:39 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 15.429 | 🔺 Rising |
| 2026-01-12 06:03:38 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:03:36 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | -0.029 |  |
| 2026-01-12 06:03:20 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:02:38 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:02:38 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-01-12 06:02:35 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-12 06:02:32 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:02:30 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:02:23 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-01-12 06:02:03 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 06:02:00 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 06:01:36 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-12 06:01:28 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 06:01:28 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-01-12 06:01:27 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:01:25 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-01-12 06:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-12 06:01:08 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.024 |  |
| 2026-01-12 06:00:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-12 06:00:10 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.103 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 06:04:00 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 15.429 | 🔺 Rising |
| 2026-01-12 06:10:43 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.453 | 🔺 Rising |
| 2026-01-12 06:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-12 06:04:08 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-12 06:02:35 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-12 06:00:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 06:02:03 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 06:01:28 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 06:02:00 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 06:10:52 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 06:02:32 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:01:27 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:02:30 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:19:04 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:14:18 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:03:43 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:03:20 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:06:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:02:38 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:10:41 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:06:38 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:08:11 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:05:51 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:04:47 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:37:10 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.005 |  |
| 2026-01-12 06:10:24 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.009 |  |
| 2026-01-12 06:01:28 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-01-12 06:01:25 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-01-12 06:04:21 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.011 |  |
| 2026-01-12 06:01:36 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-12 06:02:23 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-01-12 06:02:38 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-01-12 06:01:08 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.024 |  |
| 2026-01-12 06:06:51 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-01-12 06:03:36 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | -0.029 |  |
| 2026-01-12 06:09:14 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.062 |  |
| 2026-01-12 06:00:10 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.103 |  |
| 2026-01-12 06:04:40 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)