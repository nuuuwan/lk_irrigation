# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_01:05:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,012 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 01:05:48 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | -0.009 |  |
| 2026-08-12 01:04:57 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:04:56 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:03:58 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-08-12 01:03:49 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.039 |  |
| 2026-08-12 01:03:44 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:03:01 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:02:55 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:02:42 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:02:42 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 01:02:30 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-08-12 01:02:26 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 01:02:22 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:02:09 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.005 |  |
| 2026-08-12 01:01:57 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.031 |  |
| 2026-08-12 01:01:50 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:01:14 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:01:11 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:00:53 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 00:01:58 | Weraganthota (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.541 | 🔺 Rising |
| 2026-08-12 00:06:04 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-08-12 00:07:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-08-12 00:01:28 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-12 01:02:42 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 01:02:26 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 00:10:40 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 01:02:09 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.005 |  |
| 2026-08-12 00:08:00 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.003 |  |
| 2026-08-12 01:01:14 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:01:11 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:00:53 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-12 00:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:03:44 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 00:00:12 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:15:33 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 00:09:28 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-12 00:12:22 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:04:57 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-12 00:01:19 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:01:50 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:02:22 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:03:01 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:02:42 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:04:56 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:01:06 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-12 00:03:26 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:02:55 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-11 22:01:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-08-12 01:05:48 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | -0.009 |  |
| 2026-08-12 00:04:58 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-08-12 01:03:58 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-08-12 00:05:08 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-08-12 01:02:30 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-08-12 01:01:57 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.031 |  |
| 2026-08-12 01:03:49 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.039 |  |
| 2026-08-12 00:04:13 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.040 |  |
| 2026-08-12 00:06:29 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -2.400 |  |
| 2026-08-12 00:03:12 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -126.000 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)