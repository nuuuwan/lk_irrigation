# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_09:07:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,746 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 09:07:06 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:06:42 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-02-23 09:06:34 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.013 |  |
| 2026-02-23 09:06:20 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.066 |  |
| 2026-02-23 09:06:16 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.042 |  |
| 2026-02-23 09:06:12 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-02-23 09:05:29 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:05:27 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.032 |  |
| 2026-02-23 09:04:12 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:04:07 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | -0.144 |  |
| 2026-02-23 09:03:57 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.290 |  |
| 2026-02-23 09:03:27 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:03:24 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:03:08 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:03:06 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.127 |  |
| 2026-02-23 09:03:04 | Kithulgala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.292 |  |
| 2026-02-23 09:02:47 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:02:46 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:02:40 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.020 |  |
| 2026-02-23 09:02:37 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-23 09:02:34 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | -0.019 |  |
| 2026-02-23 09:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.099 |  |
| 2026-02-23 09:02:18 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-02-23 09:02:14 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:02:01 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:01:58 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-23 09:01:57 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2026-02-23 09:01:47 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:01:45 | Manampitiya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-23 09:01:34 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-23 09:01:31 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:01:30 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.040 |  |
| 2026-02-23 09:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:01:00 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 09:00:41 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-02-23 08:20:30 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 09:01:45 | Manampitiya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-23 09:01:58 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-23 09:02:37 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-23 09:01:34 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-23 08:01:54 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-23 09:01:00 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 09:01:47 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:04:12 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:18 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:03:27 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:07:06 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:01:31 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:02:46 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:02:47 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:05:29 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:02:08 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:03:24 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:02:01 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:03:08 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:02:14 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:00:41 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-02-23 08:05:36 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:06:34 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.013 |  |
| 2026-02-23 09:06:12 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-02-23 09:02:34 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | -0.019 |  |
| 2026-02-23 09:02:40 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.020 |  |
| 2026-02-23 09:02:18 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-02-23 09:06:42 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-02-23 09:01:57 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2026-02-23 09:05:27 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.032 |  |
| 2026-02-23 09:01:30 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.040 |  |
| 2026-02-23 09:06:16 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.042 |  |
| 2026-02-23 09:06:20 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.066 |  |
| 2026-02-23 09:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.099 |  |
| 2026-02-23 09:03:06 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.127 |  |
| 2026-02-23 09:04:07 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | -0.144 |  |
| 2026-02-23 09:03:57 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.290 |  |
| 2026-02-23 09:03:04 | Kithulgala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.292 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)