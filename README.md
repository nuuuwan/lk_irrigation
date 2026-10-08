# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_22:34:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,627 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 22:34:35 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.013 |  |
| 2026-10-08 22:18:02 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-08 22:13:13 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-08 22:07:19 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:07:02 | Rathnapura (Kalu Ganga) | 3.76 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-10-08 22:05:58 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-08 22:05:58 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-08 22:05:50 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.039 |  |
| 2026-10-08 22:05:36 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:05:35 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-08 22:05:09 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-08 22:05:09 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-08 22:05:02 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.019 |  |
| 2026-10-08 22:04:04 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-08 22:03:59 | Thawalama (Gin Ganga) | 3.59 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-08 22:03:51 | Holombuwa (Kelani Ganga) | 3.74 | 🟠 Minor Flood | -0.488 |  |
| 2026-10-08 22:03:50 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:03:16 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 22:02:56 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-08 22:02:54 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-10-08 22:02:46 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-08 22:02:36 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-08 22:02:26 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 22:02:10 | Glencourse (Kelani Ganga) | 12.07 | 🟢 Normal | 0.515 | 🔺 Rising |
| 2026-10-08 22:02:06 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:02:00 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 22:01:56 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-08 22:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:01:41 | Giriulla (Maha Oya) | 3.68 | 🟢 Normal | 0.742 | 🔺 Rising |
| 2026-10-08 22:01:27 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 22:01:09 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-10-08 22:01:02 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:00:43 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 22:00:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | 0.055 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 22:03:51 | Holombuwa (Kelani Ganga) | 3.74 | 🟠 Minor Flood | -0.488 |  |
| 2026-10-08 22:01:41 | Giriulla (Maha Oya) | 3.68 | 🟢 Normal | 0.742 | 🔺 Rising |
| 2026-10-08 22:02:10 | Glencourse (Kelani Ganga) | 12.07 | 🟢 Normal | 0.515 | 🔺 Rising |
| 2026-10-08 22:07:02 | Rathnapura (Kalu Ganga) | 3.76 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-10-08 22:03:59 | Thawalama (Gin Ganga) | 3.59 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-08 22:02:56 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-08 22:13:13 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-08 22:05:09 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-08 22:05:35 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-08 22:18:02 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-08 22:05:09 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-08 22:00:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-08 22:02:46 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-08 22:02:36 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-08 22:01:56 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-08 22:05:58 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-08 22:05:58 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-08 21:00:42 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 22:01:27 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 22:02:26 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 22:00:43 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 22:02:00 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 22:03:16 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:02:06 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:01:02 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:05:36 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:03:50 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:07:19 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 22:04:04 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-08 22:01:09 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-10-08 22:34:35 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.013 |  |
| 2026-10-08 22:05:02 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.019 |  |
| 2026-10-08 22:02:54 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-10-08 21:08:53 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-10-08 22:05:50 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)