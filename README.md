# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_07:20:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,812 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 07:20:02 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:12:50 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:09:35 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:09:19 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-07-04 07:09:05 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:08:22 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:08:10 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-07-04 07:07:34 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-07-04 07:06:03 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-07-04 07:05:55 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-07-04 07:05:54 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:05:33 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 07:05:17 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-04 07:05:17 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-07-04 07:05:08 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:05:00 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:05:00 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-07-04 07:04:39 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:04:32 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:04:15 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 07:03:58 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-04 07:03:40 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-07-04 07:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.070 |  |
| 2026-07-04 07:02:55 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 07:02:50 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-07-04 07:02:43 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:02:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:02:22 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-07-04 07:02:12 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:01:57 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:01:41 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.121 |  |
| 2026-07-04 07:01:35 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-04 07:01:20 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 07:01:18 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-07-04 07:01:05 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.054 |  |
| 2026-07-04 07:01:05 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 07:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-07-04 07:01:18 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-07-04 07:03:40 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-07-04 07:05:00 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-07-04 07:02:50 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-07-04 07:05:17 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-07-04 07:07:34 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-07-04 07:05:55 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-07-04 07:01:35 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-04 07:05:17 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-04 07:08:10 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-07-04 07:02:55 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 07:01:20 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 07:04:15 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 07:03:58 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-04 07:05:33 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 07:06:03 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-07-04 07:01:05 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:01:57 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:02:12 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:02:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:02:22 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:05:00 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:12:50 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:01:08 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:02:43 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:05:54 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:04:32 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:08:22 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:09:35 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:09:05 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:20:02 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:04:39 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:05:08 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:09:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-07-04 07:09:19 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-07-04 07:01:05 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.054 |  |
| 2026-07-04 07:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.070 |  |
| 2026-07-04 07:01:41 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)