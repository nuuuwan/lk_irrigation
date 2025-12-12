# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_02:29:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,360 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 02:29:04 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:29:02 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:26:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 18.857 | 🔺 Rising |
| 2025-12-13 02:25:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 18.857 | 🔺 Rising |
| 2025-12-13 02:13:20 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:13:00 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:10:24 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:10:19 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:07:14 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-13 02:07:14 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:06:45 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:06:14 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:05:47 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.059 |  |
| 2025-12-13 02:05:33 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:05:04 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.202 |  |
| 2025-12-13 02:04:15 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2025-12-13 02:04:14 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-13 02:03:56 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-13 02:03:49 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:03:25 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.030 |  |
| 2025-12-13 02:03:18 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-13 02:03:17 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-13 02:02:41 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:02:38 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-13 02:02:30 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:02:19 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2025-12-13 02:02:06 | Horowpothana (Yan Oya) | 6.28 | 🟡 Alert | -0.031 |  |
| 2025-12-13 02:02:01 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:01:33 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:01:32 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:01:27 | Ellagawa (Kalu Ganga) | 6.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 02:01:23 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -3.200 |  |
| 2025-12-13 02:01:16 | Manampitiya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.057 |  |
| 2025-12-13 02:00:38 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -3.200 |  |
| 2025-12-13 02:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2025-12-13 01:43:26 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 02:02:06 | Horowpothana (Yan Oya) | 6.28 | 🟡 Alert | -0.031 |  |
| 2025-12-13 02:26:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 18.857 | 🔺 Rising |
| 2025-12-12 23:05:26 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2025-12-13 02:03:17 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-13 01:32:49 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-13 02:04:14 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-13 02:07:14 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-13 02:01:27 | Ellagawa (Kalu Ganga) | 6.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 02:03:56 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-12 23:02:57 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:02:41 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:05:33 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:01:33 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:01:32 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:29:04 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:02:30 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:07:14 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:10:19 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:06:45 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:10:24 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:06:14 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:13:20 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:03:49 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 02:03:18 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-13 02:02:38 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-13 02:04:15 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2025-12-13 02:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2025-12-13 01:43:26 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.014 |  |
| 2025-12-13 00:03:57 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2025-12-13 02:02:19 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2025-12-13 02:03:25 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.030 |  |
| 2025-12-13 02:01:16 | Manampitiya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.057 |  |
| 2025-12-13 02:05:47 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.059 |  |
| 2025-12-13 01:00:29 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.105 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |
| 2025-12-13 02:05:04 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.202 |  |
| 2025-12-13 02:01:23 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -3.200 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)