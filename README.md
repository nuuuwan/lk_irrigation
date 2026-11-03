# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_15:02:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,787 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 15:02:53 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.029 |  |
| 2026-11-03 15:02:46 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 15:02:40 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.088 |  |
| 2026-11-03 15:02:40 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-03 15:02:40 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-11-03 15:02:39 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | -0.022 |  |
| 2026-11-03 15:02:24 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.044 |  |
| 2026-11-03 15:02:21 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-03 15:02:16 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-11-03 15:01:48 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-03 15:01:45 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | -0.021 |  |
| 2026-11-03 15:01:24 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-03 15:01:20 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 15:00:30 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 15:00:12 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 14:02:16 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-03 15:02:40 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-03 14:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-03 14:03:41 | Moragaswewa (Deduru Oya) | 4.26 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-03 14:09:52 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-03 15:00:12 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-03 15:02:46 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 14:09:05 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 15:01:20 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 15:02:21 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-03 15:00:30 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 14:03:59 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-03 14:02:41 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 15:01:24 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-03 14:01:35 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-03 14:03:12 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-03 14:04:40 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-11-03 14:16:37 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.011 |  |
| 2026-11-03 15:01:48 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-03 15:02:16 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-11-03 15:02:40 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-11-03 15:01:45 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | -0.021 |  |
| 2026-11-03 14:03:50 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.022 |  |
| 2026-11-03 15:02:39 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | -0.022 |  |
| 2026-11-03 14:03:45 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.024 |  |
| 2026-11-03 14:06:26 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-11-03 15:02:53 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.029 |  |
| 2026-11-03 14:05:22 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-11-03 14:02:51 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.039 |  |
| 2026-11-03 14:02:56 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.040 |  |
| 2026-11-03 15:02:24 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.044 |  |
| 2026-11-03 14:05:20 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | -0.051 |  |
| 2026-11-03 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.81 | 🟢 Normal | -0.051 |  |
| 2026-11-03 14:02:51 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.059 |  |
| 2026-11-03 14:08:19 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.086 |  |
| 2026-11-03 15:02:40 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.088 |  |
| 2026-11-03 14:08:10 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.097 |  |
| 2026-11-03 14:03:43 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.100 |  |
| 2026-11-03 14:03:27 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)