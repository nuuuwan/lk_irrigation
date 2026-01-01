# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_08:24:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,537 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 08:24:46 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 08:23:47 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.031 |  |
| 2026-01-01 08:14:05 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | -0.014 |  |
| 2026-01-01 08:09:12 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.041 |  |
| 2026-01-01 08:08:41 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-01 08:08:18 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-01 08:07:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-01-01 08:07:48 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 08:07:38 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:06:49 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-01-01 08:06:32 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-01-01 08:06:01 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:05:52 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:05:27 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-01-01 08:04:59 | Siyambalanduwa (Heda Oya) | 1.76 | 🟢 Normal | -0.078 |  |
| 2026-01-01 08:04:43 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-01 08:04:37 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:04:22 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:03:58 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-01 08:03:55 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 08:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.138 |  |
| 2026-01-01 08:03:47 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:03:45 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:03:45 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:03:45 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-01-01 08:03:20 | Horowpothana (Yan Oya) | 2.83 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-01 08:02:30 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 08:02:03 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.092 |  |
| 2026-01-01 08:02:02 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:01:53 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-01 08:01:46 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:01:34 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-01-01 08:01:26 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:01:24 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:01:08 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.027 |  |
| 2026-01-01 08:01:01 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-01 08:00:41 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.034 |  |
| 2026-01-01 08:00:30 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 08:06:32 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-01-01 08:01:01 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-01 08:04:43 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-01 08:01:53 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-01 08:03:58 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-01 08:03:20 | Horowpothana (Yan Oya) | 2.83 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-01 08:08:41 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-01 08:02:30 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 08:03:55 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 08:07:48 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 08:24:46 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 08:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:06:01 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:01:24 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:03:47 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:03:45 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:04:37 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:07:38 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-01 08:05:52 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:01:26 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:00:30 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:02:02 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:04:22 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:03:45 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:01:46 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:03:45 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-01-01 08:14:05 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | -0.014 |  |
| 2026-01-01 08:08:18 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-01 08:06:49 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-01-01 08:01:34 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-01-01 08:05:27 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-01-01 08:01:08 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.027 |  |
| 2026-01-01 08:07:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-01-01 08:23:47 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.031 |  |
| 2026-01-01 08:00:41 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.034 |  |
| 2026-01-01 08:09:12 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.041 |  |
| 2026-01-01 08:04:59 | Siyambalanduwa (Heda Oya) | 1.76 | 🟢 Normal | -0.078 |  |
| 2026-01-01 08:02:03 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.092 |  |
| 2026-01-01 08:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)