# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_08:26:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,703 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 08:26:06 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-01 08:22:46 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.001 |  |
| 2026-11-01 08:19:03 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:14:29 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:13:15 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-11-01 08:12:13 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:12:10 | Thawalama (Gin Ganga) | 2.83 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-01 08:08:51 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.152 |  |
| 2026-11-01 08:08:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.53 | 🟢 Normal | -0.019 |  |
| 2026-11-01 08:08:01 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:07:57 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.067 |  |
| 2026-11-01 08:06:42 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.018 |  |
| 2026-11-01 08:06:33 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:06:09 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 08:06:07 | Galgamuwa (Mee Oya) | 1.05 | 🟢 Normal | -36.000 |  |
| 2026-11-01 08:06:06 | Galgamuwa (Mee Oya) | 1.06 | 🟢 Normal | -36.000 |  |
| 2026-11-01 08:06:04 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-01 08:05:48 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:05:27 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.060 |  |
| 2026-11-01 08:05:15 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.039 |  |
| 2026-11-01 08:04:48 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:04:16 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:03:25 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-01 08:03:07 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.029 |  |
| 2026-11-01 08:03:04 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 08:02:56 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-01 08:02:52 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:02:49 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 08:02:41 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:02:31 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:02:24 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-11-01 08:02:21 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:02:17 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:01:39 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:01:12 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:01:11 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:00:44 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:00:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:00:43 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 08:13:15 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-11-01 08:06:04 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-01 08:02:56 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-01 08:03:25 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-01 08:12:10 | Thawalama (Gin Ganga) | 2.83 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-01 08:06:09 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 08:03:04 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 08:02:49 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 08:26:06 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-01 08:01:39 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 07:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:08:01 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:00:44 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:14:29 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:02:21 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:02:17 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:00:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:05:48 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:04:48 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:01:11 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:19:03 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:06:33 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:22:46 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.001 |  |
| 2026-11-01 08:04:16 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:02:41 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:02:52 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:01:12 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:00:43 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | -0.014 |  |
| 2026-11-01 08:06:42 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.018 |  |
| 2026-11-01 07:08:16 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-11-01 08:08:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.53 | 🟢 Normal | -0.019 |  |
| 2026-11-01 08:02:24 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-11-01 08:03:07 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.029 |  |
| 2026-11-01 08:05:15 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.039 |  |
| 2026-11-01 08:05:27 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.060 |  |
| 2026-11-01 08:07:57 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.067 |  |
| 2026-11-01 08:08:51 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.152 |  |
| 2026-11-01 08:06:07 | Galgamuwa (Mee Oya) | 1.05 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)