# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_14:23:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,931 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 14:23:47 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.054 |  |
| 2026-04-23 14:20:20 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:20:19 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:15:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.066 |  |
| 2026-04-23 14:12:28 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.026 |  |
| 2026-04-23 14:11:05 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.056 |  |
| 2026-04-23 14:10:00 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:09:45 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-04-23 14:09:23 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | -0.017 |  |
| 2026-04-23 14:08:59 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 14:09:45 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-04-23 14:01:21 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-23 14:00:19 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-23 14:06:27 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 14:01:50 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:00:40 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:03:17 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:01:42 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:03:33 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:20:20 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:03:07 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:03:34 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:10:00 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:03:40 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:00:57 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:08:59 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-23 14:06:58 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2026-04-23 14:05:46 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-23 14:04:02 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-23 14:04:04 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-23 14:03:14 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-23 14:04:18 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-04-23 14:00:43 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.015 |  |
| 2026-04-23 14:09:23 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | -0.017 |  |
| 2026-04-23 14:04:14 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-04-23 14:01:20 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-04-23 14:03:29 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-04-23 14:03:45 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.021 |  |
| 2026-04-23 14:06:50 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.024 |  |
| 2026-04-23 14:12:28 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.026 |  |
| 2026-04-23 14:06:33 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.027 |  |
| 2026-04-23 14:00:44 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.031 |  |
| 2026-04-23 14:03:06 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.052 |  |
| 2026-04-23 14:23:47 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.054 |  |
| 2026-04-23 14:05:00 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.054 |  |
| 2026-04-23 14:11:05 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.056 |  |
| 2026-04-23 14:15:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.066 |  |
| 2026-04-23 14:05:15 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.071 |  |
| 2026-04-23 14:00:32 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)