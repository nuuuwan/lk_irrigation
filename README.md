# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_10:15:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,759 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 10:15:09 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.076 |  |
| 2026-10-12 10:13:12 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.035 |  |
| 2026-10-12 10:11:10 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-12 10:09:37 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.149 |  |
| 2026-10-12 10:08:50 | Dunamale (Aththanagalu Oya) | 2.81 | 🟢 Normal | -0.018 |  |
| 2026-10-12 10:08:14 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.121 |  |
| 2026-10-12 10:08:03 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-10-12 10:08:02 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | -0.038 |  |
| 2026-10-12 10:07:59 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.118 |  |
| 2026-10-12 10:07:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:07:18 | Panadugama (Nilwala Ganga) | 4.77 | 🟢 Normal | -0.034 |  |
| 2026-10-12 10:05:48 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.048 |  |
| 2026-10-12 10:05:46 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.085 |  |
| 2026-10-12 10:05:44 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | -0.070 |  |
| 2026-10-12 10:05:43 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:04:53 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 10:04:41 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:03:58 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 10:03:54 | Ellagawa (Kalu Ganga) | 7.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 10:03:41 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-10-12 10:03:21 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-10-12 10:03:17 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.090 |  |
| 2026-10-12 10:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:03:06 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.081 |  |
| 2026-10-12 10:02:24 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.000 |  |
| 2026-10-12 10:02:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-12 10:02:13 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.071 |  |
| 2026-10-12 10:02:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:02:07 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-12 10:02:05 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:01:58 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:01:53 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | -0.021 |  |
| 2026-10-12 10:01:47 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:01:32 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-10-12 10:01:29 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-12 10:01:23 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.044 |  |
| 2026-10-12 10:01:03 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-12 10:00:45 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 10:00:16 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 10:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.000 |  |
| 2026-10-12 10:01:03 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-12 10:11:10 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-12 10:02:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-12 10:03:58 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 10:00:45 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 10:03:54 | Ellagawa (Kalu Ganga) | 7.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 10:04:53 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 10:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:01:58 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:02:24 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:02:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:01:47 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:05:43 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:02:05 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:07:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-12 10:08:03 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-10-12 10:03:21 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-10-12 10:02:07 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-12 10:00:16 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-12 10:08:50 | Dunamale (Aththanagalu Oya) | 2.81 | 🟢 Normal | -0.018 |  |
| 2026-10-12 10:01:29 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-12 10:01:32 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-10-12 10:03:41 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-10-12 10:01:53 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | -0.021 |  |
| 2026-10-12 10:07:18 | Panadugama (Nilwala Ganga) | 4.77 | 🟢 Normal | -0.034 |  |
| 2026-10-12 10:13:12 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.035 |  |
| 2026-10-12 10:08:02 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | -0.038 |  |
| 2026-10-12 10:01:23 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.044 |  |
| 2026-10-12 10:05:48 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.048 |  |
| 2026-10-12 10:05:44 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | -0.070 |  |
| 2026-10-12 10:02:13 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.071 |  |
| 2026-10-12 10:15:09 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.076 |  |
| 2026-10-12 10:03:06 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.081 |  |
| 2026-10-12 10:05:46 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.085 |  |
| 2026-10-12 10:03:17 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.090 |  |
| 2026-10-12 10:07:59 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.118 |  |
| 2026-10-12 10:08:14 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.121 |  |
| 2026-10-12 10:09:37 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)