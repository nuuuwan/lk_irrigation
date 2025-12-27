# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_05:13:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,870 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 05:13:44 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-28 05:11:26 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:10:15 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:09:58 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.049 |  |
| 2025-12-28 05:09:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 05:09:00 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.027 |  |
| 2025-12-28 05:08:17 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.009 |  |
| 2025-12-28 05:07:46 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:07:19 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:07:17 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:05:08 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-28 05:05:03 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.005 |  |
| 2025-12-28 05:04:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.005 |  |
| 2025-12-28 05:04:21 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.079 |  |
| 2025-12-28 05:04:10 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2025-12-28 05:04:10 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:03:58 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:03:24 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.021 |  |
| 2025-12-28 05:03:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-28 05:02:59 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:02:58 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-28 05:02:48 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:02:44 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:02:09 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:02:05 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:01:57 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -36.000 |  |
| 2025-12-28 05:01:56 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -36.000 |  |
| 2025-12-28 05:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:01:51 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:01:46 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.005 |  |
| 2025-12-28 05:00:58 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:00:52 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.344 |  |
| 2025-12-28 04:47:21 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.067 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 05:05:08 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-28 03:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-28 05:13:44 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-28 04:07:59 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 05:09:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 04:02:18 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-28 05:01:46 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.005 |  |
| 2025-12-28 05:04:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.005 |  |
| 2025-12-27 19:15:41 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:03:58 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:02:09 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:11:26 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:02:59 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:28 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:07:19 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:02:48 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:02:44 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:02:05 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:10:15 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 04:02:50 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:04:10 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:00:58 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:07:46 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:01:51 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-28 05:05:03 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.005 |  |
| 2025-12-28 05:08:17 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.009 |  |
| 2025-12-28 05:03:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-28 05:02:58 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:01:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-28 05:04:10 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2025-12-28 04:00:26 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.012 |  |
| 2025-12-28 04:09:33 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.020 |  |
| 2025-12-28 05:03:24 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.021 |  |
| 2025-12-28 05:09:00 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.027 |  |
| 2025-12-28 05:09:58 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.049 |  |
| 2025-12-28 05:04:21 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.079 |  |
| 2025-12-28 05:00:52 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.344 |  |
| 2025-12-28 05:01:57 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)