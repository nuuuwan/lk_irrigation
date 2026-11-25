# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_15:15:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,427 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 15:15:51 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.018 |  |
| 2026-11-25 15:13:26 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.047 |  |
| 2026-11-25 15:12:15 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-25 15:08:34 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.019 |  |
| 2026-11-25 15:07:12 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-25 15:06:25 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.038 |  |
| 2026-11-25 15:06:00 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.180 |  |
| 2026-11-25 15:05:48 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-25 15:05:44 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-25 15:05:28 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-25 15:05:11 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | -0.020 |  |
| 2026-11-25 15:04:34 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -2.118 |  |
| 2026-11-25 15:04:32 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:04:30 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 15:04:28 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-11-25 15:04:26 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 15:04:19 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:04:02 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:04:00 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -2.118 |  |
| 2026-11-25 15:03:53 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-11-25 15:03:31 | Moraketiya (Walawe Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:03:27 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-11-25 15:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.73 | 🟢 Normal | -0.053 |  |
| 2026-11-25 15:03:10 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | -0.040 |  |
| 2026-11-25 15:03:06 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.058 |  |
| 2026-11-25 15:03:03 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-11-25 15:02:54 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.100 |  |
| 2026-11-25 15:02:41 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 15:02:20 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:02:03 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-25 15:01:49 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-11-25 15:01:46 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:01:46 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.124 |  |
| 2026-11-25 15:01:39 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 15:01:34 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:01:34 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.080 |  |
| 2026-11-25 15:01:29 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 15:01:01 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.678 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 15:01:01 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.678 | 🔺 Rising |
| 2026-11-25 15:02:03 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-25 15:07:12 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-25 15:05:44 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-25 15:01:29 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 15:02:41 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 15:05:48 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-25 15:04:30 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 15:01:39 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 15:04:26 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 15:12:15 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-25 15:05:28 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-25 15:01:46 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:02:20 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:03:31 | Moraketiya (Walawe Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:04:19 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:04:32 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:01:34 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-25 14:14:40 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-25 15:03:27 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-11-25 15:15:51 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.018 |  |
| 2026-11-25 15:08:34 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.019 |  |
| 2026-11-25 15:03:53 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-11-25 15:05:11 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | -0.020 |  |
| 2026-11-25 14:05:03 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-11-25 15:04:28 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-11-25 15:01:49 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 15:03:03 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-11-25 15:06:25 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.038 |  |
| 2026-11-25 15:03:10 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | -0.040 |  |
| 2026-11-25 15:13:26 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.047 |  |
| 2026-11-25 15:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.73 | 🟢 Normal | -0.053 |  |
| 2026-11-25 15:03:06 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.058 |  |
| 2026-11-25 15:01:34 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.080 |  |
| 2026-11-25 15:02:54 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.100 |  |
| 2026-11-25 15:01:46 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.124 |  |
| 2026-11-25 15:06:00 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.180 |  |
| 2026-11-25 15:04:34 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -2.118 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)