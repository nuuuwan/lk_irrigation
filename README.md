# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_14:26:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **237,761 measurements** from **39** stations.
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
| 2026-08-19 14:26:29 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:21:55 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:18:27 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-19 14:14:02 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-08-19 14:11:13 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-08-19 14:10:11 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.019 |  |
| 2026-08-19 14:09:43 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:06:49 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.012 |  |
| 2026-08-19 14:06:35 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:06:29 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:05:31 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.028 |  |
| 2026-08-19 14:05:22 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.020 |  |
| 2026-08-19 14:04:17 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-19 14:04:09 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:04:08 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:04:07 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:04:07 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:03:53 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.248 |  |
| 2026-08-19 14:03:45 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 14:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:03:40 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-19 14:03:33 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-08-19 14:03:29 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.012 |  |
| 2026-08-19 14:03:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | -0.042 |  |
| 2026-08-19 14:03:09 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 14:03:07 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-08-19 14:03:05 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-19 14:03:04 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:02:31 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-19 14:02:22 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-19 14:02:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-19 14:02:08 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-08-19 14:02:06 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:02:01 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:01:33 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.020 |  |
| 2026-08-19 14:01:30 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:00:56 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:00:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:00:11 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-19 13:59:29 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 14:02:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-19 14:18:27 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-19 14:03:40 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-19 14:02:22 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-19 14:03:09 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 14:03:45 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 14:01:30 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:00:11 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:02:01 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:00:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:02:06 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 13:15:32 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-19 13:59:29 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:21:55 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:03:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:04:09 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:06:35 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:09:43 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:26:29 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:06:29 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:00:56 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:04:07 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-19 14:11:13 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-08-19 14:14:02 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-08-19 14:02:31 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-19 14:03:07 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-08-19 14:03:05 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-19 14:04:17 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-19 14:03:29 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.012 |  |
| 2026-08-19 14:06:49 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.012 |  |
| 2026-08-19 14:10:11 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.019 |  |
| 2026-08-19 14:03:33 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-08-19 14:01:33 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.020 |  |
| 2026-08-19 14:05:22 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.020 |  |
| 2026-08-19 14:05:31 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.028 |  |
| 2026-08-19 14:02:08 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-08-19 14:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | -0.042 |  |
| 2026-08-19 14:03:53 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.248 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)