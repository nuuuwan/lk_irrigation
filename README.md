# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_09:21:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,820 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 09:21:29 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:10:25 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.027 |  |
| 2026-08-26 09:09:48 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:09:11 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-26 09:08:14 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:07:37 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-26 09:06:54 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:06:33 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 09:06:26 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-26 09:06:26 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-08-26 09:06:05 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:05:54 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:05:52 | Nagalagam Street (Kelani Ganga) | 0.26 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-26 09:05:11 | Rathnapura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.062 |  |
| 2026-08-26 09:05:10 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2026-08-26 09:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-26 09:04:17 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-08-26 09:04:14 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-26 09:04:01 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.074 |  |
| 2026-08-26 09:03:13 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 09:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-08-26 09:03:08 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:02:52 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-08-26 09:02:50 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:02:39 | Ellagawa (Kalu Ganga) | 6.58 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-26 09:02:34 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.023 |  |
| 2026-08-26 09:02:27 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-08-26 09:02:26 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.069 |  |
| 2026-08-26 09:02:19 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-26 09:02:14 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:02:14 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.234 |  |
| 2026-08-26 09:02:10 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:02:01 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:01:24 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:01:23 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:01:17 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:01:15 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 09:00:52 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.011 |  |
| 2026-08-26 09:00:43 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 09:04:17 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-08-26 09:02:39 | Ellagawa (Kalu Ganga) | 6.58 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-26 09:05:52 | Nagalagam Street (Kelani Ganga) | 0.26 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-26 09:04:14 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-26 09:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-26 09:07:37 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-26 09:09:11 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-26 09:06:26 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-26 09:02:19 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-26 09:03:13 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 09:01:15 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 09:06:33 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 09:02:01 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:00:43 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:03:08 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:01:24 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:06:05 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:21:29 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:03:06 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:02:10 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:05:54 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:08:14 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:02:14 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:01:23 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:06:54 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:01:17 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:02:50 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-26 09:06:26 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-08-26 09:00:52 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.011 |  |
| 2026-08-26 09:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-08-26 09:02:52 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-08-26 09:02:34 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.023 |  |
| 2026-08-26 09:10:25 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.027 |  |
| 2026-08-26 09:02:27 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-08-26 09:05:10 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2026-08-26 09:05:11 | Rathnapura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.062 |  |
| 2026-08-26 09:02:26 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.069 |  |
| 2026-08-26 09:04:01 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.074 |  |
| 2026-08-26 09:02:14 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)