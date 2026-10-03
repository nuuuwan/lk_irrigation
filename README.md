# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_11:39:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,699 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 11:39:06 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:12:51 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-10-03 11:12:50 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:09:13 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-10-03 11:08:20 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 11:06:17 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -36.000 |  |
| 2026-10-03 11:06:16 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -36.000 |  |
| 2026-10-03 11:05:34 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.253 |  |
| 2026-10-03 11:05:32 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:05:25 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-03 11:05:25 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | -0.060 |  |
| 2026-10-03 11:05:24 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.048 |  |
| 2026-10-03 11:05:10 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.130 |  |
| 2026-10-03 11:05:03 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:04:46 | Ellagawa (Kalu Ganga) | 6.43 | 🟢 Normal | -0.040 |  |
| 2026-10-03 11:04:39 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-10-03 11:04:36 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.073 |  |
| 2026-10-03 11:04:35 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:04:17 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-03 11:04:01 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 11:03:51 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-10-03 11:03:31 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:03:18 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | -0.040 |  |
| 2026-10-03 11:03:15 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | -0.028 |  |
| 2026-10-03 11:03:01 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.063 |  |
| 2026-10-03 11:02:59 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:02:56 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.43 | 🟢 Normal | -0.020 |  |
| 2026-10-03 11:02:46 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-03 11:02:32 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:02:15 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:02:15 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.073 |  |
| 2026-10-03 11:02:12 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:02:08 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 11:02:02 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.207 |  |
| 2026-10-03 11:01:55 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.111 |  |
| 2026-10-03 11:01:47 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:01:03 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 11:01:00 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.020 |  |
| 2026-10-03 11:00:53 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 11:02:46 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-03 11:01:03 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 11:02:08 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 11:04:01 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 11:08:20 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 11:02:12 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:04:35 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:39:06 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:01:47 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:05:32 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:05:03 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:12:50 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:02:32 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:03:31 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:02:59 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:00:53 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:02:15 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 11:12:51 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-10-03 11:09:13 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-10-03 11:04:17 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-03 11:05:25 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-03 11:03:51 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-10-03 11:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.43 | 🟢 Normal | -0.020 |  |
| 2026-10-03 11:04:39 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-10-03 11:01:00 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.020 |  |
| 2026-10-03 11:03:15 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | -0.028 |  |
| 2026-10-03 11:04:46 | Ellagawa (Kalu Ganga) | 6.43 | 🟢 Normal | -0.040 |  |
| 2026-10-03 11:03:18 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | -0.040 |  |
| 2026-10-03 11:05:24 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.048 |  |
| 2026-10-03 11:05:25 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | -0.060 |  |
| 2026-10-03 11:03:01 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.063 |  |
| 2026-10-03 11:04:36 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.073 |  |
| 2026-10-03 11:02:15 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.073 |  |
| 2026-10-03 11:01:55 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.111 |  |
| 2026-10-03 11:05:10 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.130 |  |
| 2026-10-03 11:02:02 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.207 |  |
| 2026-10-03 11:05:34 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.253 |  |
| 2026-10-03 11:06:17 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)