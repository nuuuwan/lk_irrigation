# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_19:10:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,412 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 19:10:14 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:08:36 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:07:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:06:58 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:06:41 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.019 |  |
| 2026-09-29 19:05:20 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 19:04:59 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:04:38 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | -0.058 |  |
| 2026-09-29 19:04:04 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:03:45 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-29 19:03:38 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-09-29 19:03:21 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 19:03:19 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-09-29 19:03:12 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:03:03 | Baddegama (Gin Ganga) | 2.88 | 🟢 Normal | -0.030 |  |
| 2026-09-29 19:03:00 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-09-29 19:02:39 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.041 |  |
| 2026-09-29 19:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:02:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-09-29 19:02:19 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.021 |  |
| 2026-09-29 19:02:18 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.050 |  |
| 2026-09-29 19:02:10 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:01:56 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:01:48 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-09-29 19:01:45 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-09-29 19:01:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.090 |  |
| 2026-09-29 19:01:32 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:01:18 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-09-29 19:00:35 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-29 19:00:33 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-29 19:00:26 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:00:12 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 19:01:45 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-09-29 19:00:33 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-29 19:05:20 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 19:03:21 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:00:12 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:01:32 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:08:36 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:10:14 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:06:58 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:07:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:00:26 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:03:12 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:44 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:04:04 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:04:59 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:01:56 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:02:10 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-09-29 19:03:45 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-29 19:03:00 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-09-29 19:00:35 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-29 18:04:39 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-09-29 19:01:18 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-09-29 18:05:06 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.013 |  |
| 2026-09-29 19:06:41 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.019 |  |
| 2026-09-29 19:03:38 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-09-29 19:03:19 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-09-29 19:01:48 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-09-29 19:02:19 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.021 |  |
| 2026-09-29 19:03:03 | Baddegama (Gin Ganga) | 2.88 | 🟢 Normal | -0.030 |  |
| 2026-09-29 19:02:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-09-29 18:02:13 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | -0.040 |  |
| 2026-09-29 19:02:39 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.041 |  |
| 2026-09-29 19:02:18 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.050 |  |
| 2026-09-29 19:04:38 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | -0.058 |  |
| 2026-09-29 19:01:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)