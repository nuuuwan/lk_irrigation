# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_09:23:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,447 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 09:23:59 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:20:34 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:19:39 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | -0.017 |  |
| 2025-12-15 09:18:06 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:10:11 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.019 |  |
| 2025-12-15 09:08:56 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.063 |  |
| 2025-12-15 09:08:34 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2025-12-15 09:08:06 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.056 |  |
| 2025-12-15 09:06:26 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:05:43 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.011 |  |
| 2025-12-15 09:05:34 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 09:05:27 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:04:41 | Weraganthota (Mahaweli Ganga) | -1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:04:41 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.054 |  |
| 2025-12-15 09:04:22 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:04:00 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:03:39 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:03:37 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:03:36 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:03:36 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2025-12-15 09:03:35 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:03:34 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:03:22 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:03:01 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 09:02:54 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-15 09:02:43 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:02:43 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:02:15 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-15 09:02:12 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-15 09:02:11 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:02:06 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:01:59 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.212 |  |
| 2025-12-15 09:01:44 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:01:39 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:01:33 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:01:31 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:01:29 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:01:19 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 09:00:42 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:00:28 | Horowpothana (Yan Oya) | 4.07 | 🟢 Normal | -0.030 |  |
| 2025-12-15 09:00:13 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.021 |  |
| 2025-12-15 09:00:12 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 09:02:15 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-15 09:02:54 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-15 09:01:19 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 09:03:01 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 09:05:34 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 09:01:44 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:00:12 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:02:06 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:20:34 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:23:59 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:02:43 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:03:22 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:01:33 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:18:06 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:02:43 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:06:26 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:04:00 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:01:31 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 09:00:42 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:05:01 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:04:22 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:05:27 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:02:11 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:01:29 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:01:39 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:04:41 | Weraganthota (Mahaweli Ganga) | -1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.010 |  |
| 2025-12-15 09:05:43 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.011 |  |
| 2025-12-15 09:19:39 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | -0.017 |  |
| 2025-12-15 09:10:11 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.019 |  |
| 2025-12-15 09:02:12 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-15 09:08:34 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2025-12-15 09:00:13 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.021 |  |
| 2025-12-15 09:00:28 | Horowpothana (Yan Oya) | 4.07 | 🟢 Normal | -0.030 |  |
| 2025-12-15 09:03:36 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2025-12-15 09:04:41 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.054 |  |
| 2025-12-15 09:08:06 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.056 |  |
| 2025-12-15 09:08:56 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.063 |  |
| 2025-12-15 09:01:59 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.212 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)