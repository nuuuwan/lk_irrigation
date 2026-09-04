# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_07:09:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,398 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 07:09:25 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:09:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:09:05 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:09:00 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:08:37 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-09-04 07:08:36 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.063 |  |
| 2026-09-04 07:06:45 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:05:53 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:05:38 | Thanamalwila (Kirindi Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:05:23 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-09-04 07:05:21 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:04:59 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.021 |  |
| 2026-09-04 07:04:50 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:04:33 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-04 07:03:43 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:03:32 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.083 |  |
| 2026-09-04 07:03:17 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | -0.011 |  |
| 2026-09-04 07:03:17 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:02:49 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 07:02:38 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.050 |  |
| 2026-09-04 07:02:35 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.071 |  |
| 2026-09-04 07:02:33 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:02:28 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.180 |  |
| 2026-09-04 07:02:20 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:02:16 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.029 |  |
| 2026-09-04 07:02:14 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:01:24 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:01:08 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:01:05 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | -0.002 |  |
| 2026-09-04 07:00:22 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 06:29:24 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 07:04:33 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-04 06:09:11 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-04 06:01:13 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-04 07:02:49 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 06:02:22 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:05:53 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:00:22 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:01:08 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 06:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:09:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:03:43 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:02:20 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:04:50 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:09:25 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-04 06:06:18 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:05:21 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:09:05 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-04 06:06:15 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:01:24 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:02:14 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-04 06:01:56 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:03:17 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:02:33 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:09:00 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:06:45 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:05:38 | Thanamalwila (Kirindi Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-04 07:01:05 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | -0.002 |  |
| 2026-09-04 06:16:43 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.004 |  |
| 2026-09-04 07:08:37 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-09-04 07:05:23 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-09-04 07:03:17 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | -0.011 |  |
| 2026-09-04 07:04:59 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.021 |  |
| 2026-09-04 07:02:16 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.029 |  |
| 2026-09-04 07:02:38 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.050 |  |
| 2026-09-04 07:08:36 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.063 |  |
| 2026-09-04 06:08:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.066 |  |
| 2026-09-04 07:02:35 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.071 |  |
| 2026-09-04 07:03:32 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.083 |  |
| 2026-09-04 07:02:28 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)