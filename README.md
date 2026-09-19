# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_04:02:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,698 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 04:02:46 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-20 04:02:42 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:02:20 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.003 |  |
| 2026-09-20 04:02:16 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 04:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 04:02:04 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:01:58 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-20 04:01:50 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:01:48 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.197 |  |
| 2026-09-20 04:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:01:18 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:00:52 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 04:00:34 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | 0.324 | 🔺 Rising |
| 2026-09-20 03:45:44 | Magura (Kalu Ganga) | 3.97 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-09-20 03:41:16 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 04:00:34 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | 0.324 | 🔺 Rising |
| 2026-09-20 03:04:36 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-09-20 04:02:46 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-20 03:06:51 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-20 03:09:39 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-20 03:08:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-20 03:06:25 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-20 03:13:45 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-20 03:02:56 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-20 02:02:16 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-20 03:03:29 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 04:02:16 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 03:04:08 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 04:01:58 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-20 04:00:52 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 04:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 03:01:42 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 03:02:24 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:55 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-20 03:03:40 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 03:01:49 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-20 03:03:06 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:02:04 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:02:42 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:39 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-20 03:02:42 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:01:18 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:01:50 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:02:20 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.003 |  |
| 2026-09-20 03:05:54 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.009 |  |
| 2026-09-19 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-20 03:04:47 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-09-20 03:02:00 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-09-20 03:41:16 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.013 |  |
| 2026-09-20 03:07:45 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | -0.019 |  |
| 2026-09-20 03:05:41 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.021 |  |
| 2026-09-20 03:02:10 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.052 |  |
| 2026-09-20 04:01:48 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)