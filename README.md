# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_15:14:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,057 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 15:14:40 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.084 |  |
| 2026-10-11 15:09:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:07:52 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.028 |  |
| 2026-10-11 15:07:44 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.048 |  |
| 2026-10-11 15:07:23 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:07:19 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:07:13 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.040 |  |
| 2026-10-11 15:07:12 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.018 |  |
| 2026-10-11 15:07:03 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:06:51 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-11 15:06:41 | Moragaswewa (Deduru Oya) | 2.50 | 🟢 Normal | -0.129 |  |
| 2026-10-11 15:06:37 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.096 |  |
| 2026-10-11 15:06:26 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-10-11 15:06:23 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:06:21 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.257 |  |
| 2026-10-11 15:05:59 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:05:50 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-11 15:05:45 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:05:09 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-11 15:04:25 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 15:04:24 | Badalgama (Maha Oya) | 3.54 | 🟢 Normal | -0.070 |  |
| 2026-10-11 15:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | -0.042 |  |
| 2026-10-11 15:03:53 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | -0.072 |  |
| 2026-10-11 15:03:49 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.019 |  |
| 2026-10-11 15:03:44 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.057 |  |
| 2026-10-11 15:03:43 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-10-11 15:03:41 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.039 |  |
| 2026-10-11 15:03:20 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.031 |  |
| 2026-10-11 15:03:15 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-10-11 15:02:55 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-10-11 15:02:48 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-10-11 15:02:40 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-11 15:02:20 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-10-11 15:02:18 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:02:11 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.033 |  |
| 2026-10-11 15:02:04 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.345 | 🔺 Rising |
| 2026-10-11 15:01:55 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-11 15:01:53 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-10-11 15:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-11 15:01:04 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 15:03:15 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-10-11 15:02:04 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.345 | 🔺 Rising |
| 2026-10-11 15:02:40 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-11 15:05:50 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-11 15:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-11 15:01:04 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 15:04:25 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 15:07:23 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:02:18 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:06:23 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:07:19 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:09:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:05:45 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:05:59 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:07:03 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-11 15:06:51 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-11 15:02:48 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-10-11 15:01:55 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-11 15:07:12 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.018 |  |
| 2026-10-11 15:03:49 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.019 |  |
| 2026-10-11 15:06:26 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-10-11 15:02:20 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-10-11 15:05:09 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-11 15:01:53 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-10-11 15:07:52 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.028 |  |
| 2026-10-11 15:03:43 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-10-11 15:03:20 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.031 |  |
| 2026-10-11 15:02:11 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.033 |  |
| 2026-10-11 15:03:41 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.039 |  |
| 2026-10-11 15:07:13 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.040 |  |
| 2026-10-11 15:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | -0.042 |  |
| 2026-10-11 15:07:44 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.048 |  |
| 2026-10-11 15:03:44 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.057 |  |
| 2026-10-11 15:04:24 | Badalgama (Maha Oya) | 3.54 | 🟢 Normal | -0.070 |  |
| 2026-10-11 15:03:53 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | -0.072 |  |
| 2026-10-11 15:14:40 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.084 |  |
| 2026-10-11 15:06:37 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.096 |  |
| 2026-10-11 15:06:41 | Moragaswewa (Deduru Oya) | 2.50 | 🟢 Normal | -0.129 |  |
| 2026-10-11 15:06:21 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.257 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)