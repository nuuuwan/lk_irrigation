# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_21:14:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,069 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 21:14:50 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.008 |  |
| 2026-07-07 21:12:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:11:04 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:09:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 21:08:22 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:06:28 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:06:16 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:06:07 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 21:05:37 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:05:05 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-07-07 21:05:05 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.280 |  |
| 2026-07-07 21:04:57 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:04:57 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-07 21:04:43 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:04:20 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-07-07 21:04:15 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:03:50 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:03:39 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:03:30 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-07 21:03:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-07-07 21:03:24 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:03:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:03:08 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:03:06 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:02:58 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:02:50 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-07 21:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-07-07 21:02:32 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.040 |  |
| 2026-07-07 21:02:22 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.031 |  |
| 2026-07-07 21:02:17 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:02:16 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.024 |  |
| 2026-07-07 21:02:15 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-07-07 21:02:08 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | -0.012 |  |
| 2026-07-07 21:01:52 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:01:35 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:01:15 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.012 |  |
| 2026-07-07 21:01:01 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 21:05:05 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-07-07 21:06:07 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 21:09:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 21:02:50 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-07 21:04:57 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-07 18:04:20 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:03:39 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:01:52 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:05:37 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:01:35 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:12:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:00 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:08:22 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:01:01 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:02:58 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:03:08 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:03:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:06:28 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:03:50 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:02:17 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:04:43 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:04:57 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:03:24 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:11:04 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:02 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:04:15 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:06:16 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-07 21:14:50 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.008 |  |
| 2026-07-07 21:03:30 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-07 21:03:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-07-07 21:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-07-07 21:01:15 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.012 |  |
| 2026-07-07 21:02:08 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | -0.012 |  |
| 2026-07-07 21:02:16 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.024 |  |
| 2026-07-07 21:02:15 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-07-07 21:02:22 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.031 |  |
| 2026-07-07 21:02:32 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.040 |  |
| 2026-07-07 21:04:20 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-07-07 21:05:05 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.280 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)