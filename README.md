# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_06:38:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,726 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 06:38:32 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-05-01 06:22:27 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:19:00 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-01 06:16:18 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.008 |  |
| 2026-05-01 06:14:42 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -18.000 |  |
| 2026-05-01 06:14:40 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -18.000 |  |
| 2026-05-01 06:14:39 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -18.000 |  |
| 2026-05-01 06:13:54 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:13:00 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.053 |  |
| 2026-05-01 06:11:03 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.002 |  |
| 2026-05-01 06:07:42 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 06:07:32 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-05-01 06:07:01 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.023 |  |
| 2026-05-01 06:06:15 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-05-01 06:05:53 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-05-01 06:05:39 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-01 06:04:51 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-05-01 06:04:45 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.039 |  |
| 2026-05-01 06:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-05-01 06:03:51 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -3.130 |  |
| 2026-05-01 06:03:30 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.071 |  |
| 2026-05-01 06:03:28 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -3.130 |  |
| 2026-05-01 06:03:20 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.013 |  |
| 2026-05-01 06:03:10 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:03:01 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:02:38 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-05-01 06:02:36 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-01 06:02:23 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-01 06:02:07 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:02:07 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:01:50 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.051 |  |
| 2026-05-01 06:01:45 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-01 06:01:37 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-05-01 06:01:05 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.074 |  |
| 2026-05-01 06:00:40 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-01 06:00:36 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.842 | 🔺 Rising |
| 2026-05-01 06:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:59:40 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:55:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:50:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.304 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 06:00:36 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.842 | 🔺 Rising |
| 2026-05-01 06:01:37 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-05-01 06:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-05-01 06:19:00 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-01 06:05:39 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-01 06:01:45 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-01 06:02:23 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-01 06:00:40 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-01 06:07:42 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 06:11:03 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.002 |  |
| 2026-05-01 06:02:07 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:02:07 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:03:10 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:02:44 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:03:01 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-05-01 05:11:59 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:22:27 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:13:54 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:16:18 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.008 |  |
| 2026-05-01 06:06:15 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-05-01 05:05:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-01 06:02:36 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-01 06:04:51 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-05-01 06:05:53 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-05-01 06:38:32 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-05-01 06:03:20 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.013 |  |
| 2026-05-01 05:14:06 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | -0.017 |  |
| 2026-05-01 06:07:32 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-05-01 06:07:01 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.023 |  |
| 2026-05-01 06:02:38 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-05-01 06:04:45 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.039 |  |
| 2026-05-01 06:01:50 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.051 |  |
| 2026-05-01 06:13:00 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.053 |  |
| 2026-05-01 06:03:30 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.071 |  |
| 2026-05-01 06:01:05 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.074 |  |
| 2026-05-01 06:03:51 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -3.130 |  |
| 2026-05-01 06:14:42 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)