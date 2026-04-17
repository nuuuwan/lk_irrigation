# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_07:22:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,302 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 07:22:53 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | -0.008 |  |
| 2026-04-17 07:13:01 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.051 |  |
| 2026-04-17 07:09:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-17 07:09:06 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.093 |  |
| 2026-04-17 07:08:32 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:07:49 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.012 |  |
| 2026-04-17 07:07:32 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.027 |  |
| 2026-04-17 07:07:19 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2026-04-17 07:07:15 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:06:50 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-04-17 07:06:14 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-04-17 07:05:54 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.038 |  |
| 2026-04-17 07:04:46 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:04:42 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-17 07:04:36 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.145 |  |
| 2026-04-17 07:03:42 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.060 |  |
| 2026-04-17 07:03:29 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.022 |  |
| 2026-04-17 07:03:11 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:02:58 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-04-17 07:02:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 07:02:47 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:02:45 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 07:02:44 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:02:41 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.015 |  |
| 2026-04-17 07:02:36 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-04-17 07:02:28 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-17 07:02:25 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.041 |  |
| 2026-04-17 07:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.077 |  |
| 2026-04-17 07:02:16 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.056 |  |
| 2026-04-17 07:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:01:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:01:55 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.020 |  |
| 2026-04-17 07:01:49 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-17 07:01:13 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:00:59 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.006 |  |
| 2026-04-17 07:00:52 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:00:16 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.050 |  |
| 2026-04-17 07:00:10 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.073 |  |
| 2026-04-17 06:38:46 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 06:31:33 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 07:07:19 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2026-04-17 07:02:45 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 07:02:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 07:01:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:01:13 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:00:52 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:02:44 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:02:47 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:08:32 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:04:46 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:03:11 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:07:15 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 07:00:59 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.006 |  |
| 2026-04-17 07:22:53 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | -0.008 |  |
| 2026-04-17 07:06:50 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-04-17 07:09:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-17 07:04:42 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-17 07:01:49 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-17 07:02:28 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-17 06:08:56 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-04-17 07:07:49 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.012 |  |
| 2026-04-17 07:02:41 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.015 |  |
| 2026-04-17 07:06:14 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-04-17 07:01:55 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.020 |  |
| 2026-04-17 07:02:58 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-04-17 07:03:29 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.022 |  |
| 2026-04-17 07:07:32 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.027 |  |
| 2026-04-17 07:02:36 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-04-17 07:05:54 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.038 |  |
| 2026-04-17 07:02:25 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.041 |  |
| 2026-04-17 07:00:16 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.050 |  |
| 2026-04-17 07:13:01 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.051 |  |
| 2026-04-17 07:02:16 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.056 |  |
| 2026-04-17 07:03:42 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.060 |  |
| 2026-04-17 07:00:10 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.073 |  |
| 2026-04-17 07:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.077 |  |
| 2026-04-17 07:09:06 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.093 |  |
| 2026-04-17 07:04:36 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)