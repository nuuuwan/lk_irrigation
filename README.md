# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_22:25:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,647 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 22:25:55 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:16:18 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:10:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:08:19 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.009 |  |
| 2026-02-19 22:08:09 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:06:54 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:06:19 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:06:10 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:05:19 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:05:03 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:04:48 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:04:30 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 22:04:05 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:03:53 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 22:03:53 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:03:45 | Padiyathalawa (Maduru Oya) | 4.20 | 🟡 Alert | 0.236 | 🔺 Rising |
| 2026-02-19 22:03:43 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:03:37 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-02-19 22:03:21 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-19 22:03:06 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 22:02:52 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-19 22:02:32 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-02-19 22:02:13 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:01:58 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:01:24 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.011 |  |
| 2026-02-19 22:01:19 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:01:06 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-19 22:00:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:00:27 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 22:03:45 | Padiyathalawa (Maduru Oya) | 4.20 | 🟡 Alert | 0.236 | 🔺 Rising |
| 2026-02-19 22:03:37 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-02-19 18:04:32 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-19 21:02:22 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-19 22:02:52 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-19 22:03:53 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 19:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 22:01:06 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-19 22:04:30 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 22:00:27 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 22:03:06 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 22:08:09 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:03:53 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 21:02:37 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:03:43 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:03:40 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:06:10 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:04:05 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:16:18 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:00:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:05:03 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:02:13 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:25:55 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:10:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:06:54 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:04:48 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:06:19 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:01:54 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:05:19 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 21:08:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:01:19 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:01:58 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:08:19 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.009 |  |
| 2026-02-19 22:03:21 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-19 22:01:24 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.011 |  |
| 2026-02-19 22:02:32 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-02-19 21:00:52 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.113 |  |
| 2026-02-19 21:04:52 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)