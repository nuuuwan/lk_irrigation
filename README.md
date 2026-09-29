# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_05:33:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,866 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 05:33:05 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -8.690 |  |
| 2026-09-29 05:32:36 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | -8.690 |  |
| 2026-09-29 05:28:44 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -74.667 |  |
| 2026-09-29 05:28:17 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | -74.667 |  |
| 2026-09-29 05:18:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:16:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | -0.009 |  |
| 2026-09-29 05:14:48 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:14:04 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:12:03 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.067 |  |
| 2026-09-29 05:11:07 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:09:46 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:07:06 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-09-29 05:06:51 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-09-29 05:06:49 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:06:24 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-09-29 05:06:14 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.087 |  |
| 2026-09-29 05:05:31 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.083 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 05:03:51 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-29 05:01:08 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 05:04:06 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-29 05:03:48 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-29 04:57:34 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:00:07 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:01:22 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:00:41 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:03:35 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:06:49 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:14:04 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:02:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:01:43 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:01:04 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:14:48 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:18:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:01:14 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:09:46 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:04:14 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:11:07 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 05:16:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | -0.009 |  |
| 2026-09-29 05:06:51 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-09-29 05:04:24 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-29 05:04:13 | Thalgahagoda (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-09-29 05:02:19 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-29 05:06:24 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-09-29 05:07:06 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-09-29 05:03:19 | Baddegama (Gin Ganga) | 3.34 | 🟢 Normal | -0.034 |  |
| 2026-09-29 05:12:03 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.067 |  |
| 2026-09-29 05:05:31 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.083 |  |
| 2026-09-29 05:06:14 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.087 |  |
| 2026-09-29 05:01:08 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.144 |  |
| 2026-09-29 04:02:59 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.348 |  |
| 2026-09-29 05:33:05 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -8.690 |  |
| 2026-09-29 05:28:44 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -74.667 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)