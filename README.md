# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_20:15:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,345 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 20:15:07 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.017 |  |
| 2026-10-10 20:12:21 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-10 20:10:06 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-10 20:09:44 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | -0.017 |  |
| 2026-10-10 20:07:57 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-10 20:07:56 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-10 20:07:06 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.942 | 🔺 Rising |
| 2026-10-10 20:06:51 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.044 |  |
| 2026-10-10 20:06:43 | Giriulla (Maha Oya) | 3.01 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-10 20:06:11 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.059 |  |
| 2026-10-10 20:05:55 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -0.040 |  |
| 2026-10-10 20:05:39 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-10-10 20:05:29 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-10 20:04:59 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:04:44 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.074 |  |
| 2026-10-10 20:04:42 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-10 20:04:24 | Moragaswewa (Deduru Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:04:13 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:03:48 | Norwood (Kelani Ganga) | 1.72 | 🟡 Alert | 0.695 | 🔺 Rising |
| 2026-10-10 20:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-10 20:03:21 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.088 |  |
| 2026-10-10 20:03:10 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-10 20:03:08 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:02:39 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 20:02:34 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.134 |  |
| 2026-10-10 20:02:29 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.079 |  |
| 2026-10-10 20:02:15 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | -0.072 |  |
| 2026-10-10 20:02:11 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:02:11 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:01:41 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:01:36 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-10 20:01:31 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.024 |  |
| 2026-10-10 20:01:20 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-10 20:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.005 |  |
| 2026-10-10 20:01:14 | Moragaswewa (Deduru Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:00:50 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 20:00:35 | Thawalama (Gin Ganga) | 2.62 | 🟢 Normal | 0.079 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 20:03:48 | Norwood (Kelani Ganga) | 1.72 | 🟡 Alert | 0.695 | 🔺 Rising |
| 2026-10-10 20:07:06 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.942 | 🔺 Rising |
| 2026-10-10 20:03:10 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-10 20:07:56 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-10 20:07:57 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-10 20:04:42 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-10 20:00:35 | Thawalama (Gin Ganga) | 2.62 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-10 20:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-10 20:05:29 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-10 20:06:43 | Giriulla (Maha Oya) | 3.01 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-10 20:01:36 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-10 20:01:20 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-10 20:12:21 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-10 20:00:50 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 20:02:39 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 20:04:24 | Moragaswewa (Deduru Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:01:41 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:02:11 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:26 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:04:59 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:02:11 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:04:13 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:03:08 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:00:50 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-10 20:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.005 |  |
| 2026-10-10 20:10:06 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-10 20:15:07 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.017 |  |
| 2026-10-10 20:09:44 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | -0.017 |  |
| 2026-10-10 20:05:39 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-10-10 20:01:31 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.024 |  |
| 2026-10-10 20:05:55 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -0.040 |  |
| 2026-10-10 20:06:51 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.044 |  |
| 2026-10-10 18:05:26 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.050 |  |
| 2026-10-10 20:06:11 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.059 |  |
| 2026-10-10 20:02:15 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | -0.072 |  |
| 2026-10-10 20:04:44 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.074 |  |
| 2026-10-10 20:02:29 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.079 |  |
| 2026-10-10 20:03:21 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.088 |  |
| 2026-10-10 20:02:34 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)