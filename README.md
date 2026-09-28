# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_08:21:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,087 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 08:21:49 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.005 |  |
| 2026-09-28 08:13:49 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | -0.053 |  |
| 2026-09-28 08:11:52 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:09:40 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.029 |  |
| 2026-09-28 08:08:33 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-09-28 08:08:14 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:07:09 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | -0.024 |  |
| 2026-09-28 08:07:04 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:06:55 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:06:47 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:05:53 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-09-28 08:05:46 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-28 08:05:45 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:04:55 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:04:42 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-09-28 08:04:03 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-09-28 08:03:53 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-28 08:03:45 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.131 |  |
| 2026-09-28 08:03:44 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:03:44 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.022 |  |
| 2026-09-28 08:03:39 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-09-28 08:03:22 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | -0.031 |  |
| 2026-09-28 08:03:12 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:03:00 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:02:51 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.101 |  |
| 2026-09-28 08:02:35 | Putupaula (Kalu Ganga) | 2.14 | 🟢 Normal | -0.075 |  |
| 2026-09-28 08:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | -0.092 |  |
| 2026-09-28 08:02:33 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:02:18 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-09-28 08:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:02:12 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:02:08 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-09-28 08:01:58 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:01:39 | Thaldena (Mahaweli Ganga) | 0.04 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-09-28 08:01:34 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.039 |  |
| 2026-09-28 08:01:09 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:01:07 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:00:34 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:00:22 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 08:07:09 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | -0.024 |  |
| 2026-09-28 08:13:49 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | -0.053 |  |
| 2026-09-28 08:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | -0.092 |  |
| 2026-09-28 08:03:39 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-09-28 08:05:46 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-28 08:03:00 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:08:14 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:01:07 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:02:12 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:07:04 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:00:34 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:03:44 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:02:33 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-28 07:14:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:06:47 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:06:55 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:04:55 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:03:12 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:11:52 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:01:09 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:01:58 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:00:22 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:05:45 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 08:21:49 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.005 |  |
| 2026-09-28 08:03:53 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-28 08:08:33 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-09-28 08:02:18 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-09-28 08:02:08 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-09-28 08:04:03 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-09-28 08:04:42 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-09-28 08:05:53 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-09-28 08:03:44 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.022 |  |
| 2026-09-28 08:09:40 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.029 |  |
| 2026-09-28 08:03:22 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | -0.031 |  |
| 2026-09-28 08:01:34 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.039 |  |
| 2026-09-28 08:02:35 | Putupaula (Kalu Ganga) | 2.14 | 🟢 Normal | -0.075 |  |
| 2026-09-28 08:02:51 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.101 |  |
| 2026-09-28 08:03:45 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)