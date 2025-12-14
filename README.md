# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_14:06:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,736 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 14:06:15 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.076 |  |
| 2025-12-14 14:05:31 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.068 |  |
| 2025-12-14 14:05:09 | Moragaswewa (Deduru Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:05:07 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:05:06 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 14:04:59 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:04:42 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:04:02 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-14 14:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2025-12-14 14:03:26 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:03:21 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:03:18 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:03:11 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2025-12-14 14:02:40 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:02:39 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:02:29 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:02:28 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-14 14:02:25 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-14 14:02:24 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:01:57 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.039 |  |
| 2025-12-14 14:01:55 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:01:50 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.050 |  |
| 2025-12-14 14:01:45 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:01:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.049 |  |
| 2025-12-14 14:01:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:01:29 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:01:25 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:01:20 | Horowpothana (Yan Oya) | 4.37 | 🟢 Normal | -0.050 |  |
| 2025-12-14 14:01:19 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.066 |  |
| 2025-12-14 14:01:18 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:01:09 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.050 |  |
| 2025-12-14 14:00:48 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:00:48 | Thanthirimale (Malwathu Oya) | 4.26 | 🟢 Normal | -0.020 |  |
| 2025-12-14 14:00:27 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-14 14:00:14 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:12:40 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 14:03:11 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2025-12-14 14:02:28 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-14 14:02:25 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-14 14:05:06 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 14:02:40 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:03:21 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:01:25 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:01:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:00:48 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:03:26 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:02:29 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:00:14 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:04:42 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:12:40 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:04:27 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:03:18 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:04:59 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:05:09 | Moragaswewa (Deduru Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:01:29 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:01:55 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:05:07 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:01:45 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:01:18 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:02:39 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:02:24 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:00:27 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-14 14:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2025-12-14 14:04:02 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-14 14:00:48 | Thanthirimale (Malwathu Oya) | 4.26 | 🟢 Normal | -0.020 |  |
| 2025-12-14 14:01:57 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.039 |  |
| 2025-12-14 14:01:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.049 |  |
| 2025-12-14 14:01:20 | Horowpothana (Yan Oya) | 4.37 | 🟢 Normal | -0.050 |  |
| 2025-12-14 14:01:50 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.050 |  |
| 2025-12-14 14:01:09 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.050 |  |
| 2025-12-14 13:06:16 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.053 |  |
| 2025-12-14 13:01:36 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.054 |  |
| 2025-12-14 14:01:19 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.066 |  |
| 2025-12-14 14:05:31 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.068 |  |
| 2025-12-14 14:06:15 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)