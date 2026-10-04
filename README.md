# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_14:03:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,716 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 14:03:28 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:03:26 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:03:24 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.030 |  |
| 2026-10-04 14:02:57 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-10-04 14:02:47 | Hanwella (Kelani Ganga) | 2.57 | 🟢 Normal | -0.071 |  |
| 2026-10-04 14:02:38 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-04 14:02:23 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.042 |  |
| 2026-10-04 14:02:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:02:11 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:02:11 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-10-04 14:01:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2026-10-04 14:01:43 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 14:01:39 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:01:15 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:01:01 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-04 14:00:51 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:00:38 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:00:27 | Weraganthota (Mahaweli Ganga) | -3.47 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-04 14:00:09 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-04 14:00:08 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 13:01:51 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.678 | 🔺 Rising |
| 2026-10-04 14:02:38 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-04 14:01:43 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 14:00:27 | Weraganthota (Mahaweli Ganga) | -3.47 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:02:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:03:26 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:00:38 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-10-04 13:01:50 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-04 13:04:58 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-04 13:04:05 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:01:15 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 13:03:44 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:03:28 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:02:11 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:00:51 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 13:14:11 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-04 14:01:39 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-04 13:08:55 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.009 |  |
| 2026-10-04 14:00:09 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-04 14:01:01 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-04 14:00:08 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-10-04 13:10:50 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.018 |  |
| 2026-10-04 13:08:28 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.018 |  |
| 2026-10-04 13:00:52 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-10-04 14:02:11 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-10-04 14:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-04 13:09:27 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-10-04 14:02:57 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-10-04 13:02:35 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.022 |  |
| 2026-10-04 13:17:50 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.025 |  |
| 2026-10-04 13:04:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.030 |  |
| 2026-10-04 14:03:24 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.030 |  |
| 2026-10-04 14:01:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2026-10-04 13:02:14 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.033 |  |
| 2026-10-04 13:04:06 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.039 |  |
| 2026-10-04 13:05:23 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.041 |  |
| 2026-10-04 14:02:23 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.042 |  |
| 2026-10-04 14:02:47 | Hanwella (Kelani Ganga) | 2.57 | 🟢 Normal | -0.071 |  |
| 2026-10-04 13:03:20 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)