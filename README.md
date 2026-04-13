# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_17:24:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,119 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 17:24:09 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.158 |  |
| 2026-04-13 17:18:24 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-13 17:12:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:10:11 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:08:06 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:08:01 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.030 |  |
| 2026-04-13 17:07:53 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.046 |  |
| 2026-04-13 17:06:12 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.146 |  |
| 2026-04-13 17:05:43 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.059 |  |
| 2026-04-13 17:05:02 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-13 17:04:57 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:04:54 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-13 17:04:40 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.039 |  |
| 2026-04-13 17:04:28 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:04:16 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.034 |  |
| 2026-04-13 17:03:57 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-13 17:03:48 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.059 |  |
| 2026-04-13 17:03:37 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.180 |  |
| 2026-04-13 17:03:37 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:03:35 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:03:08 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.051 |  |
| 2026-04-13 17:03:06 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.049 |  |
| 2026-04-13 17:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | -0.059 |  |
| 2026-04-13 17:03:01 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.014 |  |
| 2026-04-13 17:02:47 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-04-13 17:02:25 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-04-13 17:02:13 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.011 |  |
| 2026-04-13 17:02:06 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-13 17:01:57 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:01:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:01:38 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:01:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.062 |  |
| 2026-04-13 17:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 17:01:24 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:01:23 | Katharagama (Menik Ganga) | -0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:01:01 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 17:00:52 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-13 17:00:38 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 17:02:47 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-04-13 17:02:25 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-04-13 17:03:57 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-13 17:18:24 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-13 17:02:06 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-13 17:00:52 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-13 17:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 17:00:38 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-13 17:04:54 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-13 17:01:01 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 16:01:15 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:12:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:01:53 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:01:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:03:35 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:01:24 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:10:11 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:04:57 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:03:37 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:01:57 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:01:23 | Katharagama (Menik Ganga) | -0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:08:06 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:04:28 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 17:05:02 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-13 17:02:13 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.011 |  |
| 2026-04-13 17:03:01 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.014 |  |
| 2026-04-13 17:08:01 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.030 |  |
| 2026-04-13 17:04:16 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.034 |  |
| 2026-04-13 17:04:40 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.039 |  |
| 2026-04-13 17:07:53 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.046 |  |
| 2026-04-13 17:03:06 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.049 |  |
| 2026-04-13 17:03:08 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.051 |  |
| 2026-04-13 17:05:43 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.059 |  |
| 2026-04-13 17:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | -0.059 |  |
| 2026-04-13 17:03:48 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.059 |  |
| 2026-04-13 17:01:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.062 |  |
| 2026-04-13 17:06:12 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.146 |  |
| 2026-04-13 17:24:09 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.158 |  |
| 2026-04-13 17:03:37 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)