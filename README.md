# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_09:14:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,032 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 09:14:53 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.086 |  |
| 2026-10-09 09:13:49 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-10-09 09:07:59 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:07:55 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-10-09 09:07:42 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:07:09 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | -0.142 |  |
| 2026-10-09 09:06:47 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-09 09:06:45 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | -0.058 |  |
| 2026-10-09 09:06:19 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:05:18 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.079 |  |
| 2026-10-09 09:05:12 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:04:43 | Badalgama (Maha Oya) | 4.71 | 🟢 Normal | -0.093 |  |
| 2026-10-09 09:04:42 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:04:34 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:04:24 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-09 09:04:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-09 09:04:10 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:04:04 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.019 |  |
| 2026-10-09 09:04:03 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.192 |  |
| 2026-10-09 09:03:35 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:03:33 | Dunamale (Aththanagalu Oya) | 2.93 | 🟢 Normal | -0.010 |  |
| 2026-10-09 09:03:28 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -11.520 |  |
| 2026-10-09 09:03:18 | Moragaswewa (Deduru Oya) | 1.70 | 🟢 Normal | -0.078 |  |
| 2026-10-09 09:03:03 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -11.520 |  |
| 2026-10-09 09:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:02:57 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.061 |  |
| 2026-10-09 09:02:56 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.166 |  |
| 2026-10-09 09:02:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:02:30 | Ellagawa (Kalu Ganga) | 6.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 09:02:23 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:02:10 | Giriulla (Maha Oya) | 3.48 | 🟢 Normal | -0.111 |  |
| 2026-10-09 09:02:09 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.049 |  |
| 2026-10-09 09:02:03 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:02:01 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:01:58 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-10-09 09:01:56 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-09 09:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-09 09:00:46 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.012 |  |
| 2026-10-09 09:00:42 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.011 |  |
| 2026-10-09 09:00:31 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 09:06:47 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-09 09:04:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-09 09:02:30 | Ellagawa (Kalu Ganga) | 6.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 09:04:10 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:02:03 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:02:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:05:12 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:06:19 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 09:00:31 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:04:34 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:07:42 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:04:42 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:02:01 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:03:35 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:02:23 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:07:59 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 09:01:56 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-09 09:04:24 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-09 09:01:58 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-10-09 09:03:33 | Dunamale (Aththanagalu Oya) | 2.93 | 🟢 Normal | -0.010 |  |
| 2026-10-09 09:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-09 09:00:42 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.011 |  |
| 2026-10-09 09:00:46 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.012 |  |
| 2026-10-09 09:07:55 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-10-09 09:04:04 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.019 |  |
| 2026-10-09 09:13:49 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-10-09 09:02:09 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.049 |  |
| 2026-10-09 09:06:45 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | -0.058 |  |
| 2026-10-09 09:02:57 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.061 |  |
| 2026-10-09 09:03:18 | Moragaswewa (Deduru Oya) | 1.70 | 🟢 Normal | -0.078 |  |
| 2026-10-09 09:05:18 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.079 |  |
| 2026-10-09 09:14:53 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.086 |  |
| 2026-10-09 09:04:43 | Badalgama (Maha Oya) | 4.71 | 🟢 Normal | -0.093 |  |
| 2026-10-09 09:02:10 | Giriulla (Maha Oya) | 3.48 | 🟢 Normal | -0.111 |  |
| 2026-10-09 09:07:09 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | -0.142 |  |
| 2026-10-09 09:02:56 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.166 |  |
| 2026-10-09 09:04:03 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.192 |  |
| 2026-10-09 09:03:28 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -11.520 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)