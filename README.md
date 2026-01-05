# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_12:20:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,287 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 12:20:32 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.016 |  |
| 2026-01-05 12:13:45 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.011 |  |
| 2026-01-05 12:10:11 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.017 |  |
| 2026-01-05 12:07:29 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.010 |  |
| 2026-01-05 12:07:04 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:06:53 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 12:06:39 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:05:56 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:05:01 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-05 12:04:55 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:04:46 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-05 12:04:33 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:03:49 | Galgamuwa (Mee Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:03:41 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.059 |  |
| 2026-01-05 12:03:40 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 12:03:32 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-01-05 12:03:31 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:03:30 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-05 12:03:28 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:03:24 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-05 12:03:10 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-05 12:03:02 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.205 |  |
| 2026-01-05 12:02:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-05 12:02:41 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 12:02:33 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.005 |  |
| 2026-01-05 12:02:30 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:02:24 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:02:15 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-05 12:02:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:01:45 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:01:44 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-05 12:01:43 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.032 |  |
| 2026-01-05 12:01:24 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-01-05 12:01:16 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-01-05 12:01:16 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:00:59 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:00:16 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 12:02:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-05 12:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-05 12:01:44 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-05 12:03:24 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-05 12:05:01 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-05 12:02:41 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 12:06:53 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 12:03:40 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 12:04:33 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:01:45 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:00:16 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:01:16 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:02:30 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:03:49 | Galgamuwa (Mee Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:05:56 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:06:39 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:00:59 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:04:55 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:03:31 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:03:28 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:02:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:07:04 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:02:24 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:02:15 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-05 12:02:33 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.005 |  |
| 2026-01-05 12:04:46 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-05 12:03:30 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-05 12:03:10 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-05 12:07:29 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.010 |  |
| 2026-01-05 12:01:16 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-01-05 12:03:32 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-01-05 12:01:24 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-01-05 12:13:45 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.011 |  |
| 2026-01-05 12:20:32 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.016 |  |
| 2026-01-05 12:10:11 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.017 |  |
| 2026-01-05 12:01:43 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.032 |  |
| 2026-01-05 12:03:41 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.059 |  |
| 2026-01-05 12:03:02 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)