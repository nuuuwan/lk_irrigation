# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_22:25:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 22:25:11 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.023 |  |
| 2026-02-22 22:16:25 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.032 |  |
| 2026-02-22 22:11:58 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:11:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:09:24 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:08:51 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.061 |  |
| 2026-02-22 22:07:59 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-02-22 22:07:15 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.039 |  |
| 2026-02-22 22:06:24 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:06:15 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.028 |  |
| 2026-02-22 22:05:53 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:05:45 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.092 |  |
| 2026-02-22 22:05:31 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.025 |  |
| 2026-02-22 22:05:29 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.067 |  |
| 2026-02-22 22:05:17 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.029 |  |
| 2026-02-22 22:05:01 | Manampitiya (Mahaweli Ganga) | 3.10 | 🟡 Alert | -0.121 |  |
| 2026-02-22 22:04:52 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.103 |  |
| 2026-02-22 22:04:52 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 22:04:46 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:04:43 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.031 |  |
| 2026-02-22 22:04:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:03:44 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.133 |  |
| 2026-02-22 22:03:40 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:02:53 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:02:43 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:02:29 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-22 22:02:22 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:02:06 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:01:53 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:01:50 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:00:54 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:00:49 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:00:27 | Padiyathalawa (Maduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:00:23 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 22:05:01 | Manampitiya (Mahaweli Ganga) | 3.10 | 🟡 Alert | -0.121 |  |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-22 22:02:29 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-22 22:04:52 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 22:06:24 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:05:53 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:03:40 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:00:49 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:00:27 | Padiyathalawa (Maduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:09:24 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:04:46 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:02:53 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:00:23 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:11:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:11:58 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:04:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-02-22 21:03:56 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:02:06 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:02:43 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:01:50 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:00:54 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:07:59 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-02-22 22:25:11 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.023 |  |
| 2026-02-22 22:05:31 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.025 |  |
| 2026-02-22 22:06:15 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.028 |  |
| 2026-02-22 22:05:17 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.029 |  |
| 2026-02-22 22:04:43 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.031 |  |
| 2026-02-22 22:16:25 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.032 |  |
| 2026-02-22 22:07:15 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.039 |  |
| 2026-02-22 21:04:27 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | -0.040 |  |
| 2026-02-22 22:08:51 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.061 |  |
| 2026-02-22 21:02:52 | Ellagawa (Kalu Ganga) | 7.61 | 🟢 Normal | -0.061 |  |
| 2026-02-22 22:05:29 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.067 |  |
| 2026-02-22 22:05:45 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.092 |  |
| 2026-02-22 22:04:52 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.103 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-22 21:02:56 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.117 |  |
| 2026-02-22 22:03:44 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)