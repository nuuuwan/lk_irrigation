# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_16:10:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,698 measurements** from **39** stations.
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
| 2026-10-25 16:10:54 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-25 16:10:10 | Pitabeddara (Nilwala Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-10-25 16:09:50 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 16:08:16 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-25 16:08:09 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:07:37 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-10-25 16:06:44 | Ellagawa (Kalu Ganga) | 6.87 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-25 16:06:30 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-10-25 16:06:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 16:06:04 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:05:54 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-25 16:05:48 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 16:05:45 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.037 |  |
| 2026-10-25 16:05:41 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:05:30 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.019 |  |
| 2026-10-25 16:05:28 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-25 16:04:54 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-10-25 16:04:44 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:04:24 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-10-25 16:04:19 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 16:04:11 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.048 |  |
| 2026-10-25 16:03:50 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-25 16:03:27 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.107 |  |
| 2026-10-25 16:03:26 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-25 16:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 16:02:47 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 16:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 16:02:41 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-10-25 16:02:36 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-25 16:02:25 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-10-25 16:02:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:02:09 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:02:09 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.064 |  |
| 2026-10-25 16:01:51 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-25 16:01:28 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:01:03 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 16:00:58 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-10-25 16:00:48 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:00:34 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 16:04:54 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-10-25 16:08:16 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-25 16:02:25 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-10-25 16:10:54 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-25 16:02:36 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-25 16:05:54 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-25 16:03:26 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-25 16:01:51 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-25 16:05:28 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-25 16:06:44 | Ellagawa (Kalu Ganga) | 6.87 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-25 16:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 16:04:19 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 16:05:48 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 16:01:03 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 16:03:50 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-25 16:02:47 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 16:06:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 16:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 16:09:50 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 16:00:48 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:02:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:00:34 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:06:04 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:08:09 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:01:28 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:04:44 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:05:41 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:02:09 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:04:24 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-10-25 16:02:41 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-10-25 16:00:58 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-10-25 16:06:30 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-10-25 16:10:10 | Pitabeddara (Nilwala Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-10-25 16:05:30 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.019 |  |
| 2026-10-25 16:07:37 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-10-25 16:05:45 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.037 |  |
| 2026-10-25 16:04:11 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.048 |  |
| 2026-10-25 16:02:09 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.064 |  |
| 2026-10-25 16:03:27 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)