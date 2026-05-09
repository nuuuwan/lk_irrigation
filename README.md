# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_06:33:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,827 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 06:33:27 | Galgamuwa (Mee Oya) | 2.95 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-09 06:12:29 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.065 |  |
| 2026-05-09 06:11:13 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-09 06:10:54 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.035 |  |
| 2026-05-09 06:09:19 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.210 |  |
| 2026-05-09 06:08:41 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | -0.063 |  |
| 2026-05-09 06:07:52 | Thanamalwila (Kirindi Oya) | 3.51 | 🟢 Normal | -2.015 |  |
| 2026-05-09 06:07:10 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.046 |  |
| 2026-05-09 06:06:56 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.038 |  |
| 2026-05-09 06:06:53 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.018 |  |
| 2026-05-09 06:06:33 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-09 06:05:42 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-09 06:04:27 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-05-09 06:03:55 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.041 |  |
| 2026-05-09 06:03:53 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 06:03:49 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-09 06:03:45 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 06:03:18 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-09 06:02:58 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 06:02:50 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-05-09 06:02:49 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 06:02:45 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-09 06:02:03 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 06:01:56 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-09 06:01:48 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.136 |  |
| 2026-05-09 06:01:46 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.099 |  |
| 2026-05-09 06:01:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.096 |  |
| 2026-05-09 06:01:39 | Moragaswewa (Deduru Oya) | 3.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-09 06:01:35 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.129 |  |
| 2026-05-09 06:01:33 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-09 06:01:31 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 06:01:21 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-09 06:01:18 | Wellawaya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.178 |  |
| 2026-05-09 06:01:15 | Kuda Oya (Kirindi Oya) | 3.70 | 🟢 Normal | -1.389 |  |
| 2026-05-09 06:00:48 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | -0.013 |  |
| 2026-05-09 06:00:21 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.005 |  |
| 2026-05-09 06:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-09 06:00:16 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -180.000 |  |
| 2026-05-09 06:00:15 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -180.000 |  |
| 2026-05-09 05:47:11 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 05:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.68 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-09 06:01:21 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-09 06:01:56 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-09 06:06:33 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-09 06:01:33 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-09 06:01:39 | Moragaswewa (Deduru Oya) | 3.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-09 06:03:49 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 06:33:27 | Galgamuwa (Mee Oya) | 2.95 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-09 06:02:58 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 06:03:45 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 06:02:03 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 06:05:42 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-09 06:02:49 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 06:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-09 06:02:50 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-05-09 06:03:53 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 06:11:13 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-09 06:01:31 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 06:00:21 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.005 |  |
| 2026-05-09 06:02:45 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-09 06:00:48 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | -0.013 |  |
| 2026-05-09 06:06:53 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.018 |  |
| 2026-05-09 06:04:27 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-05-09 06:10:54 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.035 |  |
| 2026-05-09 06:06:56 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.038 |  |
| 2026-05-09 06:03:55 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.041 |  |
| 2026-05-09 06:07:10 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.046 |  |
| 2026-05-09 06:08:41 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | -0.063 |  |
| 2026-05-09 06:12:29 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.065 |  |
| 2026-05-09 06:01:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.096 |  |
| 2026-05-09 06:01:46 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.099 |  |
| 2026-05-09 06:01:35 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.129 |  |
| 2026-05-09 06:01:48 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.136 |  |
| 2026-05-09 06:01:18 | Wellawaya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.178 |  |
| 2026-05-09 06:09:19 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.210 |  |
| 2026-05-09 06:01:15 | Kuda Oya (Kirindi Oya) | 3.70 | 🟢 Normal | -1.389 |  |
| 2026-05-09 06:07:52 | Thanamalwila (Kirindi Oya) | 3.51 | 🟢 Normal | -2.015 |  |
| 2026-05-09 06:00:16 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)