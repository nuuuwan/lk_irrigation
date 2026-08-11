# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_11:18:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,492 measurements** from **39** stations.
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
| 2026-08-11 11:18:24 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:17:55 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:13:39 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-08-11 11:13:38 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:12:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:08:17 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:07:46 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-08-11 11:07:37 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-08-11 11:07:36 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:07:19 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.031 |  |
| 2026-08-11 11:07:10 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:07:07 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-11 11:06:28 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:06:24 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -60.797 |  |
| 2026-08-11 11:06:23 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:05:48 | Peradeniya (Mahaweli Ganga) | 3.37 | 🟢 Normal | -0.019 |  |
| 2026-08-11 11:05:06 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 11:04:53 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-08-11 11:04:19 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:03:39 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.010 |  |
| 2026-08-11 11:03:19 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:03:08 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-11 11:03:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:02:59 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:02:56 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-11 11:02:37 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:02:34 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:02:23 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-08-11 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-08-11 11:02:11 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-11 11:01:55 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-08-11 11:01:38 | Putupaula (Kalu Ganga) | 5.42 | 🔴 Major Flood | -60.797 |  |
| 2026-08-11 11:01:30 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:01:22 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:01:13 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.022 |  |
| 2026-08-11 11:00:59 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:00:47 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-08-11 11:00:40 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:00:32 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 10:59:20 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 11:07:07 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-11 11:02:11 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-11 11:02:56 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-11 11:03:08 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-11 11:00:32 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 11:05:06 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 11:00:59 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:01:30 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:03:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:08:17 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:00:40 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:07:10 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:02:23 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:02:59 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-11 10:02:06 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:03:19 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:13:38 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:18:24 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:07:36 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:04:19 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:06:28 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:01:22 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:06:23 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:17:55 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:12:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:02:34 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-11 11:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-08-11 11:07:37 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-08-11 11:00:47 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-08-11 11:03:39 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.010 |  |
| 2026-08-11 11:05:48 | Peradeniya (Mahaweli Ganga) | 3.37 | 🟢 Normal | -0.019 |  |
| 2026-08-11 11:04:53 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-08-11 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-08-11 11:01:55 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-08-11 11:01:13 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.022 |  |
| 2026-08-11 11:13:39 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-08-11 11:07:46 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-08-11 11:07:19 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.031 |  |
| 2026-08-11 11:06:24 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -60.797 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)