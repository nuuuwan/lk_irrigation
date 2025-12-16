# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_10:20:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,385 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 10:20:10 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.039 |  |
| 2025-12-16 10:13:59 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:12:59 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:11:28 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.028 |  |
| 2025-12-16 10:11:13 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 10:10:04 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:08:32 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:08:10 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2025-12-16 10:06:44 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:06:39 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:06:38 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | -0.171 |  |
| 2025-12-16 10:06:17 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.345 |  |
| 2025-12-16 10:06:14 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:05:26 | Thanthirimale (Malwathu Oya) | 3.82 | 🟢 Normal | -0.057 |  |
| 2025-12-16 10:05:07 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:05:00 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | -0.020 |  |
| 2025-12-16 10:04:46 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:04:23 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:04:15 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:04:10 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:04:03 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:03:45 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:03:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-16 10:03:24 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-16 10:02:40 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:02:39 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-16 10:02:39 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:02:36 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:02:22 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 10:02:21 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:01:31 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.718 | 🔺 Rising |
| 2025-12-16 10:01:29 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:01:24 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:01:23 | Yaka Wewa (Ma Oya) | 1.78 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-16 10:01:15 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:01:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:00:52 | Horowpothana (Yan Oya) | 4.92 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2025-12-16 10:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2025-12-16 09:57:58 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2025-12-16 09:28:29 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 10:01:31 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.718 | 🔺 Rising |
| 2025-12-16 10:00:52 | Horowpothana (Yan Oya) | 4.92 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2025-12-16 10:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2025-12-16 10:01:23 | Yaka Wewa (Ma Oya) | 1.78 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-16 10:02:39 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-16 10:02:22 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 10:03:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-16 10:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-16 10:11:13 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 10:02:36 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:04:23 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:06:14 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:05:07 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:04:10 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:08:32 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:01:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:01:24 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:12:59 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:01:29 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:03:24 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:04:46 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:13:59 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:04:03 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:06:44 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:06:39 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:02:21 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:08:10 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2025-12-16 10:04:15 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:03:45 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:02:39 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:01:15 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:10:04 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:02:40 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-16 10:05:00 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | -0.020 |  |
| 2025-12-16 10:11:28 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.028 |  |
| 2025-12-16 10:20:10 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.039 |  |
| 2025-12-16 10:05:26 | Thanthirimale (Malwathu Oya) | 3.82 | 🟢 Normal | -0.057 |  |
| 2025-12-16 10:06:38 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | -0.171 |  |
| 2025-12-16 10:06:17 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.345 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)