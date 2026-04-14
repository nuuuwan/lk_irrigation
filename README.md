# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_00:31:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,268 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 00:31:43 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:21:44 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:20:25 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.016 |  |
| 2026-04-15 00:19:42 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:19:27 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.018 |  |
| 2026-04-15 00:18:52 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.008 |  |
| 2026-04-15 00:17:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-15 00:12:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-04-15 00:12:23 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-04-15 00:11:35 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:11:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:08:31 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:08:04 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:06:56 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-15 00:06:36 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:06:19 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:05:53 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-15 00:05:42 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:05:10 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:04:52 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-15 00:04:29 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-15 00:03:47 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-15 00:03:41 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-15 00:03:34 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:03:09 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:02:49 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.012 |  |
| 2026-04-15 00:02:25 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-04-15 00:02:22 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.021 |  |
| 2026-04-15 00:01:42 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-04-15 00:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:01:35 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.039 |  |
| 2026-04-15 00:01:15 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-15 00:01:09 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:00:46 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:52:02 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 00:12:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-04-15 00:03:41 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-15 00:05:53 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-15 00:17:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-15 00:03:47 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-15 00:04:52 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-15 00:01:15 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-15 00:06:56 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-15 00:19:42 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:11:35 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:03:09 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:31:43 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:06:36 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:05:10 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 23:17:13 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:01:09 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:21:44 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:03:34 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:08:31 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:00:46 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:05:42 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:08:04 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 22:01:35 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:11:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:18:52 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.008 |  |
| 2026-04-15 00:04:29 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-14 22:01:47 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-15 00:02:49 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.012 |  |
| 2026-04-15 00:20:25 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.016 |  |
| 2026-04-15 00:19:27 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.018 |  |
| 2026-04-15 00:12:23 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-04-15 00:01:42 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-04-15 00:02:25 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-04-15 00:02:22 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.021 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-15 00:01:35 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.039 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)