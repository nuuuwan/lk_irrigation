# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_03:20:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,940 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 03:20:19 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.015 |  |
| 2026-01-05 03:19:13 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.008 |  |
| 2026-01-05 03:13:06 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:10:40 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:09:01 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.040 |  |
| 2026-01-05 03:08:56 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:07:26 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:07:10 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:06:59 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:06:22 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.289 |  |
| 2026-01-05 03:06:07 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:05:22 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:05:21 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 03:04:50 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:04:28 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-05 03:04:19 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-05 03:04:12 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-05 03:04:00 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:03:58 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.089 |  |
| 2026-01-05 03:03:37 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:03:22 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-01-05 03:03:15 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:03:10 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:03:10 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:03:03 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:02:50 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:02:49 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 03:02:38 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 03:02:27 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.012 |  |
| 2026-01-05 03:02:25 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:02:17 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-05 03:01:53 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-01-05 03:01:48 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.014 |  |
| 2026-01-05 03:01:15 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:01:07 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 03:01:53 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-01-05 03:02:17 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-05 02:17:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-05 03:04:12 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-05 03:04:19 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-04 18:04:42 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-05 03:05:21 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 03:02:49 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 03:02:38 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 03:02:25 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:03:03 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:02:50 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:03:37 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:03:10 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:13:06 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:06:59 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:03:10 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:01:15 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:04:50 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-05 00:02:57 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:07:26 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:08:56 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:06:07 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:05:22 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:32 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:10:40 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:07:10 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:19:13 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.008 |  |
| 2026-01-05 03:01:07 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-05 03:04:28 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-05 03:02:27 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.012 |  |
| 2026-01-05 03:01:48 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.014 |  |
| 2026-01-05 03:20:19 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.015 |  |
| 2026-01-05 03:03:22 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-01-05 02:08:26 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.028 |  |
| 2026-01-05 03:09:01 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.040 |  |
| 2026-01-04 18:15:36 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | -0.048 |  |
| 2026-01-05 03:03:58 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.089 |  |
| 2026-01-05 03:06:22 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.289 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)