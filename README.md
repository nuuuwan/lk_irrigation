# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_14:03:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,499 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 14:03:41 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:03:29 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-24 14:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | -0.101 |  |
| 2026-11-24 14:03:12 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-24 14:03:07 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-24 14:02:39 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:02:37 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-24 14:02:36 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | -0.091 |  |
| 2026-11-24 14:02:22 | Badalgama (Maha Oya) | 3.86 | 🟢 Normal | -0.121 |  |
| 2026-11-24 14:02:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:02:17 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.122 |  |
| 2026-11-24 14:02:12 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-24 14:01:46 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-24 14:01:45 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:01:43 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 14:01:40 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-11-24 14:01:23 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.044 |  |
| 2026-11-24 14:01:18 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-24 14:01:05 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.139 |  |
| 2026-11-24 14:00:42 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 13:28:45 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-24 13:19:26 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.016 |  |
| 2026-11-24 13:16:52 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-24 13:16:50 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.040 |  |
| 2026-11-24 13:16:13 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-24 13:15:50 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-24 13:14:09 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 13:01:22 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-24 14:01:46 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-24 14:01:18 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-24 14:01:43 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 13:28:45 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-24 13:04:59 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-24 14:03:07 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-24 14:03:12 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-24 13:03:12 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 13:04:34 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:03:41 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 13:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:01:45 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 13:08:28 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-24 13:16:13 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:02:39 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:00:42 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:02:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 13:11:48 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.009 |  |
| 2026-11-24 13:10:35 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.009 |  |
| 2026-11-24 13:03:57 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-24 13:02:00 | Moraketiya (Walawe Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-11-24 14:02:37 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-24 13:19:26 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.016 |  |
| 2026-11-24 13:12:07 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.018 |  |
| 2026-11-24 13:06:05 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.019 |  |
| 2026-11-24 13:03:13 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.020 |  |
| 2026-11-24 14:03:29 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-24 14:02:12 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 13:05:41 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | -0.029 |  |
| 2026-11-24 14:01:40 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-11-24 14:01:23 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.044 |  |
| 2026-11-24 14:02:36 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | -0.091 |  |
| 2026-11-24 14:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | -0.101 |  |
| 2026-11-24 14:02:22 | Badalgama (Maha Oya) | 3.86 | 🟢 Normal | -0.121 |  |
| 2026-11-24 14:02:17 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.122 |  |
| 2026-11-24 14:01:05 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.139 |  |
| 2026-11-24 13:03:09 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)