# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_23:28:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,916 measurements** from **39** stations.
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
| 2026-11-05 23:28:26 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-05 23:20:45 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:10:16 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-05 23:09:09 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-05 23:08:59 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | -0.064 |  |
| 2026-11-05 23:08:18 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.023 |  |
| 2026-11-05 23:07:12 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-05 23:06:47 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-11-05 23:06:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.72 | 🟢 Normal | -0.058 |  |
| 2026-11-05 23:06:17 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:06:02 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-05 23:06:01 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.143 |  |
| 2026-11-05 23:06:00 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:05:29 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-11-05 23:05:28 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:05:11 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 23:05:07 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-05 23:04:59 | Rathnapura (Kalu Ganga) | 2.89 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-05 23:04:33 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-05 23:04:14 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-05 23:03:27 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:03:25 | Thanamalwila (Kirindi Oya) | 1.91 | 🟢 Normal | -0.022 |  |
| 2026-11-05 23:03:21 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 23:03:09 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-05 23:02:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:02:40 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-05 23:02:36 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:02:15 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:56 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | -0.050 |  |
| 2026-11-05 23:01:44 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-05 23:01:21 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:16 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 23:01:02 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:00:20 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-05 23:00:11 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 23:07:12 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-05 23:28:26 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-05 23:04:59 | Rathnapura (Kalu Ganga) | 2.89 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-05 23:00:20 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-05 23:01:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-05 23:04:14 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-05 23:06:02 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-05 23:05:11 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 23:05:07 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-05 23:09:09 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-05 23:01:16 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 23:03:21 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 23:00:11 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:44 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:02:15 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:02:36 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:06:17 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:03:27 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:21 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:05:28 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:20:45 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-05 22:03:42 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:02:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:06:00 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:01:02 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:04:33 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-05 23:05:29 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-11-05 23:02:40 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-05 23:03:09 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-05 23:03:25 | Thanamalwila (Kirindi Oya) | 1.91 | 🟢 Normal | -0.022 |  |
| 2026-11-05 23:08:18 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.023 |  |
| 2026-11-05 23:06:47 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-05 23:01:56 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | -0.050 |  |
| 2026-11-05 23:06:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.72 | 🟢 Normal | -0.058 |  |
| 2026-11-05 23:08:59 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | -0.064 |  |
| 2026-11-05 23:06:01 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.143 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)