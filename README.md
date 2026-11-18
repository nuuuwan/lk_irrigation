# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_10:31:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,076 measurements** from **39** stations.
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
| 2026-11-18 10:31:05 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-11-18 10:29:00 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:18:39 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:17:55 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.008 |  |
| 2026-11-18 10:16:11 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:13:01 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:06:54 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-11-18 10:06:29 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.014 |  |
| 2026-11-18 10:06:18 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:06:06 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-11-18 10:06:02 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:05:23 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.061 |  |
| 2026-11-18 10:04:53 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:04:44 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.028 |  |
| 2026-11-18 10:04:42 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:04:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-11-18 10:04:23 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-11-18 10:04:11 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.030 |  |
| 2026-11-18 10:04:04 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.020 |  |
| 2026-11-18 10:03:19 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:03:05 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:03:02 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 10:02:53 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:51 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:32 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:28 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:27 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-18 10:02:26 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:23 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:16 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:01:56 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:01:45 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | -4.617 |  |
| 2026-11-18 10:01:43 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:01:40 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | -0.030 |  |
| 2026-11-18 10:01:27 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:01:25 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:00:34 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:00:34 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 10:02:27 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-18 10:03:02 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 10:01:27 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:26 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:16:11 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:01:43 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:18:39 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:00:34 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:23 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:01:25 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:53 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:06:02 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:51 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:04:42 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:13:01 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:32 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:00:34 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:28 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:29:00 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:01:56 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:17:55 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.008 |  |
| 2026-11-18 10:31:05 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-11-18 10:06:06 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-11-18 10:05:23 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:03:19 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:04:53 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:06:18 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:02:16 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:04:23 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-11-18 10:06:29 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.014 |  |
| 2026-11-18 10:06:54 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-11-18 10:04:04 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.020 |  |
| 2026-11-18 10:04:44 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.028 |  |
| 2026-11-18 10:04:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-11-18 10:01:40 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | -0.030 |  |
| 2026-11-18 10:04:11 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.030 |  |
| 2026-11-18 10:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.061 |  |
| 2026-11-18 10:01:45 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | -4.617 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)