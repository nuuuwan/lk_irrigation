# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_11:50:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,651 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 11:50:29 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-01 11:36:22 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:21:29 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:20:49 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:08:33 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:07:43 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:07:08 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 11:06:45 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.084 |  |
| 2026-01-01 11:05:55 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:05:51 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:05:36 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 11:04:50 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.103 |  |
| 2026-01-01 11:04:42 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:04:29 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.005 |  |
| 2026-01-01 11:04:25 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-01-01 11:04:20 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:04:20 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-01-01 11:04:11 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-01 11:04:10 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-01 11:03:46 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-01 11:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-01-01 11:03:33 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 11:03:29 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-01 11:03:28 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-01 11:03:21 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-01-01 11:03:16 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-01 11:03:14 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.040 |  |
| 2026-01-01 11:03:09 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:02:51 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.061 |  |
| 2026-01-01 11:02:43 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:02:05 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.022 |  |
| 2026-01-01 11:01:43 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.070 |  |
| 2026-01-01 11:01:39 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.030 |  |
| 2026-01-01 11:01:34 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | -0.020 |  |
| 2026-01-01 11:01:21 | Thanthirimale (Malwathu Oya) | 2.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-01 11:01:18 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:01:17 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 11:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:00:17 | Siyambalanduwa (Heda Oya) | 1.50 | 🟢 Normal | -0.105 |  |
| 2026-01-01 11:00:06 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 11:04:11 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-01 11:03:46 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-01 11:03:16 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-01 11:03:28 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-01 11:03:29 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-01 11:01:21 | Thanthirimale (Malwathu Oya) | 2.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-01 11:03:33 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 11:07:08 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 11:01:17 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 11:05:36 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 11:50:29 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-01 11:01:18 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:04:20 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:04:42 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:03:09 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-01 10:04:05 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:21:29 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:36:22 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:04:29 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.005 |  |
| 2026-01-01 11:05:55 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:05:51 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:07:43 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:08:33 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:02:43 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:03:21 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-01-01 11:04:20 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-01-01 11:01:34 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | -0.020 |  |
| 2026-01-01 11:00:06 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-01-01 11:04:25 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-01-01 11:02:05 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.022 |  |
| 2026-01-01 11:01:39 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.030 |  |
| 2026-01-01 11:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-01-01 11:03:14 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.040 |  |
| 2026-01-01 11:02:51 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.061 |  |
| 2026-01-01 11:01:43 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.070 |  |
| 2026-01-01 11:06:45 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.084 |  |
| 2026-01-01 11:04:50 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.103 |  |
| 2026-01-01 11:00:17 | Siyambalanduwa (Heda Oya) | 1.50 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)