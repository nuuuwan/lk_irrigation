# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_15:14:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,702 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 15:14:07 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:09:02 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.058 |  |
| 2026-02-06 15:09:00 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-06 15:08:31 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:07:01 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | -0.112 |  |
| 2026-02-06 15:06:11 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:06:04 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.005 |  |
| 2026-02-06 15:05:47 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:05:24 | Manampitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-06 15:05:01 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:04:58 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-02-06 15:04:49 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-06 15:04:43 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:04:30 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.031 |  |
| 2026-02-06 15:04:15 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-06 15:04:09 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:03:57 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:03:28 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-06 15:03:28 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:03:25 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:03:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:03:16 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-02-06 15:03:12 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-02-06 15:03:00 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-06 15:02:41 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 15:02:29 | Baddegama (Gin Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:02:19 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 15:02:08 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:02:07 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:01:58 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:01:48 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-02-06 15:01:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-06 15:01:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-06 15:01:14 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-02-06 15:01:14 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 15:03:12 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-02-06 15:01:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 15:04:49 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-06 15:09:00 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-06 15:04:15 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-06 15:03:28 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-06 15:02:41 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 15:05:24 | Manampitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-06 15:02:19 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 15:01:14 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:03:28 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:01:58 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:03:25 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:03:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:02:08 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:03:57 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:02:29 | Baddegama (Gin Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:08:31 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:03:00 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:04:09 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:05:01 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:05:47 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:02:07 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:06:11 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:14:07 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-06 15:06:04 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.005 |  |
| 2026-02-06 15:04:58 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-02-06 15:01:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-06 15:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-06 15:01:48 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-02-06 15:01:14 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-02-06 15:04:30 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.031 |  |
| 2026-02-06 15:03:16 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-02-06 15:09:02 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.058 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 15:07:01 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)