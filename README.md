# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_11:08:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,207 measurements** from **39** stations.
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
| 2026-10-08 11:08:44 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-10-08 11:08:35 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 11:07:53 | Dunamale (Aththanagalu Oya) | 2.87 | 🟢 Normal | -0.055 |  |
| 2026-10-08 11:07:24 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | -0.046 |  |
| 2026-10-08 11:06:47 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.106 |  |
| 2026-10-08 11:06:26 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:06:08 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.132 |  |
| 2026-10-08 11:05:35 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.019 |  |
| 2026-10-08 11:05:35 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.013 |  |
| 2026-10-08 11:04:58 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:04:58 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.074 |  |
| 2026-10-08 11:04:20 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.092 |  |
| 2026-10-08 11:03:54 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 11:03:06 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.039 |  |
| 2026-10-08 11:02:48 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.205 |  |
| 2026-10-08 11:02:48 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.022 |  |
| 2026-10-08 11:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.020 |  |
| 2026-10-08 11:02:42 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 11:02:41 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.031 |  |
| 2026-10-08 11:02:39 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 11:02:35 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.050 |  |
| 2026-10-08 11:02:35 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-08 11:02:19 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-10-08 11:02:16 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-10-08 11:02:13 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 11:02:05 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:01:54 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:01:46 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-08 11:01:43 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:01:35 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:01:23 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-08 11:01:09 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:00:56 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:00:40 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.032 |  |
| 2026-10-08 11:00:29 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-08 11:00:24 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-10-08 10:34:03 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-10-08 10:28:33 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 11:02:16 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-10-08 11:00:24 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-10-08 11:00:29 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-08 10:06:40 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-08 11:02:42 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 11:02:13 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 11:02:39 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 11:03:54 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 11:08:35 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 11:01:23 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:00:56 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:01:43 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:02:05 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:06:26 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:01:35 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:04:58 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:01:54 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:01:09 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-08 11:08:44 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-10-08 11:01:46 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-08 11:02:35 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-08 11:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-08 11:05:35 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.013 |  |
| 2026-10-08 10:22:12 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.017 |  |
| 2026-10-08 11:05:35 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.019 |  |
| 2026-10-08 11:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.020 |  |
| 2026-10-08 11:02:19 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-10-08 11:02:48 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.022 |  |
| 2026-10-08 11:02:41 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.031 |  |
| 2026-10-08 11:00:40 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.032 |  |
| 2026-10-08 11:03:06 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.039 |  |
| 2026-10-08 11:07:24 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | -0.046 |  |
| 2026-10-08 11:02:35 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.050 |  |
| 2026-10-08 11:07:53 | Dunamale (Aththanagalu Oya) | 2.87 | 🟢 Normal | -0.055 |  |
| 2026-10-08 11:04:58 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.074 |  |
| 2026-10-08 11:04:20 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.092 |  |
| 2026-10-08 11:06:47 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.106 |  |
| 2026-10-08 11:06:08 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.132 |  |
| 2026-10-08 11:02:48 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)