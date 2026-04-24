# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_13:36:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,784 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 13:36:19 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.007 |  |
| 2026-04-24 13:20:53 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-04-24 13:14:53 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.018 |  |
| 2026-04-24 13:12:22 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.052 |  |
| 2026-04-24 13:10:30 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-24 13:09:47 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | -0.029 |  |
| 2026-04-24 13:08:33 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 13:06:57 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.088 |  |
| 2026-04-24 13:06:50 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-04-24 13:05:59 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.051 |  |
| 2026-04-24 13:05:29 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-24 13:04:49 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 13:04:19 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-24 13:04:10 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 13:03:57 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-24 13:03:48 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 13:03:36 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.054 |  |
| 2026-04-24 13:03:36 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-24 13:03:27 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-24 13:03:24 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-04-24 13:03:03 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.060 |  |
| 2026-04-24 13:03:02 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-24 13:02:56 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 13:03:27 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-24 13:02:41 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-24 13:02:07 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-24 13:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-24 13:03:36 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-24 13:04:19 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-24 13:03:48 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 13:10:30 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-24 13:03:02 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-24 13:01:06 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 13:04:10 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 13:04:49 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 13:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 13:08:33 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 13:01:37 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 13:02:34 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 13:05:29 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-24 13:03:57 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-24 13:36:19 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.007 |  |
| 2026-04-24 13:06:50 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-04-24 13:01:33 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-04-24 13:00:52 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-24 13:02:56 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:06:35 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-04-24 13:14:53 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.018 |  |
| 2026-04-24 13:02:52 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-04-24 13:02:08 | Katharagama (Menik Ganga) | 2.02 | 🟢 Normal | -0.022 |  |
| 2026-04-24 13:09:47 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | -0.029 |  |
| 2026-04-24 13:03:24 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-04-24 13:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.031 |  |
| 2026-04-24 13:02:41 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-04-24 13:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.41 | 🟢 Normal | -0.050 |  |
| 2026-04-24 13:20:53 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-04-24 13:05:59 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.051 |  |
| 2026-04-24 13:12:22 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.052 |  |
| 2026-04-24 13:03:36 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.054 |  |
| 2026-04-24 13:03:03 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.060 |  |
| 2026-04-24 13:00:15 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.062 |  |
| 2026-04-24 13:06:57 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)