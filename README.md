# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_08:15:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,744 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 08:15:27 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:15:09 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-17 08:12:54 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-08-17 08:11:55 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:10:51 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-17 08:09:51 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.026 |  |
| 2026-08-17 08:08:36 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 08:07:03 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 08:06:02 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:05:17 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-17 08:04:58 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:04:53 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:04:37 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:04:21 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.094 |  |
| 2026-08-17 08:04:17 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-08-17 08:04:10 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-08-17 08:03:50 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 08:03:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:03:47 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:03:45 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-08-17 08:03:35 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:03:26 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | -0.022 |  |
| 2026-08-17 08:03:22 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:03:19 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:02:52 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 08:02:30 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 08:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.060 |  |
| 2026-08-17 08:02:13 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:02:13 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:02:05 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:01:40 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.031 |  |
| 2026-08-17 08:01:25 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:01:08 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:00:56 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.035 |  |
| 2026-08-17 08:00:36 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:00:10 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.031 |  |
| 2026-08-17 08:00:09 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:47:09 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.026 |  |
| 2026-08-17 07:43:40 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-08-17 07:33:19 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 08:04:10 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-08-17 08:15:09 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-17 08:08:36 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 08:07:03 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 08:05:17 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-17 08:02:30 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 08:02:52 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 08:03:50 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 08:03:35 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:00:09 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:00:36 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:03:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:03:47 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:01:12 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:04:58 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:04:37 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:11:55 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:03:22 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:02:05 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:01:08 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:03:19 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:02:13 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:15:27 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:04:53 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:06:02 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:01:25 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:02:13 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:10:51 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-17 08:04:17 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-08-17 08:03:45 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-08-17 08:03:26 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | -0.022 |  |
| 2026-08-17 08:09:51 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.026 |  |
| 2026-08-17 08:00:10 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.031 |  |
| 2026-08-17 08:01:40 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.031 |  |
| 2026-08-17 08:00:56 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.035 |  |
| 2026-08-17 08:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.060 |  |
| 2026-08-17 08:12:54 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-08-17 08:04:21 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)