# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_16:19:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,081 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 16:19:33 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.032 |  |
| 2026-04-13 16:17:43 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:16:50 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-13 16:16:28 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-13 16:13:12 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:12:58 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:11:31 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.082 |  |
| 2026-04-13 16:10:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:10:35 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:09:36 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-04-13 16:07:40 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.019 |  |
| 2026-04-13 16:06:02 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 16:05:43 | Katharagama (Menik Ganga) | -0.50 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-13 16:04:39 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.153 |  |
| 2026-04-13 16:04:31 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-04-13 16:04:28 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.069 |  |
| 2026-04-13 16:04:16 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:04:06 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-04-13 16:03:58 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 16:03:46 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.108 |  |
| 2026-04-13 16:03:42 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.051 |  |
| 2026-04-13 16:03:31 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.205 |  |
| 2026-04-13 16:03:25 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-13 16:03:23 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-13 16:03:22 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-13 16:03:16 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.098 |  |
| 2026-04-13 16:03:08 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 16:05:43 | Katharagama (Menik Ganga) | -0.50 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-13 16:16:28 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-13 16:16:50 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-13 16:03:23 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-13 16:06:02 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 16:03:58 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 16:00:40 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 16:02:16 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 16:01:15 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:03:08 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:01:53 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:10:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:17:43 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:00:28 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:04:16 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:02:33 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:13:12 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:10:35 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:01:18 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:12:58 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:09:36 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-04-13 16:03:22 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-13 16:01:00 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-13 16:01:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-13 16:03:25 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-13 16:02:03 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-13 16:04:31 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-04-13 16:07:40 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.019 |  |
| 2026-04-13 16:04:06 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-04-13 16:19:33 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.032 |  |
| 2026-04-13 16:02:28 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | -0.032 |  |
| 2026-04-13 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.41 | 🟢 Normal | -0.051 |  |
| 2026-04-13 16:03:42 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.051 |  |
| 2026-04-13 16:04:28 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.069 |  |
| 2026-04-13 16:11:31 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.082 |  |
| 2026-04-13 16:03:16 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.098 |  |
| 2026-04-13 16:03:46 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.108 |  |
| 2026-04-13 16:04:39 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.153 |  |
| 2026-04-13 16:03:31 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)