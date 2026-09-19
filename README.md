# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_02:03:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,626 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 02:03:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:02:50 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-20 02:02:48 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 02:02:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:02:16 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-20 02:02:12 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.021 |  |
| 2026-09-20 02:01:53 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 02:01:48 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 02:01:46 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:01:44 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:01:25 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:00:45 | Magura (Kalu Ganga) | 3.92 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-09-20 01:38:15 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-20 01:24:30 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.015 |  |
| 2026-09-20 01:22:36 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 01:16:26 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 01:06:34 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-09-20 01:01:37 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-09-20 01:01:55 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-09-20 01:07:22 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-09-20 02:00:45 | Magura (Kalu Ganga) | 3.92 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-09-20 02:02:48 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 01:04:20 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-20 02:02:16 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-20 02:01:53 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 01:01:22 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 01:16:26 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 01:08:21 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-20 01:02:59 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 02:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 01:00:30 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:01:25 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:01:48 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:04:33 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:55 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:03:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:01:46 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-20 01:12:48 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 01:04:31 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-20 02:02:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 01:03:59 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:39 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-20 01:10:40 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 01:11:43 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-20 02:02:50 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-20 01:24:30 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.015 |  |
| 2026-09-20 02:02:12 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.021 |  |
| 2026-09-20 00:06:05 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.029 |  |
| 2026-09-20 00:04:09 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.041 |  |
| 2026-09-20 01:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.041 |  |
| 2026-09-20 00:16:15 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.049 |  |
| 2026-09-20 01:02:47 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.050 |  |
| 2026-09-20 01:04:20 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)