# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_10:13:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,899 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 10:13:12 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-05-10 10:12:39 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-05-10 10:12:14 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-05-10 10:11:47 | Thanthirimale (Malwathu Oya) | 3.01 | 🟢 Normal | -0.017 |  |
| 2026-05-10 10:09:17 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-10 10:08:10 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.037 |  |
| 2026-05-10 10:07:57 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-05-10 10:07:15 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.021 |  |
| 2026-05-10 10:06:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.020 |  |
| 2026-05-10 10:06:07 | Dunamale (Aththanagalu Oya) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-05-10 10:06:04 | Thanamalwila (Kirindi Oya) | 2.21 | 🟢 Normal | -0.146 |  |
| 2026-05-10 10:05:59 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-05-10 10:05:54 | Moragaswewa (Deduru Oya) | 2.36 | 🟢 Normal | -0.239 |  |
| 2026-05-10 10:05:36 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.048 |  |
| 2026-05-10 10:05:35 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-10 10:05:18 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.010 |  |
| 2026-05-10 10:04:35 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-05-10 10:04:19 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-10 10:03:56 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.205 |  |
| 2026-05-10 10:03:51 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-05-10 10:03:48 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-05-10 10:03:04 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-10 10:03:01 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-05-10 10:02:56 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | -0.054 |  |
| 2026-05-10 10:02:44 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | -0.034 |  |
| 2026-05-10 10:02:37 | Katharagama (Menik Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-05-10 10:02:19 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 10:02:13 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-10 10:02:04 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-10 10:02:02 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.518 | 🔺 Rising |
| 2026-05-10 10:01:58 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-05-10 10:01:57 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.080 |  |
| 2026-05-10 10:01:50 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.041 |  |
| 2026-05-10 10:01:47 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 10:01:21 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-10 10:01:13 | Kuda Oya (Kirindi Oya) | 2.11 | 🟢 Normal | -0.070 |  |
| 2026-05-10 10:00:42 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 10:02:02 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.518 | 🔺 Rising |
| 2026-05-10 10:00:42 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-10 10:02:13 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-10 09:07:13 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-10 10:02:19 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 10:05:35 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-10 10:09:17 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-10 10:02:04 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-10 10:01:47 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 10:04:19 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-10 10:12:39 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-05-10 10:07:57 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-05-10 10:06:07 | Dunamale (Aththanagalu Oya) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-05-10 10:12:14 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-05-10 10:03:48 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-05-10 10:03:04 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-10 10:05:18 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.010 |  |
| 2026-05-10 10:02:37 | Katharagama (Menik Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-05-10 10:03:51 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-05-10 10:11:47 | Thanthirimale (Malwathu Oya) | 3.01 | 🟢 Normal | -0.017 |  |
| 2026-05-10 10:13:12 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-05-10 10:03:01 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-05-10 10:01:21 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-10 10:06:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.020 |  |
| 2026-05-10 10:07:15 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.021 |  |
| 2026-05-10 10:05:59 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-05-10 10:02:44 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | -0.034 |  |
| 2026-05-10 10:08:10 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.037 |  |
| 2026-05-10 10:04:35 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-05-10 10:01:58 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-05-10 10:01:50 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.041 |  |
| 2026-05-10 10:05:36 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.048 |  |
| 2026-05-10 10:02:56 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | -0.054 |  |
| 2026-05-10 10:01:13 | Kuda Oya (Kirindi Oya) | 2.11 | 🟢 Normal | -0.070 |  |
| 2026-05-10 10:01:57 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.080 |  |
| 2026-05-10 10:06:04 | Thanamalwila (Kirindi Oya) | 2.21 | 🟢 Normal | -0.146 |  |
| 2026-05-10 10:03:56 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.205 |  |
| 2026-05-10 10:05:54 | Moragaswewa (Deduru Oya) | 2.36 | 🟢 Normal | -0.239 |  |
| 2026-05-10 09:04:08 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -3.789 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)