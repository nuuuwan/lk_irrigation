# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_07:19:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,071 measurements** from **39** stations.
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
| 2026-11-17 07:19:53 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.008 |  |
| 2026-11-17 07:18:21 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.016 |  |
| 2026-11-17 07:15:07 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | -0.026 |  |
| 2026-11-17 07:12:56 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:09:54 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-11-17 07:08:44 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.034 |  |
| 2026-11-17 07:08:32 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.073 |  |
| 2026-11-17 07:08:32 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 07:08:19 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:08:09 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.038 |  |
| 2026-11-17 07:06:47 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:06:05 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.028 |  |
| 2026-11-17 07:05:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-11-17 07:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.155 |  |
| 2026-11-17 07:05:07 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:05:03 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-11-17 07:04:47 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:04:17 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:04:17 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-17 07:04:08 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-17 07:04:00 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:03:52 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:03:46 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-11-17 07:03:45 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-11-17 07:03:24 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:03:12 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:03:04 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:03:01 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-17 07:02:41 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:02:24 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:01:59 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:01:10 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-17 07:01:08 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:01:06 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:01:00 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | -0.027 |  |
| 2026-11-17 07:00:49 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.009 |  |
| 2026-11-17 07:00:33 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:00:23 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-17 06:59:26 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 07:03:01 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-17 07:08:32 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 07:03:04 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:01:08 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:01:06 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:04:00 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:05:07 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:01:59 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:03:24 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:04:17 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-17 06:59:26 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:00:33 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:02:41 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:08:19 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:04:47 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:02:24 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:06:47 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:03:52 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:12:56 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:03:12 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-17 07:19:53 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.008 |  |
| 2026-11-17 07:00:49 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.009 |  |
| 2026-11-17 07:09:54 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-11-17 07:04:17 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-17 07:03:46 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-11-17 07:01:10 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-17 07:04:08 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-17 07:00:23 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-17 07:18:21 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.016 |  |
| 2026-11-17 07:03:45 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-11-17 07:15:07 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | -0.026 |  |
| 2026-11-17 07:01:00 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | -0.027 |  |
| 2026-11-17 07:06:05 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.028 |  |
| 2026-11-17 07:08:44 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.034 |  |
| 2026-11-17 07:08:09 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.038 |  |
| 2026-11-17 07:05:03 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-11-17 07:05:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-11-17 07:08:32 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.073 |  |
| 2026-11-17 07:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)