# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_10:21:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,371 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 10:21:53 | Thanthirimale (Malwathu Oya) | 2.62 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-13 10:16:30 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:11:58 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:11:53 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | -0.009 |  |
| 2026-01-13 10:08:46 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:08:21 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-13 10:07:16 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-13 10:06:58 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.006 |  |
| 2026-01-13 10:06:35 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-13 10:06:04 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 10:05:50 | Horowpothana (Yan Oya) | 3.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 10:05:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.028 |  |
| 2026-01-13 10:05:29 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.058 |  |
| 2026-01-13 10:05:21 | Baddegama (Gin Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-13 10:05:07 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-13 10:04:36 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.050 |  |
| 2026-01-13 10:04:09 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:03:58 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.058 |  |
| 2026-01-13 10:03:51 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:03:50 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-01-13 10:03:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 10:03:35 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:03:22 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-01-13 10:03:17 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.013 |  |
| 2026-01-13 10:02:56 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:02:52 | Dunamale (Aththanagalu Oya) | 1.21 | 🟢 Normal | -0.033 |  |
| 2026-01-13 10:02:51 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-13 10:02:40 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-01-13 10:02:22 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:02:14 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:01:53 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:01:52 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:01:36 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-13 10:01:10 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:01:06 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:00:40 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 10:00:34 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:00:29 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 10:07:16 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-13 10:05:50 | Horowpothana (Yan Oya) | 3.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 10:00:40 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 10:03:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 10:06:04 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 10:21:53 | Thanthirimale (Malwathu Oya) | 2.62 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-13 10:01:10 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:02:14 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:01:53 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:15 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:16:30 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:01:52 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:08:46 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:02:22 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:03:35 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:02:56 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:03:51 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:01:06 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:11:58 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:04:09 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:00:34 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:06:58 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.006 |  |
| 2026-01-13 10:11:53 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | -0.009 |  |
| 2026-01-13 10:05:21 | Baddegama (Gin Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-13 10:06:35 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-13 10:01:36 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-13 10:08:21 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-13 10:05:07 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-13 10:03:50 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-01-13 10:03:22 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-01-13 10:03:17 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.013 |  |
| 2026-01-13 10:02:51 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-13 10:00:29 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-01-13 10:05:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.028 |  |
| 2026-01-13 10:02:40 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-01-13 10:02:52 | Dunamale (Aththanagalu Oya) | 1.21 | 🟢 Normal | -0.033 |  |
| 2026-01-13 10:04:36 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.050 |  |
| 2026-01-13 10:03:58 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.058 |  |
| 2026-01-13 10:05:29 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)