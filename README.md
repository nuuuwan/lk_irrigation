# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_11:17:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,931 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 11:17:39 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:16:13 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:12:58 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:12:36 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-01 11:12:33 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.046 |  |
| 2026-05-01 11:12:22 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:09:51 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-01 11:09:25 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:08:48 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-05-01 11:08:05 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-05-01 11:07:04 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:06:48 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.047 |  |
| 2026-05-01 11:06:29 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-05-01 11:05:34 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.079 |  |
| 2026-05-01 11:05:11 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:05:02 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-05-01 11:04:27 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-01 11:04:00 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.005 |  |
| 2026-05-01 11:03:48 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-05-01 11:03:34 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:03:21 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:03:12 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:03:12 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:03:01 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.035 |  |
| 2026-05-01 11:03:00 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.014 |  |
| 2026-05-01 11:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.059 |  |
| 2026-05-01 11:02:36 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:02:31 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-01 11:02:14 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.071 |  |
| 2026-05-01 11:02:05 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:01:59 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.112 |  |
| 2026-05-01 11:01:54 | Thanthirimale (Malwathu Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:01:52 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -54.000 |  |
| 2026-05-01 11:01:50 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -54.000 |  |
| 2026-05-01 11:01:35 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:01:29 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.054 |  |
| 2026-05-01 11:01:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-01 11:01:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.031 |  |
| 2026-05-01 11:00:28 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 11:01:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-01 11:04:27 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-01 11:09:51 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-01 10:06:01 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-01 11:04:00 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.005 |  |
| 2026-05-01 11:01:35 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:02:36 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:03:12 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:12:58 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:16:13 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:03:12 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:03:34 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:03:21 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:12:22 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:05:11 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:07:04 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:02:05 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:01:54 | Thanthirimale (Malwathu Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:17:39 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 11:08:05 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-05-01 11:12:36 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-01 11:02:31 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-01 11:03:00 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.014 |  |
| 2026-05-01 11:05:02 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-05-01 11:08:48 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-05-01 11:06:29 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-05-01 11:00:28 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.020 |  |
| 2026-05-01 11:01:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.031 |  |
| 2026-05-01 11:03:48 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-05-01 11:03:01 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.035 |  |
| 2026-05-01 11:12:33 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.046 |  |
| 2026-05-01 11:06:48 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.047 |  |
| 2026-05-01 11:01:29 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.054 |  |
| 2026-05-01 11:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.059 |  |
| 2026-05-01 11:02:14 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.071 |  |
| 2026-05-01 11:05:34 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.079 |  |
| 2026-05-01 11:01:59 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.112 |  |
| 2026-05-01 11:01:52 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)