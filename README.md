# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_08:10:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,379 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 08:10:43 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 08:10:35 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:10:21 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | -0.009 |  |
| 2026-09-15 08:07:48 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-09-15 08:07:45 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.133 |  |
| 2026-09-15 08:07:35 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:07:22 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-15 08:07:11 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:07:02 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | -0.039 |  |
| 2026-09-15 08:06:55 | Magura (Kalu Ganga) | 5.03 | 🟡 Alert | -0.034 |  |
| 2026-09-15 08:06:13 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.153 |  |
| 2026-09-15 08:06:07 | Baddegama (Gin Ganga) | 2.92 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-15 08:05:15 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.056 |  |
| 2026-09-15 08:04:23 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-09-15 08:04:07 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.126 |  |
| 2026-09-15 08:04:07 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.268 |  |
| 2026-09-15 08:04:04 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-09-15 08:03:43 | Thanthirimale (Malwathu Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 08:03:42 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-15 08:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.69 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-09-15 08:02:35 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:02:33 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-15 08:02:30 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-09-15 08:02:27 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:02:21 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:02:16 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.049 |  |
| 2026-09-15 08:02:16 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-15 08:02:13 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:02:12 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 08:01:52 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.051 |  |
| 2026-09-15 08:01:46 | Manampitiya (Mahaweli Ganga) | -0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:01:34 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:01:22 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-09-15 08:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:00:51 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:35:52 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.007 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 08:02:16 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-15 08:06:55 | Magura (Kalu Ganga) | 5.03 | 🟡 Alert | -0.034 |  |
| 2026-09-15 08:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.69 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-09-15 07:04:19 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-09-15 08:01:22 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-09-15 08:06:07 | Baddegama (Gin Ganga) | 2.92 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-15 08:04:23 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-09-15 07:02:50 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-15 08:02:33 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-15 08:07:22 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-15 08:03:42 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-15 08:10:43 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 08:02:12 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 08:03:43 | Thanthirimale (Malwathu Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 07:35:52 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-09-15 08:10:35 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:01:34 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:02:13 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:07:11 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:07:35 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:02:21 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:00:51 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:01:46 | Manampitiya (Mahaweli Ganga) | -0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:04:17 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 08:10:21 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | -0.009 |  |
| 2026-09-15 08:02:30 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-09-15 08:07:48 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-09-15 08:04:04 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-09-15 08:07:02 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | -0.039 |  |
| 2026-09-15 07:05:15 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-09-15 08:02:16 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.049 |  |
| 2026-09-15 08:01:52 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.051 |  |
| 2026-09-15 08:05:15 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.056 |  |
| 2026-09-15 08:04:07 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.126 |  |
| 2026-09-15 08:07:45 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.133 |  |
| 2026-09-15 08:06:13 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.153 |  |
| 2026-09-15 07:10:03 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.179 |  |
| 2026-09-15 08:04:07 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.268 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)