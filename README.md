# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_19:17:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,574 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 19:17:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.023 |  |
| 2026-04-28 19:16:44 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:14:04 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-04-28 19:10:14 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.074 |  |
| 2026-04-28 19:08:14 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-28 19:06:35 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-04-28 19:06:34 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.093 |  |
| 2026-04-28 19:04:46 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:04:43 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-04-28 19:04:23 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.041 |  |
| 2026-04-28 19:04:09 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-04-28 19:04:04 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.071 |  |
| 2026-04-28 19:03:46 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-04-28 19:03:35 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-28 19:03:07 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.049 |  |
| 2026-04-28 19:03:07 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.031 |  |
| 2026-04-28 19:02:49 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-04-28 19:02:48 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:02:46 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-04-28 19:02:44 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:02:25 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.108 |  |
| 2026-04-28 19:02:18 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-28 19:02:15 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:02:13 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:02:09 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.050 |  |
| 2026-04-28 19:02:09 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.042 |  |
| 2026-04-28 19:02:05 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:02:02 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-28 19:01:57 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:01:52 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 19:01:26 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:01:18 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:00:55 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-04-28 19:00:46 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 19:00:40 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 19:03:35 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-28 19:01:52 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 19:00:40 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 19:00:46 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 18:04:58 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 19:04:46 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:02:05 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:03:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:16:44 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:02:48 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:01:26 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:02:13 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:01:18 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:01:57 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:02:15 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:02:44 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 19:04:43 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-04-28 19:06:35 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-28 19:08:14 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-28 19:02:02 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-28 19:00:55 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-04-28 19:02:18 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-28 19:17:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.023 |  |
| 2026-04-28 19:02:49 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-04-28 19:03:07 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.031 |  |
| 2026-04-28 19:02:46 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-04-28 19:04:09 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-04-28 19:14:04 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-04-28 19:04:23 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.041 |  |
| 2026-04-28 19:02:09 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.042 |  |
| 2026-04-28 19:03:07 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.049 |  |
| 2026-04-28 19:03:46 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-04-28 19:02:09 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.050 |  |
| 2026-04-28 19:04:04 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.071 |  |
| 2026-04-28 19:10:14 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.074 |  |
| 2026-04-28 19:06:34 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.093 |  |
| 2026-04-28 19:02:25 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)