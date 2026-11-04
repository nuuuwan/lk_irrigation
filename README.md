# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_09:10:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,482 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 09:10:58 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-04 09:09:43 | Urawa (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.097 |  |
| 2026-11-04 09:08:09 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | -0.083 |  |
| 2026-11-04 09:07:53 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.036 |  |
| 2026-11-04 09:06:38 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-04 09:06:31 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.159 |  |
| 2026-11-04 09:06:13 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.170 |  |
| 2026-11-04 09:06:03 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.058 |  |
| 2026-11-04 09:05:31 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | -0.065 |  |
| 2026-11-04 09:05:24 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.058 |  |
| 2026-11-04 09:05:15 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-04 09:05:08 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:04:40 | Moraketiya (Walawe Ganga) | 1.67 | 🟢 Normal | -0.084 |  |
| 2026-11-04 09:04:11 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | -0.118 |  |
| 2026-11-04 09:04:09 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:04:08 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:04:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-04 09:04:01 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.059 |  |
| 2026-11-04 09:03:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-04 09:03:57 | Galgamuwa (Mee Oya) | 1.07 | 🟢 Normal | -0.040 |  |
| 2026-11-04 09:03:32 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:03:22 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:03:18 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | -0.125 |  |
| 2026-11-04 09:02:52 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-11-04 09:02:47 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.020 |  |
| 2026-11-04 09:02:46 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-04 09:02:45 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 09:02:40 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.029 |  |
| 2026-11-04 09:02:40 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.124 |  |
| 2026-11-04 09:02:17 | Moragaswewa (Deduru Oya) | 4.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-04 09:02:09 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.022 |  |
| 2026-11-04 09:02:03 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-04 09:02:00 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:01:18 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:01:09 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.050 |  |
| 2026-11-04 09:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-04 09:00:39 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-04 09:00:33 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-11-04 09:00:08 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 09:04:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-04 09:00:39 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-04 09:03:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-04 09:02:46 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-04 09:06:38 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-04 09:10:58 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-04 09:02:17 | Moragaswewa (Deduru Oya) | 4.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-04 09:02:45 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 09:00:08 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:01:18 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:03:32 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:04:09 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:03:22 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:04:08 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:02:00 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:05:08 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:02:03 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-04 09:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-04 09:02:47 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.020 |  |
| 2026-11-04 09:02:52 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-11-04 09:02:09 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.022 |  |
| 2026-11-04 09:02:40 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.029 |  |
| 2026-11-04 09:00:33 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-11-04 09:07:53 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.036 |  |
| 2026-11-04 09:03:57 | Galgamuwa (Mee Oya) | 1.07 | 🟢 Normal | -0.040 |  |
| 2026-11-04 09:05:15 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-04 09:01:09 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.050 |  |
| 2026-11-04 09:05:24 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.058 |  |
| 2026-11-04 09:06:03 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.058 |  |
| 2026-11-04 09:04:01 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.059 |  |
| 2026-11-04 09:05:31 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | -0.065 |  |
| 2026-11-04 09:08:09 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | -0.083 |  |
| 2026-11-04 09:04:40 | Moraketiya (Walawe Ganga) | 1.67 | 🟢 Normal | -0.084 |  |
| 2026-11-04 09:09:43 | Urawa (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.097 |  |
| 2026-11-04 09:04:11 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | -0.118 |  |
| 2026-11-04 09:02:40 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.124 |  |
| 2026-11-04 09:03:18 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | -0.125 |  |
| 2026-11-04 09:06:31 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.159 |  |
| 2026-11-04 09:06:13 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)