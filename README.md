# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_06:30:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,289 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 06:30:39 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:18:22 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.134 |  |
| 2026-08-11 06:13:45 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.025 |  |
| 2026-08-11 06:12:37 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-08-11 06:12:04 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.017 |  |
| 2026-08-11 06:06:56 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-11 06:06:21 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:06:07 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-11 06:05:57 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-08-11 06:05:52 | Peradeniya (Mahaweli Ganga) | 3.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-11 06:05:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:04:58 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | -0.009 |  |
| 2026-08-11 06:03:41 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-11 06:03:41 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.096 |  |
| 2026-08-11 06:03:39 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-08-11 06:03:21 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:03:21 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.019 |  |
| 2026-08-11 06:03:14 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-11 06:03:02 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.031 |  |
| 2026-08-11 06:02:59 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-11 06:02:45 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 06:02:31 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-08-11 06:02:30 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-11 06:02:22 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:02:16 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:02:08 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.031 |  |
| 2026-08-11 06:02:06 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:02:00 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.025 |  |
| 2026-08-11 06:01:45 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-11 06:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:01:14 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:01:10 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:00:38 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.035 |  |
| 2026-08-11 06:00:28 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:00:13 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 06:06:56 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-11 06:06:07 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-11 06:01:45 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-11 06:05:52 | Peradeniya (Mahaweli Ganga) | 3.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-11 06:02:45 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 06:03:14 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-11 06:01:14 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:00:13 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:00:28 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:30:39 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:02:25 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:03:21 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:05:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 05:02:36 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:02:22 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:06:21 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:02:16 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:42:25 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:01:10 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 06:12:37 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-08-11 06:04:58 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | -0.009 |  |
| 2026-08-11 06:03:41 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-11 06:05:57 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-08-11 06:02:31 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-08-11 06:02:59 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-11 06:02:30 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-11 06:12:04 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.017 |  |
| 2026-08-11 06:03:21 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.019 |  |
| 2026-08-11 06:03:39 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-08-11 05:02:07 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-08-11 04:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-08-11 06:13:45 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.025 |  |
| 2026-08-11 06:02:00 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.025 |  |
| 2026-08-11 06:02:08 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.031 |  |
| 2026-08-11 06:03:02 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.031 |  |
| 2026-08-11 06:00:38 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.035 |  |
| 2026-08-11 06:03:41 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.096 |  |
| 2026-08-11 06:18:22 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)