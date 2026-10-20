# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_21:07:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,411 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 21:07:16 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-10-20 21:06:58 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-10-20 21:06:58 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-10-20 21:06:54 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-20 21:06:18 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -7.200 |  |
| 2026-10-20 21:05:53 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -7.200 |  |
| 2026-10-20 21:05:47 | Thaldena (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.055 |  |
| 2026-10-20 21:05:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:04:53 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.009 |  |
| 2026-10-20 21:04:36 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-20 21:03:55 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-20 21:03:49 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.022 |  |
| 2026-10-20 21:03:16 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 21:02:56 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 21:02:43 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:43 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:42 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.178 |  |
| 2026-10-20 21:02:41 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:40 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | -0.040 |  |
| 2026-10-20 21:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:31 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | -0.023 |  |
| 2026-10-20 21:02:28 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-20 21:02:28 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.075 |  |
| 2026-10-20 21:02:26 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-20 21:02:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:02 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | -0.049 |  |
| 2026-10-20 21:01:29 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-20 21:01:24 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-20 21:01:12 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-20 21:00:52 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.119 |  |
| 2026-10-20 21:00:14 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 20:26:58 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -7.200 |  |
| 2026-10-20 20:26:29 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -7.200 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 21:02:31 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | -0.023 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-20 21:01:29 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-20 21:01:12 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-20 21:06:54 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-20 21:03:55 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-20 21:02:26 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-20 21:02:56 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 21:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 21:03:16 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:43 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:43 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:00:14 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:41 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:05:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:04:53 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.009 |  |
| 2026-10-20 21:06:58 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-10-20 21:01:24 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-20 20:05:54 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-20 21:06:58 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-10-20 21:04:36 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-20 21:02:28 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-20 20:04:52 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-10-20 21:07:16 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-10-20 20:06:02 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.019 |  |
| 2026-10-20 20:05:33 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-10-20 21:03:49 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.022 |  |
| 2026-10-20 20:03:09 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.033 |  |
| 2026-10-20 21:02:40 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | -0.040 |  |
| 2026-10-20 21:02:02 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | -0.049 |  |
| 2026-10-20 21:05:47 | Thaldena (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.055 |  |
| 2026-10-20 21:02:28 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.075 |  |
| 2026-10-20 21:00:52 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.119 |  |
| 2026-10-20 21:02:42 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.178 |  |
| 2026-10-20 21:06:18 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -7.200 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)