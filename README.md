# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_21:23:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,936 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 21:23:40 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:21:24 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:09:53 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.224 |  |
| 2026-04-07 21:08:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.055 |  |
| 2026-04-07 21:07:43 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.009 |  |
| 2026-04-07 21:07:23 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:06:55 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:05:50 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:05:41 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-04-07 21:05:17 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:04:46 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-07 21:04:39 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-07 21:04:26 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-04-07 21:04:22 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:03:42 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-04-07 21:03:40 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.031 |  |
| 2026-04-07 21:03:26 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:03:25 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:03:25 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-07 21:03:18 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.066 |  |
| 2026-04-07 21:03:02 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-04-07 21:02:57 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.010 |  |
| 2026-04-07 21:02:49 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:02:48 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:02:41 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-07 21:02:35 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:02:24 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-07 21:02:24 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:02:17 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 21:02:03 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-04-07 21:02:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:01:40 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:01:28 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:01:24 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-04-07 21:00:16 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 21:04:39 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-07 21:02:17 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 21:03:25 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-07 21:00:16 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:02:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:02:35 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:06:55 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:03:25 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:02:49 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:23:40 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:04:22 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:02:48 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:05:50 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:05:17 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:03:26 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:01:28 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:01:40 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:21:24 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:02:24 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:07:23 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-07 21:07:43 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.009 |  |
| 2026-04-07 21:04:26 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-04-07 21:02:41 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-07 21:04:46 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-07 21:02:03 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-04-07 21:02:24 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-07 21:02:57 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.010 |  |
| 2026-04-07 21:01:24 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-04-07 21:05:41 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-04-07 18:00:44 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-04-07 21:03:02 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-04-07 20:06:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.022 |  |
| 2026-04-07 21:03:42 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-04-07 21:03:40 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.031 |  |
| 2026-04-07 18:02:51 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.032 |  |
| 2026-04-07 21:08:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.055 |  |
| 2026-04-07 18:01:46 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.060 |  |
| 2026-04-07 21:03:18 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.066 |  |
| 2026-04-07 21:09:53 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.224 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)