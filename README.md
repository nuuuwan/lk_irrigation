# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_06:16:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,018 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 06:16:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:12:16 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-10 06:12:02 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:10:47 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:09:48 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:08:46 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:08:29 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.023 |  |
| 2026-04-10 06:07:08 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.013 |  |
| 2026-04-10 06:06:24 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.102 |  |
| 2026-04-10 06:05:56 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:05:55 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.026 |  |
| 2026-04-10 06:05:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2026-04-10 06:05:21 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:05:19 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:04:13 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:03:52 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.046 |  |
| 2026-04-10 06:03:41 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-10 06:03:22 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:03:16 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:02:55 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 06:02:39 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.054 |  |
| 2026-04-10 06:02:31 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:02:29 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 06:02:27 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-10 06:02:20 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:01:36 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 06:01:30 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.229 |  |
| 2026-04-10 06:01:29 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:01:23 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:01:21 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-04-10 06:01:19 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.026 |  |
| 2026-04-10 06:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-10 06:01:10 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-04-10 06:00:41 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:00:33 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.101 |  |
| 2026-04-10 06:00:15 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:46:57 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:46:44 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 03:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-10 06:02:29 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 06:02:27 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-10 06:03:41 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-10 06:12:16 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-10 06:01:36 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 06:02:55 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 06:00:15 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:00:41 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:16:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:02:31 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:07:05 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:09:48 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:12:02 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:05:56 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:05:19 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:01:23 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:03:22 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:03:16 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:04:13 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:05:21 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:10:47 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:07 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:02:20 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:01:29 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:08:46 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:07:08 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.013 |  |
| 2026-04-10 06:01:10 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-04-10 06:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-10 06:08:29 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.023 |  |
| 2026-04-10 06:01:19 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.026 |  |
| 2026-04-10 06:05:55 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.026 |  |
| 2026-04-10 06:01:21 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-04-10 06:05:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2026-04-10 06:03:52 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.046 |  |
| 2026-04-10 06:02:39 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.054 |  |
| 2026-04-10 06:00:33 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.101 |  |
| 2026-04-10 06:06:24 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.102 |  |
| 2026-04-10 06:01:30 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)