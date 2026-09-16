# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_08:08:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,274 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 08:08:32 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | -0.019 |  |
| 2026-09-16 08:08:12 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:07:31 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 08:07:25 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:07:11 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.070 |  |
| 2026-09-16 08:06:53 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-09-16 08:05:53 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.031 |  |
| 2026-09-16 08:05:42 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.103 |  |
| 2026-09-16 08:05:34 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.070 |  |
| 2026-09-16 08:05:18 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:05:10 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.048 |  |
| 2026-09-16 08:05:00 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-09-16 08:04:53 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.086 |  |
| 2026-09-16 08:04:09 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-09-16 08:03:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:03:31 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:03:23 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:03:12 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-16 08:03:04 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:03:00 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 08:02:52 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-09-16 08:02:29 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-16 08:02:24 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-09-16 08:02:16 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:02:02 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:02:01 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.012 |  |
| 2026-09-16 08:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-16 08:01:48 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:01:45 | Magura (Kalu Ganga) | 2.82 | 🟢 Normal | -0.110 |  |
| 2026-09-16 08:01:29 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-16 08:01:25 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:01:21 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-09-16 08:01:20 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.129 |  |
| 2026-09-16 08:00:29 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.051 |  |
| 2026-09-16 08:00:22 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-16 08:00:15 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 08:02:24 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-09-16 08:02:29 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-16 08:00:15 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-16 08:00:22 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-16 08:01:29 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-16 08:03:12 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-16 08:03:00 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 08:07:31 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 08:03:23 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:07:25 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:05:18 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:02:16 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:03:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:02:02 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:03:31 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:08:12 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:01:25 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:03:04 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-16 07:12:41 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:01:48 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:04:09 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-09-16 08:05:00 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-09-16 08:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-16 08:01:21 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-09-16 08:02:01 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.012 |  |
| 2026-09-16 08:08:32 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | -0.019 |  |
| 2026-09-16 08:06:53 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-09-16 08:02:52 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-09-16 07:03:09 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-09-16 08:05:53 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.031 |  |
| 2026-09-16 08:05:10 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.048 |  |
| 2026-09-16 08:00:29 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.051 |  |
| 2026-09-16 08:07:11 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.070 |  |
| 2026-09-16 08:05:34 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.070 |  |
| 2026-09-16 07:13:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | -0.083 |  |
| 2026-09-16 08:04:53 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.086 |  |
| 2026-09-16 08:05:42 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.103 |  |
| 2026-09-16 08:01:45 | Magura (Kalu Ganga) | 2.82 | 🟢 Normal | -0.110 |  |
| 2026-09-16 08:01:20 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)