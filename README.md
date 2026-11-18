# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_09:03:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,018 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 09:03:26 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:03:19 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:03:17 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-11-18 09:03:12 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-11-18 09:02:35 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:02:33 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:02:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-11-18 09:02:26 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:02:26 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-18 09:02:14 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-18 09:02:13 | Katharagama (Menik Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-11-18 09:02:11 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:02:06 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:02:02 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:01:51 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:01:50 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:01:22 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-18 09:01:17 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 09:01:17 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.100 |  |
| 2026-11-18 09:01:07 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:00:59 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 09:00:37 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:00:26 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:59:46 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:22:42 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:18:31 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.008 |  |
| 2026-11-18 08:12:12 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 08:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-18 09:01:17 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 09:00:59 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 09:01:50 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:00:26 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:09:15 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:00:37 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:02:35 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:02:02 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:12:12 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:03:19 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:02:06 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:02:33 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:05:28 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:02:32 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:04:36 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:04:24 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:01:07 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:03:26 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:05:32 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:02:11 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-18 09:02:26 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:22:42 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:02:49 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-18 08:18:31 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.008 |  |
| 2026-11-18 08:06:21 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-11-18 09:03:17 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-11-18 09:02:13 | Katharagama (Menik Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-11-18 09:03:12 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-11-18 08:05:05 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.010 |  |
| 2026-11-18 08:05:21 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-18 09:01:22 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-18 09:02:14 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-18 09:02:26 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-18 08:06:21 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-11-18 08:04:10 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-11-18 08:02:33 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.030 |  |
| 2026-11-18 09:02:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-11-18 09:01:17 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)