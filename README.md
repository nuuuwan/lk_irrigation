# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_23:47:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,949 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 23:47:08 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.012 |  |
| 2026-02-01 23:23:36 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-02-01 23:10:08 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.043 |  |
| 2026-02-01 23:07:56 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.010 |  |
| 2026-02-01 23:06:47 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 23:06:12 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:06:11 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 23:05:28 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-01 23:05:21 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.209 |  |
| 2026-02-01 23:05:05 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:04:31 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:03:54 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-02-01 23:03:47 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-02-01 23:03:42 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-02-01 23:03:39 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:03:35 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-02-01 23:03:05 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.080 |  |
| 2026-02-01 23:02:59 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.060 |  |
| 2026-02-01 23:02:35 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 23:02:25 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-02-01 23:02:12 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:02:12 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:01:55 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.069 |  |
| 2026-02-01 23:01:55 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 23:01:52 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 23:01:36 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-01 23:01:29 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:01:19 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:01:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-01 23:01:11 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-01 23:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:00:33 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:00:18 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 23:02:25 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-02-01 23:23:36 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-02-01 23:03:35 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-02-01 23:01:36 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-01 18:00:43 | Thanthirimale (Malwathu Oya) | 2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 23:01:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-01 23:05:28 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-01 23:06:11 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 23:01:55 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 23:02:35 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 23:01:52 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 23:06:47 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 23:01:29 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:02:12 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:00:33 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:06:12 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:03:39 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:01:02 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:03:34 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:26:45 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:02:12 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:24 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:05:05 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:01:19 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:00:18 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:04:31 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 23:03:42 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-02-01 23:07:56 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:53 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-01 23:03:47 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-02-01 23:01:11 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-01 23:47:08 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.012 |  |
| 2026-02-01 23:10:08 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.043 |  |
| 2026-02-01 18:01:47 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.050 |  |
| 2026-02-01 23:02:59 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.060 |  |
| 2026-02-01 23:01:55 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.069 |  |
| 2026-02-01 23:03:05 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.080 |  |
| 2026-02-01 23:05:21 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.209 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)