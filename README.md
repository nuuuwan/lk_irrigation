# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_11:16:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,829 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 11:16:16 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.026 |  |
| 2026-02-23 11:14:53 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.042 |  |
| 2026-02-23 11:11:28 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:10:12 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-02-23 11:09:13 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:08:21 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-02-23 11:06:49 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-02-23 11:06:41 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.074 |  |
| 2026-02-23 11:05:20 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:04:59 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.144 |  |
| 2026-02-23 11:04:28 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-23 11:04:24 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-02-23 11:04:21 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-02-23 11:04:20 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-02-23 11:04:04 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-23 11:04:03 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-02-23 11:03:59 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:03:50 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:03:43 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.048 |  |
| 2026-02-23 11:03:42 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:03:40 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:03:37 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-23 11:03:31 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:03:21 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:03:19 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.108 |  |
| 2026-02-23 11:03:01 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:02:46 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 11:02:20 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.100 |  |
| 2026-02-23 11:02:10 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:02:07 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-02-23 11:01:43 | Manampitiya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-23 11:01:36 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.064 |  |
| 2026-02-23 11:01:24 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:01:23 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:01:19 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:01:15 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:00:54 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:00:15 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 11:02:07 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-02-23 11:03:37 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-23 11:04:28 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-23 11:04:04 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-23 11:01:43 | Manampitiya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-23 11:02:46 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 11:01:15 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:00:40 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:00:54 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:03:31 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:03:50 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:09:13 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:03:42 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:01:19 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:03:01 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:02:20 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:02:10 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 11:08:21 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-02-23 11:04:24 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-02-23 11:03:40 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:03:21 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:11:28 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:00:15 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:03:59 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:01:24 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:01:23 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-23 11:10:12 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-02-23 11:04:20 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-02-23 11:04:03 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-02-23 11:16:16 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.026 |  |
| 2026-02-23 11:06:49 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-02-23 11:04:21 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-02-23 11:14:53 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.042 |  |
| 2026-02-23 11:03:43 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.048 |  |
| 2026-02-23 11:01:36 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.064 |  |
| 2026-02-23 11:06:41 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.074 |  |
| 2026-02-23 11:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.100 |  |
| 2026-02-23 11:03:19 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.108 |  |
| 2026-02-23 11:04:59 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)