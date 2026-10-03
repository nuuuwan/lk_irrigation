# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_10:19:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,658 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 10:19:44 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | -0.043 |  |
| 2026-10-03 10:14:19 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.102 |  |
| 2026-10-03 10:06:54 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-10-03 10:06:53 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.105 |  |
| 2026-10-03 10:06:04 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 10:06:02 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:05:59 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:04:57 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | -0.061 |  |
| 2026-10-03 10:04:45 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.077 |  |
| 2026-10-03 10:04:35 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.038 |  |
| 2026-10-03 10:04:33 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.032 |  |
| 2026-10-03 10:04:21 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 10:04:04 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-10-03 10:04:02 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | -0.050 |  |
| 2026-10-03 10:03:52 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-03 10:03:49 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.153 |  |
| 2026-10-03 10:03:23 | Hanwella (Kelani Ganga) | 2.41 | 🟢 Normal | -0.030 |  |
| 2026-10-03 10:03:20 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:03:16 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-10-03 10:02:56 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:02:37 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-10-03 10:02:32 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:02:17 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:02:05 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:01:50 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:01:45 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 10:01:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:01:33 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:01:33 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:01:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:01:11 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.050 |  |
| 2026-10-03 10:01:10 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-03 10:01:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-03 10:00:29 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:00:23 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 10:01:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-03 10:01:10 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-03 10:01:45 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 10:04:21 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 10:06:04 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 10:02:56 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:00:29 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:02:05 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:01:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:01:33 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:02:17 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:03:20 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:05:59 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:01:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:01:33 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:06:02 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:00:23 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:02:32 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:01:50 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 10:06:54 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-10-03 10:03:52 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-03 10:02:37 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:11:01 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.018 |  |
| 2026-10-03 10:03:16 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-10-03 10:04:04 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-10-03 10:03:23 | Hanwella (Kelani Ganga) | 2.41 | 🟢 Normal | -0.030 |  |
| 2026-10-03 10:04:33 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.032 |  |
| 2026-10-03 10:04:35 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.038 |  |
| 2026-10-03 10:19:44 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | -0.043 |  |
| 2026-10-03 10:01:11 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.050 |  |
| 2026-10-03 10:04:02 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | -0.050 |  |
| 2026-10-03 10:04:57 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | -0.061 |  |
| 2026-10-03 10:04:45 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.077 |  |
| 2026-10-03 09:02:43 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.094 |  |
| 2026-10-03 10:14:19 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.102 |  |
| 2026-10-03 10:06:53 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.105 |  |
| 2026-10-03 10:03:49 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)