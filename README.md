# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_08:19:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,326 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 08:19:08 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:15:38 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:13:46 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:13:10 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:09:45 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.109 |  |
| 2026-04-08 08:09:14 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:08:23 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:08:09 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:07:38 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-04-08 08:07:36 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:07:09 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.012 |  |
| 2026-04-08 08:06:54 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.010 |  |
| 2026-04-08 08:06:48 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.093 |  |
| 2026-04-08 08:06:10 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:05:47 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.047 |  |
| 2026-04-08 08:05:41 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.086 |  |
| 2026-04-08 08:05:22 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:05:21 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-08 08:05:17 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-08 08:04:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.031 |  |
| 2026-04-08 08:04:36 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-04-08 08:04:19 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 08:03:59 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-08 08:03:56 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.126 |  |
| 2026-04-08 08:03:49 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:03:15 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-08 08:03:09 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-08 08:03:09 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:03:08 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-04-08 08:02:22 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:01:53 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:01:42 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:01:31 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:01:29 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:01:19 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.091 |  |
| 2026-04-08 08:01:18 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-08 08:01:17 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:01:15 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:01:09 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-04-08 08:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-08 08:00:52 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-08 08:00:45 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 08:04:36 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-04-08 08:01:18 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-08 08:07:38 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-04-08 08:03:15 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-08 08:03:09 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-08 08:05:17 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-08 08:05:21 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-08 08:03:59 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-08 08:04:19 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 08:03:49 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:09:14 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:00:45 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:05:22 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:08:23 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:01:15 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:03:09 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:15:38 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:01:42 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:01:31 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:06:10 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:19:08 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:07:36 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:01:17 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:02:22 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:13:46 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:13:10 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-08 08:06:54 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.010 |  |
| 2026-04-08 08:03:08 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-04-08 08:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-08 08:00:52 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-08 08:07:09 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.012 |  |
| 2026-04-08 08:01:09 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-04-08 08:04:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.031 |  |
| 2026-04-08 08:05:47 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.047 |  |
| 2026-04-08 08:05:41 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.086 |  |
| 2026-04-08 08:01:19 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.091 |  |
| 2026-04-08 08:06:48 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.093 |  |
| 2026-04-08 08:09:45 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.109 |  |
| 2026-04-08 08:03:56 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)