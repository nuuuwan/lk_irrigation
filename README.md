# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_15:05:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,782 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 15:05:26 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.059 |  |
| 2026-01-11 15:05:25 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | -0.019 |  |
| 2026-01-11 15:05:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-11 15:04:22 | Manampitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-01-11 15:04:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-11 15:03:58 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-11 15:03:53 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:03:47 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:03:32 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:03:26 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:03:11 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 15:03:06 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 15:03:03 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-11 15:03:02 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:03:02 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:02:48 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 15:02:35 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-11 15:02:13 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:02:07 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:54 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:53 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:50 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:42 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-11 15:01:33 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:20 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:18 | Thanthirimale (Malwathu Oya) | 1.76 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-11 15:01:13 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-01-11 15:01:09 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:00:51 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 15:00:33 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-01-11 14:24:11 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:22:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-11 14:21:44 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-11 14:08:45 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-11 14:08:34 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 15:03:03 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-11 15:02:35 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-11 15:04:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-11 15:05:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-11 15:03:58 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-11 15:01:18 | Thanthirimale (Malwathu Oya) | 1.76 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-11 15:00:51 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 15:03:06 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 15:03:11 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 15:02:48 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 15:01:53 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:54 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:05:09 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:33 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:20 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:03:47 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:09 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:03:02 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:02:13 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:03:26 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:30 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:03:53 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-01-11 13:13:01 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:03:02 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:06:40 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:50 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:03:32 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:02:07 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:04:27 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:01:42 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-11 15:00:33 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-01-11 14:03:10 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-11 15:01:13 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-01-11 15:05:25 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | -0.019 |  |
| 2026-01-11 15:04:22 | Manampitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-01-11 14:03:30 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-01-11 15:05:26 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.059 |  |
| 2026-01-11 14:03:36 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)