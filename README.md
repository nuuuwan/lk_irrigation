# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_23:17:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,482 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 23:17:59 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.067 |  |
| 2026-05-09 23:17:32 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:17:08 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-09 23:14:29 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.041 |  |
| 2026-05-09 23:09:25 | Katharagama (Menik Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:08:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.064 |  |
| 2026-05-09 23:08:51 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.027 |  |
| 2026-05-09 23:08:02 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.038 |  |
| 2026-05-09 23:07:25 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -24.000 |  |
| 2026-05-09 23:07:22 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -24.000 |  |
| 2026-05-09 23:07:21 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:06:54 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:06:52 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.205 |  |
| 2026-05-09 23:05:00 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-05-09 23:04:50 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.071 |  |
| 2026-05-09 23:04:45 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | -0.030 |  |
| 2026-05-09 23:04:44 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.175 |  |
| 2026-05-09 23:04:21 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:03:59 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-05-09 23:03:59 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:03:47 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-09 23:03:45 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.838 | 🔺 Rising |
| 2026-05-09 23:03:42 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-05-09 23:03:39 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:03:36 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-05-09 23:02:53 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:02:49 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:02:22 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.078 |  |
| 2026-05-09 23:01:48 | Kuda Oya (Kirindi Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:01:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:01:28 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-05-09 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-05-09 23:01:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:00:56 | Wellawaya (Kirindi Oya) | 3.55 | 🟢 Normal | -0.069 |  |
| 2026-05-09 23:00:31 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 23:03:45 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.838 | 🔺 Rising |
| 2026-05-09 23:03:36 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-09 23:17:08 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-09 23:03:47 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-09 23:02:49 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:01:47 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:03:39 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:17:32 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:01:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:01:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:03:59 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-09 23:07:21 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:04:21 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:02:53 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:06:54 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:01:48 | Kuda Oya (Kirindi Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:09:25 | Katharagama (Menik Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-09 23:03:42 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-05-09 23:05:00 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-05-09 23:08:51 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.027 |  |
| 2026-05-09 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-05-09 23:03:59 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-05-09 23:04:45 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | -0.030 |  |
| 2026-05-09 23:01:28 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-05-09 23:00:31 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.031 |  |
| 2026-05-09 23:08:02 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.038 |  |
| 2026-05-09 23:14:29 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.041 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-09 23:08:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.064 |  |
| 2026-05-09 23:17:59 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.067 |  |
| 2026-05-09 23:00:56 | Wellawaya (Kirindi Oya) | 3.55 | 🟢 Normal | -0.069 |  |
| 2026-05-09 23:04:50 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.071 |  |
| 2026-05-09 23:02:22 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.078 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-09 22:06:28 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.092 |  |
| 2026-05-09 23:04:44 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.175 |  |
| 2026-05-09 23:06:52 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.205 |  |
| 2026-05-09 23:07:25 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -24.000 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)