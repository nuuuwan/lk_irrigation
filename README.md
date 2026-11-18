# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_23:02:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,552 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 23:02:46 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-18 23:02:29 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:02:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-11-18 23:02:08 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | -0.050 |  |
| 2026-11-18 23:02:08 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:01:51 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:01:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:36 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:35 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:25 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.014 |  |
| 2026-11-18 23:01:24 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-11-18 23:01:18 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:06 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:00 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:00:52 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:47:43 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.006 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 22:03:23 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-18 23:02:46 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-18 22:03:36 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-18 22:01:08 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-18 23:01:06 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:04 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:01:05 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:05:45 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:00 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:13 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:06:21 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:02:29 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:18 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:06:52 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:03:19 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:00:52 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:05:15 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:10 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:03:43 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:01:57 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:35 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-18 23:01:36 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-18 22:47:43 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.006 |  |
| 2026-11-18 22:09:27 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-11-18 22:09:59 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-11-18 22:02:31 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-18 22:07:12 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.010 |  |
| 2026-11-18 22:10:39 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:01:51 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 22:01:37 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:02:08 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.010 |  |
| 2026-11-18 23:01:24 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-11-18 22:03:42 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | -0.011 |  |
| 2026-11-18 23:01:25 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.014 |  |
| 2026-11-18 23:02:08 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | -0.050 |  |
| 2026-11-18 23:02:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-11-18 22:01:11 | Moraketiya (Walawe Ganga) | 2.46 | 🟢 Normal | -0.264 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)