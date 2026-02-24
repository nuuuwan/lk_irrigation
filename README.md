# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_16:37:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,924 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 16:37:36 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.007 |  |
| 2026-02-24 16:15:42 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-24 16:14:54 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.017 |  |
| 2026-02-24 16:14:14 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.008 |  |
| 2026-02-24 16:14:06 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-24 16:07:06 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:06:23 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-02-24 16:05:37 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | -0.019 |  |
| 2026-02-24 16:05:09 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:05:04 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:04:57 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 16:04:49 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.020 |  |
| 2026-02-24 16:04:42 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-24 16:04:05 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:03:51 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:03:42 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-24 16:03:38 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:03:30 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:03:29 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 16:03:42 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-24 16:02:16 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-24 16:14:06 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-24 16:15:42 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-24 16:02:33 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 16:04:57 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 16:04:42 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-24 16:03:30 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:01:45 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:02:23 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:00:39 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:01:04 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:01:36 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:05:09 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:02:55 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:04:05 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:05:04 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:05:37 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:02:42 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-24 16:37:36 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.007 |  |
| 2026-02-24 16:14:14 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.008 |  |
| 2026-02-24 16:06:23 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-02-24 16:07:06 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:03:51 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:01:26 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:02:10 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:01:37 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:00:54 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:01:45 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:02:50 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:03:38 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.010 |  |
| 2026-02-24 16:01:32 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-02-24 16:14:54 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.017 |  |
| 2026-02-24 16:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | -0.019 |  |
| 2026-02-24 16:04:49 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.020 |  |
| 2026-02-24 16:00:41 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | -0.020 |  |
| 2026-02-24 16:03:29 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-02-24 16:00:54 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.023 |  |
| 2026-02-24 16:01:45 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.042 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)