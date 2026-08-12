# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_08:18:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,278 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 08:18:36 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-08-12 08:12:55 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.017 |  |
| 2026-08-12 08:10:38 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-08-12 08:08:45 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-08-12 08:08:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.165 |  |
| 2026-08-12 08:08:09 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:07:17 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-12 08:06:58 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.013 |  |
| 2026-08-12 08:06:47 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-12 08:06:09 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-12 08:05:48 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:05:37 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:05:36 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-12 08:05:06 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:04:15 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:03:58 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:03:56 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-08-12 08:03:28 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:03:24 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 08:03:12 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:03:08 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:02:58 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:02:54 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:02:50 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-12 08:02:47 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:02:27 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:02:14 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.087 |  |
| 2026-08-12 08:02:10 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:01:51 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.031 |  |
| 2026-08-12 08:01:41 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-08-12 08:01:33 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.031 |  |
| 2026-08-12 08:01:19 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:01:14 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.030 |  |
| 2026-08-12 08:01:02 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.099 |  |
| 2026-08-12 08:00:14 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 08:00:12 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.059 |  |
| 2026-08-12 08:00:02 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:46:28 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 08:06:47 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-12 08:06:09 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-12 08:07:17 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-12 08:00:14 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 08:03:24 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 08:02:58 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:05:48 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:03:58 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:02:10 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:03:28 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:02:54 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:01:14 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:02:27 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:08:09 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:03:08 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:05:06 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:02:47 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:03:12 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:04:15 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:05:37 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-08-12 07:23:00 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:01:19 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-12 08:08:45 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-08-12 08:18:36 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-08-12 08:10:38 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-08-12 08:05:36 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-12 08:02:50 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-12 08:03:56 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-08-12 08:06:58 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.013 |  |
| 2026-08-12 08:12:55 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.017 |  |
| 2026-08-12 08:01:41 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-08-12 08:01:14 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.030 |  |
| 2026-08-12 08:01:51 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.031 |  |
| 2026-08-12 08:01:33 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.031 |  |
| 2026-08-12 08:00:12 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.059 |  |
| 2026-08-12 08:02:14 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.087 |  |
| 2026-08-12 08:01:02 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.099 |  |
| 2026-08-12 08:08:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)