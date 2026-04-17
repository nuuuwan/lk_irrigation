# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_05:39:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,224 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 05:39:22 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-04-17 05:19:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-17 05:16:49 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:15:01 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:12:26 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-04-17 05:07:30 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.032 |  |
| 2026-04-17 05:07:11 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-17 05:06:15 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-17 05:05:50 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:05:40 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2026-04-17 05:05:35 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.047 |  |
| 2026-04-17 05:04:51 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-17 05:04:50 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-17 05:04:49 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-17 05:04:15 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:03:56 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-04-17 05:03:47 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:02:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:02:36 | Kithulgala (Kelani Ganga) | 1.09 | 🟢 Normal | -10.286 |  |
| 2026-04-17 05:02:35 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-04-17 05:02:33 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.026 |  |
| 2026-04-17 05:02:31 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:02:30 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:02:26 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:02:24 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.092 |  |
| 2026-04-17 05:02:18 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-17 05:02:16 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-17 05:02:15 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -10.286 |  |
| 2026-04-17 05:02:00 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-17 05:01:46 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.059 |  |
| 2026-04-17 05:01:29 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-04-17 05:01:26 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-17 05:01:18 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-17 05:01:17 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.020 |  |
| 2026-04-17 05:00:52 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:00:22 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:00:13 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.056 |  |
| 2026-04-17 05:00:01 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.156 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 05:04:51 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-17 05:39:22 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-04-17 05:01:26 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-17 04:01:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-17 05:02:18 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-17 05:19:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-17 05:07:11 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-17 05:00:52 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:02:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:02:30 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:19 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:00:22 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:02:26 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:03:47 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:02:31 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 04:03:37 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:04:15 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:15:01 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:16:49 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 05:05:40 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2026-04-17 05:06:15 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-17 05:04:50 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-17 05:02:16 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-17 05:01:18 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-17 05:02:35 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-04-17 05:02:00 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-17 05:01:17 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.020 |  |
| 2026-04-17 05:03:56 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-04-17 05:01:29 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-04-17 05:02:33 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.026 |  |
| 2026-04-17 05:07:30 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.032 |  |
| 2026-04-17 05:05:35 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.047 |  |
| 2026-04-17 05:00:13 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.056 |  |
| 2026-04-17 05:01:46 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.059 |  |
| 2026-04-17 05:02:24 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.092 |  |
| 2026-04-16 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -4.696 |  |
| 2026-04-17 05:02:36 | Kithulgala (Kelani Ganga) | 1.09 | 🟢 Normal | -10.286 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)