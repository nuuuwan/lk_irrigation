# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_21:22:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,358 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 21:22:22 | Magura (Kalu Ganga) | 3.99 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-27 21:19:14 | Rathnapura (Kalu Ganga) | 4.64 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-27 21:13:14 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:09:11 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:08:29 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-27 21:06:55 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-27 21:06:43 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:06:37 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-05-27 21:06:06 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-27 21:06:02 | Glencourse (Kelani Ganga) | 12.16 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-27 21:05:15 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:04:54 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-27 21:04:44 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-27 21:04:16 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-05-27 21:04:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:04:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:03:46 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-27 21:03:43 | Hanwella (Kelani Ganga) | 4.19 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-27 21:03:37 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-27 21:03:33 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:03:27 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:03:16 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:03:01 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-27 21:02:56 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:02:44 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2026-05-27 21:02:27 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:02:24 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:02:16 | Deraniyagala (Kelani Ganga) | 2.75 | 🟢 Normal | -0.300 |  |
| 2026-05-27 21:02:15 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:02:05 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.45 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-05-27 21:01:59 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:01:55 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:01:51 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 21:01:30 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:01:28 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 21:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.45 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-05-27 21:04:44 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-27 21:06:02 | Glencourse (Kelani Ganga) | 12.16 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-27 21:19:14 | Rathnapura (Kalu Ganga) | 4.64 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-27 21:06:55 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-27 21:22:22 | Magura (Kalu Ganga) | 3.99 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-27 21:08:29 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-27 18:00:23 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-27 21:04:54 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-27 21:03:43 | Hanwella (Kelani Ganga) | 4.19 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-27 21:06:06 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-27 21:03:46 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-27 21:03:01 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-27 21:01:28 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-27 21:01:51 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 21:03:37 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-27 21:02:05 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:04:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 20:35:02 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:01:30 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:03:16 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:01:55 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:02:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:02:15 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:02:56 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:09:11 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:06:43 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:04:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:03:33 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:02:24 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:13:14 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:01:59 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:02:27 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 21:05:15 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:05:39 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.009 |  |
| 2026-05-27 21:06:37 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-05-27 21:02:44 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2026-05-27 21:04:16 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-05-27 21:02:16 | Deraniyagala (Kelani Ganga) | 2.75 | 🟢 Normal | -0.300 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)