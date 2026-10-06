# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_20:20:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,762 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 20:20:15 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-06 20:07:20 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-06 20:07:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.062 |  |
| 2026-10-06 20:07:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-06 20:06:49 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:06:38 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-06 20:06:06 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-06 20:06:05 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | -0.101 |  |
| 2026-10-06 20:05:33 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:05:30 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.057 |  |
| 2026-10-06 20:05:10 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-10-06 20:05:02 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 20:04:57 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-10-06 20:04:57 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-06 20:04:55 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-10-06 20:04:50 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:04:32 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.039 |  |
| 2026-10-06 20:04:18 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:04:02 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.079 |  |
| 2026-10-06 20:03:50 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-10-06 20:03:35 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-10-06 20:03:26 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-10-06 20:02:48 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:02:37 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:02:35 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.033 |  |
| 2026-10-06 20:02:29 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-06 20:02:29 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.060 |  |
| 2026-10-06 20:02:16 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:02:11 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-06 20:02:08 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:02:07 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-06 20:01:48 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-06 20:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:01:09 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 20:00:11 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 20:05:10 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-10-06 20:03:50 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-10-06 20:07:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-06 20:04:57 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-06 20:02:11 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-06 20:02:29 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-06 20:06:06 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-06 20:05:02 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 20:01:09 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 20:07:20 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-06 20:20:15 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-06 20:06:49 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:05:33 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-06 19:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:00:11 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:04:18 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:04:50 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:02:16 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:02:48 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:02:37 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:02:08 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-06 20:02:07 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-06 20:06:38 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-06 20:01:48 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:01:43 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.011 |  |
| 2026-10-06 20:04:57 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-10-06 20:03:35 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-10-06 20:03:26 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-10-06 20:04:55 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-10-06 20:02:35 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.033 |  |
| 2026-10-06 20:04:32 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.039 |  |
| 2026-10-06 20:05:30 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.057 |  |
| 2026-10-06 20:02:29 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.060 |  |
| 2026-10-06 20:07:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.062 |  |
| 2026-10-06 20:04:02 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.079 |  |
| 2026-10-06 20:06:05 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)