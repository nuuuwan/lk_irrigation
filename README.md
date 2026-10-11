# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_13:15:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,978 measurements** from **39** stations.
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
| 2026-10-11 13:15:38 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:12:53 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.063 |  |
| 2026-10-11 13:11:14 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-10-11 13:09:45 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.009 |  |
| 2026-10-11 13:09:13 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.091 |  |
| 2026-10-11 13:09:01 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | -0.051 |  |
| 2026-10-11 13:07:45 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:06:28 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.019 |  |
| 2026-10-11 13:06:27 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.217 |  |
| 2026-10-11 13:06:14 | Nagalagam Street (Kelani Ganga) | 0.72 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-11 13:06:11 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:05:58 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.039 |  |
| 2026-10-11 13:05:51 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-10-11 13:05:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | -0.019 |  |
| 2026-10-11 13:05:40 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-10-11 13:05:21 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.071 |  |
| 2026-10-11 13:04:49 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:04:48 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:04:34 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-11 13:04:25 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:04:21 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:04:07 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.021 |  |
| 2026-10-11 13:03:20 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | -0.031 |  |
| 2026-10-11 13:03:17 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-11 13:03:11 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.050 |  |
| 2026-10-11 13:03:07 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.039 |  |
| 2026-10-11 13:03:05 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.092 |  |
| 2026-10-11 13:02:58 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:02:11 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-11 13:02:09 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.250 |  |
| 2026-10-11 13:02:06 | Ellagawa (Kalu Ganga) | 6.54 | 🟢 Normal | -0.020 |  |
| 2026-10-11 13:02:02 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:01:58 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:01:57 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 13:06:14 | Nagalagam Street (Kelani Ganga) | 0.72 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-11 13:02:11 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-11 13:04:49 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:02:02 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:01:03 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:07:45 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:01:27 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:01:58 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:00:13 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:02:58 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:06:11 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:04:48 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:15:38 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:04:25 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:09:45 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.009 |  |
| 2026-10-11 13:04:34 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-11 13:03:17 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-11 13:00:36 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.011 |  |
| 2026-10-11 13:05:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | -0.019 |  |
| 2026-10-11 13:06:28 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.019 |  |
| 2026-10-11 13:11:14 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-10-11 13:00:23 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-10-11 13:02:06 | Ellagawa (Kalu Ganga) | 6.54 | 🟢 Normal | -0.020 |  |
| 2026-10-11 13:05:51 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-10-11 13:04:07 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.021 |  |
| 2026-10-11 13:05:40 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-10-11 13:03:20 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | -0.031 |  |
| 2026-10-11 13:05:58 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.039 |  |
| 2026-10-11 13:03:07 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.039 |  |
| 2026-10-11 13:00:23 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.042 |  |
| 2026-10-11 13:03:11 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.050 |  |
| 2026-10-11 13:09:01 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | -0.051 |  |
| 2026-10-11 13:12:53 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.063 |  |
| 2026-10-11 13:05:21 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.071 |  |
| 2026-10-11 13:09:13 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.091 |  |
| 2026-10-11 13:03:05 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.092 |  |
| 2026-10-11 13:06:27 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.217 |  |
| 2026-10-11 13:02:09 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.250 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)