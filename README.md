# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_03:35:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,571 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 03:35:15 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-13 03:17:10 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-13 03:16:41 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.024 |  |
| 2026-04-13 03:15:28 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.145 |  |
| 2026-04-13 03:12:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-04-13 03:10:36 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-04-13 03:10:35 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-04-13 03:09:52 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:09:52 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 03:09:44 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:09:03 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:07:52 | Rathnapura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.029 |  |
| 2026-04-13 03:06:16 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-13 03:05:57 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:05:48 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.070 |  |
| 2026-04-13 03:05:09 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.091 |  |
| 2026-04-13 03:04:53 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.079 |  |
| 2026-04-13 03:04:40 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.504 |  |
| 2026-04-13 03:04:05 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-04-13 03:03:57 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-13 03:03:50 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:03:49 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-13 03:03:01 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:03:00 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:02:54 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:02:23 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:01:58 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-04-13 03:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 03:01:19 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-13 03:01:17 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:00:49 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 03:10:36 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-04-13 02:39:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 2.667 | 🔺 Rising |
| 2026-04-13 03:04:05 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-04-13 03:01:58 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-04-12 18:07:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-13 03:06:16 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-13 03:17:10 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-13 03:35:15 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-13 03:03:49 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-13 03:09:52 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 03:03:57 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-13 02:28:42 | Magura (Kalu Ganga) | 3.96 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-13 03:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 03:00:49 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:05:57 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 00:03:32 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:09:44 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:01:17 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:09:03 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:03:50 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:03:00 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:02:23 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:03:01 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:02:54 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:03:43 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 02:03:03 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:09:52 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-13 03:01:19 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-13 03:16:41 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.024 |  |
| 2026-04-13 03:07:52 | Rathnapura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.029 |  |
| 2026-04-13 03:12:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-04-12 18:12:59 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.033 |  |
| 2026-04-13 03:05:48 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.070 |  |
| 2026-04-13 03:04:53 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.079 |  |
| 2026-04-13 03:05:09 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.091 |  |
| 2026-04-13 03:15:28 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.145 |  |
| 2026-04-13 03:04:40 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.504 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)