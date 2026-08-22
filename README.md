# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_18:07:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,619 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 18:07:26 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-22 18:07:20 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:06:22 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-08-22 18:05:37 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:05:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-08-22 18:05:09 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-08-22 18:04:59 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:04:57 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:04:56 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:04:54 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:04:29 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.039 |  |
| 2026-08-22 18:04:25 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:04:14 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:03:56 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.062 |  |
| 2026-08-22 18:03:55 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:03:43 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | -0.030 |  |
| 2026-08-22 18:03:33 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 18:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-08-22 18:03:19 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:03:06 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-08-22 18:03:03 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-22 18:02:54 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-22 18:02:45 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:41 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:23 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.020 |  |
| 2026-08-22 18:02:20 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:16 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-22 18:02:14 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:11 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:04 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-08-22 18:01:56 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:54 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-22 18:01:50 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:46 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-08-22 18:01:45 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:22 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:13 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:00:59 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:00:58 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:00:28 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-08-22 18:00:14 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-08-22 17:25:40 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 18:02:04 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-08-22 18:07:26 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-22 18:02:16 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-22 18:02:54 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-22 18:03:03 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-22 18:03:33 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 18:00:58 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:50 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:20 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:45 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:00:59 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:07:20 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:04:59 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:04:56 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:04:25 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:13 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:04:14 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:41 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:23 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:14 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:56 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:05:37 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:04:54 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:22 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:02:11 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:05:09 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-08-22 18:00:28 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-08-22 18:01:54 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-22 18:00:14 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-08-22 18:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-08-22 18:06:22 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-08-22 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.020 |  |
| 2026-08-22 18:01:46 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-08-22 18:05:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-08-22 18:03:43 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | -0.030 |  |
| 2026-08-22 18:03:06 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-08-22 18:04:29 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.039 |  |
| 2026-08-22 18:03:56 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)