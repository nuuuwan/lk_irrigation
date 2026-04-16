# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_03:36:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,154 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 03:36:03 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:18:16 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:13:23 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.197 |  |
| 2026-04-17 03:09:34 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.005 |  |
| 2026-04-17 03:09:07 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:08:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.141 |  |
| 2026-04-17 03:06:36 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:05:54 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 03:05:45 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-17 03:05:25 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:05:11 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-04-17 03:04:50 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 03:04:47 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:04:21 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:04:05 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.020 |  |
| 2026-04-17 03:03:58 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-17 03:03:45 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:03:45 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:03:40 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-17 03:03:40 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:03:19 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:02:46 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:02:44 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-17 03:02:20 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.030 |  |
| 2026-04-17 03:02:14 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -1.800 |  |
| 2026-04-17 03:02:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:01:56 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:01:56 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-04-17 03:01:55 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.206 |  |
| 2026-04-17 03:01:34 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -1.800 |  |
| 2026-04-17 03:00:50 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-17 03:00:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 01:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-17 03:05:45 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-17 03:00:50 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-17 02:04:21 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-17 03:03:58 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-17 03:02:44 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-17 02:04:40 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-17 02:51:09 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-17 03:05:54 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 03:04:50 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 03:00:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:18:16 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:02:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:01:56 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:31:15 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:19 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:36:03 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:04:47 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:02:46 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:09:07 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:03:40 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:05:25 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:03:45 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:03:45 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:05:10 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.005 |  |
| 2026-04-17 03:09:34 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.005 |  |
| 2026-04-17 02:05:33 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-17 03:05:11 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-04-17 03:01:56 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-04-17 03:04:05 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.020 |  |
| 2026-04-17 03:03:40 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-17 02:15:05 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.026 |  |
| 2026-04-17 03:02:20 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.030 |  |
| 2026-04-17 03:08:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.141 |  |
| 2026-04-17 03:13:23 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.197 |  |
| 2026-04-17 03:01:55 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.206 |  |
| 2026-04-17 03:02:14 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -1.800 |  |
| 2026-04-16 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -4.696 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)