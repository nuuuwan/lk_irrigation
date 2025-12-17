# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_10:12:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,282 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 10:12:34 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:11:32 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2025-12-17 10:10:11 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:09:49 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:09:05 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:08:26 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.009 |  |
| 2025-12-17 10:07:54 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:07:22 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:06:34 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-17 10:06:02 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:05:30 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-17 10:05:22 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:05:14 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:04:58 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:04:53 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.020 |  |
| 2025-12-17 10:04:46 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-17 10:04:32 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:04:30 | Weraganthota (Mahaweli Ganga) | -1.18 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2025-12-17 10:03:53 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:03:52 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:03:41 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.050 |  |
| 2025-12-17 10:03:38 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:03:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -2.141 |  |
| 2025-12-17 10:03:15 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:02:56 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:02:52 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:02:52 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:02:50 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-17 10:02:44 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2025-12-17 10:02:43 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 10:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:02:13 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-17 10:02:12 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2025-12-17 10:02:02 | Thanthirimale (Malwathu Oya) | 3.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-17 10:01:55 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.026 |  |
| 2025-12-17 10:01:48 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:00:43 | Horowpothana (Yan Oya) | 5.86 | 🟢 Normal | -0.043 |  |
| 2025-12-17 10:00:23 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 10:04:30 | Weraganthota (Mahaweli Ganga) | -1.18 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2025-12-17 10:04:46 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-17 10:02:13 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-17 10:05:30 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-17 10:06:34 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-17 10:02:50 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-17 10:02:02 | Thanthirimale (Malwathu Oya) | 3.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-17 10:02:43 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 10:02:52 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:10:11 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:09:05 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:02:56 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:03:53 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:06:02 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:07:54 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:03:38 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:05:14 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:07:22 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:04:32 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:04:58 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:01:48 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:12:34 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 10:11:32 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2025-12-17 10:08:26 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.009 |  |
| 2025-12-17 10:05:22 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:09:49 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:02:12 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:03:52 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:02:52 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:03:15 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-17 10:00:23 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.012 |  |
| 2025-12-17 10:02:44 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2025-12-17 10:04:53 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.020 |  |
| 2025-12-17 10:01:55 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.026 |  |
| 2025-12-17 10:00:43 | Horowpothana (Yan Oya) | 5.86 | 🟢 Normal | -0.043 |  |
| 2025-12-17 10:03:41 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.050 |  |
| 2025-12-17 10:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2025-12-17 10:03:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -2.141 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)