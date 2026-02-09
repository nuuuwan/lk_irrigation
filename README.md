# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_17:00:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,503 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 17:00:33 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:30:16 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-09 16:24:15 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:13:00 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:11:04 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-09 16:09:36 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:08:58 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-02-09 16:08:55 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:08:22 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-09 16:07:22 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:06:51 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:06:30 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-09 16:06:09 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:04:44 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:04:37 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 16:02:41 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-09 16:02:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-09 16:06:30 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-09 16:08:22 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-09 16:30:16 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-09 16:04:20 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 16:04:37 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 16:11:04 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-09 16:02:24 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 16:03:53 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 16:02:23 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 16:02:56 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:02:08 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:00:10 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:01:39 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:03:00 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:06:09 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:02:28 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:06:51 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:13:00 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:01:21 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 17:00:33 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:07:22 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:02:56 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:08:55 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:24:15 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:02:37 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:09:36 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-09 16:03:59 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-02-09 16:02:00 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-09 16:04:04 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-09 16:01:25 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-02-09 16:03:04 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-09 16:00:29 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.012 |  |
| 2026-02-09 16:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-02-09 16:04:25 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-02-09 16:01:47 | Weraganthota (Mahaweli Ganga) | -2.54 | 🟢 Normal | -0.030 |  |
| 2026-02-09 16:08:58 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.038 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)