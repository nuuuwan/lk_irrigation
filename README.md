# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_08:03:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,680 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 08:03:07 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.029 |  |
| 2026-11-01 08:03:04 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 08:02:56 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-01 08:02:52 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:02:49 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 08:02:41 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:02:31 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
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
| 2026-11-01 07:02:53 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-01 07:09:48 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-01 07:04:25 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-01 07:08:57 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-01 07:08:43 | Baddegama (Gin Ganga) | 2.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 08:02:56 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-01 07:06:05 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-01 08:03:04 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 08:02:49 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 07:03:44 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-01 06:59:10 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.001 |  |
| 2026-11-01 08:01:39 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 07:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:00:44 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:02:21 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:02:17 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:00:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-01 07:00:06 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 07:02:15 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-11-01 07:04:13 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-01 08:01:11 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-01 07:11:52 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:01:41 | Galgamuwa (Mee Oya) | 1.06 | 🟢 Normal | -0.003 |  |
| 2026-11-01 07:05:46 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:02:41 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:02:31 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:02:52 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:01:12 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-11-01 08:00:43 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | -0.014 |  |
| 2026-11-01 07:08:16 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-11-01 08:02:24 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-11-01 08:03:07 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.029 |  |
| 2026-11-01 07:01:45 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.039 |  |
| 2026-11-01 07:02:43 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.041 |  |
| 2026-11-01 07:05:15 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.047 |  |
| 2026-11-01 07:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.55 | 🟢 Normal | -0.084 |  |
| 2026-11-01 07:00:08 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | -0.084 |  |
| 2026-11-01 07:05:12 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.221 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)