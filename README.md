# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_03:07:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,070 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 03:07:14 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:07:02 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:06:23 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:06:21 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-02 03:05:51 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-02-02 03:05:40 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:04:56 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:04:55 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.015 |  |
| 2026-02-02 03:04:09 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 03:04:09 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-02-02 03:03:48 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-02 03:03:26 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.040 |  |
| 2026-02-02 03:03:18 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-02 03:02:52 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:02:42 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-02-02 03:02:41 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-02-02 03:02:38 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 03:02:36 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:02:20 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-02 03:02:18 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.012 |  |
| 2026-02-02 03:02:12 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:02:07 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.706 |  |
| 2026-02-02 03:02:04 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-02 03:01:43 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:01:35 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-02 03:01:26 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:01:16 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.706 |  |
| 2026-02-02 03:00:41 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:58:18 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.042 |  |
| 2026-02-02 02:22:29 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:22:06 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:17:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-02 02:11:58 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-02 02:11:34 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 03:04:09 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-02-02 03:03:48 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-02 03:01:35 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-01 18:00:43 | Thanthirimale (Malwathu Oya) | 2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-02 02:11:58 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-02 03:02:20 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-02 02:17:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-02 03:06:21 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-02 03:04:09 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 03:02:04 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-02 03:02:38 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 03:01:43 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:05:40 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:02:12 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:07:29 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:07:02 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:02:36 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:06:23 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:24 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:02:52 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:07:14 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:22:06 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:04:56 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:00:41 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:01:26 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 03:03:18 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-02 03:02:42 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:53 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-02 03:02:18 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.012 |  |
| 2026-02-02 03:04:55 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.015 |  |
| 2026-02-02 01:17:16 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.018 |  |
| 2026-02-02 03:02:41 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-02-02 02:05:05 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-02-02 03:05:51 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-02-02 02:02:53 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-02-02 03:03:26 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.040 |  |
| 2026-02-02 02:58:18 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.042 |  |
| 2026-02-01 18:01:47 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.050 |  |
| 2026-02-02 03:02:07 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.706 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)