# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_15:08:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,566 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 15:08:59 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:08:22 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-13 15:07:35 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-01-13 15:07:06 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-01-13 15:06:58 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.019 |  |
| 2026-01-13 15:05:21 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:05:00 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:04:58 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-01-13 15:04:46 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.019 |  |
| 2026-01-13 15:04:41 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-01-13 15:04:40 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 15:04:36 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 15:04:34 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 15:04:11 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:03:43 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:03:26 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:03:09 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-01-13 15:03:01 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:02:58 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-13 15:02:54 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-13 15:02:44 | Thanthirimale (Malwathu Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-01-13 15:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:02:26 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.111 |  |
| 2026-01-13 15:02:24 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:02:06 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:02:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:02:02 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-13 15:01:57 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:01:52 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.021 |  |
| 2026-01-13 15:01:50 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:01:37 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:01:35 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:01:32 | Yaka Wewa (Ma Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-01-13 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-01-13 15:00:46 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | -0.020 |  |
| 2026-01-13 15:00:40 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:00:22 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-13 15:00:08 | Horowpothana (Yan Oya) | 3.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-13 14:19:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:18:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-13 14:16:07 | Horowpothana (Yan Oya) | 3.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-13 14:14:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:14:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 14:13:46 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 15:02:54 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-13 15:00:08 | Horowpothana (Yan Oya) | 3.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-13 15:02:58 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-13 15:04:34 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 15:04:36 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 14:18:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-13 15:04:40 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 15:01:57 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:02:24 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:00:40 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:01:50 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:05:21 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:05:00 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:01:37 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:04:11 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:02:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:03:43 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:02:06 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:03:26 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:08:59 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:01:35 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:03:01 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:04:58 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-01-13 15:08:22 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-13 15:02:44 | Thanthirimale (Malwathu Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-01-13 15:00:22 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-13 15:07:35 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-01-13 15:02:02 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-13 15:07:06 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-01-13 15:04:46 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.019 |  |
| 2026-01-13 15:06:58 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.019 |  |
| 2026-01-13 15:00:46 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | -0.020 |  |
| 2026-01-13 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-01-13 15:01:52 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.021 |  |
| 2026-01-13 15:04:41 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-01-13 15:01:32 | Yaka Wewa (Ma Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-01-13 15:03:09 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-01-13 15:02:26 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)