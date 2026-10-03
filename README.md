# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_09:12:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,620 measurements** from **39** stations.
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
| 2026-10-03 09:12:05 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-10-03 09:11:01 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.018 |  |
| 2026-10-03 09:09:52 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.072 |  |
| 2026-10-03 09:09:20 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.092 |  |
| 2026-10-03 09:08:03 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.027 |  |
| 2026-10-03 09:08:01 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:07:36 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -7.294 |  |
| 2026-10-03 09:07:34 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-03 09:07:01 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-10-03 09:06:09 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.042 |  |
| 2026-10-03 09:05:22 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 09:04:59 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-03 09:04:04 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:03:57 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:03:56 | Ellagawa (Kalu Ganga) | 6.52 | 🟢 Normal | -0.021 |  |
| 2026-10-03 09:03:45 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:03:34 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 09:03:29 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:03:16 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.030 |  |
| 2026-10-03 09:03:12 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.034 |  |
| 2026-10-03 09:03:11 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:03:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:03:03 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:02:43 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.094 |  |
| 2026-10-03 09:02:34 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:02:19 | Siyambalanduwa (Heda Oya) | 0.29 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-03 09:02:05 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-10-03 09:02:02 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-10-03 09:01:55 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:01:51 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:01:43 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:01:37 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.023 |  |
| 2026-10-03 09:01:34 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-03 09:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:01:15 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:01:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:00:43 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.030 |  |
| 2026-10-03 09:00:30 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 09:02:19 | Siyambalanduwa (Heda Oya) | 0.29 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-03 09:01:34 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-03 09:07:34 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-03 09:05:22 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 09:04:59 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-03 09:03:34 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 09:01:43 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:01:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:01:15 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:03:45 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:02:34 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:03:03 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:03:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:03:11 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:01:51 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:00:30 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 09:12:05 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-10-03 09:03:57 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:01:55 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:03:29 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:08:01 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:04:04 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-03 09:11:01 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.018 |  |
| 2026-10-03 09:02:05 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-10-03 09:03:56 | Ellagawa (Kalu Ganga) | 6.52 | 🟢 Normal | -0.021 |  |
| 2026-10-03 09:01:37 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.023 |  |
| 2026-10-03 09:08:03 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.027 |  |
| 2026-10-03 09:07:01 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-10-03 09:03:16 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.030 |  |
| 2026-10-03 09:00:43 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.030 |  |
| 2026-10-03 09:02:02 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-10-03 09:03:12 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.034 |  |
| 2026-10-03 09:06:09 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.042 |  |
| 2026-10-03 09:09:52 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.072 |  |
| 2026-10-03 09:09:20 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.092 |  |
| 2026-10-03 09:02:43 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.094 |  |
| 2026-10-03 09:07:36 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -7.294 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)