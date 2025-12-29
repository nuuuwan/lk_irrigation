# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_01:17:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,511 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 01:17:03 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-30 01:13:34 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:09:17 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-30 01:09:15 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-30 01:07:27 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:05:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-30 01:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2025-12-30 01:04:53 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-30 01:04:43 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.085 |  |
| 2025-12-30 01:04:10 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2025-12-30 01:04:05 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:03:50 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 01:03:20 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-30 01:02:48 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-30 01:02:33 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-30 01:02:29 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.011 |  |
| 2025-12-30 01:02:18 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:02:09 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:01:59 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:01:48 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:01:34 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:01:27 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 01:01:22 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2025-12-30 01:01:16 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:01:06 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:00:09 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.012 |  |
| 2025-12-30 00:39:12 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-30 00:36:07 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 01:04:10 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2025-12-30 01:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2025-12-30 01:05:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-30 01:09:17 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-30 01:02:48 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-30 01:17:03 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-29 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 01:03:50 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 01:01:27 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 01:09:15 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-30 00:05:17 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:01:48 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:01:06 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:07:53 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-30 00:04:47 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:02:09 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 00:09:20 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:01:16 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-30 00:08:21 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:04:05 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:01:34 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:07:27 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:13:34 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-30 00:02:07 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 01:02:18 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:25:04 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 00:36:07 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-30 00:10:43 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2025-12-29 18:06:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-30 01:02:33 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-30 01:04:53 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-30 01:02:29 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.011 |  |
| 2025-12-30 01:00:09 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.012 |  |
| 2025-12-30 01:03:20 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-29 23:10:21 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2025-12-29 23:02:56 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.041 |  |
| 2025-12-30 01:04:43 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.085 |  |
| 2025-12-30 00:04:37 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)