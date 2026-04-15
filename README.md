# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_05:21:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,428 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 05:21:17 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.304 |  |
| 2026-04-15 05:18:04 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-04-15 05:15:31 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-15 05:14:10 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-15 05:13:53 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:11:29 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-04-15 05:06:27 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-15 05:06:20 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.028 |  |
| 2026-04-15 05:06:17 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:05:06 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-15 05:04:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-04-15 05:04:43 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-15 05:04:39 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.012 |  |
| 2026-04-15 05:04:26 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.026 |  |
| 2026-04-15 05:04:14 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.119 |  |
| 2026-04-15 05:03:40 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:03:34 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-04-15 05:03:31 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-04-15 05:03:30 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-15 05:03:12 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-04-15 05:02:53 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:02:45 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.039 |  |
| 2026-04-15 05:02:10 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.079 |  |
| 2026-04-15 05:01:58 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.051 |  |
| 2026-04-15 05:01:49 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:01:15 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 05:00:45 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-15 05:00:42 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-15 05:00:13 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.090 |  |
| 2026-04-15 05:00:10 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:57:01 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:47:35 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 04:23:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 7.714 | 🔺 Rising |
| 2026-04-15 05:00:42 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-15 05:05:06 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-15 05:15:31 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-15 05:04:43 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-15 05:06:27 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-15 05:14:10 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-15 04:04:45 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-15 04:01:11 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 05:01:15 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 05:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:02:53 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:57:01 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:01:49 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:03:40 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:00:10 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:13:53 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:06:17 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-15 05:11:29 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-04-15 05:03:30 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-15 04:00:57 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-04-15 05:03:34 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-04-15 05:03:31 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-04-15 05:03:12 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-04-15 05:04:39 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.012 |  |
| 2026-04-15 05:00:45 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-15 05:04:26 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.026 |  |
| 2026-04-15 05:06:20 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.028 |  |
| 2026-04-15 05:18:04 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-04-15 05:02:45 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.039 |  |
| 2026-04-15 05:01:58 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.051 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-15 05:04:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-15 05:02:10 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.079 |  |
| 2026-04-15 05:00:13 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.090 |  |
| 2026-04-15 05:04:14 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.119 |  |
| 2026-04-15 05:21:17 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.304 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)